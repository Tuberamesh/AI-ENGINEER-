
# Day 31 — Build Semantic Search

## 1. Goal
- Build a simple semantic search system over local notes.
- Semantic search finds information based on meaning instead of only exact keywords.
- Example query: "How do I containerize an application?"
- Expected result: Docker-related chunk.

## 2. Imports
- `from pathlib import Path`
- `from sentence_transformers import SentenceTransformer`
- `from sentence_transformers.util import cos_sim`

## 3. Load Embedding Model
- Use `all-MiniLM-L6-v2`.
- `model = SentenceTransformer("all-MiniLM-L6-v2")`
- This model converts text into 384-dimensional vectors.

## 4. Read Notes
- `notes_folder = Path("notes")`
- `documents = []`
- `for file in notes_folder.glob("*.txt"):`
- `    text = file.read_text()`
- `glob("*.txt")` finds all text files inside the notes folder.

## 5. Split Into Chunks
- `chunks = text.split("\n\n")`
- Every blank line separates one chunk.
- Example: 4 files × 4 chunks = 16 chunks.

## 6. Create Chunk Embeddings
- `for chunk in chunks:`
- `    embedding = model.encode(chunk)`
- Every chunk becomes a 384-number vector.

## 7. Store Chunk + Embedding
- `documents.append({"text": chunk, "embedding": embedding})`
- We store both the original text and its vector.
- The vector is used for searching.
- The original text is returned as the result.

## 8. Query
- `query = "How do I containerize an application?"`
- The user question is also converted into a vector.
- `query_embedding = model.encode(query)`
- Query embedding also contains 384 numbers.

## 9. Calculate Similarity
- Loop through every stored document.
- `for doc in documents:`
- `    score = cos_sim(query_embedding, doc["embedding"]).item()`
- Cosine similarity gives a similarity score between the query vector and each stored vector.

## 10. Find Best Match
- `best_score = -1`
- `best_chunk = None`
- `for doc in documents:`
- `    score = cos_sim(query_embedding, doc["embedding"]).item()`
- `    if score > best_score:`
- `        best_score = score`
- `        best_chunk = doc["text"]`
- The highest score becomes the best match.

## 11. Return Result
- `print("\nBest match:")`
- `print(best_chunk)`
- `print("Score:", best_score)`
- Example:
- `Best match: Docker is a tool for packaging applications and their dependencies.`
- `Score: 0.487...`

## 12. Complete Code Flow
- `from pathlib import Path`
- `from sentence_transformers import SentenceTransformer`
- `from sentence_transformers.util import cos_sim`
- `notes_folder = Path("notes")`
- `model = SentenceTransformer("all-MiniLM-L6-v2")`
- `documents = []`
- `for file in notes_folder.glob("*.txt"):`
- `    text = file.read_text()`
- `    chunks = text.split("\n\n")`
- `    for chunk in chunks:`
- `        embedding = model.encode(chunk)`
- `        documents.append({"text": chunk, "embedding": embedding})`
- `query = "How do I containerize an application?"`
- `query_embedding = model.encode(query)`
- `best_score = -1`
- `best_chunk = None`
- `for doc in documents:`
- `    score = cos_sim(query_embedding, doc["embedding"]).item()`
- `    if score > best_score:`
- `        best_score = score`
- `        best_chunk = doc["text"]`
- `print("\nBest match:")`
- `print(best_chunk)`
- `print("Score:", best_score)`

## 13. Mental Model
- Notes → Chunks → Embeddings → Store
- User question → Query embedding
- Query embedding → Compare with every stored embedding
- Cosine similarity → Similarity score
- Highest score → Best matching chunk

## 14. Important Concepts
- Chunk = small piece of text.
- Embedding = numerical representation of text meaning.
- Vector = the numbers representing the embedding.
- Query embedding = embedding of the user's question.
- Cosine similarity = measures similarity between vectors.
- Similarity search = finds the closest stored vector.
- Semantic search = search based on meaning.

## 15. Why Same Vector Size?
- `all-MiniLM-L6-v2` always produces 384 values.
- Different text produces different values.
- Same vector dimensions allow the vectors to be compared.

## 16. Cosine Similarity vs Similarity Search
- Cosine similarity = calculation/measurement.
- Similarity search = complete process.
- Search calculates similarity for stored vectors and selects the highest score.

## 17. Connection To RAG
- Semantic search is a core part of RAG.
- RAG flow:
- User question → Query embedding → Vector search → Retrieve chunks → LLM → Answer.
- Day 31 builds the search/retrieval part.
- Full RAG will be built later.

## 18. Final Takeaway
- Text → Embedding → Vector → Similarity → Relevant chunk.
- The system does not simply search for matching words.
- It compares the meaning represented by vectors.