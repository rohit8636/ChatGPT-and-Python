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

# chatbot with history
print("\nWelcome my friends! I am your personal assistant. Ask me anything!\nWrite 'exit' to end the chat")

prev_questions = []
prev_answers = []

while True:
    history=""
    user_input = input("\nYou:")
    if user_input.lower() == 'exit':
        break

    for question, answer in zip(prev_questions,prev_answers):
        history += f"user asks: {question}"
        history += f"ChatGPT answers: {answer}"

    prompt = f"The user asks: {user_input}\nChatGPT answers:"
    history += prompt
    gpt_answer = ask_chat_gpt(history)
    print(f"Chatbot: {gpt_answer}")

    prev_questions.append(user_input)
    prev_answers.append(gpt_answer)