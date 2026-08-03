from rag.ingest import load_pdf, split_documents
from rag.vector_store import create_vector_store
from agents.research_agent import answer_question


pdf_path = "data/papers/sample9.pdf"


documents = load_pdf(pdf_path)

print("Number of pages:", len(documents))

print("\nFirst page content:")
print(documents[0].page_content[:1000])

chunks = split_documents(documents)

print("Number of chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0].page_content[:1000])


vectorstore = create_vector_store(chunks)

results = vectorstore.similarity_search(
    "What is the title of this paper?",
    k=3
)

print("\nRetrieved documents:")

for i, doc in enumerate(results):
    print("\nChunk", i+1)
    print(doc.page_content[:500])


question = "What is the title of this paper?"


answer = answer_question(
    question,
    vectorstore
)


print("====================")
print("Question:")
print(question)

print("\nAnswer:")
print(answer)