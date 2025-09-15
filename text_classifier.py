from openai import OpenAI
import os
from dotenv import load_dotenv
from constants import MODEL_NAME

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

categories = ["art", "science", "sports", "health", "technology", "entertainment"]


def classify_text(text):

    prompt = f"Please classify the following text:'{text} into one of the categories: {','.join(categories)}. The category is: "

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful, concise assistant."},
            {"role": "user", "content": prompt},
        ],
        max_completion_tokens=100,
        temperature=0.8,  # between 0 to 2
    )
    return response.choices[0].message.content


text = input(
    f"Please enter text to classify into categories. Categories are: {categories}. Text: "
)
text_classifier = classify_text(text)
print(f"\nThe text belongs to category:{text_classifier}")
