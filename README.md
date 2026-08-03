
# 📚 AI Research Assistant

An Agentic AI application for analyzing research papers using Retrieval-Augmented Generation (RAG).

The system allows users to upload research papers and perform:
- Question answering
- Paper summarization
- Research paper comparison

---

# Features

✅ PDF document processing  
✅ RAG-based question answering  
✅ Multi-agent architecture  
✅ Research paper summarization  
✅ Research paper comparison  
✅ Reflection agent for answer improvement  
✅ Streamlit interface


---

# System Architecture

User
 |
 v
Streamlit Application
 |
 v
Planner Agent
 |
 +----------------+
 |                |
Research       Summary
Agent          Agent
 |
Comparison Agent
 |
Reflection Agent
 |
Final Answer


---

# Agent Description

## Planner Agent

Purpose:
- Detects user intention
- Selects appropriate task

Tasks:
- Research
- Summary
- Comparison


## Research Agent

Purpose:
- Answers questions from uploaded papers
- Uses RAG retrieval


## Summary Agent

Purpose:
- Generates structured summaries:
  - Objective
  - Methodology
  - Findings
  - Conclusion


## Comparison Agent

Purpose:
- Compares two research papers


## Reflection Agent

Purpose:
- Reviews generated answers
- Improves quality


---

# RAG Pipeline

1. User uploads PDF

2. PDF text extraction

3. Document splitting into chunks

4. Embedding generation

5. Vector database storage

6. Relevant chunks retrieval

7. LLM generates answer


Upload PDF
     │
     ▼
Load PDF
     │
     ▼
Split into Chunks
     │
     ▼
Embeddings
     │
     ▼
Chroma Vector Database
     │
     ▼
Similarity Search
     │
     ▼
LLM
     │
     ▼
Answer

---

# AI Models Used


| Task       |  Model            
| ---------- | ----------------------- |
| Planner    | Groq Llama 3.1 8B       | 
| Research   | OpenRouter Llama 3.3 8B | 
| Summary    | Groq Llama 3.3 70B      | 
| Comparison | Groq Llama 3.3 70B      | 
| Reflection | Groq Llama 3.3 70B      |


---

# Installation


## Clone repository:

```bash
git clone https://github.com/Amasha1009/ai-research-assistant.git

cd ai-research-assistant
```

---



# How to Run Locally

After installation:

## Running the Application

Create a `.env` file in the project root with your API keys:


GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key

Install dependencies:
    pip install -r requirements.txt

Run the Streamlit application:
    streamlit run app.py

---

# Testing

the application was tested with:
- Research queries
- Paper summarization
- Paper comparison
- Empty input validation
- Missing Paper 2 validation

---

# Live Demo 

```bash
Streamlit app : https://ai-research-assistant-spow9sfgcqu7xe78rtafqe.streamlit.app/

```
---

# GitHub Repository Link

```bash

https://github.com/Amasha1009/ai-research-assistant



---
