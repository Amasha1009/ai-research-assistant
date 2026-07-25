from agents.planner_agent import classify_task

queries = [
    "Summarize this paper",
    "Compare these two papers",
    "What dataset was used in this paper?"
]

for q in queries:
    print(f"Question: {q}")
    print("Planner:", classify_task(q))
    print("-" * 40)