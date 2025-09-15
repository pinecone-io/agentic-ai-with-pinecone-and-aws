---
slug: agentic-rag
id: y3ygny5gklwa
type: challenge
title: Run multiple tools with agentic RAG
teaser: In this module, you'll learn how to implement agentic RAG using multiple tools
  to retrieve data from both a web search and semantic search over a Pinecone index.
tabs:
- id: nq5sqk0awl3f
  title: Jupyter
  type: service
  hostname: jupyter
  path: /lab/workspaces/auto-c/tree/agentic-ai-with-pinecone-and-aws/notebooks/3_agentic_rag.ipynb
  port: 8888
- id: wru3vpetuhxw
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
- how to create tools
- how models use tools
- how to implement an agentic flow that orchestrates a RAG pipeline by deciding which tools to invoke and when

# Agentic retrieval-augmented generation (RAG)
==

Agents are now **orchestrators of the core RAG components** to:

- construct more effective queries
- access additional retrieval tools
- evaluate the accuracy and relevance of the retrieved context
- apply reasoning to validate retrieved information, to trust or discard it.

These operations can be performed by an agent or agents as part of a larger, iterative plan. Agents as orchestrators of RAG bring even more opportunities for review, revision of queries, reasoning or validation of context, allowing them to make better decisions, take more informed actions, and generate more accurate and relevant output.

![Agentic RAG](../assets/05-agentic-rag.png)

# Work through the notebook
==

➡️ Now, it's your turn! You'll work through a Jupyter notebook to build **agentic RAG using tool calling:**

1. Navigate to the [Jupyter tab](tab-0)
2. Open the notebook in the `notebooks` folder called `3_agentic_rag.ipynb` (if it's not already open)
3. Select `Python 3 (ipykernel)` for the kernel in the upper right
4. Work through each cell in the notebook

Take some time to work through this notebook to explore how you can orchestrate a RAG pipeline using an agent. The model will decide if, when, and how to use a tool (or multiple tools). In our case, the tools will assist us in retrieval, but tools can also take action like posting a message to a Slack channel or booking a flight.

In the next challenge, you'll work with the demo app, ChatterPine 2000, a Chainlit webapp to interact with this agentic RAG pipeline through a chat interface.