# DAY 22 — AI Text Analyzer Project

## 🎯 Goal

Build a small **AI Text Analyzer** that takes user text and produces structured analysis containing:

* Summary
* Sentiment
* Keywords
* Category

Today we also connected **Pydantic** to the project to validate the structure and data types of the analysis result.

> Note: A real LLM API was not used today. Since an API key was unavailable, a local rule-based analyzer was used to understand the project architecture and Pydantic validation.

---

# 1. Project Architecture

The project follows this flow:

```text
User Text
    ↓
main.py
    ↓
analyze_text()
    ↓
Python result dictionary
    ↓
Pydantic validation
    ↓
AnalysisResult
    ↓
model_dump()
    ↓
JSON file
```

The project structure:

```text
ai-text-analyzer/
│
├── main.py
├── analyzer.py
├── result.json
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 2. Creating the Project

Created the project folder:

```bash
mkdir -p ai-text-analyzer
cd ai-text-analyzer
```

Created the files:

```bash
touch main.py analyzer.py result.json .env .gitignore requirements.txt README.md
```

To see hidden files such as `.env` and `.gitignore`:

```bash
ls -la
```

---

# 3. Creating the Virtual Environment

Created a Python virtual environment:

```bash
python3 -m venv .venv
```

Activated it:

```bash
source .venv/bin/activate
```

After activation, the terminal shows:

```text
(.venv)
```

This keeps the project's Python packages isolated from the system Python environment.

---

# 4. Installing Dependencies

Installed Pydantic:

```bash
pip install pydantic
```

Saved the installed packages:

```bash
pip freeze > requirements.txt
```

Pydantic is used to define and validate structured data.

---

# 5. Understanding the Analysis Result

The analyzer should produce data like:

```json
{
    "summary": "The user is highly satisfied with the product.",
    "sentiment": "positive",
    "keywords": [
        "product",
        "fast",
        "simple",
        "useful"
    ],
    "category": "product review"
}
```

This is structured data because each piece of information has a defined field.

---

# 6. Pydantic Model

Created this model in `analyzer.py`:

```python
from pydantic import BaseModel


class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
    category: str
```

This defines the expected structure.

## Meaning

```python
summary: str
```

`summary` must be a string.

```python
sentiment: str
```

`sentiment` must be a string.

```python
keywords: list[str]
```

`keywords` must be a list containing strings.

Example:

```python
["fast", "simple", "useful"]
```

```python
category: str
```

`category` must be a string.

---

# 7. Rule-Based Analyzer

Because a real LLM API was not used, a simple local analyzer was created.

```python
from pydantic import BaseModel


class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
    category: str


def analyze_text(text):
    text = text.lower()

    # Sentiment
    if "love" in text or "enjoy" in text or "good" in text:
        sentiment = "positive"

    elif "hate" in text or "bad" in text or "worst" in text:
        sentiment = "negative"

    else:
        sentiment = "neutral"

    # Keywords
    possible_keywords = [
        "product",
        "fast",
        "simple",
        "useful",
        "slow",
        "expensive",
        "cheap",
    ]

    keywords = []

    for word in possible_keywords:
        if word in text:
            keywords.append(word)

    # Category
    if "product" in text:
        category = "product review"

    elif "movie" in text:
        category = "movie review"

    elif "food" in text or "restaurant" in text:
        category = "food review"

    else:
        category = "general"

    result = {
        "summary": text,
        "sentiment": sentiment,
        "keywords": keywords,
        "category": category,
    }

    return AnalysisResult(**result)
```

---

# 8. Why `text.lower()`?

```python
text = text.lower()
```

This converts the input to lowercase.

For example:

```text
I LOVE this PRODUCT
```

becomes:

```text
i love this product
```

This makes simple keyword matching easier.

Without converting to lowercase:

```python
"love" in "I LOVE this product"
```

would be:

```text
False
```

because Python string matching is case-sensitive.

---

# 9. Sentiment Detection

The code checks simple keywords.

```python
if "love" in text or "enjoy" in text or "good" in text:
    sentiment = "positive"
```

If the text contains one of those words:

```text
positive
```

is assigned.

For negative sentiment:

```python
elif "hate" in text or "bad" in text or "worst" in text:
    sentiment = "negative"
```

Otherwise:

```python
else:
    sentiment = "neutral"
```

This is only a simple demonstration.

A real LLM would understand much more complex language.

---

# 10. Keyword Extraction

A list of possible keywords was created:

```python
possible_keywords = [
    "product",
    "fast",
    "simple",
    "useful",
    "slow",
    "expensive",
    "cheap",
]
```

Then:

```python
keywords = []

for word in possible_keywords:
    if word in text:
        keywords.append(word)
```

Example:

Input:

```text
I really enjoyed this product. It is fast, simple and very useful.
```

Possible result:

```python
[
    "product",
    "fast",
    "simple",
    "useful"
]
```

---

# 11. Category Detection

The program checks keywords to determine a simple category.

```python
if "product" in text:
    category = "product review"

elif "movie" in text:
    category = "movie review"

elif "food" in text or "restaurant" in text:
    category = "food review"

else:
    category = "general"
```

For example:

```text
This product is fast.
```

becomes:

```text
product review
```

---

# 12. Creating the Result Dictionary

The analyzer creates a normal Python dictionary:

```python
result = {
    "summary": text,
    "sentiment": sentiment,
    "keywords": keywords,
    "category": category,
}
```

At this point, `result` is just a normal Python dictionary.

Example:

```python
{
    "summary": "i really enjoyed this product",
    "sentiment": "positive",
    "keywords": ["product"],
    "category": "product review"
}
```

---

# 13. Passing Data to Pydantic

The dictionary is passed to the Pydantic model:

```python
return AnalysisResult(**result)
```

The `**` expands the dictionary.

For example:

```python
result = {
    "summary": "hello",
    "sentiment": "positive",
    "keywords": ["fast"],
    "category": "product review"
}
```

This:

```python
AnalysisResult(**result)
```

is effectively similar to:

```python
AnalysisResult(
    summary="hello",
    sentiment="positive",
    keywords=["fast"],
    category="product review"
)
```

Pydantic then validates the data against the defined schema.

---

# 14. What Pydantic Does

Pydantic checks whether the data matches the expected structure and types.

Schema:

```python
class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
    category: str
```

Expected:

```text
summary   → string
sentiment → string
keywords  → list of strings
category  → string
```

---

# 15. Testing Pydantic Intentionally

To prove that Pydantic was actually working, invalid data was intentionally created.

Normally:

```python
"keywords": keywords
```

was used.

It was intentionally changed to:

```python
"keywords": "fast"
```

But the schema says:

```python
keywords: list[str]
```

So the program received:

```text
Expected:
list[str]

Received:
str
```

---

# 16. Pydantic Validation Error

Running:

```bash
python main.py
```

produced:

```text
ValidationError: 1 validation error for AnalysisResult

keywords
Input should be a valid list
```

This proves that Pydantic was validating the data.

The important part was:

```text
keywords
Input should be a valid list
```

Pydantic identified:

```text
Field:
keywords

Expected:
list

Received:
string
```

---

# 17. Understanding the Error

The schema:

```python
keywords: list[str]
```

means:

```text
keywords
   ↓
must be a list
   ↓
each item must be a string
```

But we provided:

```python
"keywords": "fast"
```

which is:

```text
string
```

Therefore:

```text
list[str]  ← expected
str        ← received
```

Result:

```text
❌ ValidationError
```

---

# 18. Why This Is Important for AI Engineering

LLMs can produce structured-looking data, but the output can still contain incorrect types or fields.

For example, an application may expect:

```json
{
    "keywords": ["fast", "simple"]
}
```

but receive:

```json
{
    "keywords": "fast, simple"
}
```

Pydantic can validate whether the data matches the application's schema.

The general AI application flow can therefore be:

```text
User
 ↓
Prompt
 ↓
LLM
 ↓
Structured Output
 ↓
Pydantic Validation
 ↓
Application
```

---

# 19. Pydantic Does NOT Mean the AI Is Correct

This is one of the most important concepts from today.

Suppose the LLM returns:

```json
{
    "summary": "The product is terrible.",
    "sentiment": "positive",
    "keywords": ["product"],
    "category": "product review"
}
```

The structure is valid:

```text
summary   → string ✅
sentiment → string ✅
keywords  → list[str] ✅
category  → string ✅
```

So basic Pydantic validation can accept it.

But the sentiment may be logically wrong.

Therefore:

```text
Pydantic
   ↓
Checks structure/types/schema

Pydantic does NOT automatically know:
   ↓
whether the AI's conclusion is factually or semantically correct
```

---

# 20. Parsing vs Pydantic

These concepts are related but different.

## Parsing

Parsing means taking data and turning it into a usable structure.

For example:

```text
JSON string
   ↓
json.loads()
   ↓
Python dictionary
```

## Pydantic

Pydantic validates the structure and types against a schema.

```text
Python dictionary
   ↓
AnalysisResult(...)
   ↓
Validation
```

Simple comparison:

```text
Parsing
↓
"Can I turn this data into a usable structure?"

Pydantic
↓
"Does this usable structure match my expected schema?"
```

---

# 21. JSON `dump()` vs Pydantic `model_dump()`

These are different operations.

## Pydantic `model_dump()`

```python
result.model_dump()
```

Converts:

```text
Pydantic model
      ↓
Python dictionary
```

Example:

```python
AnalysisResult(...)
```

becomes:

```python
{
    "summary": "...",
    "sentiment": "...",
    "keywords": [...],
    "category": "..."
}
```

## JSON `dump()`

```python
json.dump(result.model_dump(), file, indent=4)
```

converts:

```text
Python dictionary
      ↓
JSON file
```

So:

```text
Pydantic model
      ↓
model_dump()
      ↓
Python dict
      ↓
json.dump()
      ↓
JSON file
```

---

# 22. JSON Load vs Dump

Also learned the difference between these functions:

```python
json.dump()
```

Python object → JSON file

```python
json.load()
```

JSON file → Python object

```python
json.dumps()
```

Python object → JSON string

```python
json.loads()
```

JSON string → Python object

Remember:

```text
dump  → file
dumps → string

load  → file
loads → string
```

---

# 23. `main.py`

The main program takes user input and saves the result.

```python
import json

from analyzer import analyze_text


text = input("Enter your text: ")

result = analyze_text(text)

with open("result.json", "w") as file:
    json.dump(result.model_dump(), file, indent=4)

print("Analysis saved to result.json")
```

Flow:

```text
input()
   ↓
analyze_text()
   ↓
AnalysisResult
   ↓
model_dump()
   ↓
Python dictionary
   ↓
json.dump()
   ↓
result.json
```

---

# 24. Example Input

Run:

```bash
python main.py
```

Enter:

```text
I really enjoyed this product. It is fast, simple and very useful.
```

The analyzer detects:

```text
sentiment → positive
keywords  → product, fast, simple, useful
category  → product review
```

The final JSON is saved to:

```text
result.json
```

---

# 25. Important Error We Fixed

An indentation error happened because `analyze_text()` was accidentally placed inside the Pydantic class.

Incorrect:

```python
class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
    category: str

    def analyze_text(self, text):
        ...
```

That makes `analyze_text()` a method of `AnalysisResult`.

Correct:

```python
class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    keywords: list[str]
    category: str


def analyze_text(text):
    ...
```

Here:

```text
AnalysisResult
     ↓
Pydantic model

analyze_text()
     ↓
Separate function
```

Python indentation determines structure.

---

# 26. What I Learned Today

### Python

* Functions
* Dictionaries
* Lists
* Loops
* Conditional statements
* String operations
* `**dictionary` unpacking
* File writing

### JSON

* `json.dump()`
* `json.load()`
* `json.dumps()`
* `json.loads()`
* Python dictionary → JSON
* JSON → Python dictionary

### Pydantic

* `BaseModel`
* Type annotations
* Schema definition
* Model creation
* `AnalysisResult(**result)`
* `model_dump()`
* Validation errors
* Type validation

### AI Engineering Concepts

* Structured output
* Parsing vs validation
* Schema validation
* LLM output can still contain incorrect data
* Pydantic validates structure/types
* Pydantic does not automatically fix semantic mistakes

---

# 27. Most Important Mental Model

Remember this:

```text
LLM Output
     ↓
Is the data structured?
     ↓
Parsing
     ↓
Does it match my expected schema?
     ↓
Pydantic
     ↓
Can my application safely use it?
     ↓
Application
```

And:

```text
Pydantic ≠ AI correctness checker

Pydantic = Schema/type validator
```

---

# 28. Current Project Status

The project currently uses a **local rule-based analyzer** instead of a real LLM API.

Current:

```text
User Text
   ↓
Python Rules
   ↓
Result Dictionary
   ↓
Pydantic
   ↓
JSON
```

Future real AI version:

```text
User Text
   ↓
Prompt
   ↓
LLM API
   ↓
LLM
   ↓
Structured JSON
   ↓
Pydantic
   ↓
Validated Python Object
   ↓
JSON / Application
```

The local version was useful for understanding the architecture without requiring an API key.

---

# 29. Day 22 Summary

Today I built the foundation of an **AI Text Analyzer** and learned how structured AI output can be handled safely inside a Python application.

The most important concept:

```text
LLM
 ↓
Structured Output
 ↓
Pydantic Validation
 ↓
Application
```

Pydantic does not magically make an LLM correct. It ensures that the data follows the structure and types that the application expects.

## Day 22 Status

**✅ COMPLETE**


