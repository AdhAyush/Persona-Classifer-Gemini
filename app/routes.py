from fastapi import APIRouter
from pydantic import BaseModel
from app.gemini_client import get_sentiment

router = APIRouter()

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str

@router.post("/analyze", response_model=SentimentResponse)
def analyze(input: TextInput):
    sentiment = get_sentiment(input.text)
    return SentimentResponse(sentiment=sentiment)
