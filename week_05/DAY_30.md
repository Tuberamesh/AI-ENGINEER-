# Day 30 — Embedding Models + Chunking

## 1. What Is an Embedding Model?

* An embedding model converts text into a numerical vector.
* The vector represents the semantic meaning of the input.
* Example: "Python is easy to learn" → [0.21, -0.45, 0.78, ...]
* The values themselves are not human-readable meanings.
* The complete vector is used by machines for comparison and similarity-based tasks.

## 2. Embedding Model vs LLM

* Embedding model: converts information into numerical vectors.
* LLM: understands context and generates text.
* Embedding models are mainly used for representation and similarity.
* LLMs are mainly used for generation, reasoning, summarization, and conversation.

## 3. Input → Embedding Vector

* Input text is passed to an embedding model.
* The model produces one vector for that input.
* Example: Text → Embedding Model → Vector.
* A vector may look like [0.21, -0.45, 0.78, ...].
* The vector can then be compared with other vectors.

## 4. Embedding Dimensions

* Embedding dimension means the number of values in an embedding vector.
* A 768-dimensional embedding contains 768 numerical values.
* Dimension does not mean the number of words or concepts.
* It simply describes the size of the vector representation.

## 5. Why Not Embed an Entire Huge Document?

* A huge document can contain many different topics.
* One embedding for the entire document gives only one representation.
* It becomes difficult to retrieve one specific piece of information.
* Example: A 100-page document may contain the required answer on page 73.
* Instead of embedding the entire document as one vector, we split it into smaller chunks.

## 6. What Is Chunking?

* Chunking means splitting a large document into smaller pieces called chunks.
* Each chunk contains a smaller portion of the original document.
* Each chunk can then receive its own embedding.
* Example: Large Document → Chunk 1, Chunk 2, Chunk 3, Chunk 4.
* Chunking makes specific information easier to retrieve.

## 7. Why Does Chunk Size Matter?

* Chunks that are too small may lose important context.
* Chunks that are too large may contain too much unrelated information.
* Good chunking tries to keep enough context while keeping the information focused.
* There is no single perfect chunk size for every RAG application.
* Chunk size depends on the document type and use case.

## 8. Chunk Overlap

* Chunk overlap means repeating some text between neighboring chunks.
* Example: Chunk 1 contains A B C D E and Chunk 2 contains D E F G H.
* D and E are the overlapping information.
* Overlap helps preserve context when an important idea crosses a chunk boundary.

## 9. Basic Chunking Strategies

* Fixed-size chunking splits text using a target number of characters or tokens.
* Sentence-based chunking splits text around sentence boundaries.
* Paragraph-based chunking splits text around paragraph boundaries.
* Recursive chunking tries to preserve meaningful text boundaries while respecting a target chunk size.
* Recursive character splitting is commonly used in beginner RAG implementations.

## 10. Tools for Chunking

* Chunking can be implemented manually or using libraries.
* LangChain provides text splitters such as Recursive Character Text Splitter.
* LlamaIndex provides built-in document and node splitting utilities.
* Tools automate the splitting process, but the developer still needs to choose suitable chunking settings.

## 11. What Is Retrieval?

* Retrieval means finding and bringing back information relevant to a user's query.
* In RAG, retrieval usually means finding the most relevant document chunks.
* Example: User asks "What is the refund policy?" → system searches stored chunks → relevant refund chunks are retrieved.

## 12. How Embeddings Help Retrieval

* Each document chunk can be converted into an embedding.
* The user's question can also be converted into an embedding.
* The question embedding can be compared with stored chunk embeddings.
* Similarity search helps identify the chunks that are semantically related to the question.
* The relevant chunks are then retrieved for the LLM.

## 13. How Chunking and Embeddings Connect to RAG

* Chunking prepares a large document by breaking it into smaller searchable pieces.
* Embeddings convert those chunks into numerical vectors.
* The vectors can be stored in a vector database.
* A user's question is converted into a query embedding.
* Similarity search finds relevant stored chunks.
* Retrieval brings those chunks back.
* The retrieved chunks are provided to the LLM.
* The LLM uses the retrieved context to generate the answer.

## 14. Basic RAG Flow

* Large Document → Chunking → Small Chunks → Embeddings → Vector Database.
* User Question → Query Embedding → Similarity Search.
* Similarity Search → Relevant Chunks → LLM.
* LLM → Final Answer.

## 15. Key Takeaway

* Embedding model = converts information into vectors.
* Embedding dimension = number of values in a vector.
* Chunking = splitting large documents into smaller pieces.
* Chunk size = controls how much information each chunk contains.
* Chunk overlap = preserves context between neighboring chunks.
* Retrieval = finds relevant chunks.
* RAG = retrieves relevant information and gives it to an LLM to generate a grounded answer.

## 16. Day 30 Revision Line

* Large Document → Chunk → Embed → Store → Query → Embed Query → Similarity Search → Retrieve → LLM → Answer.
