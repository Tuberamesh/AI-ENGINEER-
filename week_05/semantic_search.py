# from pathlib import Path

# notes_folder = Path("notes")

# for file in notes_folder.glob("*.txt"):
#     text = file.read_text()

#     print(f"\n--- {file.name} ---")
#     print(text)


# from pathlib import Path

# notes_folder = Path("notes")

# for file in notes_folder.glob("*.txt"):
#     text = file.read_text()

#     chunks = text.split("\n\n")

#     print(f"\n--- {file.name} ---")

#     for chunk in chunks:
#         print("CHUNK:", chunk)



# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("all-MiniLM-L6-v2")
# text = "Docker runs applications inside containers"

# embedding = model.encode(text)

# print(embedding)
# print("Vector length:", len(embedding))




# from pathlib import Path
# from sentence_transformers import SentenceTransformer

# notes_folder = Path("notes")

# model = SentenceTransformer("all-MiniLM-L6-v2")

# for file in notes_folder.glob("*.txt"):
#     text = file.read_text()

#     chunks = text.split("\n\n")

#     for chunk in chunks:
#         embedding = model.encode(chunk)

#         print("\nCHUNK:", chunk)
#         print("VECTOR LENGTH:", len(embedding))


from pathlib import Path
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")
notes_folder = Path("notes")
documents = []

for file in notes_folder.glob("*.txt"):
    text = file.read_text()

    chunks = text.split("\n\n")

    for chunk in chunks:
        embedding = model.encode(chunk)

        documents.append({
            "text": chunk,
            "embedding": embedding
        })
print("Stored chunks:", len(documents))

query = "How do I containerize an application?"

query_embedding = model.encode(query)
best_score = -1
best_chunk = None

for doc in documents:
    score = cos_sim(query_embedding, doc["embedding"]).item()

    if score > best_score:
        best_score = score
        best_chunk = doc["text"]

print("\nBest match:")
print(best_chunk)
print("Score:", best_score)