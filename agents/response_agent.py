from groq import Groq
from utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def format_response(user_question, answer):
    prompt = f"""
You are the final response agent.

Format the following answer into Markdown.

Question:
{user_question}

Answer:
{answer}

Use this format:

# Answer

...

# Key Points

- Point 1
- Point 2

# Confidence

High / Medium / Low
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content