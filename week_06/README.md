# College/Documentation RAG Assistant

A local Retrieval-Augmented Generation (RAG) project that answers questions using information retrieved from personal documents, text files, and college PDFs.

The project combines semantic search with a locally running Large Language Model (LLM), helping users find answers grounded in their documents.

## Features

- Extract text from PDF documents using PyMuPDF.
- Split text into smaller chunks.
- Generate text embeddings using Sentence Transformers.
- Store and retrieve document passages using ChromaDB.
- Generate answers locally using Ollama and Gemma 3 1B.
- Ask multiple questions in one session.
- Display retrieved source filenames and page numbers when available.
- Reject weak retrieval matches using a distance threshold.
- Instruct the model to admit when the documents do not contain an answer.

## Architecture

```text
College PDFs and TXT files
          |
          v
   PDF Text Extraction
       (PyMuPDF)
          |
          v
       Chunking
          |
          v
     Embeddings
  (all-MiniLM-L6-v2)
          |
          v
       ChromaDB
          |
          v
     User Question
          |
          v
  Semantic Retrieval
          |
          v
  Relevance Threshold
          |
          v
   Retrieved Context
          |
          v
  Ollama + Gemma 3 1B
          |
          v
     Final Answer
```

## Technologies Used

- Python
- ChromaDB
- Sentence Transformers
- all-MiniLM-L6-v2
- PyMuPDF
- Ollama
- Gemma 3 1B

## Project Structure

```text
week_06/
├── README.md
├── day_39.md
├── day_40.md
├── day_41.md
└── personal-knowledge-search/
    ├── data/
    │   ├── python.txt
    │   ├── sql.txt
    │   ├── ai_engineering.txt
    │   └── Module 2 FDS.pdf
    ├── chroma_db/
    ├── ingest.py
    ├── read_pdf.py
    ├── chunk_documents.py
    ├── vector_store.py
    ├── search.py
    ├── rag_pipeline.py
    ├── requirements.txt
    └── README.md
```

*The file listing above describes the expected project layout; filenames may differ depending on your local setup.*

## Requirements

- Python installed
- Ollama installed
- Gemma 3 1B downloaded through Ollama
- Python dependencies listed in `requirements.txt`
- Documents placed in the project's `data/` directory

## Setup

### 1. Enter the project directory

```bash
cd personal-knowledge-search
```

### 2. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

If a dependency is missing, install it separately:

```bash
python -m pip install chromadb sentence-transformers pymupdf ollama
```

### 3. Start Ollama and download the model if needed

```bash
ollama pull gemma3:1b
```

### 4. Prepare the document collection

If your documents have already been ingested into ChromaDB, you can skip this step.

Otherwise, run the existing ingestion script:

```bash
python ingest.py
```

### 5. Start the assistant

```bash
python rag_pipeline.py
```

Ask questions about your documents. Type `exit` to end the session.

## Example Questions

Questions supported by the documents:

```text
What is RAG?
Define embeddings.
What is SQL used for?
```

Example of a question that may be outside the documents:

```text
What is the capital of Japan?
```

When the closest retrieved passage exceeds the configured distance threshold, the assistant declines to answer.

## How Retrieval Works

The embedding model converts text and questions into numerical vectors. ChromaDB compares these vectors and retrieves the closest passages.

The configured distance threshold rejects weak matches before the question reaches the LLM. The threshold must be evaluated against the actual documents and questions because distance values are not confidence percentages.

The LLM receives the retrieved passages and is instructed to answer from that context. Prompt instructions and a distance threshold reduce unsupported answers but do not guarantee that every answer is correct.

## Current Limitations

- The assistant works with the documents indexed in the local ChromaDB collection.
- Retrieval quality depends on document content, chunking, and embedding similarity.
- The distance threshold may reject valid questions or accept irrelevant matches if poorly calibrated.
- Answers should be checked against their cited source passages.
- Scanned PDFs may require OCR if they contain no extractable text.
- The application currently runs in the terminal rather than a web interface.

## Learning Outcomes

- Understood the RAG architecture.
- Extracted text from PDFs.
- Implemented document chunking and embeddings.
- Stored and retrieved document passages with ChromaDB.
- Connected retrieval to a local LLM using Ollama.
- Added source references and a retrieval distance threshold.
- Tested questions that are and are not answered by the indexed documents.

## Future Improvements

- Improve threshold calibration using a larger set of relevant and irrelevant questions.
- Add more college notes and documentation.
- Improve source citations and answer evaluation.
- Build a simple web interface.
- Add conversation history and document upload support.

## Author

Built as a hands-on AI Engineering learning project.
