from pprint import pprint

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_transcribe():
    response = client.post("/transcribe", files={"file": open("testdata/harvard.wav", "rb")})
    assert response.status_code == 200
    content = response.json()
    pprint(content, indent=2)
