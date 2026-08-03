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


    # Retrieve relevant chunks
    docs = retrieve_documents(
        vectorstore,
        question,
        k=5
    )


    # Create context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )


    # Debug retrieved content
    print("\n========== RETRIEVED CONTEXT ==========")
    print(context[:3000])
    print("=======================================\n")


    prompt = f"""
You are an AI Research Assistant.

Answer the question using ONLY the context below.

Context:
{context}


Question:
{question}


If the answer is not available in the context, say:
"I could not find the answer in the uploaded paper."
"""

    try:
        response = client.chat.completions.create(
       model="meta-llama/llama-3.3-8b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
        return response.choices[0].message.content

    except Exception as e:
     return f"Error generating answer: {str(e)}"