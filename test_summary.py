from rag.ingest import load_pdf
from agents.summary_agent import summarize_text

documents = load_pdf("data/papers/sample.pdf")

text = "\n".join(doc.page_content for doc in documents)

summary = summarize_text(text)

print(summary)