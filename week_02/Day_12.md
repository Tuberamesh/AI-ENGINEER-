# DAY 12 — 🔥 Build: AI Text Utility

## 🎯 Goal

Today I combined the Python concepts learned during Week 2 into one small real-world project.

Instead of learning another isolated Python topic, I built a simple **AI Text Utility** that:

1. Takes a text paragraph
2. Analyzes the text
3. Counts words
4. Counts characters
5. Extracts simple keywords
6. Calls an external API
7. Handles API errors
8. Saves the result as JSON
9. Displays the result

---

# 🧠 What I Built

The project structure is:

```text
ai-text-utility/
│
├── main.py
├── text_utils.py
├── api_utils.py
├── result.json
├── .env
├── .gitignore
└── requirements.txt
```

### What each file does

| File               | Purpose                                  |
| ------------------ | ---------------------------------------- |
| `main.py`          | Main program that connects everything    |
| `text_utils.py`    | Functions for text analysis              |
| `api_utils.py`     | Function for making API requests         |
| `result.json`      | Stores the final result                  |
| `.env`             | Stores configuration/secrets when needed |
| `.gitignore`       | Prevents unwanted files/secrets from Git |
| `requirements.txt` | Lists external Python packages           |

---

# 🏗️ Project Architecture

The basic flow is:

```text
                    main.py
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
    text_utils.py             api_utils.py
          │                         │
          ↓                         ↓
   Analyze the text             Call API
          │                         │
          └────────────┬────────────┘
                       ↓
                  main.py
                       │
                       ↓
                 result dictionary
                       │
                       ↓
                  result.json
                       │
                       ↓
                    Output
```

The important idea is:

> `main.py` controls the application, while other modules contain reusable logic.

---

# 1️⃣ `text_utils.py`

I created separate functions for text processing.

```python
def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    return len(text)


def extract_keywords(text):
    words = text.lower().split()

    keywords = []

    for word in words:
        word = word.strip(".,!?;:")

        if len(word) > 4 and word not in keywords:
            keywords.append(word)

    return keywords[:5]
```

---

# 🔹 `word_count()`

```python
def word_count(text):
    words = text.split()
    return len(words)
```

### How it works

If:

```text
"Python is amazing for AI"
```

Then:

```python
text.split()
```

produces:

```text
["Python", "is", "amazing", "for", "AI"]
```

Then:

```python
len(words)
```

returns:

```text
5
```

So:

```python
word_count(text)
```

returns the number of words.

---

# 🔹 `character_count()`

```python
def character_count(text):
    return len(text)
```

`len(text)` counts the characters in the complete string.

Example:

```python
character_count("Hello")
```

returns:

```text
5
```

---

# 🔹 `extract_keywords()`

```python
def extract_keywords(text):
    words = text.lower().split()

    keywords = []

    for word in words:
        word = word.strip(".,!?;:")

        if len(word) > 4 and word not in keywords:
            keywords.append(word)

    return keywords[:5]
```

This function performs simple keyword extraction.

### Step 1 — Convert to lowercase

```python
text.lower()
```

Example:

```text
"Python PYTHON python"
```

becomes:

```text
"python python python"
```

This helps treat different capitalizations as the same word.

---

### Step 2 — Split the text

```python
text.lower().split()
```

Example:

```text
"Python is amazing for AI applications."
```

becomes:

```python
["python", "is", "amazing", "for", "ai", "applications."]
```

---

### Step 3 — Remove punctuation

```python
word.strip(".,!?;:")
```

For example:

```text
"applications."
```

becomes:

```text
"applications"
```

`strip()` removes the specified characters from the **beginning and end** of a string.

It does not remove punctuation from the middle.

---

### Step 4 — Check word length

```python
len(word) > 4
```

Only words with more than 4 characters are considered.

For example:

```text
"AI"       ❌
"is"       ❌
"Python"   ✅
"amazing"  ✅
```

---

### Step 5 — Avoid duplicates

```python
word not in keywords
```

This prevents the same keyword from being added multiple times.

Both conditions must be true:

```python
if len(word) > 4 and word not in keywords:
```

Meaning:

```text
Word must have more than 4 characters
AND
Word must not already exist in keywords
```

---

### Step 6 — Keep only 5 keywords

```python
return keywords[:5]
```

This returns a maximum of 5 keywords.

---

# 2️⃣ Importing Functions Between Modules

In `main.py`, I imported the functions from `text_utils.py`:

```python
from text_utils import word_count, character_count, extract_keywords
```

A `.py` file can act as a **Python module**.

Because `text_utils.py` is in the same project folder, `main.py` can import its functions.

Instead of writing the same logic again in `main.py`, I can simply call:

```python
word_count(text)
character_count(text)
extract_keywords(text)
```

This demonstrates **code reuse and separation of responsibilities**.

---

# 3️⃣ `api_utils.py`

I created another module for API-related logic.

```python
import requests


def get_api_data():
    url = "https://jsonplaceholder.typicode.com/users/6"

    try:
        response = requests.get(url)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

        return None
```

---

# 🔹 Why create `api_utils.py`?

Instead of putting API code directly inside `main.py`, I separated it.

```text
main.py
    ↓
Controls the application

api_utils.py
    ↓
Handles API communication
```

This makes the project easier to understand and maintain.

---

# 🔹 Calling the API Function

In `main.py`:

```python
from api_utils import get_api_data
```

This imports the function.

Then:

```python
api_data = get_api_data()
```

calls the function.

---

# 🔄 Important Python Execution Flow

When Python reaches:

```python
api_data = get_api_data()
```

execution jumps into the function:

```python
def get_api_data():
```

Then Python executes the lines inside the function from **top to bottom**.

```text
main.py
   ↓
get_api_data()
   ↓
api_utils.py
   ↓
url = "..."
   ↓
requests.get(url)
   ↓
API request
   ↓
response received
   ↓
response.raise_for_status()
   ↓
return response.json()
   ↓
BACK TO main.py
   ↓
api_data = returned result
```

The important concept is:

> A function's body runs when the function is called.

Simply defining:

```python
def get_api_data():
```

does not execute the function.

It executes only when:

```python
get_api_data()
```

is reached.

---

# 🔹 Why Does Python Execute `api_data = get_api_data()` Before the Print?

Python executes code from **top to bottom**.

For example:

```python
print(api_data)

api_data = get_api_data()
```

This causes an error because Python tries to use `api_data` before it has been created.

```text
print(api_data)
      ↓
"Where is api_data?"
      ↓
Not created yet
      ↓
NameError
```

Python does not look ahead and think:

> "I will create this variable later."

It executes the current line first.

Therefore this is correct:

```python
api_data = get_api_data()

print("API Data:", api_data)
```

---

# 4️⃣ HTTP Request

The API request is made using:

```python
response = requests.get(url)
```

`requests.get()` sends an HTTP **GET request** to the URL.

The API returns a response.

That response is stored in:

```python
response
```

---

# 5️⃣ Checking for HTTP Errors

I used:

```python
response.raise_for_status()
```

This checks whether the HTTP response indicates an error.

For example:

```text
200 → successful
404 → resource not found
500 → server error
```

If the response represents an HTTP error, an exception can be raised.

---

# 6️⃣ Exception Handling

The API request is inside:

```python
try:
    ...
except requests.exceptions.RequestException as error:
    ...
```

The purpose is to prevent the entire application from crashing because of a request problem.

### Normal situation

```text
try
 ↓
API request
 ↓
successful
 ↓
return JSON
```

### Error situation

```text
try
 ↓
API request
 ↓
ERROR
 ↓
except
 ↓
print error
 ↓
return None
```

This uses the exception-handling concepts learned on Day 9.

---

# 7️⃣ JSON Response

The API response is converted into Python data using:

```python
response.json()
```

For example, the API might return JSON like:

```json
{
    "id": 6,
    "name": "Leanne Graham",
    "username": "Bret"
}
```

Python can work with this data like a dictionary.

---

# 8️⃣ Saving Results to JSON

I used the `json` module in `main.py`:

```python
import json
```

Then created a dictionary:

```python
result = {
    "text": text,
    "word_count": words,
    "character_count": characters,
    "keywords": keywords,
    "api_data": api_data
}
```

Then saved it:

```python
with open("result.json", "w") as file:
    json.dump(result, file, indent=4)
```

---

# 🔹 How JSON Saving Works

```text
Python dictionary
       ↓
json.dump()
       ↓
result.json
```

The `"w"` means:

```text
write mode
```

The file is created or overwritten.

`indent=4` makes the JSON easier for humans to read.

---

# 9️⃣ Complete `main.py`

The main application connects all the pieces:

```python
import json

from text_utils import word_count, character_count, extract_keywords
from api_utils import get_api_data


text = "Python is amazing for building AI applications."

words = word_count(text)
characters = character_count(text)
keywords = extract_keywords(text)

api_data = get_api_data()


result = {
    "text": text,
    "word_count": words,
    "character_count": characters,
    "keywords": keywords,
    "api_data": api_data
}


with open("result.json", "w") as file:
    json.dump(result, file, indent=4)


print("\n--- Text Analysis ---")
print("Words:", words)
print("Characters:", characters)
print("Keywords:", keywords)
print("API Data:", api_data)
```

---

# 🔟 Complete Application Flow

This is the complete execution flow I built:

```text
                    START
                      ↓
                  main.py
                      ↓
             Define input text
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
    word_count()  character_count() extract_keywords()
          ↓           ↓           ↓
       words      characters     keywords
          └───────────┼───────────┘
                      ↓
              get_api_data()
                      ↓
                api_utils.py
                      ↓
              requests.get()
                      ↓
                 API response
                      ↓
             raise_for_status()
                      ↓
               response.json()
                      ↓
                 api_data
                      ↓
              Create dictionary
                      ↓
                 result = {}
                      ↓
              Save as result.json
                      ↓
                  Print output
                      ↓
                    END
```

---

# 🧠 What I Learned Today

### Python

* How to combine multiple Python modules
* How imports work
* How functions are called
* How execution moves between files
* How return values come back to the caller
* How dictionaries can hold different types of data
* How JSON can be saved to a file
* How `with open()` works
* How exceptions can handle API failures

### APIs

* How Python makes an HTTP GET request
* How `requests.get()` works
* What an HTTP response is
* Why status codes matter
* How `raise_for_status()` detects HTTP errors
* How `response.json()` converts JSON into Python data
* How API logic can be separated into its own module

### Software Engineering

* Separation of responsibilities
* Reusable functions
* Modular project structure
* Keeping the main program clean
* Handling failures instead of letting the application crash
* Saving application output

---

# 🔗 How Day 12 Combines Week 2

Day 12 is the integration day for everything learned during Week 2.

| Day    | Concept                        | Used in Day 12          |
| ------ | ------------------------------ | ----------------------- |
| Day 7  | Functions                      | ✅                       |
| Day 7  | Modules                        | ✅                       |
| Day 7  | Packages                       | ✅                       |
| Day 7  | Virtual environment            | ✅                       |
| Day 8  | Dictionaries                   | ✅                       |
| Day 8  | JSON                           | ✅                       |
| Day 8  | File handling                  | ✅                       |
| Day 9  | Exceptions                     | ✅                       |
| Day 9  | Environment variables / `.env` | Project structure ready |
| Day 10 | HTTP                           | ✅                       |
| Day 10 | `requests`                     | ✅                       |
| Day 10 | API responses                  | ✅                       |
| Day 11 | Type hints                     | Learned separately      |
| Day 11 | Async basics                   | Learned separately      |
| Day 12 | Project integration            | 🔥                      |

The main goal was not to force every single concept into one project.

The goal was to understand how the concepts work together in a real Python application.

---

# ▶️ How to Run

From the `ai-text-utility` folder:

```bash
python main.py
```

The program analyzes the text, calls the API, saves the result, and displays the output.

---

# 🎯 Final Takeaway

The biggest lesson from Day 12 is that real projects are not usually one giant Python file.

Instead:

```text
main.py
   ↓
controls the application

text_utils.py
   ↓
handles text logic

api_utils.py
   ↓
handles API logic

result.json
   ↓
stores output
```

Each part has a responsibility.

This makes the application easier to:

* understand
* test
* reuse
* debug
* maintain
* expand

**Day 12 complete. 🚀**
