
from pathlib import Path
import sys

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.schemas import AskRequest, AskResponse

# Locate the existing RAG project.
RAG_PROJECT = (
    Path(__file__).resolve().parents[2]
    / "week_06"
    / "personal-knowledge-search"
)

sys.path.insert(0, str(RAG_PROJECT))

from rag_pipeline import answer_question


app = FastAPI(title="Week 7 - AI Engineer API")


@app.get("/")
def home():
    return {"message": "Welcome to my AI Engineer API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    try:
        result = answer_question(
            question=request.question,
            top_k=request.top_k
        )

        return AskResponse(
            question=request.question,
            answer=result["answer"],
            top_k=request.top_k,
            sources=result["sources"]
        )

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="The RAG service is temporarily unavailable."
        )


@app.get("/documents/{document_id}")
def get_document(document_id: int):
    documents = {
        1: {"id": 1, "title": "RAG Basics"},
        2: {"id": 2, "title": "Python Basics"},
    }

    if document_id not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return documents[document_id]


@app.exception_handler(Exception)
async def unexpected_error_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"}
    )