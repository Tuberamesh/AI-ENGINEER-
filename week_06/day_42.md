

# Day 42 — Complete the RAG Portfolio Project

## Project
College/Documentation RAG Assistant

## Objective
Build a local assistant that retrieves information from college documents and generates answers using a Large Language Model.

## What I Built
- PDF text extraction using PyMuPDF.
- Document chunking and embedding generation.
- Semantic retrieval using ChromaDB.
- Local answer generation using Ollama and Gemma 3 1B.
- A terminal-based assistant that supports multiple questions in one session.
- Source filename and page references where available.
- A retrieval distance threshold to reject weak matches.
- Instructions to answer using retrieved context and admit when information is missing.

## RAG Pipeline
1. Load documents.
2. Extract PDF text.
3. Split text into chunks.
4. Generate embeddings with all-MiniLM-L6-v2.
5. Retrieve relevant passages from ChromaDB.
6. Check the best retrieval distance.
7. Pass accepted context and the question to Gemma.
8. Display the answer and retrieved source.

## Technologies
- Python
- PyMuPDF
- Sentence Transformers
- ChromaDB
- Ollama
- Gemma 3 1B

## Key Learnings
- Embeddings represent text as numerical vectors.
- Vector databases support semantic search.
- Retrieval provides external context to an LLM.
- Prompt instructions help guide grounded answers.
- Retrieval distance thresholds can filter weak matches.
- A low distance is a similarity signal, not a guarantee of correctness.
- Retrieval and generated answers must be tested with both relevant and irrelevant questions.

## Project Files
- `read_pdf.py` — PDF text extraction.
- `chunk_documents.py` — text chunking and embedding demonstration.
- `ingest.py` — document ingestion into ChromaDB.
- `vector_store.py` — retrieval from ChromaDB.
- `rag_pipeline.py` — retrieval plus local LLM answer generation.
- `../README.md` — project documentation.

## Outcome
Built and tested a basic local RAG assistant that retrieves document passages and generates answers using Gemma 3 1B.

## Future Improvements
- Evaluate the retrieval threshold on more questions.
- Improve answer evaluation and source citation accuracy.
- Add more college documents.
- Build a simple web interface.
