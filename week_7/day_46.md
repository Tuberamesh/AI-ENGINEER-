# DAY 46 — FastAPI + RAG Integration

## 🎯 Objective

Connect the existing Week 6 Retrieval-Augmented Generation (RAG) pipeline to the Week 7 FastAPI application and expose it through HTTP endpoints.

## ✅ Tasks Completed

- Created a FastAPI application using `app/main.py`.
- Created request and response schemas using Pydantic in `app/schemas.py`.
- Implemented API endpoints:
  - `GET /` — Welcome message.
  - `GET /health` — Health check.
  - `GET /hello/{name}` — Personalized greeting.
  - `GET /documents/{document_id}` — Retrieve a sample document.
  - `POST /ask` — Ask questions using the RAG pipeline.
- Added request validation using Pydantic `BaseModel` and `Field`.
- Added HTTP error handling.
- Connected FastAPI to the existing Week 6 RAG pipeline.
- Tested the API through Swagger UI.
- Fixed the RAG system prompt to improve context-based answers.

## 🧠 Project Structure

```text
AI-ENGINEER-/
├── week_06/
│   └── personal-knowledge-search/
│       ├── rag_pipeline.py
│       ├── chroma_db/
│       ├── requirements.txt
│       └── .venv/
│
└── week_7/
    ├── app/
    │   ├── main.py
    │   └── schemas.py
    └── .venv/
```

## 🔌 How FastAPI Connects to RAG

The FastAPI application imports the reusable `answer_question()` function from the existing `rag_pipeline.py` file.

```python
RAG_PROJECT = (
    Path(__file__).resolve().parents[2]
    / "week_06"
    / "personal-knowledge-search"
)

sys.path.insert(0, str(RAG_PROJECT))

from rag_pipeline import answer_question
```

The `/ask` endpoint calls the RAG function:

```python
result = answer_question(
    question=request.question,
    top_k=request.top_k
)
```

The RAG pipeline then:

1. Receives the user's question.
2. Searches ChromaDB for relevant document chunks.
3. Filters retrieved results using the distance threshold.
4. Sends the retrieved context and question to Gemma through Ollama.
5. Returns the generated answer and source metadata.
6. FastAPI validates and returns the final JSON response.

## 📦 Dependencies Installed

| Package | Purpose |
|---|---|
| `fastapi` | Build HTTP API endpoints |
| `uvicorn[standard]` | Run the FastAPI server |
| `chromadb` | Store and retrieve document embeddings |
| `sentence-transformers` | Generate embeddings for semantic search |
| `ollama` | Communicate with the local LLM |

The Week 7 virtual environment needs the RAG dependencies because Python environments are isolated.

Install the dependencies from the `week_7` directory:

```bash
.venv/bin/python -m pip install \
  -r ../week_06/personal-knowledge-search/requirements.txt ollama
```

**Important:** The existing Week 6 `chroma_db` was reused. It was not recreated or moved.

## 🤖 Local LLM

- Runtime: Ollama
- Model: `gemma3:1b`
- Embedding model: `all-MiniLM-L6-v2`
- Vector database: ChromaDB
- Generation temperature: `0`

## ▶️ Running the Application

### Terminal 1 — Ollama

```bash
ollama serve
```

Keep the Ollama service running. If it is already running, do not start another instance.

### Terminal 2 — FastAPI

```bash
cd ~/Desktop/AI-ENGINEER-/week_7

.venv/bin/python -m uvicorn app.main:app --reload
```

Open Swagger UI:

http://127.0.0.1:8000/docs

## 🧪 API Test

Endpoint:

```text
POST /ask
```

Request body:

```json
{
  "question": "What is RAG?",
  "top_k": 1
}
```

Successful response:

```json
{
  "question": "what is rag",
  "answer": "RAG stands for Retrieval-Augmented Generation.",
  "top_k": 1,
  "sources": [
    {
      "source": "ai_engineering.txt",
      "page": 0,
      "distance": 0.4708
    }
  ]
}
```

HTTP status: `200 OK`

## 📚 Key Concepts Learned

- FastAPI routing and HTTP methods.
- Request and response validation with Pydantic.
- Python imports across project directories.
- Virtual environments and dependency management.
- Integrating a reusable RAG function into an API.
- ChromaDB semantic retrieval.
- LLM inference through Ollama.
- Swagger UI API testing.
- Returning source metadata with generated answers.

## 🏁 Final Outcome

Successfully connected the existing Week 6 RAG pipeline to the Week 7 FastAPI application. The `/ask` endpoint accepts a question, retrieves relevant document content, generates an answer using Gemma, and returns a structured JSON response with source information.

**Status:** Core RAG–FastAPI integration completed and tested.
