import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def get_persona(text: str) -> str:
    prompt = f"What is the Persona (Optimistic, Pessimistic, Feiendly, Formal, Sarcastic, Neutral) of this text : {text}    \n give only the category as a response. Must choose from the following categories: Optimistic, Pessimistic, Friendly, Formal, Sarcastic, Neutral"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip().lower()
