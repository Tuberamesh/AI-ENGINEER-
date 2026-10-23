
import chromadb
import ollama
from chromadb.utils import embedding_functions

# Connect to the existing ChromaDB
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

MODEL = "gemma3:1b"
N_RESULTS = 1
DISTANCE_THRESHOLD = 0.7


SYSTEM_PROMPT = """
You are a helpful College Documentation Assistant.

Answer the user's question using the supplied document context.

IMPORTANT:
- Read the entire context carefully.
- If the context contains information that answers the question,
  give a clear and direct answer.
- You may rephrase the information in simple English.
- Do not refuse when the answer is present in the context.
- Do not add facts that are not supported by the context.
- Only if the answer is genuinely absent from the context, say:
  "I couldn't find that information in the provided documents."
"""


print("College/Documentation RAG Assistant")
print("Ask questions about your documents.")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()

    if question.lower() in {"exit", "quit"}:
        print("Goodbye, bro!")
        break

    if not question:
        continue

    # Retrieve the single closest passage
    results = collection.query(
        query_texts=[question],
        n_results=N_RESULTS,
        include=["documents", "metadatas", "distances"]
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    # Handle empty results
    if not documents:
        print(
            "\nAssistant: I couldn't find that information "
            "in the provided documents.\n"
        )
        continue

    distance = distances[0]

    # Reject weak matches before asking Gemma
    if distance > DISTANCE_THRESHOLD:
        print(f"\nBest match distance: {distance:.4f}")
        print(
            "Assistant: I couldn't find that information "
            "in the provided documents.\n"
        )
        continue

    document = documents[0]
    metadata = metadatas[0]

    source = metadata.get("source", "Unknown")
    page = metadata.get("page", 0)

    reference = f"{source}, page {page}" if page else source

    # Display the accepted source
    print("\nRetrieved source:")
    print(f"Source: {reference}")
    print(f"Distance: {distance:.4f}")
    print(f"Passage: {document[:500]}")

    # Prepare context for Gemma
    context = f"Source: {reference}\nContent: {document}"

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": (
                    f"Document context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ]
    )

    print("\nAssistant:", response["message"]["content"])
    print("\n" + "-" * 50 + "\n")
