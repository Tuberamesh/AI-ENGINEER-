
from fastapi import FastAPI, HTTPException
from app.schemas import AskRequest, AskResponse


from fastapi import Request
from fastapi.responses import JSONResponse

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
    return AskResponse(
        question=request.question,
        answer=f"You asked: {request.question}",
        top_k=request.top_k
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
    # Log the real exception privately in production.
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"}
    )