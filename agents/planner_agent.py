from groq import Groq
from utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def classify_task(user_query: str) -> str:
    """
    Decide which agent should handle the user's request.
    """

    prompt = f"""
You are a routing agent.

Classify the user's request into ONLY ONE of these labels:

RESEARCH
SUMMARY
COMPARISON

Reply with only the label.

User Request:
{user_query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()