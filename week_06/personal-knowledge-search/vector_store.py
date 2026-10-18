import chromadb
from chromadb.utils import embedding_functions

# 1. Connect to the existing database
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Use the same embedding model as ingestion
embedding_function = (
    embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

# 3. Get the existing collection
collection = client.get_collection(
    name="knowledge",
    embedding_function=embedding_function
)

# 4. Ask a question
query = input("Ask a question about your documents: ")

# 5. Retrieve the 3 most relevant chunks
results = collection.query(
    query_texts=[query],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)

# 6. Display the retrieved context
print("\nRetrieved passages:\n")

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances), start=1
):
    print(f"--- Result {i} ---")
    print(f"Source: {metadata.get('source', 'Unknown')}")
    print(f"Distance: {distance:.4f}")
    print(f"Passage: {document}\n")
