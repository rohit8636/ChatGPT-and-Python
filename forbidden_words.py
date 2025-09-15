from openai import OpenAI
import os
from dotenv import load_dotenv
from constants import MODEL_NAME
import spacy

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Load spaCy model
spacy_model = spacy.load("en_core_web_sm")

# Define forbidden words 
FORBIDDEN_WORDS = ["london", "uk", "america", "europe"]

def black_list_filter(text, black_list):
    """Filter out forbidden words from the text."""
    tokens = spacy_model(text)
    result = []
    for token in tokens:
        if token.text.lower() not in black_list:
            result.append(token.text)
        else:
            result.append("[xxxx]")
    return " ".join(result)

def ask_chat_gpt(prompt, model=MODEL_NAME):
    """Interact with OpenAI's GPT model and filter the response."""
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful, concise assistant."},
                {"role": "user", "content": prompt},
            ],
            max_completion_tokens=150,
            temperature=0.2
        )
        original_response = completion.choices[0].message.content
        filtered_response = black_list_filter(original_response, FORBIDDEN_WORDS)
        return filtered_response
    except Exception as e:
        print(f"Error during API call: {e}")
        return "An error occurred. Please try again."

def main():
    """Main function to run the chatbot."""
    print("\nWelcome my friends! I am your personal assistant. Ask me anything!\nWrite 'exit' to end the chat")

    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "exit":
            break

        prompt = f"\nUser asks: {user_input}, \nChatGPT answers: "
        response = ask_chat_gpt(prompt)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()