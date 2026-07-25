def retrieve_documents(vectorstore, query, k=3):
    """
    Retrieve the most relevant document chunks.
    """

    results = vectorstore.similarity_search(query, k=k)

    return results