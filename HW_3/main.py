# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Request to Gemini API.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import genai
import google.generativeai as genai
from dotenv import load_dotenv

# --- Load variables from .env file ---
load_dotenv()

# --- Load API key from environment variable ---
api_key = os.getenv("GEMINI_API_KEY")

# --- Configure the API client ---
genai.configure(api_key=api_key)

# --- Create a model instance ---
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Send a request to the model ---
response = model.generate_content("How does AI work?")

print(response.text)
