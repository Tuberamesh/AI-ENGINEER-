from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions


# 1. Create persistent Chroma database
client = chromadb.PersistentClient(path="./chroma_db")


# 2. Create embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# 3. Create/get collection
collection = client.get_or_create_collection(
    name="knowledge",
    embedding_function=embedding_function
)


# 4. Find documents
data_folder = Path("data")

documents = []
ids = []
metadatas = []


# 5. Read each .txt file
for file in data_folder.glob("*.txt"):

    text = file.read_text()

    # Simple chunking for now
    chunks = [text[i:i+300] for i in range(0, len(text), 300)]

    for i, chunk in enumerate(chunks):

        documents.append(chunk)
        ids.append(f"{file.stem}-{i}")

        metadatas.append({
            "source": file.name
        })


# 6. Store documents in Chroma
collection.upsert(
    documents=documents,
    ids=ids,
    metadatas=metadatas
)


print(f"Stored {len(documents)} chunks in Chroma.")