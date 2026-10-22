
from fastapi import FastAPI
from app.schemas import AskRequest, AskResponse
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
