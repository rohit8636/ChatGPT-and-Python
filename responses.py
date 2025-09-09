import os
from openai import OpenAI
from dotenv import load_dotenv
from constants import MODEL_NAME

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Responses API
response = client.responses.create(
    model="gpt-5-nano",
    input="Tell me a three sentence bedtime story about a unicorn.",
    max_output_tokens=100,
    reasoning={"effort": "minimal", "summary": "concise"},
)

print(response.to_json())
