from openai import OpenAI
import os
from dotenv import load_dotenv
from constants import MODEL_NAME
import spacy

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
            "content": "Write a short story about a trip to European country",
        },
    ],
    max_completion_tokens=50,
    n=5,  # allow for more number of responses
)

generated_text = completion.choices[0].message.content
print(generated_text)
print("**************")

# use spacy
model_spacy = spacy.load("en_core_web_sm")
analysis = model_spacy(generated_text)

# print(analysis)

location = None

for ent in analysis.ents:
    if ent.label_ == "GPE": # this is updated from LOC to GPE for location entity in the latest spacy doc
        location = ent
        break
if location:
    prompt2 = f"Tell me more about {location}"
    response2 = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt2,
            },
        ],
        max_completion_tokens=100,
        n=1,  # allow for more number of responses
    )
    print(response2.choices[0].message.content)