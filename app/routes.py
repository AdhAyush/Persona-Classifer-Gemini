from fastapi import APIRouter
from pydantic import BaseModel
from app.gemini_client import get_persona

router = APIRouter()

class TextInput(BaseModel):
    text: str

class PersonaResponse(BaseModel):
    persona: str

@router.post("/analyze", response_model=PersonaResponse)
def analyze(input: TextInput):
    persona = get_persona(input.text)
    return PersonaResponse(persona=persona)
