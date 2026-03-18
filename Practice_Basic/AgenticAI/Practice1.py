from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPEN_API_KEY"))

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Explain Laravel in simple words"}
    ]
)

print(response.choices[0].message.content)