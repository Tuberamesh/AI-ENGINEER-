from pathlib import Path
import logging
import sys

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.config import APP_NAME, LOG_LEVEL
from app.schemas import AskRequest, AskResponse

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

# Locate the existing Week 6 RAG project.
RAG_PROJECT = (
    Path(__file__).resolve().parents[2]
    / "week_06"
    / "personal-knowledge-search"
)
sys.path.insert(0, str(RAG_PROJECT))

from rag_pipeline import answer_question

app = FastAPI(title=APP_NAME)


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
    logger.info("RAG question received; top_k=%s", request.top_k)

    try:
        result = answer_question(
            question=request.question,
            top_k=request.top_k,
        )

        logger.info("RAG question processed successfully")

        return AskResponse(
            question=request.question,
            answer=result["answer"],
            top_k=request.top_k,
            sources=result["sources"],
        )

    except Exception as exc:
        logger.exception("RAG service failed")
        raise HTTPException(
            status_code=503,
            detail="The RAG service is temporarily unavailable.",
        ) from exc


@app.get("/documents/{document_id}")
def get_document(document_id: int):
    documents = {
        1: {"id": 1, "title": "RAG Basics"},
        2: {"id": 2, "title": "Python Basics"},
    }

    if document_id not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return documents[document_id]


@app.exception_handler(Exception)
async def unexpected_error_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unexpected error handling %s %s",
        request.method,
        request.url.path,
        exc_info=exc,
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"},
    )
