---
slug: summary-clean-up
id: kysajn7w4mew
type: challenge
title: Summary & clean up
teaser: We'll clean up the resources we created in this workshop and then review what
  we learned.
tabs:
- id: m0ih4vss4mx7
  title: Terminal
  type: terminal
  hostname: jupyter
  workdir: /home/jovyan
  cmd: su jovyan
- id: bj3rpbxiaqae
  title: Jupyter
  type: service
  hostname: jupyter
  path: /lab/workspaces/auto-c/tree/agentic-ai-with-bedrock/
  port: 8888
difficulty: ""
enhanced_loading: null
---
# Delete the Pinecone index
==
Because you are running this as part of a Pinecone-hosted event and in the AWS sandbox provided to you, you do not need clean up any AWS resources. However, in order to prevent unforseen charges to your Pinecone account, we recommend deleting the Pinecone index that was created during this workshop. If you plan to use this index later, remember to clean up once you are done.

To delete the Pinecone index:
1. Navigate to the Jupyter tab
2. Open the notebook `4_clean_up.ipynb`
3. Select `conda_python3` for the kernel
4. Execute the cells in the notebook to delete the index.

# Wrapping up
==
In this workshop you learned:
- The fundamentals of vector databases and how to create intelligent, context-aware applications leveraging advanced techniques for semantic search and language modeling
- Understanding of the agentic RAG architecture and its applications, including information storage, retrieval and augmented text generation
- Hands-on experience with Pinecone's state-of-the-art vector database and AWS services for building and deploying AI solutions
- Best practices for integrating Pinecone and AWS services to create robust and scalable AI workflows

# Extra resources
==

TODO

discord invite