from agents.reflection_agent import reflect_answer


question = "What is machine learning?"

answer = """
Machine learning is a method where computers learn patterns from data.
"""


result = reflect_answer(question, answer)


print(result)