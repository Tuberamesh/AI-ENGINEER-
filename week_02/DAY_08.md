
# 🚀 DAY 08 — Dictionaries, JSON & File Handling

> **Goal:** Become comfortable moving between **Python → JSON → Files**.

Today we are learning three things that are extremely common in AI Engineering, backend development, APIs, and data processing:

* Python Dictionaries
* JSON
* File Handling

The important part is not just remembering the syntax. You should understand **why we use them and how they work together**.

---

# 1. 🧠 Python Dictionaries

A **dictionary** stores data in **key → value** pairs.

Think of it like a real-world record.

Instead of storing:

```python
student = ["Ramesh", 20, "Data Science"]
```

we can use meaningful names:

```python
student = {
    "name": "Ramesh",
    "age": 20,
    "branch": "Data Science"
}
```

Now we can clearly understand what each value represents.

## Why use dictionaries?

Dictionaries are useful when data has **named properties**.

They are commonly used for:

* API responses
* JSON data
* Configuration
* User information
* Database records
* AI application data
* Backend development

---

# 2. Accessing Dictionary Values

Use the key to access its value:

```python
student = {
    "name": "Ramesh",
    "age": 20,
    "branch": "Data Science"
}

print(student["name"])
print(student["age"])
```

Output:

```text
Ramesh
20
```

### Important

With a list:

```python
student[0]
```

we access using a numeric index.

With a dictionary:

```python
student["name"]
```

we access using a meaningful key.

---

# 3. Adding and Updating Values

## Add a new key

```python
student["college"] = "NHCE"
```

Now the dictionary contains:

```python
{
    "name": "Ramesh",
    "age": 20,
    "branch": "Data Science",
    "college": "NHCE"
}
```

## Update an existing value

```python
student["age"] = 21
```

The same syntax is used for both adding and updating.

```python
dictionary[key] = value
```

If the key already exists → **update**

If the key doesn't exist → **add**

---

# 4. Looping Through a Dictionary

If we do:

```python
for key in student:
    print(key)
```

we get the keys.

Example:

```text
name
age
branch
college
```

But what if we want both the key and value?

Use `.items()`:

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Ramesh
age : 20
branch : Data Science
college : NHCE
```

## Why `.items()`?

`.items()` gives us the **key + value pair**.

Think:

```text
.keys()    → keys
.values()  → values
.items()   → keys + values
```

This is very common when processing structured data.

### Interview answer

> `.items()` is used when we need to iterate over both the keys and values of a dictionary.

---

# 5. Nested Dictionaries

A dictionary can contain another dictionary.

Example:

```python
student = {
    "name": "Ramesh",
    "details": {
        "age": 20,
        "branch": "Data Science"
    }
}
```

Here:

```text
student
 ├── name
 └── details
      ├── age
      └── branch
```

To access the branch:

```python
print(student["details"]["branch"])
```

Output:

```text
Data Science
```

## Why are nested dictionaries important?

Real-world API responses are often nested.

For example, an API might return:

```python
user = {
    "id": 101,
    "name": "Ramesh",
    "address": {
        "city": "Bengaluru",
        "country": "India"
    }
}
```

You might access:

```python
user["address"]["city"]
```

---

# 6. List of Dictionaries

A very common structure is:

```python
students = [
    {"name": "Ramesh", "age": 20},
    {"name": "Rahul", "age": 21},
    {"name": "Anu", "age": 20}
]
```

Here:

* The **list** stores multiple records.
* Each **dictionary** represents one record.

Think of it like a table:

| Name   | Age |
| ------ | --: |
| Ramesh |  20 |
| Rahul  |  21 |
| Anu    |  20 |

We can loop through them:

```python
for student in students:
    print(student["name"], student["age"])
```

Output:

```text
Ramesh 20
Rahul 21
Anu 20
```

This structure is extremely common when working with API responses and JSON.

---

# 7. What is JSON?

**JSON = JavaScript Object Notation**

JSON is a **data format** used to store and exchange structured data.

It is commonly used between:

* Frontend ↔ Backend
* Application ↔ API
* Python ↔ API
* Application ↔ Database systems
* Different programming languages

A JSON object looks like:

```json
{
    "name": "Ramesh",
    "age": 20,
    "branch": "Data Science"
}
```

---

# 8. Dictionary vs JSON

This is an important concept.

A Python dictionary:

```python
student = {
    "name": "Ramesh",
    "age": 20
}
```

A JSON object:

```json
{
    "name": "Ramesh",
    "age": 20
}
```

They **look almost identical**, but they are NOT the same thing.

### Python Dictionary

A dictionary is a **Python data structure**.

### JSON

JSON is a **language-independent data format**.

The easiest way to remember:

```text
Dictionary → Python data structure

JSON → Data interchange format
```

JSON allows different programming languages and systems to exchange structured data.

---

# 9. Python → JSON String

Python provides the `json` module.

First:

```python
import json
```

We can convert a Python dictionary into a JSON string using:

```python
json.dumps()
```

Example:

```python
import json

student = {
    "name": "Ramesh",
    "age": 20
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))
```

The important point is:

```text
Python dictionary
       ↓
   json.dumps()
       ↓
JSON string
```

---

# 10. JSON String → Python Dictionary

The opposite operation is:

```python
json.loads()
```

Example:

```python
import json

json_data = '{"name": "Ramesh", "age": 20}'

student = json.loads(json_data)

print(student)
print(type(student))
```

Now:

```text
JSON string
     ↓
json.loads()
     ↓
Python dictionary
```

---

# 11. `dump()` vs `dumps()`

This is a very common confusion.

Remember:

> **The `s` stands for string.**

### `dumps()`

Python dictionary → JSON **string**

```python
json.dumps(data)
```

### `dump()`

Python dictionary → JSON **file**

```python
json.dump(data, file)
```

So:

```text
dumps() → string
dump()  → file
```

---

# 12. `load()` vs `loads()`

Same idea.

### `loads()`

JSON **string** → Python dictionary

```python
json.loads(json_data)
```

### `load()`

JSON **file** → Python dictionary

```python
json.load(file)
```

So remember the complete table:

| Function  | Conversion           |
| --------- | -------------------- |
| `dumps()` | Python → JSON string |
| `loads()` | JSON string → Python |
| `dump()`  | Python → JSON file   |
| `load()`  | JSON file → Python   |

### Easy memory trick

```text
        STRING
          ↑ ↓
      dumps / loads

         FILE
          ↑ ↓
       dump / load
```

---

# 13. File Handling in Python

Python allows us to create, read, write, and modify files.

The main function is:

```python
open()
```

Basic structure:

```python
open("filename", "mode")
```

Example:

```python
file = open("data.txt", "r")
```

Here:

```text
data.txt → file name
"r"      → mode
```

---

# 14. File Modes

The most important modes are:

| Mode  | Meaning |
| ----- | ------- |
| `"r"` | Read    |
| `"w"` | Write   |
| `"a"` | Append  |

## `"r"` — Read

Used to read existing content.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

---

# 15. `"w"` — Write

Used to write content into a file.

```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

### Important

`"w"` can **overwrite existing content**.

For example, if the file contains:

```text
Hello
```

and we run:

```python
with open("data.txt", "w") as file:
    file.write("Python")
```

the file becomes:

```text
Python
```

The old content is replaced.

---

# 16. `"a"` — Append

Append means **add content to the end**.

```python
with open("data.txt", "a") as file:
    file.write("\nLearning AI Engineering")
```

If the file already contains:

```text
Hello Python
```

it becomes:

```text
Hello Python
Learning AI Engineering
```

Unlike `"w"`, `"a"` does not overwrite the existing content.

---

# 17. `read()` and `write()`

These two methods are important.

### `write()`

Puts content **into** a file:

```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

### `read()`

Gets content **from** a file:

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

Easy way to remember:

```text
write() → Python → File

read()  → File → Python
```

---

# 18. Why use `with open()`?

You will often see:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

instead of:

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

The `with` statement automatically handles closing the file.

So:

```python
with open(...)
```

is the preferred and safer pattern for normal file handling.

---

# 19. What is `file`?

In this code:

```python
with open("data.txt", "r") as file:
```

`file` is **just a variable name**.

It is NOT a Python keyword.

We could write:

```python
with open("data.txt", "r") as f:
```

or:

```python
with open("data.txt", "r") as my_file:
```

All are valid.

The variable stores the opened file object.

---

# 20. Python → JSON File

Now let's combine everything.

Suppose we have:

```python
import json

student = {
    "name": "Ramesh",
    "age": 20,
    "branch": "Data Science"
}
```

We can save it as JSON:

```python
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

This creates:

```text
student.json
```

with:

```json
{
    "name": "Ramesh",
    "age": 20,
    "branch": "Data Science"
}
```

`indent=4` simply makes the JSON easier to read.

---

# 21. JSON File → Python Dictionary

We can read that JSON file back:

```python
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
```

The flow is:

```text
Python Dictionary
       ↓
   json.dump()
       ↓
    JSON File
       ↓
   json.load()
       ↓
Python Dictionary
```

This pattern is extremely useful in real applications.

---

# 22. 🛠️ Day 8 Mini Project

Now let's build a small text utility.

### Goal

Take a paragraph and create:

```json
{
    "text": "...",
    "word_count": 22,
    "character_count": 131
}
```

Then save the result as:

```text
result.json
```

---

## Step 1 — Import JSON

```python
import json
```

---

## Step 2 — Store the paragraph

```python
text = """
Python is a powerful programming language.
Python is widely used in data science and AI.
I am learning Python for AI engineering.
"""
```

---

## Step 3 — Count words

```python
words = text.split()
word_count = len(words)

print(word_count)
```

### What does `.split()` do?

It breaks the string into separate words.

For example:

```python
text = "Python is powerful"
```

After:

```python
text.split()
```

we get:

```python
["Python", "is", "powerful"]
```

Then:

```python
len(words)
```

counts how many words are in the list.

---

## Step 4 — Count characters

```python
character_count = len(text)

print(character_count)
```

`len(text)` counts characters including:

* letters
* spaces
* punctuation
* newline characters

---

## Step 5 — Create a dictionary

```python
result = {
    "text": text,
    "word_count": word_count,
    "character_count": character_count
}

print(result)
```

Now our information is structured.

---

## Step 6 — Save as JSON

```python
with open("result.json", "w") as file:
    json.dump(result, file, indent=4)
```

This creates:

```text
result.json
```

---

## Step 7 — Read the JSON file

```python
with open("result.json", "r") as file:
    data = json.load(file)

print(data)
print(data["word_count"])
```

Now the JSON file has been converted back into a Python dictionary.

---

# 23. Complete Mini Project

Here is the complete program:

```python
import json

text = """
Python is a powerful programming language.
Python is widely used in data science and AI.
I am learning Python for AI engineering.
"""

words = text.split()
word_count = len(words)

character_count = len(text)

result = {
    "text": text,
    "word_count": word_count,
    "character_count": character_count
}

print(result)

with open("result.json", "w") as file:
    json.dump(result, file, indent=4)

with open("result.json", "r") as file:
    data = json.load(file)

print(data)
print(data["word_count"])
```

---

# 24. 🧠 The Big Picture

This is the most important thing to understand from Day 8:

```text
                 Python
                   │
                   ▼
             Dictionary
                   │
             json.dump()
                   │
                   ▼
               JSON File
                   │
              json.load()
                   │
                   ▼
             Python Dictionary
```

And for strings:

```text
Python Dictionary
       │
   json.dumps()
       ▼
  JSON String
       │
   json.loads()
       ▼
Python Dictionary
```

---

# 25. 🎯 Interview Questions

### Q1. What is a dictionary?

A dictionary is a Python data structure that stores data as key-value pairs.

---

### Q2. Why use a dictionary instead of a list?

A dictionary allows us to access values using meaningful keys instead of numeric indexes.

---

### Q3. What does `.items()` do?

It returns the key-value pairs of a dictionary, allowing us to iterate over both.

---

### Q4. What is JSON?

JSON is a language-independent data interchange format used to represent and exchange structured data.

---

### Q5. Is JSON the same as a Python dictionary?

No.

A dictionary is a Python data structure, while JSON is a data format.

They can have a similar structure, but they are different representations.

---

### Q6. Difference between `dump()` and `dumps()`?

```text
dump()  → Python → JSON file
dumps() → Python → JSON string
```

The `s` stands for **string**.

---

### Q7. Difference between `load()` and `loads()`?

```text
load()  → JSON file → Python
loads() → JSON string → Python
```

---

### Q8. What is `"w"` mode?

Write mode.

It writes data to a file and can overwrite existing content.

---

### Q9. What is `"a"` mode?

Append mode.

It adds new content to the end of an existing file.

---

### Q10. Why use `with open()`?

It automatically handles closing the file after the operation is complete.

---

# 26. 🔥 Day 8 Cheat Sheet

```text
DICTIONARY
dict = {"name": "Ramesh"}

Access:
dict["name"]

Add / Update:
dict["key"] = value

Loop:
for key, value in dict.items():
    ...

Nested:
data["details"]["branch"]

List of dictionaries:
[
    {"name": "Ramesh"},
    {"name": "Rahul"}
]


JSON
Python → JSON string:
json.dumps()

JSON string → Python:
json.loads()

Python → JSON file:
json.dump()

JSON file → Python:
json.load()


FILE HANDLING
open("file.txt", "r")  → read
open("file.txt", "w")  → write / overwrite
open("file.txt", "a")  → append

file.read()  → get content
file.write() → put content

Preferred pattern:
with open(...) as file:
    ...
```

---

# 🚀 What You Should Be Able To Do After Day 8

By the end of this day, you should be able to:

* Create and access dictionaries
* Add and update dictionary values
* Loop through dictionaries
* Use `.items()`
* Work with nested dictionaries
* Work with lists of dictionaries
* Understand what JSON is
* Explain Dictionary vs JSON
* Convert Python ↔ JSON strings
* Convert Python ↔ JSON files
* Read and write text files
* Understand `r`, `w`, and `a`
* Use `with open()`
* Build a small JSON-based text utility

### Most important mental model:

> **Dictionary helps Python structure data. JSON helps systems exchange/store structured data. Files help us persist data.**

```text
Python Data
    ↓
Dictionary
    ↓
JSON
    ↓
File / API
    ↓
Another System
```

**Day 8 complete. ✅**
