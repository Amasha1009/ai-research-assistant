from workflow.graph import graph


state = {
    "question": "Summarize this research paper",
    "task": "",
    "answer": "",
    "vectorstore": None,
    "paper1": "Artificial Intelligence is a field of computer science.",
    "paper2": ""
}


result = graph.invoke(state)


print("Task selected:")
print(result["task"])

print("\nAnswer:")
print(result["answer"])