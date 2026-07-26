from openai import OpenAI
from utils.config import OPENROUTER_API_KEY
from rag.retrieve import retrieve_documents

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def answer_question(question, vectorstore):
    """
    Answer a question using RAG.
    """
 # Safety check 1: No question
    if not question or question.strip() == "":
        return "Please enter a question."


    # Safety check 2: No vector database
    if vectorstore is None:
        return "Please upload a research paper first."

    
    docs = retrieve_documents(vectorstore, question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an AI Research Assistant.

Use ONLY the information below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, say:
"I could not find the answer in the uploaded paper."
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content