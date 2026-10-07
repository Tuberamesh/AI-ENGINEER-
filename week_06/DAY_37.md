
# Personal Knowledge Search Engine — Day 37

## Workflow

Documents → Chunks → Embeddings → ChromaDB → Query → Similarity Search → Top-K Results

## Project Structure

personal-knowledge-search/
├── data/
│   ├── python.txt
│   ├── sql.txt
│   └── ai_engineering.txt
├── ingest.py
├── search.py
├── requirements.txt
└── README.md

## Install

requirements.txt:

    chromadb
    sentence-transformers

Install:

    pip install -r requirements.txt

## 1. Persistent ChromaDB

Used in both ingest.py and search.py:

    import chromadb

    client = chromadb.PersistentClient(path="./chroma_db")

Same path = same persistent database.

    ingest.py ──→ ./chroma_db
    search.py ──→ ./chroma_db

## 2. Embedding Function

    from chromadb.utils import embedding_functions

    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

all-MiniLM-L6-v2:

    text chunk → 384 numbers

384 = vector dimension.

It is NOT the chunk size.

Example:

    "hi" → [0.12, -0.43, ...] → 384 numbers

## 3. Collection

Create/get:

    collection = client.get_or_create_collection(
        name="knowledge",
        embedding_function=embedding_function
    )

Get existing:

    collection = client.get_collection(
        name="knowledge"
    )

ChromaDB
└── knowledge collection
    ├── documents
    ├── embeddings
    ├── IDs
    └── metadata

`knowledge` is a collection, not a separate database.

## 4. Read Documents

    from pathlib import Path

    data_folder = Path("data")

    for file in data_folder.glob("*.txt"):
        text = file.read_text()

`file.stem` removes `.txt`.

    python.txt → python

## 5. Chunking

Current simple chunking:

    chunks = [text[i:i+300] for i in range(0, len(text), 300)]

300 = approximate character chunk size.

Each file is processed separately.

    python.txt → its own chunks
    sql.txt → its own chunks

Files do NOT combine into one chunk.

## 6. IDs + Metadata

    ids.append(f"{file.stem}-{i}")

    metadatas.append({
        "source": file.name
    })

Example IDs:

    python-0
    python-1
    sql-0
    ai_engineering-0

Example metadata:

    source → python.txt

## 7. Store in Chroma

    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

`upsert` = add new data or update existing data with the same ID.

## 8. Search

    query = "What is RAG?"

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

`query_texts` = text query input.

`n_results` = number of results requested.

`n_results=3` → return top 3 similar chunks.

## 9. What Happens During Search

    "What is RAG?"
          ↓
    query embedding
          ↓
    compare with stored embeddings
          ↓
    similarity search
          ↓
    top 3 chunks

Chroma handles the text → embedding conversion when using `query_texts`.

## 10. Get Retrieved Documents

    for result in results["documents"][0]:
        print("-", result)

Why `[0]`?

One query:

    [
        [doc1, doc2, doc3]
    ]

`[0]` selects the results for the first query.

Multiple queries:

    [
        [results for query 1],
        [results for query 2],
        [results for query 3]
    ]

So:

    [0] → query 1 results
    [1] → query 2 results
    [2] → query 3 results

## 11. Important Difference

    300 characters → chunk size
    384 numbers   → embedding/vector dimension
    16 chunks     → number of chunks

Do not confuse these.

## 12. Current search.py

    import chromadb

    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_collection(
        name="knowledge"
    )

    query = "What is RAG?"

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    for result in results["documents"][0]:
        print("-", result)

## 13. Run

    python ingest.py

    python search.py

## Key Revision

    Chunk = text

    Embedding = numbers representing the text

    384 = number of values in one embedding

    ChromaDB = stores and searches vectors + documents

    Collection = group of stored records inside ChromaDB

    query_texts = text given to search()

    n_results = how many similar results to return

    results["documents"][0] = documents returned for the first query