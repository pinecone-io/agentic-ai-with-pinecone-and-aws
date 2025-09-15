---
slug: simple-rag
id: rx3typvauhx8
type: challenge
title: Generate a response using simple RAG
teaser: In this step, we'll run a semantic search against our Pinecone index and use
  the results to augment the original query to generate a more accurate and relevant
  response
tabs:
- id: sb8oyjuzrqxv
  title: Jupyter
  type: service
  hostname: jupyter
  path: /lab/workspaces/auto-c/tree/agentic-ai-with-pinecone-and-aws/notebooks/2_data_query_pipeline.ipynb
  port: 8888
- id: uba1nlvg1yyv
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /home/jovyan
  cmd: su jovyan
difficulty: ""
enhanced_loading: null
---
# TL;DR
==

In this module, you'll work through a Jupyter notebook that shows:
- generating the vector embedding of the query using the AWS SDK for Python (Boto3) to convert it to a vector embedding via Amazon Bedrock
- retrieving the relevant information by performing a semantic search against a Pinecone index
- the augmented prompt, including the retrieved data and the original user query
- the generation of the response by the LLM using the augmented prompt via Amazon Bedrock

# Data retrieval
==

Creating intelligent, context-aware applications begins with leveraging advanced techniques for semantic search and language modeling.

The data retrieval step is designed to **fetch relevant information from external sources or databases**, playing a critical role in creating contextually informed outputs.

This process often leverages:
- an **embedding model**, which transforms queries into embeddings and
- a **vector database**, which acts as the search engine.

By utilizing advanced techniques like semantic matching, the retrieval step **identifies and extracts passages or documents that align closely with the query's intent**. The result is contextually accurate and factually relevant data, providing a robust foundation for downstream tasks such as content generation or question-answering.

# Augmented generation
==

After retrieving the relevant information, the augmented generation step comes into play. At this step:
1. we craft a prompt that augments the original query with the retrieved data and
2. send it to the large language model (LLM) to use as context to generate a response.

By blending the factual data from the retrieval step with its advanced language generation capabilities, the **model produces outputs that are both contextually relevant and factually accurate**.

# The pipeline
==

Below is the query pipeline that includes the following steps:

1. We **create a vector embedding for the text query** using Amazon Titan Text Embedding v2 model (`amazon.titan-embed-text-v2:0`) on Amazon Bedrock to capturing the query's semantic meaning in a numerical format.
2. This embedding is then used to **perform a semantic search** against the Pinecone index, retrieving the records that are most similar in meaning and context to the query.
3. Then these **results are combined with the original user query** to create a prompt, or context, for the LLM.
4. This **curated context is then used to generate output**, using the context to drive a more accurate and relevant response.

![Query pipeline](../assets/04-query-pipeline.png)

This approach ensures precise, contextually rich responses, empowering applications with cutting-edge AI capabilities for tasks like question-answering, summarization, or content generation.

# Work through the notebook
==


➡️ Now, it's your turn! You'll work through a Jupyter notebook to **build a simple RAG pipeline to generate a response**:

1. Navigate to the [Jupyter tab](tab-0)
2. Open the notebook in the `notebooks` folder called `2_data_query_pipeline.ipynb` (if it's not already open)
3. Select `Python 3 (ipykernel)` for the kernel in the upper right
4. Work through each cell in the notebook

Take some time to work through this notebook to query data from your Pinecone index and generate a more accurate and relevant response using the search results.

In the next challenge, you'll build an agentic RAG flow.