---
slug: web-based-rag-chat-app
id: wt7pwy6p8xnt
type: challenge
title: Web-based RAG chat app
teaser: A Streamlit application that demonstrates an agentic retrieval-augmented generation
  (RAG) chat interface powered by Pinecone, Amazon Bedrock, and a simple web search.
tabs:
- id: knjxflj4zf7w
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /webapp
- id: zxdbljo9uyip
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /agentic-ai-with-bedrock/webapp
  cmd: su jovyan
- id: za4a81dpnlsc
  title: Chat app
  type: service
  hostname: jupyter
  port: 8501
difficulty: ""
enhanced_loading: null
---
TODO

Update .env file to include your PINECONE_API_KEY

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```