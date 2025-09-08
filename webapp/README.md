# Streamlit Agentic RAG Chat Example

A Streamlit application that demonstrates an agentic retrieval-augmented generation (RAG) chat interface powered by Pinecone, Amazon Bedrock, and a simple web search. This application provides responses by combining knowledge from a vector database with real-time web search results.

## Features

- 🤖 **Intelligent RAG pipeline**: Powered by Amazon Bedrock for advanced reasoning and response generation
- 🔍 **Dual search capabilities**: Combines Pinecone vector search with web search for comprehensive answers
- 💬 **Chat interface**: Clean and intuitive chat UI with conversation history
- 👤 **User/agent indicators**: Clear visual distinction between user and agent messages
- 📝 **Conversation history**: Persistent chat history during the session
- ⏰ **Timestamps**: Each message shows when it was sent
- 🗑️ **Clear conversation**: Option to reset the chat history
- 📱 **Responsive design**: Works well on different screen sizes
- 🛠️ **Tool integration**: Seamless integration with Pinecone vector database and DuckDuckGo web search

## RAG pipeline architecture

The application implements a RAG pipeline that combines multiple AI capabilities:

### Core components

1. **Amazon Bedrock Integration**: Uses Amazon Bedrock for both text generation and embedding creation
2. **Tool-Based Architecture**: Implements a tool-calling system where the model can decide which tools to use
3. **Conversation Management**: Maintains context throughout multi-turn conversations

### How it works

1. **User Query Processing**: User inputs are processed and sent to the Bedrock model
2. **Tool Selection**: The model determines which tools to use based on the query:
   - **Pinecone Vector Search**: For queries related to the document knowledge base
   - **Web Search**: For general knowledge and real-time information
3. **Tool Execution**: Selected tools are executed with the appropriate parameters
4. **Response Generation**: The model generates a comprehensive response using the retrieved information
5. **Context Preservation**: The conversation history is maintained for follow-up questions

### System prompt

The system is configured with a comprehensive prompt that:
- Defines the model as an internal knowledge assistant
- Provides guidance on tool usage
- Establishes response style preferences
- Enables complex reasoning across multiple information sources

## Tools

The application includes two powerful tools that the model can use to retrieve information:

### 1. Pinecone vector search tool

**Purpose**: Searches a Pinecone vector database containing private data to find relevant information.

**Key features**:
- **Vector embeddings**: Uses Amazon Bedrock to generate embeddings for user queries
- **Semantic search**: Performs semantic search across the document collection
- **Context retrieval**: Returns the top 10 most relevant document chunks
- **Metadata access**: Retrieves full document text along with document IDs

**How it works**:
1. Converts user query to vector embedding using Bedrock
2. Searches Pinecone index for similar vectors
3. Fetches full document content for the most relevant matches
4. Returns structured results with document IDs and text content

### 2. Web search tool

**Purpose**: Searches the internet using DuckDuckGo to retrieve real-time information.

**Key features**:
- **Real-time search**: Accesses current information from the web
- **Multiple results**: Returns up to 5 relevant search results
- **Structured data**: Provides titles, URLs, and content snippets
- **No API keys required**: Uses DuckDuckGo's public search API

**How it works**:
1. Takes user query and searches DuckDuckGo
2. Retrieves search results with titles, URLs, and content snippets
3. Returns structured data for the model to process and incorporate

### Tool selection logic

The model intelligently chooses which tool to use based on the query:
- **Pinecone vector search**: Used for queries related to the internal knowledge base
- **Web search**: Used for general knowledge, current events, and information not in the vector database

## Getting started

### Prerequisites

1. **Pinecone Account**: You need a Pinecone account. Sign in or create a free account [here](https://app.pinecone.io.).
2. **Pinecone index with data**: You'll need a dense index populated with vectors. If you don't have one, you'll have the opportunity to do that below.
1. **AWS Account**: You need an [AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) with access to Amazon Bedrock and the models enabled.
3. **AWS Credentials**: Configure AWS credentials via IAM roles, AWS CLI, or environment variables.

### Environment variables

Before running the application, you need to configure the environment variables. Copy the `.env.example` file to `.env` in the project root with the following variables:

```bash
# AWS Configuration
AWS_REGION=us-east-1
GENERATION_MODEL_ID=anthropic.claude-3-5-sonnet-20241022-v2:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v1

# Pinecone Configuration
PINECONE_INDEX_NAME=your-pinecone-index-name
PINECONE_NAMESPACE=your-pinecone-namespace
# This is for non-production projects so we know which sample app the index came from.
# Remove this and related code for production.
PINECONE_SOURCE_TAG=your-pinecone-source-tag

# Optional: AWS Credentials (if not using IAM roles)
# AWS_ACCESS_KEY_ID=your-access-key
# AWS_SECRET_ACCESS_KEY=your-secret-key
# or
# AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-token
```

### Create Python virtual environment

Create and activate a Python virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

### Install Python dependencies

Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Create index and load data

TODO: This sample app is currently used as part of a workshop and dependent on data that is pre-loaded.

### Start the app

1. Start the Streamlit app from the project root directory:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

3. Start chatting!
