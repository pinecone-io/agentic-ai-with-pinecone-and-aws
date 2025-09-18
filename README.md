# Agentic AI with Pinecone & Amazon Bedrock

A comprehensive workshop and codebase for building intelligent, agentic retrieval-augmented generation (RAG) applications using [Pinecone](https://app.pinecone.io/) vector database and Amazon Bedrock. This repository provides hands-on experience with modern AI architectures, semantic search, and tool-calling agents.

## 🚀 What you'll learn

- **Vector database fundamentals**: Understanding Pinecone architecture and vector similarity search
- **RAG pipeline development**: Building end-to-end retrieval-augmented generation systems
- **Agentic AI implementation**: Creating intelligent agents that can use multiple tools and make decisions
- **AWS integration**: Leveraging Amazon Bedrock for embeddings and text generation
- **Web-based RAG chat applications**: Building a complete web-based chat application with Chainlit

## 📁 Repository structure

```
├── 📓 notebooks/           # Jupyter notebooks for learning progression
│   ├── 1_data_loading_pipeline.ipynb    # Data ingestion and vectorization
│   ├── 2_data_query_pipeline.ipynb      # Simple RAG implementation
│   ├── 3_agentic_rag.ipynb              # Agentic RAG with tool calling
│   └── 4_clean_up.ipynb                 # Resource cleanup
├── 🌐 webapp/              # Web-based RAG chat application
│   ├── app.py                           # Chainlit chat interface
│   ├── rag_pipeline.py                 # Core RAG pipeline
│   ├── pinecone_vector_search_tool.py  # Vector search tool
│   ├── web_search_tool.py              # Web search tool
│   └── requirements.txt                # Python dependencies
├── 📚 workshop/            # Interactive workshop content
│   └── instruqt/                       # Instruqt track materials and config
├── 📊 data/                # Sample dataset (Compaq 10-K filings 1994-2002)
└── 📖 README.md            # This file
```

## 🎯 Workshop learning path

TODO

### 1. **Introduction & setup** 
- Learn about Pinecone, AWS, and RAG architecture
- Create Pinecone account and index
- Set up development environment

### 2. **Data loading pipeline** 
- Parse and chunk text documents
- Generate embeddings using Amazon Bedrock
- Upload vectors to Pinecone index

### 3. **Simple RAG implementation**
- Query Pinecone with semantic search
- Augment prompts with retrieved context
- Generate responses using Amazon Bedrock

### 4. **Agentic RAG with tool calling**
- Create multiple retrieval tools
- Implement agent decision-making logic
- Orchestrate complex RAG workflows

### 5. **Web application development**
- Build interactive chat interface with Chainlit
- Deploy agentic RAG pipeline
- Test with real user interactions

### 6. **Cleanup & best practices**
- Resource management and cleanup
- Production considerations
- Next steps and resources

## 🛠️ Quick start

### Prerequisites

- **Python 3.8+** installed on your system
- **Pinecone account**: [Sign up for free](https://app.pinecone.io/)
- **AWS account**: With access to Amazon Bedrock

### 1. Clone the repository

```bash
git clone https://github.com/pinecone-io/agentic-ai-with-pinecone-and-aws.git
cd agentic-ai-with-pinecone-and-aws
```

### 2. Set up environment

Create a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

For the webapp:
```bash
cd webapp
pip install -r requirements.txt
```

For the notebooks:
```bash
pip install jupyter pinecone boto3 tqdm ddgs
```

### 4. Configure environment variables

Create a `.env` file in the `webapp/` directory:

```bash
# AWS Configuration
AWS_REGION=us-east-1
GENERATION_MODEL_ID=anthropic.claude-3-5-sonnet-20241022-v2:0
EMBEDDING_MODEL_ID=amazon.titan-embed-text-v1

# Pinecone Configuration
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX_NAME=agentic-ai-with-pinecone-and-aws
PINECONE_NAMESPACE=default
PINECONE_SOURCE_TAG=workshop

# Optional: AWS Credentials (if not using IAM roles)
# AWS_ACCESS_KEY_ID=your-access-key
# AWS_SECRET_ACCESS_KEY=your-secret-key
```

## 📚 How to use this repository

### Option 1: Follow the workshop

1. **Start with the workshop content**:
   - Navigate to the `workshop/instruqt` directory
   - Follow the step-by-step assignments in order
   - Each assignment builds upon the previous one and you'll work through Jupyter notebooks in the `notebooks` directory

2. **Run the Jupyter notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```
   - Execute notebooks in sequence: 1 → 2 → 3 → 4
   - Each notebook teaches specific concepts and skills and builds upon the previous notebook

### Option 2: Jump to the web application

If you already have a Pinecone index with data:

1. **Set up your environment** (see Quick start above)
2. **Run the chat application**:
   ```bash
   cd webapp
   chainlit run app.py
   ```
3. **Open your browser** to `http://localhost:8000`
4. **Start chatting** with the agentic RAG system!

## 🔧 Key features

### 🤖 **Agentic RAG pipeline**
- **Intelligent tool selection**: AI agent decides which tools to use based on query context
- **Multi-tool integration**: Combines vector search and web search capabilities
- **Conversation memory**: Maintains context across multiple interactions

### 🔍 **Dual search capabilities**
- **Pinecone vector search**: Semantic search over your private knowledge base
- **Web search**: Real-time information from the internet using DuckDuckGo
- **Intelligent routing**: Automatic selection of appropriate search method

### 💬 **Interactive chat interface**
- **Modern UI**: Clean, responsive design with Chainlit
- **Real-time responses**: Fast, streaming responses from the AI agent
- **Conversation history**: Persistent chat history during sessions
- **Visual indicators**: Clear distinction between user and agent messages

## 📊 Sample dataset

The repository includes Compaq Computer Corporation's 10-K filings from 1994-2002, providing:
- **Financial data**: Revenue, expenses, and business metrics
- **Business strategy**: Product development and market analysis
- **Historical context**: Technology industry evolution during the dot-com era

Perfect for testing RAG capabilities with real business documents!

## 🎓 Learning outcomes

After completing this workshop, you'll be able to:

- ✅ **Design RAG architectures**: Understand when and how to use retrieval-augmented generation
- ✅ **Implement vector search**: Build semantic search capabilities with Pinecone
- ✅ **Create AI agents**: Develop intelligent agents that can use multiple tools
- ✅ **Integrate AWS services**: Leverage Amazon Bedrock for embeddings and generation
- ✅ **Build production apps**: Create deployable chat applications
- ✅ **Handle real-world data**: Process and query business documents effectively

## 🔗 Additional resources

- **[Pinecone Documentation](https://docs.pinecone.io/)**: Comprehensive guides and API reference
- **[Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)**: AWS AI service documentation
- **[Chainlit Documentation](https://docs.chainlit.io/)**: Chat application framework
- **[RAG Best Practices](https://www.pinecone.io/learn/retrieval-augmented-generation/)**: Production considerations

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Submit issues and bug reports
- Propose new features and improvements
- Contribute code via pull requests
- Share your use cases and success stories

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
