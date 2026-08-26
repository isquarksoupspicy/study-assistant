import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

with open("notes.txt", "r") as file:
    notes = file.read()

    question = input("Ask a question about your notes: ")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"
    prompt = f"Here are my notes: \n\n{notes}\n\nBased on these notes, answer this question: {question}"
    response = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]})

    result = response.json()
    answer = result["candidates"][0]["content"]["parts"][0]["text"]

    print("\nAnswer:", answer)