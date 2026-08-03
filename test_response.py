from agents.response_agent import format_response

question = "What is RAG?"

answer = """
Retrieval-Augmented Generation (RAG) combines vector retrieval
with a large language model to answer questions using retrieved
documents.
"""

result = format_response(question, answer)

print(result)