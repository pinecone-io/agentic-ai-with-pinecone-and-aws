# To be implemented:
# - Function to take in a user query and return a generated response
# - Query Pinecone index with the user query
# - Create prompt with original user query and retrieved context from Pinecone
# - Call the Bedrock model with the augmented prompt
# - Return the generated response


from datetime import date
import os
import boto3
import chainlit as cl
from web_search_tool import WebSearchTool
from pinecone_vector_search_tool import PineconeVectorSearchTool

formated_date = date.today().strftime("%A, %B %d, %Y")

SYSTEM_PROMPT = """
## Task and Context
You are an internal knowledge assistant.
You use your advanced complex reasoning capabilities to help people by answering their questions and other requests interactively.
You will be asked a very wide array of requests on all kinds of topics.
You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer.
You may need to use multiple tools in parallel or sequentially to complete your task.
You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Date
Today date is {}

## Tool Guide
For queries related to 10k financial documents and financial information, use the pinecone_vector_search_tool.
For queries about non-financial information such as company history, customer satisfaction, use web_search_tool and rewrite the user query to be more specific.
Use multiple tools if you don't have enough information to answer the query.
Don't make up information. Only use the information provided by the tool.
Say you don't know if you don't have enough information.
Say you don't know if the information is not in the tool results.

## Tool Guide Selection Examples
<example>
Query: What is the company revenue?
Tool: pinecone_vector_search_tool

Query: Who founded the company?
Tool: web_search_tool

Query: What is the operating income in 2001?
Tool: pinecone_vector_search_tool

Query: What are the main offerings of the company?
Tool: web_search_tool

Query: What was the company founded by and what was its revenue in 2001?
Tool: web_search_tool and pinecone_vector_search_tool

Query: When was the company founded and what was its revenue in 2001?
Tool: web_search_tool and pinecone_vector_search_tool

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
""".format(formated_date)

system_prompt = [{"text": SYSTEM_PROMPT}]

class RAGPipeline:
    def __init__(self):
        # init bedrock client
        self.generation_model_id = os.getenv("GENERATION_MODEL_ID")
        self.bedrock = boto3.client('bedrock-runtime', region_name=os.getenv("AWS_REGION"), )
        self.system_prompt = [{"text": SYSTEM_PROMPT}]

        # Initialize tool instances
        self.web_search_tool = WebSearchTool()
        self.pinecone_vector_search_tool = PineconeVectorSearchTool(self.bedrock)

        # setup tools
        self.tool_config = {
            "tools": [
                self.web_search_tool.get_tool_spec(), 
                self.pinecone_vector_search_tool.get_tool_spec()
            ]
        }

        self.functions_map = {
            "web_search_tool": self.web_search_tool.web_search,
            "pinecone_vector_search_tool": self.pinecone_vector_search_tool.pinecone_vector_search,
        }

    def _send_conversation_to_bedrock(self, conversation):
        with cl.Step(name="Send conversation to Bedrock") as step:
            step.input = {"model_id": self.generation_model_id, "input": conversation[-1]["content"][0]}
            
            print("Sending the query to Bedrock:")
            print(conversation)
            print("=" * 50)

            # Send the conversation, system prompt, and tool configuration, and return the response
            response = self.bedrock.converse(
                modelId=self.generation_model_id,
                messages=conversation,
                system=self.system_prompt,
                toolConfig=self.tool_config,
            )
            
            step.output = {"output": response.get("output", {}).get("message", {}).get("content", [])}
            return response

    def _invoke_tool(self, tool_name, tool_input):
        with cl.Step(name=f"Invoke tool: {tool_name}") as step:
            step.input = {"tool_name": tool_name, "query": tool_input["query"]}
            
            result = self.functions_map[tool_name](tool_input)
            
            step.output = {"result": result}
            return result

    def run_agent(self, user_query):
        """Run the agent with streaming response for the final answer.
        Returns a generator that yields (chunk, full_content) tuples.
        """
        conversation = []

        # Step 1: get user query
        message = {"role": "user", "content": [{"text": user_query}]}
        conversation.append(message)

        # Step 2: Send the conversation to Amazon Bedrock
        bedrock_response = self._send_conversation_to_bedrock(conversation)

        print("Model response:")
        print(bedrock_response)
        print("=" * 50)
        
        while bedrock_response["stopReason"] == "tool_use":
            response_message = bedrock_response["output"]["message"]

            # Add assistant tool use back to the conversation context
            conversation.append({
                "role": "assistant",
                "content": response_message["content"]
            })
            
            # Step 3: Invoke each tool
            for content_block in response_message["content"]:
                if "toolUse" in content_block:
                    print(  
                        f"Calling tool name: {content_block['toolUse']['name']} | Parameters: {content_block['toolUse']['input']}"
                    )
                    print("=" * 50)
                    # Call the tool with input
                    tool_result = self._invoke_tool(content_block["toolUse"]["name"],
                        content_block["toolUse"]["input"]
                    )

                    tool_content = []
                    tool_result_items = []

                    for data in tool_result:
                        tool_result_items.append({
                            "json": data
                        })

                    tool_content.append(
                        {
                            "toolResult": {
                                "toolUseId": (content_block["toolUse"]["toolUseId"]),
                                "content": tool_result_items,
                            }
                        }
                    )

                    conversation.append(
                        {
                            "role": "user",
                            "content": tool_content,
                        }
                    )
                else:
                    print(f'Not a toolUse content block: {content_block}')
    
            # Step 4: Generate response
            bedrock_response = self._send_conversation_to_bedrock(conversation)
            print("Model response:")
            print(bedrock_response)
            print("=" * 50)

        print("Final response:")
        print(bedrock_response["output"]["message"]["content"][0]["text"])
        print("=" * 50)
        return bedrock_response["output"]["message"]["content"][0]["text"]
        
        
