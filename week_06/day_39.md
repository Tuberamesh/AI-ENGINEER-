# Day 39 — Chunking + Embeddings

## What I learned

- Chunking splits long documents into smaller text pieces.
- Chunk size controls how much text each chunk contains.
- Overlap preserves context between neighboring chunks.
- Embeddings convert text into numerical vectors.
- Similar meanings can have similar embedding representations.
- RAG uses embeddings to retrieve relevant document chunks.

## Implementation

- Source: Module 2 FDS.pdf
- Chunk size: 300 characters
- Overlap: 50 characters
- Embedding model: all-MiniLM-L6-v2
- Vector dimensions: 384
- Total chunks generated: 121

## Result

Successfully extracted PDF text, created overlapping chunks,
and generated local embeddings.

## Next step

Store document chunks and their embeddings in a vector database
for semantic search in the RAG pipeline.
