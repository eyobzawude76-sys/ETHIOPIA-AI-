from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_reports_model_not_configured():
    response = client.post(
        "/api/v1/chat",
        json={"message": "Akkam jirta?", "language": "om"},
    )
    assert response.status_code == 501
    assert "model is not connected yet" in response.json()["detail"]


def test_chat_rejects_empty_message():
    response = client.post(
        "/api/v1/chat",
        json={"message": "", "language": "om"},
    )
    assert response.status_code == 422
