#Testing the genai model with the gemini api key in streamlit

import streamlit as st
import google.generativeai as genai

# Hardcoded API Key (Replace with your actual key)
API_KEY = "AIzaSyBKvgkOVntPZ_c9DmbwS2TaY-vQ2q6zNKE"

# Configure Gemini API
genai.configure(api_key=API_KEY)
 
# Initialize the model
model = genai.GenerativeModel("models/gemini-2.0-flash-thinking-exp-1219")

# Streamlit UI
st.title("🌾 AgriBot - Smart Farming Assistant")
st.write("👨‍🌾 Ask about crop yield, fertilizers, and government schemes.")

# User Input
user_input = st.text_area("📝 Ask your question (any language):", "")

if st.button("🚀 Get Answer"):
    if user_input:
        system_instruction = """You are an AI assistant specialized in agriculture.
        Your role is to:
        - Provide suggestions to improve crop yield.
        - Recommend fertilizers and pest control for crop diseases.
        - Share information about government schemes for farmers in India.
        - Ensure responses are in the same language as the input."""

        prompt = f"{system_instruction}\nUser Input: {user_input}\nAI Response:"

        try:
            response = model.generate_content([{"role": "user", "parts": [{"text": prompt}]}])
            st.success("🤖 AI Response:")
            st.write(response.text)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
