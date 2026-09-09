# DAY 09 — Exceptions + Environment Variables

## 🎯 Goal

Learn how to make Python applications safer and more reliable by handling errors properly and keeping sensitive information such as API keys outside the source code.

---

# 1. Exceptions

An **exception** is an error that occurs while a Python program is running.

Instead of allowing the program to crash, we can handle expected errors using `try` and `except`.

## Basic Syntax

```python
try:
    # Code that may cause an error
except:
    # Code that runs when an error occurs
```

### Example

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number")
```

If the user enters:

```text
hello
```

Python normally raises a `ValueError`.

Using `except`, we can handle it gracefully.

---

# 2. try, except, else, finally

```python
try:
    # Code that may fail

except:
    # Runs if an error occurs

else:
    # Runs if there is NO error

finally:
    # Always runs
```

### Example

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

else:
    print("Number:", number)

finally:
    print("Program finished")
```

### Execution Flow

```text
try
 ↓
Error?
 ├── YES → except
 └── NO  → else
 ↓
finally
```

`finally` is useful for cleanup operations that should happen regardless of success or failure.

---

# 3. Common Python Exceptions

## ValueError

Occurs when a function receives a value of the correct type but an invalid value.

```python
age = int("hello")
```

---

## TypeError

Occurs when an operation is performed on incompatible types.

```python
result = 10 + "hello"
```

---

## KeyError

Occurs when trying to access a dictionary key that doesn't exist.

```python
student = {
    "name": "Ramesh"
}

print(student["age"])
```

---

## FileNotFoundError

Occurs when Python tries to open a file that doesn't exist.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

---

# 4. raise

`raise` allows us to intentionally generate an exception.

### Example

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative")
```

This is useful when we want to validate data and stop execution when the data is invalid.

---

# 5. Environment Variables

Sensitive information such as:

* API keys
* passwords
* database credentials
* secret tokens

should **not** be hardcoded directly into Python files.

❌ Bad practice:

```python
API_KEY = "my-secret-api-key"
```

If this code is pushed to GitHub, the secret could become exposed.

---

# 6. Using `.env`

A `.env` file can store environment variables locally.

### `.env`

```text
API_KEY=your_api_key_here
```

Python can then read the value without putting the secret directly inside the source code.

Install:

```bash
pip install python-dotenv
```

### Python

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)
```

### Flow

```text
.env
 ↓
load_dotenv()
 ↓
Environment variable
 ↓
os.getenv("API_KEY")
 ↓
Python application
```

---

# 7. Checking for a Missing API Key

We should also handle the situation where the API key is missing.

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

if api_key is None:
    print("API key is missing")
else:
    print("API key found")
```

In a real application, instead of simply printing an error, we could raise an exception:

```python
if api_key is None:
    raise ValueError("API_KEY is missing")
```

---

# 8. `.gitignore`

The `.env` file should **never be committed to GitHub** if it contains secrets.

Example `.gitignore`:

```text
.env
.venv/
__pycache__/
```

### Why?

```text
.env
 ↓
Contains secrets
 ↓
.gitignore
 ↓
Git doesn't track the file
 ↓
Secret stays out of GitHub
```

> `.gitignore` prevents accidental commits, but it does not encrypt secrets.

---

# 9. Day 9 Practice Project

The practice program combines everything learned today.

### Requirements

The program should:

1. Read an API key from environment variables.
2. Detect if the API key is missing.
3. Read a file.
4. Handle `FileNotFoundError`.
5. Take user input.
6. Handle `ValueError`.

### Example

```python
from dotenv import load_dotenv
import os

load_dotenv()

# API KEY
api_key = os.getenv("API_KEY")

if api_key is None:
    print("API key is missing")
else:
    print("API key found")


# FILE HANDLING
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")


# USER INPUT
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid number")
```

---

# 🧠 Key Takeaways

### Exceptions

```text
try       → try risky code
except    → handle errors
else      → runs when no error occurs
finally   → always runs
raise     → manually create an exception
```

### Environment Variables

```text
.env → environment variable → Python
```

### Security

```text
❌ Hardcode API keys
✅ Store secrets in .env
✅ Add .env to .gitignore
```

---

# 🚀 Why This Matters for AI Engineering

AI applications depend heavily on external services and APIs.

For example:

```text
Python Application
       ↓
     API
       ↓
    LLM / AI
       ↓
    Response
```

Any of these can fail because of:

* invalid input
* missing API keys
* network problems
* unavailable files
* invalid API responses
* incorrect data

Therefore, **exception handling and environment variables are essential parts of production-ready AI applications.**

---

## Day 9 Status

* [x] Exceptions
* [x] try / except
* [x] else
* [x] finally
* [x] raise
* [x] Common Python exceptions
* [x] Environment variables
* [x] `.env`
* [x] `python-dotenv`
* [x] `.gitignore`
* [x] Practice project

**Day 9 completed ✅**
