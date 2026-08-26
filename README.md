# Study Assistant

I built this as my first proper coding project while learning Python and getting familiar with Git and GitHub.

It's a simple AI study assistant where you can upload your own notes as a PDF or text file and ask questions about them. It can also generate summaries and quiz questions from the material.

## What it does

* Upload PDF or TXT notes
* Ask questions about your notes
* Get answers based on the uploaded material
* Generate summaries
* Generate quiz questions

## Built with

* Python
* Streamlit
* Google Gemini API
* PyPDF
* python-dotenv

## How to run it

Clone the repository and install the required packages:

`pip3 install streamlit pypdf requests python-dotenv`

Create a `.env` file and add your Gemini API key:

`GEMINI_API_KEY=your-key-here`

Then run:

`streamlit run app.py`

## What I learned

This was my first time actually building and running a project instead of just learning concepts separately.

I learned some Python basics, how APIs work, how to work with PDFs and text files, how Streamlit works, and how Git and GitHub fit into the whole process.

I'm still learning a lot of this, but building the project while learning has helped me understand things much better than just following tutorials.

## Next

I want to keep adding features to this and use what I learn from this project in the next ones.
