import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

def summarize(text):
    prompt = f"Summarize the following resume:\n\n{text}\n\nSummary:"
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    response.raise_for_status()
    return response.json()[0]["generated_text"]

def generate_cover_letter(resume_text, job_text):
    prompt = (
        f"Based on the resume below:\n\n{resume_text}\n\n"
        f"And the job description:\n\n{job_text}\n\n"
        "Write a professional, enthusiastic and concise cover letter suitable for applying to this position."
    )
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    response.raise_for_status()
    return response.json()[0]["generated_text"]
