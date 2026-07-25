from rag.ingest import load_pdf, split_documents
from rag.vector_store import create_vector_store
from agents.research_agent import answer_question

documents = load_pdf("data/papers/sample.pdf")

chunks = split_documents(documents)

vectorstore = create_vector_store(chunks)

question = "What dataset was used in this paper?"

answer = answer_question(question, vectorstore)

print(answer)