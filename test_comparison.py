from rag.ingest import load_pdf
from agents.comparison_agent import compare_papers

paper1 = load_pdf("data/papers/sample.pdf")
paper2 = load_pdf("data/papers/sample8.pdf")

text1 = "\n".join(doc.page_content for doc in paper1)
text2 = "\n".join(doc.page_content for doc in paper2)

result = compare_papers(text1, text2)

print(result)