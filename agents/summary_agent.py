from groq import Groq
from utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def summarize_text(text):

    print("=" * 50)
    print("SUMMARY AGENT IS RUNNING")
    print("Characters before:", len(text))

    # Limit text size
    text = text[:8000]      # Try 8000 or even 6000

    print("Characters after:", len(text))
    print("=" * 50)

    print("Text length:", len(text))
   


    prompt = f"""
You are an academic research assistant.

Summarize the following research paper.

Include ONLY:
1. Objective
2. Methodology
3. Key Findings
4. Conclusion

Research Paper:

{text}
"""

    print("Prompt length:", len(prompt))
    try:
        response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )
        return response.choices[0].message.content

    except Exception as e:
        return f"Summary generation failed: {str(e)}"