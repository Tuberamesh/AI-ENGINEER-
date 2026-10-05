import chromadb

client = chromadb.Client()

collection = client.create_collection(name="python_docs")

collection.add(
    ids=["1", "2", "3"],
    documents=[
        "Python is a programming language.",
        "FastAPI is a Python framework for building APIs.",
        "Pandas is used for data analysis."
    ]
)

#print("Collection created:", collection.count())
#print(collection.get())

collection.get(include=["documents", "embeddings"])


results = collection.query(
    query_texts=["How can I build an API with Python?"],
    n_results=2
)

print(results)