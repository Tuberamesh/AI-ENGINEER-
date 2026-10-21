
from fastapi import FastAPI

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
