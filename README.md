
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


---

# AI Models Used

| Task | Model | Provider |
|---|---|---|
| Research Question Answering | openrouter/free | OpenRouter |
| Summarization | llama-3.3-70b-versatile | Groq |
| Reflection | OpenRouter model | OpenRouter |


---

# Installation

Clone repository:

```bash
git clone <repository-url>


##testing 

The application was tested with:
- Research queries
- Paper summarization
- Paper comparison
- Empty input validation
- Missing Paper 2 validation