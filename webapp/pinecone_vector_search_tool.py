import json
import os
from pinecone import Pinecone
import boto3


class PineconeVectorSearchTool:
    """
    A tool for searching Pinecone vector database to retrieve documents relevant to input queries.
    """
    
    def __init__(self, bedrock: boto3.client):
        """
        Initialize the Pinecone vector search tool.
        """
        self.namespace = os.getenv("PINECONE_NAMESPACE")
        self.pc = Pinecone(source_tag=os.getenv("PINECONE_SOURCE_TAG"))
        desc = self.pc.describe_index(name=os.getenv("PINECONE_INDEX_NAME"))
        self.index = self.pc.Index(host=desc.host)
        self.bedrock = bedrock
        self.embedding_model_id = os.getenv("EMBEDDING_MODEL_ID")

    def embed_query(self, query: str) -> float:
        """
        Generate text embedding by using Amazon Bedrock.
        Args:
            query: string of text to embed.
        Returns:
            dict: embedding in float type.
        """

        body = json.dumps({"inputText": query})

        response = self.bedrock.invoke_model(
            body=body,
            modelId=self.embedding_model_id,
        )

        response_body = json.loads(response.get('body').read())
        embedding = response_body.get('embedding')

        return embedding
    
    def get_tool_spec(self):
        """
        Returns the JSON Schema specification for the pinecone vector search tool. The tool specification
        defines the input schema and describes the tool's functionality.
        For more information, see https://json-schema.org/understanding-json-schema/reference.

        :return: The tool specification for the pinecone vector search tool.
        """
        return {
            "toolSpec": {
                "name": "pinecone_vector_search_tool",
                "description": "Searches Pinecone vector database dense index to retrieve documents relevant to the input query. The index contains 10k documents.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query.",
                            },
                        },
                        "required": ["query"],
                    }
                },
            }
        }

    def pinecone_vector_search(self, input_data) -> list[dict]:
        """
        Searches the Pinecone vector database and retrieves documents relevant to the input query

        :param input_data: The input data containing the query.
        :return: The search results.
        """
        if not self.index:
            return {"error": "Pinecone index not initialized"}
        
        query = input_data.get("query")

        embedding = self.embed_query(query)

        search_results = self.index.query(
            namespace=self.namespace,
            vector=embedding,
            fields=["chunk_text"],
            top_k=10
        )

        document_ids = []
        
        for result in search_results['matches']:
            document_ids.append(result['id'])

        fetch_results = self.index.fetch(ids=document_ids, namespace=self.namespace)

        documents_retrieved = []

        for document_id in document_ids:
            text = fetch_results.vectors[document_id]['metadata']['chunk_text']
            documents_retrieved.append({"id": document_id, "text": text})

        return documents_retrieved

