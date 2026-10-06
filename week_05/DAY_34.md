
# DAY 34 — Documents, Metadata & Chroma

## 🎯 Goal

Understand how information is stored inside a vector database.

By the end:

```text
Document + Embedding + ID + Metadata
                ↓
             Chroma
```

---

## 1. Document vs Embedding vs Metadata

### Document

The actual text.

```python
"Python is a programming language."
```

### Embedding

Numbers representing the meaning of the document.

```python
[0.12, -0.43, 0.78, ...]
```

Used for:

```text
Similarity Search
```

### Metadata

Extra information about the document.

```python
{
    "source": "python.txt",
    "topic": "programming"
}
```

Used mainly for:

```text
Filtering
Organization
Identification
```

### Easy memory

```text
Document  → WHAT is the information?
Embedding → WHAT DOES IT MEAN?
Metadata  → DETAILS about the information
```

---

## 2. How Metadata Helps

Embeddings find semantically similar documents.

Metadata can filter the documents.

Example:

```python
collection.query(
    query_texts=["How do I build an API?"],
    where={"topic": "backend"},
    n_results=3
)
```

Conceptually:

```text
User Query
    ↓
Metadata Filter
    ↓
Relevant Candidates
    ↓
Embedding Similarity
    ↓
Top Results
```

### Important

```text
Embedding → similarity / ranking
Metadata  → filtering / organization
```

Metadata does not automatically understand that a document is about "backend".

Your application provides the metadata.

---

## 3. Automating Metadata

Metadata can be entered manually:

```python
{
    "source": "fastapi.txt",
    "topic": "backend"
}
```

But real applications can generate metadata automatically.

### Get filename

```python
from pathlib import Path

file = Path("notes/fastapi.txt")

metadata = {
    "source": file.name
}
```

Output:

```python
{
    "source": "fastapi.txt"
}
```

### Get filename without extension

```python
file.stem
```

Example:

```text
fastapi.txt
    ↓
fastapi
```

Useful for chunk IDs:

```python
ids.append(f"{file.stem}-{i}")
```

Result:

```text
fastapi-0
fastapi-1
fastapi-2
```

### Metadata can come from

```text
Filename      → source
Folder        → category/topic
Database      → user/date/etc.
Chunking      → page/chunk number
AI classifier → predicted topic
```

---

## 4. IDs

An ID uniquely identifies a stored document/chunk.

```python
ids = ["doc1", "doc2", "doc3"]
```

Example:

```python
collection.add(
    ids=["doc1"],
    documents=["Python is a programming language."]
)
```

IDs must be unique inside a collection.

### Chunk IDs

```python
ids.append(f"{file.stem}-{i}")
```

For `python.txt`:

```text
python-0
python-1
python-2
```

Think:

```text
ID → WHO is this?
```

---

## 5. Collections

A collection is a container for related documents.

```python
collection = client.get_or_create_collection(
    name="notes"
)
```

Example:

```text
Chroma
  ↓
notes collection
  ├── doc1
  ├── doc2
  ├── doc3
  └── doc4
```

You can have different collections:

```text
programming_notes
college_notes
company_docs
research_papers
```

Think:

```text
Collection → container/group of records
```

---

## 6. Adding Documents to Chroma

Basic example:

```python
collection.add(
    ids=["doc1", "doc2"],
    documents=[
        "Python is a programming language.",
        "FastAPI is a Python framework for building APIs."
    ],
    metadatas=[
        {
            "source": "python.txt",
            "topic": "programming"
        },
        {
            "source": "fastapi.txt",
            "topic": "backend"
        }
    ]
)
```

Each record contains:

```text
ID
Document
Embedding
Metadata
```

Conceptually:

```text
doc1
├── Document
├── Embedding
└── Metadata

doc2
├── Document
├── Embedding
└── Metadata
```

---

## 7. Chroma Storage Mental Model

```text
                    CHROMA
                       ↓
                  COLLECTION
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
            doc1              doc2
              ↓                 ↓
        ┌─────┼─────┐     ┌─────┼─────┐
        ID   DOC   META    ID   DOC   META
                    ↓
                EMBEDDING
```

Example record:

```python
{
    "id": "fastapi-0",

    "document": "FastAPI is a Python framework.",

    "embedding": [0.12, -0.43, 0.78, ...],

    "metadata": {
        "source": "fastapi.txt",
        "topic": "backend"
    }
}
```

---

## 8. Querying

Search using natural language:

```python
results = collection.query(
    query_texts=["How do I build an API?"],
    n_results=2
)
```

Conceptually:

```text
Query
  ↓
Query Embedding
  ↓
Similarity Search
  ↓
Most Similar Documents
```

You can also filter metadata:

```python
results = collection.query(
    query_texts=["How do I build an API?"],
    where={"topic": "backend"},
    n_results=2
)
```

---

## 9. Important Revision

```text
DOCUMENT
Actual text
        ↓
EMBEDDING
Meaning represented as numbers
        ↓
VECTOR DATABASE
Stores/searches embeddings
        ↓
METADATA
Extra information used for filtering/organization
        ↓
ID
Unique identifier
        ↓
COLLECTION
Container for related records
```

### The most important distinction

```text
Embedding → "Is this document semantically similar?"
Metadata  → "Should this document be included/filtered?"
ID        → "Which exact document is this?"
Document  → "What is the actual content?"
```

---

## 10. Day 34 Final Mental Model

```text
Documents
    ↓
Split into chunks
    ↓
Create IDs
    ↓
Create metadata
    ↓
Create embeddings
    ↓
Store in Chroma
    ↓
        ┌─────────────────────┐
        │ ID                  │
        │ Document            │
        │ Embedding           │
        │ Metadata            │
        └─────────────────────┘
                    ↓
              User Query
                    ↓
            Metadata Filter
                    ↓
          Similarity Search
                    ↓
             Relevant Chunks
```

## 🧠 One-Line Revision

> A vector database stores **documents, embeddings, IDs, and metadata**; embeddings help find similar meaning, while metadata helps filter and organize the stored information.

## ✅ Day 34 Checklist

* [x] Documents vs embeddings
* [x] What metadata is
* [x] Why metadata matters
* [x] How metadata can be automated
* [x] IDs
* [x] `file.stem`
* [x] Collections
* [x] Adding documents to Chroma
* [x] Storing metadata alongside documents
* [x] Querying Chroma
* [x] Metadata filtering

## 🔥 Next

**Day 35 → Similarity Search + Metadata Filtering + Better Retrieval**
