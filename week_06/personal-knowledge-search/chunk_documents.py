from pathlib import Path
from sentence_transformers import SentenceTransformer
import fitz

DATA_DIR = Path("data")
CHUNK_SIZE = 300
OVERLAP = 50

def split_text(text):
    text = " ".join(text.split())
    chunks = []
    start = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = end - OVERLAP

    return chunks

def main():
    pdf_files = list(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found inside the data folder.")
        return

    all_chunks = []

    for pdf_path in pdf_files:
        print(f"\nReading: {pdf_path.name}")

        with fitz.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf, start=1):
                text = page.get_text()
                chunks = split_text(text)

                for chunk_number, chunk in enumerate(chunks, start=1):
                    all_chunks.append({
                        "text": chunk,
                        "source": pdf_path.name,
                        "page": page_number,
                        "chunk": chunk_number,
                    })

    if not all_chunks:
        print("No text extracted. Check whether the PDF contains selectable text.")
        return

    print(f"\nTotal chunks: {len(all_chunks)}")
    print("Loading local embedding model...")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [item["text"] for item in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True)

    print(f"Embedding shape: {embeddings.shape}")
    print("\nSample chunk:")
    print(all_chunks[0]["text"])
    print("\nFirst embedding (first 5 values):")
    print(embeddings[0][:5])

    print("\nDay 39 task completed: chunking + embeddings generated.")
    print("No changes were made to ChromaDB.")

if __name__ == "__main__":
    main()
