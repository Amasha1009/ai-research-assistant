from openai import OpenAI
from utils.config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def compare_papers(paper1, paper2):
    prompt = f"""
You are an academic research assistant.

Compare these two research papers.

Paper 1:
{paper1}

Paper 2:
{paper2}

Compare them using these headings:

1. Research Objective
2. Methodology
3. Dataset
4. Results
5. Strengths
6. Limitations
7. Which paper is more suitable and why?

Return the comparison in Markdown format.
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content