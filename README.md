# SRS enhancement with Graph-RAG and LLM
![github-main](https://github.com/user-attachments/assets/02ce2a10-e161-47c5-837d-a61014b92c21)


## Overview
This project leverages [Microsoft Graph-RAG](https://github.com/microsoft/Graph-RAG) to retrieve relevant content from domain-specific corpora.
It then integrates modified Tree of Thoughts and Chain of Thoughts prompting techniques to assess the completeness and compliance of Software Requirement Specification (SRS) documents.

![Method](https://github.com/user-attachments/assets/3a1e8ef1-7f34-4cdf-91b9-a7f22b2d6d32)

### Graph-RAG
The configuration and prompts have been tailored to better fit this specific context.
To implement a more efficient sub-community ranking, replace the  `indexer_adapters.py` file in the GraphRAG library with the code provided in this repository.



### Prompts
The Chain of Thought (CoT) approach is used to break down complex requirements into smaller, logical components and analyze them step by step. In this project, CoT has been modified to be more strict, focusing solely on identifying severe issues. It first identifies the key components and processes in a requirement. Each component is then compared to reference material to evaluate completeness and alignment with standards. This strict modification ensures that only major deficiencies or violations that could significantly impact the success of the project are highlighted.

The Tree of Thought (ToT) approach goes a step further by generating multiple interpretations for each component of a requirement.
These interpretations are explored in parallel, considering various angles such as alignment with standards, violations, and potential ambiguities. 
Each interpretation is initially voted on based on its likelihood of deficiencies. The top interpretations are then further analyzed through a multi-step process, including lenient, moderate, and strict perspectives, to provide a refined assessment.
![prompt3](https://github.com/user-attachments/assets/a59aa7cb-aa57-4c45-b248-ed318a7296e3)
