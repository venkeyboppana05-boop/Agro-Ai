import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configure API
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("models/gemini-2.0-flash-thinking-exp-1219")

# Define chatbot function
def get_chat_response(user_input):
    system_instruction = """You are an AI assistant specialized in agriculture.
    Your role is to:
    - Provide suggestions to improve crop yield.
    - Recommend fertilizers and pest control for crop diseases.
    - Share information about government schemes for farmers in India.
    - Ensure responses are in the same language as the input."""
    
    prompt = f"{system_instruction}\nUser Input: {user_input}\nAI Response:"
    response = model.generate_content([{"role": "user", "parts": [{"text": prompt}]}])
    return response.text
