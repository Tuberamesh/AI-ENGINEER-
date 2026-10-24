# RAG Assistant API

A FastAPI wrapper for a local Retrieval-Augmented Generation (RAG) assistant. It retrieves relevant document chunks from ChromaDB and uses a local Gemma model through Ollama to generate answers.

## Features

- REST API built with FastAPI
- Request validation using Pydantic
- Semantic retrieval using ChromaDB
- Local LLM inference using Ollama
- Source metadata in responses
- Configurable application name and logging level
- Logging and HTTP error handling
- Automated tests using Pytest
- Interactive API documentation with Swagger UI

## Architecture

```text
Client / Swagger / curl
          |
          v
      FastAPI API
          |
          v
   Pydantic validation
          |
          v
   RAG pipeline
          |
          v
       ChromaDB
          |
          v
 Retrieved document context
          |
          v
     Ollama + Gemma
          |
          v
 Answer + source metadata

