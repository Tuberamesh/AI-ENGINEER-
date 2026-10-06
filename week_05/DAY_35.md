
# DAY 35 — Similarity Search

## 🎯 Goal

Understand how a Vector Database finds the most similar documents for a user query.

---

## 1. What is Similarity Search?

Similarity search finds stored content that is **most similar in meaning** to a query.

Example:

```text
Stored:
"FastAPI is a Python framework for building APIs."

Query:
"How can I create an API using Python?"

Result:
FastAPI document
```

The words are different, but the **meaning is similar**.

---

## 2. Core Workflow

```text
User Query
    ↓
Query Embedding
    ↓
Vector Database
    ↓
Compare Query Vector
with Stored Vectors
    ↓
Rank by Similarity / Distance
    ↓
Top-K Results
    ↓
Relevant Documents
```

---

## 3. Query → Embedding

Text cannot directly be compared mathematically.

It is converted into a vector:

```text
"How do I learn Python?"
          ↓
       Embedding
          ↓
[0.12, -0.45, 0.78, ...]
```

Stored documents also have embeddings.

```text
Document → Embedding → Vector
Query    → Embedding → Vector
```

The vector database compares these vectors.

---

## 4. Similarity vs Distance

Two common ideas:

```text
Similarity ↑  = More similar
Distance  ↓  = More similar
```

For the Chroma setup used today:

```text
Smaller distance = closer = more similar
```

Example:

```text
Result A → distance = 0.35
Result B → distance = 0.82

Result A is more similar.
```

---

## 5. What is Top-K?

`Top-K` means:

> Return the K most similar results.

Example:

```python
search("How do I learn Python?", top_k=2)
```

Means:

```text
Return the best 2 results.
```

Important:

```text
top_k
```

is our own function parameter.

Chroma uses:

```python
n_results
```

So:

```python
def search(query, top_k=2):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
```

Flow:

```text
top_k = 2
   ↓
n_results = 2
   ↓
Chroma returns 2 results
```

---

## 6. Basic Chroma Search

```python
def search(query, top_k=2):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results["documents"][0]
```

Use it:

```python
results = search("How do I learn Python?", top_k=2)

for result in results:
    print("-", result)
```

---

## 7. Why `[0]`?

Chroma returns results in a nested structure because it can handle multiple queries.

Example:

```python
results["documents"]
```

may look like:

```python
[
    [
        "Python is a programming language.",
        "Pandas is used for data analysis."
    ]
]
```

The outer list represents the query.

```python
results["documents"][0]
```

means:

> Give me the results for the first query.

So:

```text
results
   ↓
documents
   ↓
first query [0]
   ↓
actual documents
```

---

## 8. Full Search Function

```python
def search(query, top_k=2):

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results["documents"][0]


results = search(
    "How can I build an API with Python?",
    top_k=2
)

print("\nSearch Results:")

for result in results:
    print("-", result)
```

---

## 9. Testing Different Top-K

### Top 1

```python
search("How do I learn Python?", top_k=1)
```

Returns:

```text
Best 1 result
```

### Top 3

```python
search("How do I learn Python?", top_k=3)
```

Returns:

```text
Best 3 results
```

---

## 10. Important Experiment

Try an unrelated query:

```python
results = search(
    "What is the best recipe for pizza?",
    top_k=2
)

for result in results:
    print("-", result)
```

You may still get results such as:

```text
SQL document
Python document
```

Why?

Because:

```text
Top-K ≠ Guaranteed Relevant
```

The vector database is basically saying:

> "These are the closest 2 vectors I have."

It does NOT automatically know:

> "These documents are definitely relevant."

---

## 11. Top-K vs Relevance

```text
Query
  ↓
Compare with ALL stored vectors
  ↓
Rank them
  ↓
Pick Top-K
```

Even if everything is a bad match:

```text
Pizza Query
    ↓
No pizza document exists
    ↓
Closest available vectors
    ↓
Top 2 returned
```

Later, we can solve this using a **similarity/distance threshold**.

---

## 12. Inspect Full Chroma Response

Instead of:

```python
return results["documents"][0]
```

temporarily use:

```python
return results
```

Then:

```python
results = search(
    "What is the best recipe for pizza?",
    top_k=2
)

print(results)
```

Chroma can return information such as:

```text
ids
documents
distances
metadatas
```

The important one for today's concept:

```text
distances
```

Remember:

```text
Lower distance
      ↓
More similar
      ↓
Higher ranking
```

---

## 13. Similarity Search vs Normal Keyword Search

### Keyword Search

```text
Query:
"Python API"

Looks for matching words.

"FastAPI is a Python framework for building APIs."
```

### Semantic Search

```text
Query:
"How can I create an API using Python?"

Even without exact matching words,
the meaning can be matched.
```

So:

```text
Keyword Search
→ Match words

Semantic Search
→ Match meaning
```

---

## 14. Manual Search vs Vector Database

### Manual approach

```python
for doc in documents:

    score = similarity(
        query_vector,
        doc_vector
    )

    if score > best_score:
        best_score = score
        best_doc = doc
```

We manually compare vectors.

### Vector Database

```python
results = collection.query(
    query_texts=[query],
    n_results=2
)
```

The database handles the retrieval process internally.

---

## 15. The Big Picture

```text
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Database
    ↓
       ← Query
       ↓
Query Embedding
    ↓
Similarity Search
    ↓
Rank Results
    ↓
Top-K
    ↓
Relevant Context
```

This is a major part of **RAG**.

---

## 🧠 Quick Revision

```text
Similarity Search
= Find vectors closest to the query vector.

Embedding
= Text converted into a numerical vector.

Top-K
= Number of results we want.

Chroma n_results
= Chroma's parameter for Top-K.

Distance
= How far vectors are from each other.

Lower distance
= More similar in the current Chroma setup.

Semantic Search
= Search based on meaning, not just exact words.

Top-K
≠ Guaranteed relevance
```

---

## 🔥 One-Line Memory Trick

```text
Query → Embedding → Compare → Rank → Top-K → Documents
```

---

## ✅ Day 35 Checklist

* [x] Understand similarity search
* [x] Understand query embeddings
* [x] Understand vector comparison
* [x] Understand distance
* [x] Understand Top-K
* [x] Use Chroma `query()`
* [x] Build a `search()` function
* [x] Test different queries
* [x] Test different `top_k`
* [x] Understand why unrelated queries can still return results
* [x] Connect similarity search to RAG

**DAY 35 COMPLETE ✅**
