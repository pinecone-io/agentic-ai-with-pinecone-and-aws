---
slug: agentic-rag
id: y3ygny5gklwa
type: challenge
title: Run multiple tools with agentic RAG
teaser: In this module, you'll learn how to implement agentic RAG using multiple tools
  to retrieve data from both a web search and semantic search over a Pinecone index.
tabs:
- id: wru3vpetuhxw
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /home/jovyan
  cmd: su jovyan
- id: nq5sqk0awl3f
  title: Jupyter
  type: service
  hostname: jupyter
  path: /lab/workspaces/auto-c/tree/agentic-ai-with-pinecone-and-aws/
  port: 8888
difficulty: ""
enhanced_loading: null
---
TODO

In this module, we'll implement agentic RAG with Amazon Bedrock, Anthropic, and Pinecone.

The following notebook shows:
- how to create tools
- how models use tools
- how to implement an agentic flow that invokes multiple tools

To implement agentic RAG:
1. Navigate to the Jupyter tab
2. Open the notebook `3_agentic_rag.ipynb`
3. Select `Python 3 (ipykernel)` for the kernel in the upper right
4. Execute each cell in the notebook