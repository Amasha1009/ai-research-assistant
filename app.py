import streamlit as st

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Assistant")
st.write("Upload AI research papers and explore them using Agentic AI + RAG.")

st.header("Upload Research Papers")

uploaded_files = st.file_uploader(
    "Choose AI research papers (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    st.subheader("Uploaded Papers")

    for file in uploaded_files:
        st.write(f"📄 {file.name}")
else:
    st.info("Please upload one or more PDF research papers.")