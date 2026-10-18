import chromadb
import ollama
from chromadb.utils import embedding_functions

# 1. Connect to our existing ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

embedding_function = (
    embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

collection = client.get_collection(
    name="knowledge",
    embedding_function=embedding_function
)

# 2. Ask the user a question
question = input("\nAsk a question about your documents: ")

# 3. Retrieve relevant passages
results = collection.query(
    query_texts=[question],
    n_results=3
)

documents = results["documents"][0]

if not documents:
    print("No relevant passages found.")
    raise SystemExit

context = "\n\n".join(documents)

# 4. Send the context and question to Gemma
response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "system",
            "content": (
                "Answer using only the provided context. "
                "If the context does not contain the answer, "
                "say: I couldn't find that information in "
                "the provided documents. Do not invent facts."
            )
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }
    ]
)

# 5. Display the answer
print("\nAnswer:")
print(response["message"]["content"])
