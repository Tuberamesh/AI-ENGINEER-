# 🚀 DAY 6 — Build Your First API Application

## 👋 Welcome to Day 6!

Today we moved from **learning APIs → actually using an API in Python**.

### 🎯 Today's Task

Build a small Python application that consumes a public REST API and displays user information.

No LLM yet — just understanding how an application communicates with an API.

> 📚 **Previous Day:** [Day 5 — REST API, SDK & Postman](./DAY_05.md)

---

## 🛠️ What We Built

A simple **User Information API App**.

```text
User enters User ID
        ↓
Python
        ↓
GET Request
        ↓
REST API
        ↓
JSON Response
        ↓
Extract Data
        ↓
Display User Information
```

---

## 🌐 API Used

**JSONPlaceholder**

```text
https://jsonplaceholder.typicode.com/users/{user_id}
```

Example:

```text
/users/1
/users/2
/users/3
```

Different IDs return different users.

---

## 🧠 What I Learned Today

### 1. Consuming an API

Our Python program can request data from another application/service through an API.

```python
response = requests.get(url)
```

---

### 2. API Endpoint

An endpoint is the URL used to access a specific resource.

```text
/users/1
/users/2
/users/3
```

Here, `/users/{id}` is the endpoint pattern.

---

### 3. GET Request

```python
requests.get(url)
```

Used to **retrieve data** from the API.

---

### 4. API Response

The API sends a response back to our program.

```python
response.status_code
response.json()
```

Important parts:

```text
Status Code
Headers
Body
```

---

### 5. Status Codes

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |
| 500  | Server Error |

In our project:

```python
if response.status_code == 200:
```

means the request was successful.

---

### 6. JSON → Python

The API returns JSON data.

We convert it into a Python object using:

```python
data = response.json()
```

Then we can access the data like a dictionary:

```python
data["name"]
data["email"]
data["address"]["city"]
```

Nested data:

```text
data
 └── address
      └── city
```

---

### 7. Dynamic API Requests

Instead of hardcoding:

```text
/users/1
```

we made the user ID dynamic:

```python
user_id = input("Enter user ID: ")

url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
```

Now the same program can request:

```text
/users/1
/users/5
/users/10
```

---

### 8. Basic Error Handling

If the user doesn't exist:

```python
else:
    print("❌ User not found")
```

Example:

```text
Enter user ID: 999

❌ User not found
```

---

## 💻 Final Code

```python
import requests

user_id = input("Enter user ID: ")

url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    name = data["name"]
    email = data["email"]
    city = data["address"]["city"]

    print("User Information")
    print("----------------")
    print("Name:", name)
    print("Email:", email)
    print("City:", city)

else:
    print("❌ User not found")
```

---

## 🔑 Quick Revision

```text
API
→ Interface for software communication

REST API
→ API following REST principles

Endpoint
→ URL used to access a resource

GET
→ Retrieve data

JSON
→ Common format for API data

response.json()
→ Convert JSON response into Python data

status_code
→ Check whether the request succeeded/failed

requests.get()
→ Send a GET request from Python
```

---

## 🎯 Today's Main Takeaway

Before today:

```text
I know what an API is.
```

After today:

```text
I can consume an API using Python.
```

The basic pattern is:

```python
import requests

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
```

> **Python → Request → API → Response → JSON → Python Data**

---

## 📁 Project Structure

```text
week_01/
├── api_test.py
├── DAY_1.md
├── DAY_2.md
├── DAY_3.md
├── Day_4.md
├── DAY_05.md
├── DAY_06.md
├── day5_api_test.py
├── env_test.py
├── hello.py
└── main.py
```

---

## 🚀 Day 6 Complete!

Built my first small **API-consuming Python application**.

Next step:

**Move from consuming APIs → building APIs.**
