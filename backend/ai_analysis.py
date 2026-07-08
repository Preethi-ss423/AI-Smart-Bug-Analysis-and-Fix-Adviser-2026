from groq import Groq

# Replace with your Groq API key
client = Groq(api_key="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")

prompt = """
You are an expert software debugging assistant.

Analyze the following bug report and provide:

1. Root Cause
2. Possible Fix
3. Prevention Tips

Bug Report:
Application crashes after clicking the login button.

Respond in a professional manner.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)

print("========== AI ANALYSIS ==========")
print(response.choices[0].message.content)