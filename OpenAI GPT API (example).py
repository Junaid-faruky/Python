# 7. OpenAI GPT API (example)
from openai import OpenAI
client = OpenAI(api_key="YOUR_KEY")
print(client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":"Say hi"}]
).choices[0].message)
