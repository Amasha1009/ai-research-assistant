from agents.planner_agent import classify_task

questions = [
    "Summarize this paper",
    "What dataset was used in this research?",
    "Compare these two research papers",
    "Explain the methodology used in this paper"
]

for q in questions:
    result = classify_task(q)
    print(q)
    print("->", result)
    print()