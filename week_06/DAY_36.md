
# DAY 36 — Indexing + Retrieval Pipeline

## 🎯 Goal

Understand how a vector database searches large numbers of embeddings efficiently.

---

## 1. Why Indexing?

Without an index:

```text
Query
 ↓
Compare with every vector
 ↓
1,000,000 vectors
 ↓
Slow
```

With an index:

```text
Query
 ↓
Index
 ↓
Find promising vectors
 ↓
Similarity Search
 ↓
Top-K Results
```

**Index = a structure that helps vector search find relevant vectors faster.**

---

## 2. What is a Vector Index?

A vector index organizes embeddings in a way that makes **nearest/similar vector search faster**.

It is NOT simply sorting vectors.

```text
Embeddings
   ↓
Vector Index
   ↓
Fast similarity search
```

With millions of vectors, checking every vector can be expensive.

---

## 3. ANN — Approximate Nearest Neighbor

**ANN = Approximate Nearest Neighbor**

Instead of checking every vector, ANN search uses an index to quickly find vectors that are likely to be the nearest/similar ones.

```text
Exact Search

Query
 ↓
Check ALL vectors
 ↓
Exact nearest vectors
```

```text
ANN Search

Query
 ↓
Index
 ↓
Likely nearest vectors
 ↓
Top-K results
```

**Approximate** means the search prioritizes speed and may not guarantee the mathematically exact nearest vector.

### Remember

```text
ANN = fast search for approximately nearest vectors
```

---

## 4. How Chroma Handles Indexing

You normally DON'T build the index manually.

Chroma handles the storage and retrieval machinery.

```python
import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="notes"
)
```

When adding vectors:

```python
collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)
```

Conceptually:

```text
Documents
   ↓
Chunks
   ↓
Embeddings
   ↓
Chroma
   ↓
Storage + Index
```

Chroma manages the underlying indexing/retrieval system.

---

## 5. Retrieval

Search using:

```python
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)
```

Conceptually:

```text
Query
 ↓
Query Embedding
 ↓
Chroma
 ↓
Index / ANN Search
 ↓
Similarity Search
 ↓
Top-K Results
```

---

## 6. What is Top-K?

`n_results=2` means:

> Return the **2 most relevant chunks**.

```python
n_results=2
```

Example:

```text
Chunk 1 → similarity 0.92
Chunk 2 → similarity 0.87
Chunk 3 → similarity 0.61
```

Top 2:

```text
Chunk 1
Chunk 2
```

### Important

```text
Top-K = number of relevant chunks returned
```

It does NOT mean:

```text
❌ 2 lines from one document
❌ 2 sentences
❌ 2 original files necessarily
```

If one original document was split into multiple chunks, Top-K operates on those **chunks/vectors**.

---

## 7. Metadata vs Similarity

Metadata can be used for filtering.

Example:

```python
metadatas=[
    {"topic": "API"},
    {"topic": "Vector DB"},
    {"topic": "Python"}
]
```

Filter:

```python
where={"topic": "API"}
```

Think:

```text
Metadata → What should be searched?

Vector similarity → What is most similar?
```

---

## 8. Complete Retrieval Pipeline

```text
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
Chroma
    ↓
Indexed Storage
    ↓
User Query
    ↓
Query Embedding
    ↓
ANN / Similarity Search
    ↓
Rank Results
    ↓
Top-K Chunks
```

---

## 9. Minimal Chroma Retrieval Example

```python
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print(results["documents"])
print(results["metadatas"])
```

This asks Chroma:

```text
"Find the 3 most relevant chunks for this query."
```

---

## 🧠 Quick Revision

### Index

```text
Index = makes vector search faster
```

### ANN

```text
ANN = approximate nearest-neighbor search
```

### Top-K

```text
Top-K = number of relevant chunks returned
```

### Chroma

```text
Chroma = storage + indexing + retrieval
```

### Main idea

```text
Query
 ↓
Index
 ↓
Find likely similar vectors
 ↓
Similarity
 ↓
Top-K
```

---

## 🔥 Interview Answer

**Q: Why do vector databases use indexes?**

> Searching millions of vectors one by one can be expensive. Vector indexes help narrow the search to likely similar vectors, making similarity search much faster. Techniques such as ANN are commonly used for this.

**Q: Do you manually implement the index in Chroma?**

> No. Chroma manages the underlying storage and indexing/retrieval mechanisms. I mainly interact with it through collection add and query operations.

**Q: What does Top-K mean?**

> Top-K is the number of most relevant chunks returned by the vector search.

---

## 🎯 Day 36 Final Mental Model

```text
Documents
   ↓
Chunks
   ↓
Embeddings
   ↓
Chroma
   ↓
Index
   ↓
Query Embedding
   ↓
ANN Search
   ↓
Similarity
   ↓
Top-K Chunks
```
