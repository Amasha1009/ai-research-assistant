from openai import OpenAI
from utils.config import OPENROUTER_API_KEY


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def reflect_answer(question, answer):

    prompt = f"""
You are a Reflection Agent.

Review the generated answer.

Question:
{question}

Generated Answer:
{answer}

Tasks:
1. Check whether the answer correctly addresses the question.
2. Identify missing information.
3. Improve clarity and accuracy.
4. Return the improved final answer only.
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    if response.choices[0].message.content:
        return response.choices[0].message.content
    else:
        return answer