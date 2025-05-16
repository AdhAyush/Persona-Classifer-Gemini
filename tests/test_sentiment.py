import sys
sys.path.append(".")

from app.main import app

from fastapi.testclient import TestClient
from app.main import app  # make sure app is defined in app/main.py

client = TestClient(app)

def test_sentiment_response():
    sample_text = "I love this product!"
    response = client.post("/analyze", json={"text": sample_text})

    assert response.status_code == 200

    sentiment = response.json().get("sentiment")
    assert sentiment in ["positive", "negative", "neutral"], f"Unexpected sentiment: {sentiment}"
