

# Day 38: Introduction to RAG & PDF Text Extraction

## 1. Today's Goal

Today, I started building the document-processing part of a Retrieval-Augmented Generation (RAG) application.

Instead of only learning definitions, I worked with an actual college PDF, extracted its text using Python, and saved the extracted content into a text file.

**Project:** Personal Knowledge Search Engine
**Document:** `Module 2 FDS.pdf`
**Tools:** Python, PyMuPDF, pathlib

## 2. What Is RAG?

RAG stands for **Retrieval-Augmented Generation**.

It allows an AI application to retrieve relevant information from external documents and provide that information to an LLM as context when generating an answer.

### Example

Suppose I ask:

> Explain Principal Component Analysis (PCA) using my college notes.

A normal LLM might answer from its existing knowledge, but it does not automatically know the contents of my specific PDF.

With RAG, the application searches my indexed college notes, retrieves relevant content about PCA, and passes that content along with my question to the LLM.

The LLM then generates an answer using the supplied context and its existing knowledge.

**Important:** RAG does not inherently retrain the LLM. It retrieves relevant information at question time.

## 3. Normal LLM vs RAG

| Normal LLM                                         | RAG-based application                                   |
| -------------------------------------------------- | ------------------------------------------------------- |
| Receives a user prompt                             | Receives a user prompt and retrieved context            |
| Uses learned knowledge and supplied prompt context | Also uses relevant information retrieved from documents |
| Does not automatically search my personal PDF      | Can search an indexed PDF collection                    |
| May not know my document's contents                | Can ground answers in retrieved document content        |

RAG can improve relevance and grounding, but it does not guarantee that every answer is correct.

## 4. My First Practical Task: Extracting Text from a PDF

My project contains this PDF:

`data/Module 2 FDS.pdf`

PDF files are designed for presenting documents. To process their contents in a RAG pipeline, I first need to extract readable text.

I installed PyMuPDF:

```
python -m pip install pymupdf
```

I verified the installation:

```
python -c "import pymupdf; print('PDF library ready!')"
```

Expected output:

```
PDF library ready!
```

### Code: `read_pdf.py`

```
from pathlib import Path
import pymupdf

# Locate the PDF
pdf_path = Path("data") / "Module 2 FDS.pdf"

# Open the PDF
document = pymupdf.open(pdf_path)

# Read every page
for page_number, page in enumerate(document, start=1):
    text = page.get_text()

    print(f"\n--- Page {page_number} ---")
    print(text)

# Close the PDF
document.close()
```

### Understanding the code

**1. Import the libraries**

```
from pathlib import Path
import pymupdf
```

* `Path` helps represent and work with file paths.

* `pymupdf` provides tools for opening PDFs and extracting their text.

**2. Specify the PDF location**

```
pdf_path = Path("data") / "Module 2 FDS.pdf"
```

`Path("data")` represents the `data` directory. The `/` operator joins the directory path and filename to create the complete relative path.

**3. Open the PDF**

```
document = pymupdf.open(pdf_path)
```

This opens the PDF and gives me a document object that I can use to access its pages.

**4. Loop through the pages**

```
for page_number, page in enumerate(document, start=1):
```

`enumerate()` returns pairs containing a count and an item.

For example:

```
(1, page_object_1)
(2, page_object_2)
(3, page_object_3)
```

Python assigns the first value to `page_number` and the second value to `page`.

The variable names are my choice; their positions determine which values they receive.

I used `start=1` because PDF page numbering normally starts at 1.

**5. Extract text from the current page**

```
text = page.get_text()
```

`page.get_text()` extracts the readable text from the current page and returns it as a string.

The loop repeats this operation for every page. Each iteration assigns the current page's text to `text`.

**6. Display the page number and text**

```
print(f"\n--- Page {page_number} ---")
print(text)
```

The first statement prints a page heading. The `f` prefix allows Python to insert the current value of `page_number` into the string.

The second statement displays the extracted text.

**7. Close the PDF**

```
document.close()
```

This closes the opened document after processing is complete.

## 5. Saving All Extracted Text into One File

Printing the extracted text is useful for checking the result, but I also want to save it for further processing.

Instead of keeping only the current page's text, I need to collect the text from all pages.

### Updated code: `read_pdf.py`

```
from pathlib import Path
import pymupdf

pdf_path = Path("data") / "Module 2 FDS.pdf"
output_path = Path("data") / "Module 2 FDS_extracted.txt"

document = pymupdf.open(pdf_path)

all_text = ""

for page_number, page in enumerate(document, start=1):
    text = page.get_text()

    all_text += f"\n--- Page {page_number} ---\n"
    all_text += text

document.close()

output_path.write_text(all_text, encoding="utf-8")

print("PDF text extracted and saved successfully!")
print(f"Output file: {output_path}")
```

### New concepts learned

**1. Collecting text with** `**all_text**`

```
all_text = ""
```

This creates an empty string.

**2. Appending text using** `**+=**`

```
all_text += text
```

The `+=` operator appends text to the existing string.

For example:

* Initially: `""`

* After page 1: page 1 text

* After page 2: page 1 text + page 2 text

* After page 3: page 1 text + page 2 text + page 3 text

The page headings preserve page boundaries in the extracted text.

**3. Saving the file**

```
output_path.write_text(all_text, encoding="utf-8")
```

* `output_path` specifies where the file should be saved.

* `write_text()` writes the string into the file.

* `all_text` contains the collected text.

* `encoding="utf-8"` explicitly specifies the text encoding used when saving.

UTF-8 supports English and characters from many other languages.

If the output file already exists, `write_text()` overwrites its contents. Therefore, the script regenerates the extracted text file each time it runs.

## 6. Commands I Used

I copied the PDF into my project's `data` directory:

```
cp ~/Downloads/"Module 2 FDS.pdf" data/
```

I created and opened the Python script:

```
touch read_pdf.py
open -e read_pdf.py
```

I executed the script:

```
python read_pdf.py
```

Successful output:

```
PDF text extracted and saved successfully!
Output file: data/Module 2 FDS_extracted.txt
```

I opened the generated text file:

```
open -e "data/Module 2 FDS_extracted.txt"
```

**Result:** I successfully extracted readable text from my college PDF and saved it into a separate text file.

## 7. How This Connects to RAG

The PDF extraction task is the beginning of the document-ingestion pipeline.

```
Original PDF
    |
    v
Text Extraction
    |
    v
Extracted Text File
    |
    v
Chunking
    |
    v
Embeddings
    |
    v
Vector Database
    |
    v
Retrieve Relevant Chunks
    |
    v
Pass Context + Question to LLM
    |
    v
Generated Answer
```

### What happens in each stage?

1. **Text extraction:** Read the document's text.

2. **Chunking:** Split the extracted text into smaller pieces.

3. **Embeddings:** Convert chunks into numerical vector representations.

4. **Vector database:** Store the vectors with their associated text and metadata.

5. **Retrieval:** Find chunks relevant to a user's question.

6. **Generation:** Supply the question and retrieved context to an LLM to generate an answer.

I have already studied chunking, embeddings, and vector databases in earlier weeks. This exercise connects PDF ingestion to the rest of that pipeline.

## 8. Limitations to Remember

* `page.get_text()` extracts readable text, but a scanned PDF page may require OCR if it contains only images.

* Extracted text may not preserve the original PDF's visual layout, tables, or formatting perfectly.

* Extracting text does not create embeddings or make the document searchable by semantic similarity yet.

* The extracted text should be checked before using it in a RAG pipeline.

## 9. Day 1 Summary

Today, I learned and implemented:

* What RAG is and why external document context is useful.

* The difference between a normal LLM interaction and a RAG-based application.

* How to install and import PyMuPDF.

* How to open a PDF and extract text page by page.

* How `enumerate(document, start=1)` provides both a count and the current page object.

* How `+=` collects text across multiple iterations.

* How `Path.write_text()` saves text using UTF-8 encoding.

* How PDF text extraction fits into a complete RAG pipeline.

### Day 38 Deliverable

```
personal-knowledge-search/
├── data/
│   ├── Module 2 FDS.pdf
│   └── Module 2 FDS_extracted.txt
└── read_pdf.py
```

*The project also contains the existing ingestion, search, requirements, and vector database files from earlier work.*
