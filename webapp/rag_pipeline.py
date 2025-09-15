# To be implemented:
# - Function to take in a user query and return a generated response
# - Query Pinecone index with the user query
# - Create prompt with original user query and retrieved context from Pinecone
# - Call the Bedrock model with the augmented prompt
# - Return the generated response


from datetime import datetime
import os
import boto3
from web_search_tool import WebSearchTool
from pinecone_vector_search_tool import PineconeVectorSearchTool

SYSTEM_PROMPT = """
## Task and Context
You are an internal knowledge assistant. 
You use your advanced complex reasoning capabilities to help people by answering their questions and other requests interactively. 
You will be asked a very wide array of requests on all kinds of topics. 
You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. 
You may need to use multiple tools in parallel or sequentially to complete your task. 
You should focus on serving the user's needs as best you can, which will be wide-ranging. 

## Tool Guide
For queries related to 10k documents, use the pinecone_vector_search_tool. 
For other queries, use web_search_tool.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""

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
        print("Sending the query to Bedrock:")
        print(conversation)
        print("=" * 50)

        # Send the conversation, system prompt, and tool configuration, and return the response
        return self.bedrock.converse(
            modelId=self.generation_model_id,
            messages=conversation,
            system=self.system_prompt,
            toolConfig=self.tool_config,
        )

    def _send_conversation_to_bedrock_stream(self, conversation):
        print("Sending the query to Bedrock (streaming):")
        print(conversation)
        print("=" * 50)

        # Send the conversation, system prompt, and tool configuration, and return the streaming response
        return self.bedrock.converse_stream(
            modelId=self.generation_model_id,
            messages=conversation,
            system=self.system_prompt,
            toolConfig=self.tool_config,
        )

    def _invoke_tool(self, tool_name, tool_input):
        return self.functions_map[tool_name](tool_input)

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
        
        # For the final response, use streaming
        print("Final streaming response:")
        print("=" * 50)
        
        # Use streaming for the final response
        stream_response = self._send_conversation_to_bedrock_stream(conversation)
        
        # Process the streaming response and yield chunks
        full_content = ""
        for event in stream_response['stream']:
            if 'contentBlockDelta' in event:
                delta_text = event['contentBlockDelta']['delta']['text']
                full_content += delta_text
                print(delta_text, end='', flush=True)
                
                # Yield only the text chunk for st.write_stream
                yield delta_text
        
        print("\n" + "=" * 50)
        
