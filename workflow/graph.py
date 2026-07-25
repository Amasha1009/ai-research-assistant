from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.planner_agent import classify_task
from agents.research_agent import answer_question
from agents.summary_agent import summarize_text
from agents.comparison_agent import compare_papers


class AgentState(TypedDict):
    question: str
    task: str
    answer: str
    vectorstore: object
    paper1: str
    paper2: str


def planner_node(state):
    task = classify_task(state["question"])

    return {
        **state,
        "task": task
    }


def research_node(state):

    answer = answer_question(
        state["question"],
        state["vectorstore"]
    )

    return {
        **state,
        "answer": answer
    }


def summary_node(state):

    answer = summarize_text(
        state["paper1"]
    )

    return {
        **state,
        "answer": answer
    }


def comparison_node(state):

    answer = compare_papers(
        state["paper1"],
        state["paper2"]
    )

    return {
        **state,
        "answer": answer
    }


def router(state):

    task = state["task"].upper()

    if task == "SUMMARY":
        return "summary"

    elif task == "COMPARISON":
        return "comparison"

    else:
        return "research"


builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("research", research_node)
builder.add_node("summary", summary_node)
builder.add_node("comparison", comparison_node)

builder.set_entry_point("planner")

builder.add_conditional_edges(
    "planner",
    router,
    {
        "research": "research",
        "summary": "summary",
        "comparison": "comparison"
    }
)

builder.add_edge("research", END)
builder.add_edge("summary", END)
builder.add_edge("comparison", END)

graph = builder.compile()