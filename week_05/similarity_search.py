from pathlib import Path
import chromadb

# 1. Create persistent Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Create/get collection
collection = client.get_or_create_collection(
    name="notes"
)

# 3. Read notes
notes_folder = Path("notes")

documents = []
ids = []

for file in notes_folder.glob("*.txt"):
    text = file.read_text()

    chunks = text.split("\n\n")

    for i, chunk in enumerate(chunks):
        documents.append(chunk)
        ids.append(f"{file.stem}-{i}")

# 4. Store documents
collection.add(
    ids=ids,
    documents=documents
)

def search(query, top_k=2):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    # return results["documents"]
    return results


results = search("What is the best recipe for pizza?")

print("\nSearch Results:")

# for result in results:
#     print("-", result)
print(results)