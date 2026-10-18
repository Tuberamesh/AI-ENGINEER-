# Day 40 — Vector Database + Retrieval

## What I learned

- ChromaDB stores document chunks and their embeddings.
- Semantic search retrieves chunks related to a question.
- query_texts accepts a natural-language query.
- n_results controls the number of results returned.
- documents contains retrieved text chunks.
- metadatas contains source information.
- distances indicate how far retrieved results are from the query.
- Lower distance generally means a closer match for this setup.

## Implementation

Created vector_store.py using the existing ChromaDB database.

Test query: What is RAG?

Top result: ai_engineering.txt

The script displays each result's source, distance, and passage.

## Important distinction

file.stem returns the filename without its extension.
file.name returns the filename with its extension.

The source filename appears because ingest.py stores file.name
in the document metadata.

## Result

Successfully queried ChromaDB and retrieved relevant document chunks.

## Next step

Use retrieved context to generate answers with an LLM.
