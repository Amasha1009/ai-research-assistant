from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_store(chunks):
    """
    Create a Chroma vector database from document chunks.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    vectorstore.persist()

    return vectorstore