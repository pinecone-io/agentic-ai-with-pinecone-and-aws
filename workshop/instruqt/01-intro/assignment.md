---
slug: intro
id: bx4lxyzh9w6y
type: challenge
title: Introduction
teaser: Learn about Pinecone, AWS, and what we're building today -- an agentic retrieval-augmented
  generation (RAG) pipeline
difficulty: ""
enhanced_loading: null
---
# About Pinecone
==

Pinecone is a cloud-native, SaaS-based vector database platform designed for managing and querying high-dimensional vector data, making it a key enabler for building machine learning, artificial intelligence, and data science applications.

The goal of this workshop is to provide participants with practical skills and hands-on experience in building AI applications using Pinecone and AWS. During this workshop, participants will:
- Learn the fundamentals of vector database concepts and Pinecone architecture.
- Gain hands-on experience building an end-to-end agentic retrieval-augmented generation (RAG) chat application using Pinecone, Amazon Bedrock, and Anthropic.

This workshop will enhance participants' knowledge of the latest AI concepts on Agentic AI and empower them to confidently implement the learnings to their business use cases.

# Pinecone with AWS
===

This diagram shows a complete AI development pipeline using a Pinecone vector database and AWS services for building intelligent applications. Data from various sources (text, web logs, images, videos) stored in Amazon S3 can be processed through AWS Glue ETL pipelines and fed into Pinecone. Pinecone provides hosted embedding and reranking models alongside scalable vector storage with read/write capabilities. This system integrates with Amazon Bedrock for additional embedding and generation capabilities, enabling use cases like AI agents, semantic search, recommendation engines, and data classification through a unified knowledge base architecture.

![Pinecone with AWS Architecture](../assets/01-pinecone-with-aws-arch.png)

# What we're building today
==

Today, we'll be building an end-to-end agentic retrieval-augmented generation (RAG) chat application to query financial statements. We'll use the 10-K filings of Comapaq company from 1994 to 2002, which are in text documents. We'll implement this pipeline using Pinecone, Amazon Bedrock, with Amazon Titan Text Embedding v2 model and Anthropic Claude 3 Haiku model for generation.

We'll cover the following modules:

1. Setup your Pinecone account, index, and API key
2. Load data into your Pinecone index
3. Query Pinecone and generate a response with simple RAG
4. Run multiple tools with agentic RAG
5. Play with the web-based agentic RAG chat app
6. Clean up

But first, let's review retrieval-augmented generation.

## Retrieval-augmented generation

Retrieval-augmented generation (RAG) is an architecture that provides the most relevant and contextually-important proprietary, private, or dynamic data to your application's large language model (LLM) when it is performing tasks to enhance its accuracy and performance.

![Agentic RAG](../assets/01-agentic-rag.png)

RAG consists of four parts: a **data ingestion**, a **data retrieval** an **augmented prompt**, and **generation**.

1. Ingestion: authoritative data like company proprietary data is loaded into a data source, like a Pinecone vector database
2. Retrieval: relevant data is retrieved from an external data source based on a user query
3. Augmentation: the retrieved data and the user query are combined into a prompt to provide the model with context for the generation step
4. Generation: the model generates output from the augmented prompt, using the context to drive a more accurate and relevant response.

RAG is particularly useful for chatbots, enabling them to connect to a company's knowledge base, to choose from various retrieval or action-based tools, and to deliver more informative and accurate answers.

Let's get started!

# Cost of Workshop
===

If you are running this as part of a Pinecone-hosted event, with a new Pinecone Starter plan account (which we'll create in the next module!), and in the AWS sandbox provided to you, then there is no cost for you.

## Running this workshop outside of the sandbox

If you choose to run this workshop with an existing Pinecone account or in your own AWS environment, you may incur costs for the Pinecone usage beyond the [Starter tier limits](https://www.pinecone.io/pricing/) and will incur costs for the AWS resources you launch in your account, and API calls you make to Amazon Bedrock. Costs vary based on which LLM model you select and more. We recommend that you check the official AWS pricing pages and monitor costs. You can use [AWS Pricing Calculator](https://calculator.aws/#/) for estimation.