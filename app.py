import os
import streamlit as st
from tempfile import NamedTemporaryFile

from rag.ingest import load_pdf, split_documents
from rag.vector_store import create_vector_store
from workflow.graph import graph

from utils.config import GROQ_API_KEY, OPENROUTER_API_KEY

st.write("Groq loaded:", GROQ_API_KEY is not None)
st.write("OpenRouter loaded:", OPENROUTER_API_KEY is not None)


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

# ---------------- Session State Initialization ----------------
if "paper1_id" not in st.session_state:
    st.session_state.paper1_id = None
    st.session_state.vectorstore1 = None
    st.session_state.paper1_text = ""
    st.session_state.documents1 = []
    st.session_state.chunks1 = []

if "paper2_id" not in st.session_state:
    st.session_state.paper2_id = None
    st.session_state.paper2_text = ""
    st.session_state.documents2 = []

if "question_input" not in st.session_state:
    st.session_state.question_input = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "task" not in st.session_state:
    st.session_state.task = ""


# Helper function to process uploaded PDF to text
def process_pdf(file_obj):
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_obj.read())
        pdf_path = tmp.name

    try:
        documents = load_pdf(pdf_path)
        full_text = "\n".join(doc.page_content for doc in documents)
        return documents, full_text
    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)


# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("📚 AI Research Assistant")
    st.markdown("---")

    uploaded_file1 = st.file_uploader(
        "Upload Primary Paper (Paper 1)",
        type=["pdf"],
        key="pdf1_uploader"
    )

    uploaded_file2 = st.file_uploader(
        "Upload Secondary Paper (Paper 2 - Optional for Comparison)",
        type=["pdf"],
        key="pdf2_uploader"
    )

# ---------------- Main Page ----------------
st.title("📚 AI Research Assistant")
st.write("Analyze and compare Artificial Intelligence research papers using Agentic AI and RAG.")

# 1. Process Paper 1
if uploaded_file1:
    p1_id = f"{uploaded_file1.name}_{uploaded_file1.size}"

    if st.session_state.paper1_id != p1_id:
        with st.spinner("📄 Processing and embedding Paper 1..."):
            docs1, text1 = process_pdf(uploaded_file1)
            chunks1 = split_documents(docs1)
            vectorstore1 = create_vector_store(chunks1)

            st.session_state.vectorstore1 = vectorstore1
            st.session_state.paper1_text = text1
            st.session_state.documents1 = docs1
            st.session_state.chunks1 = chunks1
            st.session_state.paper1_id = p1_id

    st.success("✅ Paper 1 loaded successfully!")

    # Display Metrics & Preview
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Paper 1 Pages", len(st.session_state.documents1))
    with col2:
        st.metric("Paper 1 Chunks", len(st.session_state.chunks1))

    st.subheader("Paper 1 Preview")
    if st.session_state.chunks1:
        st.write(st.session_state.chunks1[0].page_content)
else:
    st.session_state.paper1_id = None
    st.session_state.vectorstore1 = None
    st.session_state.paper1_text = ""
    st.session_state.documents1 = []
    st.session_state.chunks1 = []

# 2. Process Paper 2
if uploaded_file2:
    p2_id = f"{uploaded_file2.name}_{uploaded_file2.size}"

    if st.session_state.paper2_id != p2_id:
        with st.spinner("📄 Extracting text from Paper 2..."):
            docs2, text2 = process_pdf(uploaded_file2)

            st.session_state.paper2_text = text2
            st.session_state.documents2 = docs2
            st.session_state.paper2_id = p2_id

    st.success("✅ Paper 2 loaded for comparison!")
    st.metric("Paper 2 Pages", len(st.session_state.documents2))

    if st.session_state.documents2:
        st.subheader("Paper 2 Preview")
        st.write(st.session_state.documents2[0].page_content)

else:
    st.session_state.paper2_id = None
    st.session_state.paper2_text = ""
    st.session_state.documents2 = []

st.divider()

# ---------------- Query Execution ----------------
if st.session_state.paper1_id:
    st.subheader("Ask a Question or Request Analysis")

    question = st.text_input(
        "Ask a question, request a summary, or perform a comparison:",
        key="question_input"
    )

    col1, col2 = st.columns(2)
    with col1:
        apply = st.button("▶ Apply", use_container_width=True)
    with col2:
        clear = st.button("🗑 Clear", use_container_width=True)

    if clear:
        st.session_state.question = ""
        st.session_state.answer = ""
        st.session_state.task = ""
        
        if "question" in st.session_state:
                del st.session_state["question_input"]
        
        st.rerun()

    if apply:

        st.session_state.answer = ""

        if not question.strip():
            st.error("Please enter a question before clicking Apply.")
        else:
            comparison_keywords = [
                "compare",
                "comparison",
                "compare paper",
                "compare papers",
                "difference",
                "differences",
                "versus",
                "vs"
            ]

            is_comparison_query = any(
                word in question.lower()
                for word in comparison_keywords
            )

            if is_comparison_query and not st.session_state.paper2_text:
                st.warning(
                    "Comparison requires a second paper. "
                    "Please upload Paper 2."
                )
            else:
                with st.spinner("🤖 AI is analyzing..."):
                    result = graph.invoke(
                        {
                            "question": question,
                            "task": "",
                            "answer": "",
                            "vectorstore": st.session_state.vectorstore1,
                            "paper1": st.session_state.paper1_text,
                            "paper2": st.session_state.paper2_text
                        }
                    )

                if (
                    result.get("task") == "COMPARISON"
                    and not st.session_state.paper2_text
                ):
                    st.warning(
                        "The planner selected COMPARISON but "
                        "Paper 2 has not been uploaded."
                    )
                else:
                    st.session_state.answer = result.get(
                        "answer",
                        "No answer returned."
                    )

                    st.session_state.task = result.get(
                        "task",
                        "Unknown"
                    )

    if st.session_state.task:

        st.subheader("Task Selected")

        st.info(st.session_state.task)

if st.session_state.answer:

    if st.session_state.answer.startswith("Error"):
        st.error(st.session_state.answer)
        
    else:
        st.success("Answer Generated")
        st.subheader("Answer")
        st.markdown(st.session_state.answer)

else:
    st.info("👈 Please upload at least Paper 1 from the sidebar to begin.")