import chromadb

# 1. Connect to existing Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Get existing collection
collection = client.get_collection(
    name="knowledge"
)

# 3. User query
query = "What is RAG?"

# 4. Search for similar chunks
results = collection.query(
    query_texts=[query],
    n_results=3
)

# 5. Display results
for result in results["documents"][0]:
    print("-", result)