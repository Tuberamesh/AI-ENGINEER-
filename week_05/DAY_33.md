
# DAY 33 — Vector Databases

## What I Learned

* A vector database stores and searches vectors.
* Embeddings convert text into numerical vectors.
* Normal databases mainly search structured or exact data, while vector databases support semantic similarity search.
* A vector database can store documents, embeddings, IDs, and metadata.
* An embedding model creates the vector; the vector database stores and searches it.
* Chroma is a vector database that we used for hands-on practice.
* A collection is a container inside Chroma for related documents and vectors.
* Smaller distance means greater similarity in our Chroma search.

## Basic Workflow

Text → Embedding Model → Vector → Vector Database → Similarity Search → Relevant Document

## Install Chroma

```bash
pip install chromadb
```

## Check Installation

```bash
python -c "import chromadb; print(chromadb.__version__)"
```

## Create a Chroma Collection

```python
import chromadb

client = chromadb.Client()

collection = client.create_collection(name="python_docs")
```

## Add Documents

```python
collection.add(
    ids=["1", "2", "3"],
    documents=[
        "Python is a programming language.",
        "FastAPI is a Python framework for building APIs.",
        "Pandas is used for data analysis."
    ]
)
```

## Check Stored Documents

```python
print(collection.get())
```

## Search by Meaning

```python
results = collection.query(
    query_texts=["How can I build an API with Python?"],
    n_results=2
)

print(results)
```

## Example Result

```text
1st → FastAPI is a Python framework for building APIs.
2nd → Python is a programming language.
```

## Similarity Distance

```text
FastAPI document → 0.6056
Python document  → 0.9004
```

Smaller distance means the result is more similar to the query.

## Key Mental Model

Embedding Model = converts text into vectors.

Vector Database = stores vectors and performs similarity search.

Chroma = the vector database used in this practice.

## Final Takeaway

A vector database allows AI applications to search information based on meaning instead of relying only on exact keyword matches.
