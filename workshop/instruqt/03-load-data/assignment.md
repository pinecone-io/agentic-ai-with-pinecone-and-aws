---
slug: load-data
id: jlhh8fiu6h45
type: challenge
title: Load data into Pinecone
teaser: In this step, we'll build the data storage system to ingest all the source
  data into an external knowledge base, a Pinecone index
tabs:
- id: pznrwesdbzps
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /home/jovyan
  cmd: su jovyan
- id: q1x5zlvqrjgr
  title: Jupyter
  type: service
  hostname: jupyter
  path: /lab/workspaces/auto-c/tree/agentic-ai-with-pinecone-and-aws/
  port: 8888
difficulty: ""
enhanced_loading: null
---
# Data ingestion
==
When working with large-scale text data, turning it into a searchable format is key to building efficient and intelligent applications.

- The process starts with parsing the source data to extract meaningful text, ensuring only relevant information is carried forward.
- Next, the text is semantically broken into smaller, manageable chunks and transformed into vector embeddings using an embedding model that captures their contextual meaning. These embeddings, essentially numerical representations of the text, make it easier for systems to understand and compare their content.
- Finally, the vector embeddings are uploaded into a Pinecone index, a high-performance vector database designed for fast and scalable similarity searches, enabling powerful, real-time query capabilities.

This pipeline is the foundation for building robust search and recommendation systems.

![pinecone_aws_workshop_data_storage_system.png](../assets/pinecone_aws_workshop_data_storage_system.png)

# Building the data ingestion pipeline
==

The following notebook shows:
- parsing the text data
- chunking the data
- using the AWS SDK for Python (Boto3) to convert data to vector embeddings via Amazon Bedrock
- upserting it to Pinecone

To load data into Pinecone:
1. Navigate to the Jupyter tab
2. Open the notebook `1_data_loading_pipeline.ipynb`
3. Select `Python 3 (ipykernel)` for the kernel in the upper right
4. Execute each cell in the notebook

Take some time to work through this notebook to load data into your Pinecone index, as in the next challenge you'll build the retrieval and augmentation steps.