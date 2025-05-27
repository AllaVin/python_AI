import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from requests.exceptions import Timeout
from google.api_core.exceptions import ResourceExhausted, TooManyRequests

# --- Load variables from .env file ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Check if API is exists ---
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found.")

# --- Configure the API client ---
genai.configure(api_key=api_key)

# --- Create a model instance ---
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Handler with automatic retries ---
@retry(
    reraise=True,
    stop=stop_after_attempt(3),  # max 3 attempts
    wait=wait_exponential(multiplier=1, min=2, max=10),  # delay
    retry=retry_if_exception_type((TooManyRequests, Timeout, ResourceExhausted)),
)
def get_gemini_response(prompt: str) -> str:
    try:
        time.sleep(0.3)  # Antispam - delay
        response = model.generate_content(prompt)
        return response.text
    except TooManyRequests:
        print("⚠️ PI rate limit exceeded. Please try again later....")
        raise
    except Timeout:
        print("⌛ Request timed out. Please try again later....")
        raise
    except ResourceExhausted:
        print("🔁 No API resources. Attempting...")
        raise
    except Exception as e:
        return f"❌ Unexpected error: {e}"


if __name__ == "__main__":
    prompt = "How does AI work?"
    try:
        result = get_gemini_response(prompt)
        print(f"\n✅ Gemini answer:\n{result}")
    except Exception as e:
        print(f"\n🚫 No answer from Gemini: {e}")
