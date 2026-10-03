
# Day 31 — Build Semantic Search

## 1. Goal
- Build a simple semantic search system over local notes.
- Semantic search finds information based on meaning, not only exact keywords.
- Example: "How do I containerize an application?" → retrieves Docker-related notes.

## 2. Notes Structure
- Create a `notes/` folder.
- Add `python.txt`, `sql.txt`, `docker.txt`, and `ai.txt`.
- Each file contains multiple paragraphs.
- 4 files × 4 paragraphs = 16 chunks.

## 3. Read Note Files
- Use `Path` to work with folders and files.
- `notes_folder = Path("notes")`
- `notes_folder.glob("*.txt")` finds all `.txt` files.
- `*` means any filename.
- `text = file.read_text()` reads the file content.

## 4. Chunking
- Chunking means splitting large text into smaller meaningful pieces.
- We split paragraphs using:
- `chunks = text.split("\n\n")`
- Each paragraph becomes one chunk.
- Smaller chunks make semantic search more precise.

## 5. Embeddings
- An embedding converts text into a numerical vector representing its meaning.
- We used the `sentence-transformers` library.
- Model: `all-MiniLM-L6-v2`
- Create the model with:
- `model = SentenceTransformer("all-MiniLM-L6-v2")`
- Create an embedding with:
- `embedding = model.encode(text)`

## 6. Vector Size
- `all-MiniLM-L6-v2` produces 384 numbers for every input text.
- Different text produces different values.
- The vector length stays 384 because the same model always produces the same output dimension.
- Important: The model decides HOW MANY numbers; the text decides WHAT those numbers are.
- Example: Docker chunk → 384 values.
- Example: SQL chunk → 384 values.
- Both have 384 values, but the values are different.

## 7. Create Embeddings For Chunks
- Read every note.
- Split every note into chunks.
- Convert every chunk into an embedding.
- Result:
- 16 chunks.
- 16 embeddings.
- 384 numbers per embedding.

## 8. Store Chunk + Vector
- We need to keep both the original chunk and its embedding.
- Create an empty list:
- `documents = []`
- Store both values:
- `documents.append({"text": chunk, "embedding": embedding})`
- The vector is used for searching.
- The original text is returned to the user after finding the match.
- This is a simple in-memory vector store for learning.

## 9. User Query
- Example query: `How do I containerize an application?`
- The query must also be converted into a vector.
- Create the query embedding with:
- `query_embedding = model.encode(query)`
- The query becomes another 384-number vector.

## 10. Why Embed The Query?
- Stored chunks are represented as vectors.
- The user question is initially text.
- Text cannot be directly compared with a vector.
- Therefore:
- Text chunk → embedding.
- User query → embedding.
- Now both are vectors in the same vector space.

## 11. Cosine Similarity
- Cosine similarity measures how closely two vectors point in the same direction.
- It can be used to measure semantic similarity between embeddings.
- Import it with:
- `from sentence_transformers.util import cos_sim`
- Calculate similarity with:
- `score = cos_sim(query_embedding, doc["embedding"]).item()`
- Higher similarity generally means the vectors are more semantically similar.

## 12. Cosine Similarity vs Similarity Search
- Cosine similarity = the calculation/measurement.
- Similarity search = the complete process of finding the most similar stored vector.
- Similarity search internally calculates similarity scores and selects the best result.

## 13. Compare Query With Stored Vectors
- Loop through every stored document.
- Calculate a similarity score for each document.
- Code:
- `for doc in documents:`
- `score = cos_sim(query_embedding, doc["embedding"]).item()`
- With 16 chunks, the query is compared against all 16 vectors.

## 14. Find The Highest Score
- Start with:
- `best_score = -1`
- `best_chunk = None`
- For every document:
- Calculate the similarity score.
- Check:
- `if score > best_score:`
- Save the new best score:
- `best_score = score`
- Save the matching text:
- `best_chunk = doc["text"]`
- After checking all chunks, `best_chunk` contains the most similar chunk.

## 15. Return The Result
- Print the best result with:
- `print("\nBest match:")`
- `print(best_chunk)`
- `print("Score:", best_score)`
- Example result:
- `Best match: Docker is a tool for packaging applications and their dependencies.`
- `Score: 0.487...`

## 16. Complete Semantic Search Flow
- Notes
- ↓
- Split into chunks
- ↓
- Create embeddings
- ↓
- Store chunk + vector
- ↓
- User asks a question
- ↓
- Create query embedding
- ↓
- Compare query vector with stored vectors
- ↓
- Calculate cosine similarity
- ↓
- Find highest score
- ↓
- Return relevant chunk

## 17. Important Code To Remember
- `model = SentenceTransformer("all-MiniLM-L6-v2")`
- `chunks = text.split("\n\n")`
- `embedding = model.encode(text)`
- `query_embedding = model.encode(query)`
- `score = cos_sim(query_embedding, doc["embedding"]).item()`
- `if score > best_score:`
- `best_score = score`
- `best_chunk = doc["text"]`

## 18. Connection To RAG
- Semantic search is a core building block of RAG.
- Basic RAG flow:
- User question → Query embedding → Vector search → Retrieve relevant chunks → Send chunks to LLM → Generate answer.
- Day 31 only builds the search/retrieval part.
- We have not built the complete RAG chatbot yet.

## 19. Final Revision
- Embedding = text represented as numbers.
- Vector = the numerical representation produced by the embedding model.
- Chunk = small piece of source text.
- Query embedding = vector representation of the user's question.
- Cosine similarity = similarity measurement between vectors.
- Similarity search = finding the most similar stored vectors.
- Semantic search = searching based on meaning.
- Core idea: Text → Embedding → Vector → Similarity → Relevant information.

