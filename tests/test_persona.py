import sys
sys.path.append(".")

from app.main import app

from fastapi.testclient import TestClient
from app.main import app  # make sure app is defined in app/main.py

client = TestClient(app)

def test_persona_response():
    sample_text = "I love this product!"
    response = client.post("/api/analyze", json={"text": sample_text})

    assert response.status_code == 200

    persona = response.json().get("persona")
    assert persona in ["optimistic","pessimistic", "friendly", 'formal', 'sarcastic', 'neutral'], f"Unexpected Persona: {persona}"
