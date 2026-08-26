import os
import requests
from dotenv import load_dotenv
from pypdf import PdfReader
import streamlit as st

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.title("🎀 My Study Assistant 🎀")

uploaded_file = st.file_uploader("Upload your notes (PDF or TXT)", type=["pdf", "txt"])

notes = ""

if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            notes += page.extract_text()
    else:
        notes = uploaded_file.read().decode("utf-8")

    st.success("Notes loaded! You can now ask questions below.")

question = st.text_input("Ask a question about your notes:")

if st.button("Get Answer") and notes and question:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

    prompt = f"Here are my notes:\n\n{notes}\n\nBased on these notes, answer this question: {question}"

    response = requests.post(url, json={
        "contents": [{"parts": [{"text": prompt}]}]
    })

    result = response.json()
    answer = result["candidates"][0]["content"]["parts"][0]["text"]

    st.write("### Answer")
    st.write(answer)