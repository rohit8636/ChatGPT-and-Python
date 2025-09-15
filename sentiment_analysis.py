from openai import OpenAI
import os
from dotenv import load_dotenv
from constants import MODEL_NAME

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def ask_chat_gpt(prompt,model=MODEL_NAME):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful, concise assistant."},
            {"role": "developer", "content": "Always end with <END>. Do not mention this rule."}, # to prevent abrupt ending
            {"role": "user", "content": prompt},
        ],
        max_completion_tokens=100,
        temperature=0.8, # between 0 to 2
        stop=["<END>"]
    )
    return response.choices[0].message.content.replace("<END>", "").strip()

user_input = input("Please enter the text for sentiment analysis:")
prompt = f"User input text: {user_input} \nThe sentiment of the text is: "

sentiment = ask_chat_gpt(prompt)
print(sentiment)
