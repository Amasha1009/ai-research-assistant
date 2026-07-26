from openai import OpenAI
from utils.config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def reflect_answer(question, answer):

    # Safety check: empty answer
    if not answer or answer.strip() == "":
        return "No answer was generated. Please try asking another question."


    prompt = f"""
You are a reflection agent.

Review the answer below.

Question:
{question}

Answer:
{answer}

Check:
1. Is the answer relevant?
2. Is it based on the research paper?
3. Does it contain unsupported information?

Improve the answer if needed.
Return only the improved answer.
"""


    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

        # Safety check: model returns empty response
        if not result or result.strip() == "":
            return answer

        return result


    except Exception as e:
        # If reflection fails, return original answer
        return answer