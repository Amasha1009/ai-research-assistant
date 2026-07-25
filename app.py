import streamlit as st

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📚 AI Research Assistant")
    st.markdown("---")

    uploaded_files = st.file_uploader(
        "Upload AI Research Papers",
        type=["pdf"],
        accept_multiple_files=True
    )

# Main page
st.title("AI Research Assistant")

st.write("Welcome! This application helps you analyze Artificial Intelligence research papers using Agentic AI and RAG.")

if uploaded_files:
    st.success(f"{len(uploaded_files)} paper(s) uploaded.")

    st.subheader("Uploaded Papers")

    for file in uploaded_files:
        st.write(f"📄 {file.name}")
else:
    st.info("Upload one or more AI research papers from the sidebar.")