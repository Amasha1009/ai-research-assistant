from rag.ingest import load_pdf, split_documents
from rag.vector_store import create_vector_store

documents = load_pdf("data/papers/sample.pdf")

chunks = split_documents(documents)

vectorstore = create_vector_store(chunks)

print("✅ Vector database created successfully!")
print(f"Stored {len(chunks)} chunks.")