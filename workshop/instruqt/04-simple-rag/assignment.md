---
slug: simple-rag
id: rx3typvauhx8
type: challenge
title: Generate a response using simple RAG
teaser: In this step, we'll run a semantic search against our Pinecone index and use
  the results to augment the original query to generate a more accurate and relevant
  response
tabs:
- id: uba1nlvg1yyv
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /home/jovyan
  cmd: su jovyan
- id: sb8oyjuzrqxv
  title: Jupyter
  type: service
  hostname: jupyter
  path: /lab/workspaces/auto-c/tree/agentic-ai-with-bedrock/
  port: 8888
difficulty: ""
enhanced_loading: null
---
# Data retrieval
==
Creating intelligent, context-aware applications begins with leveraging advanced techniques for semantic search and language modeling.

The data retrieval step is designed to fetch relevant information from external sources or databases, playing a critical role in creating contextually informed outputs. This process often leverages a retrieval embedding model, which transforms queries into embeddings, and a vector database, which acts as the search engine.
By utilizing advanced techniques like semantic matching, the retrieval step identifies and extracts passages or documents that align closely with the query's intent. The result is contextually accurate and factually relevant data, providing a robust foundation for downstream tasks such as content generation or question-answering.

# Augmented generation
==
After retrieving the relevant information, the augmented generation step comes into play. At this step,  we craft a prompt that augments the original query with the retrieved data and then send it to the large language model (LLM) to use as context to generate a response. By blending the factual data from the retrieval step with its advanced language generation capabilities, the model produces outputs that are both contextually relevant and factually accurate.

# The pipeline
==

TODO IMAGE

# Building the retrieval and augmented generation steps
==

1. We create a vector embedding for the text query using Amazon Titan Text Embedding v2 model (`amazon.titan-embed-text-v2:0`) on Amazon Bedrock to capturing the query's semantic meaning in a numerical format.
2. This embedding is then used to perform a semantic search against the Pinecone index, retrieving the records that are most similar in meaning and context to the query.
3. Then these results are combined with the original user query to create a prompt for the LLM.
4. This curated context is then used to generate output, using the context to drive a more accurate and relevant response.

This approach ensures precise, contextually rich responses, empowering applications with cutting-edge AI capabilities for tasks like question-answering, summarization, or content generation.

The following notebook shows:
- generating the vector embedding of the query using the AWS SDK for Python (Boto3) to convert it to a vector embedding via Amazon Bedrock
- retrieving the relevant information by performing a semantic search against a Pinecone index
- the augmented prompt, including the retrieved data and the original user query
- the generation of the response by the LLM using the augmented prompt via Amazon Bedrock

To generate a response using retrieval-augmented generation:
1. Navigate to the Jupyter tab
2. Open the notebook `2_data_query_pipeline.ipynb`
3. Select `Python 3 (ipykernel)` for the kernel in the upper right
4. Execute each cell in the notebook