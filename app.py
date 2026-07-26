import streamlit as st
from tempfile import NamedTemporaryFile

from rag.ingest import load_pdf, split_documents
from rag.vector_store import create_vector_store
from workflow.graph import graph

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("📚 AI Research Assistant")
    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload an AI Research Paper",
        type=["pdf"]
    )

# ---------------- Main Page ----------------
st.title("📚 AI Research Assistant")

st.write(
    "Analyze Artificial Intelligence research papers using Agentic AI and RAG."
)

if uploaded_file:

    # Save uploaded PDF temporarily
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Load PDF
    documents = load_pdf(pdf_path)

    # Split into chunks
    chunks = split_documents(documents)

    # Create Vector Store
    vectorstore = create_vector_store(chunks)

    # Combine all pages into one string
    full_text = "\n".join(doc.page_content for doc in documents)

    st.success("✅ PDF processed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pages", len(documents))

    with col2:
        st.metric("Chunks", len(chunks))

    st.subheader("First Chunk Preview")

    st.write(chunks[0].page_content)

    st.divider()

    st.subheader("Ask a Question")

    question = st.text_input(
        "Ask something about the uploaded paper:"
    )

    if question:

        with st.spinner("🤖 AI is analyzing the paper..."):

            result = graph.invoke(
                {
                    "question": question,
                    "task": "",
                    "answer": "",
                    "vectorstore": vectorstore,
                    "paper1": full_text,
                    "paper2": ""
                }
            )

        st.success("Answer Generated")

        st.subheader("Answer")

        st.markdown(result["answer"])

else:
    st.info("👈 Upload a PDF from the sidebar.")