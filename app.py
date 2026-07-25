import streamlit as st
from tempfile import NamedTemporaryFile
from rag.ingest import load_pdf, split_documents

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

    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Load PDF
    documents = load_pdf(pdf_path)

    # Split into chunks
    chunks = split_documents(documents)

    st.success("✅ PDF processed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pages", len(documents))

    with col2:
        st.metric("Chunks", len(chunks))

    st.subheader("First Chunk Preview")

    st.write(chunks[0].page_content)

else:
    st.info("👈 Upload a PDF from the sidebar.")