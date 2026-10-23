
from pathlib import Path

import chromadb
import ollama
from chromadb.utils import embedding_functions


# Locate the existing database regardless of the terminal directory.
DB_PATH = Path(__file__).resolve().parent / "chroma_db"

client = chromadb.PersistentClient(path=str(DB_PATH))

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
DISTANCE_THRESHOLD = 0.7
SYSTEM_PROMPT = """
You answer questions using the document context provided by the user.

Instructions:
1. Read the context carefully.
2. Answer the question using relevant information from the context.
3. If the context directly contains the answer, give that answer.
4. Only say "I couldn't find that information in the provided documents."
   if the context does not contain the answer.
5. Keep the answer short and clear.
"""


def answer_question(question: str, top_k: int = 1) -> dict:
    """Retrieve relevant passages and generate an answer with Gemma."""

    results = collection.query(
        query_texts=[question],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"]
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    sources = []
    context_parts = []

    for document, metadata, distance in zip(
        documents, metadatas, distances
    ):
        if distance > DISTANCE_THRESHOLD:
            continue

        source = metadata.get("source", "Unknown")
        page = metadata.get("page", 0)

        sources.append({
            "source": source,
            "page": page,
            "distance": round(float(distance), 4)
        })

        context_parts.append(
            f"Source: {source}, page {page}\nContent: {document}"
        )

    if not context_parts:
        return {
            "answer": (
                "I couldn't find that information "
                "in the provided documents."
            ),
            "sources": []
        }

    context = "\n\n".join(context_parts)

    response = ollama.chat(
        model=MODEL,
        options={"temperature": 0},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Document context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ]
    )

    return {
        "answer": response["message"]["content"],
        "sources": sources
    }


# Run the interactive chatbot only when this file is executed directly.
if __name__ == "__main__":
    print("College/Documentation RAG Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        result = answer_question(question)

        print("\nAssistant:", result["answer"])
        print("Sources:", result["sources"])
        print("-" * 50)
