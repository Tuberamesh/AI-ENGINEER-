
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