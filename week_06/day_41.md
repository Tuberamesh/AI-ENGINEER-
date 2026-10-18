Build a basic Retrieval-Augmented Generation (RAG) pipeline.

## What I learned
- ChromaDB stores document chunks and retrieves relevant passages.
- all-MiniLM-L6-v2 converts text into embeddings for semantic search.
- Ollama runs LLMs locally on my MacBook.
- Gemma 3 1B generates answers using the retrieved context.
- A system prompt instructs the model to answer using the provided documents.
- Prompt instructions reduce unsupported answers but cannot guarantee zero hallucinations.

## Pipeline
User Question
    ↓
Embedding Model
    ↓
ChromaDB Retrieval
    ↓
Retrieved Context + Question
    ↓
Ollama + Gemma 3 1B
    ↓
Generated Answer

## Files
- chunk_documents.py — chunks PDF text and creates embeddings.
- vector_store.py — retrieves relevant passages from ChromaDB.
- rag_pipeline.py — retrieves context and generates an answer using Gemma.
- day_41.md — learning notes.

## Run
python rag_pipeline.py

## Result
Successfully ran a local RAG pipeline using ChromaDB, Sentence Transformers, Ollama, and Gemma 3 1B.
