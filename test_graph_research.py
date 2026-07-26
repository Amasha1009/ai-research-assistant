from workflow.graph import graph


state = {
    "question": "According to this paper, what dataset was used and what were the experimental results?",
    "task": "",
    "answer": "",
    "vectorstore": None,
    "paper1": "",
    "paper2": ""
}


result = graph.invoke(state)


print("Task selected:")
print(result["task"])

print("\nAnswer:")
print(result["answer"])