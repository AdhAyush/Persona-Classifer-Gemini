import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def get_sentiment(text: str) -> str:
    prompt = f"What is the sentiment (positive, negative, or neutral) of this text: {text}    \n give only the sentiment as a response."
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip().lower()
