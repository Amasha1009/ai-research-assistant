from rag.ingest import load_pdf, split_documents
from rag.vector_store import create_vector_store
from rag.retrieve import retrieve_documents

# Load PDF
documents = load_pdf("data/papers/sample.pdf")

# Split into chunks
chunks = split_documents(documents)

# Create vector database
vectorstore = create_vector_store(chunks)

# Ask a question
query = "What is the main contribution of this paper?"

results = retrieve_documents(vectorstore, query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print("=" * 50)
    print(doc.page_content)
    print()