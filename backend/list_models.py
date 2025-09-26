import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in .env file.")
    else:
        genai.configure(api_key=api_key)
        print("--- Available Models ---")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
        print("------------------------")
except Exception as e:
    print(f"An error occurred: {e}")
