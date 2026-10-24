from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_hello():
    response = client.get("/hello/Ramesha")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Ramesha!"


def test_document_not_found():
    response = client.get("/documents/999")
    assert response.status_code == 404


def test_empty_question_rejected():
    response = client.post(
        "/ask",
        json={"question": "   ", "top_k": 1},
    )
    assert response.status_code == 422


def test_short_question_rejected():
    response = client.post(
        "/ask",
        json={"question": "hi", "top_k": 1},
    )
    assert response.status_code == 422


def test_invalid_top_k_rejected():
    response = client.post(
        "/ask",
        json={"question": "What is RAG?", "top_k": 11},
    )
    assert response.status_code == 422


def test_ask_success(monkeypatch):
    def fake_answer_question(question, top_k):
        return {
            "answer": "RAG stands for Retrieval-Augmented Generation.",
            "sources": [
                {
                    "source": "ai_engineering.txt",
                    "page": 0,
                    "distance": 0.47,
                }
            ],
        }

    monkeypatch.setattr(
        "app.main.answer_question",
        fake_answer_question,
    )

    response = client.post(
        "/ask",
        json={"question": "What is RAG?", "top_k": 1},
    )

    assert response.status_code == 200
    assert response.json()["top_k"] == 1
    assert "Retrieval-Augmented Generation" in response.json()["answer"]


def test_llm_failure_returns_503(monkeypatch):
    def fake_answer_question(question, top_k):
        raise RuntimeError("Simulated Ollama failure")

    monkeypatch.setattr(
        "app.main.answer_question",
        fake_answer_question,
    )

    response = client.post(
        "/ask",
        json={"question": "What is RAG?", "top_k": 1},
    )

    assert response.status_code == 503
    assert response.json()["detail"] == (
        "The RAG service is temporarily unavailable."
    )
