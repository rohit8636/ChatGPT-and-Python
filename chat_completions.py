from openai import OpenAI
import os
from dotenv import load_dotenv
from constants import MODEL_NAME

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Completions API
completion = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "What is the capital of Austria?",
        },
    ],
    max_completion_tokens=100,
    n=1 # because we use n=1, so the response required is at choices[0]
)

print(completion.choices[0].message.content)
