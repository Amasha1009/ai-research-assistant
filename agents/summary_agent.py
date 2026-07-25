from groq import Groq
from utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def summarize_text(text):
    prompt = f"""
You are an academic research assistant.

Summarize the following research paper.

Include:

- Objective
- Methodology
- Key Findings
- Conclusion

Paper:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content