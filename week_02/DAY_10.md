# DAY 10 — HTTP Requests & APIs

> Week 2 — Python for AI Engineering

## 📚 Navigation

* [← Back to Day 9 — Exceptions & Environment Variables](./DAY_09.md)
* [Next → Day 11 — Type Hints & Async Basics](./DAY_11.md)

---

# 🎯 What I Learned

Today I learned how Python applications communicate with external services using:

* HTTP
* APIs
* GET requests
* POST requests
* URL
* Parameters
* Headers
* Request body
* Status codes
* JSON responses
* Python `requests` library
* API keys and environment variables

These concepts are important for AI engineering because modern AI applications communicate with external APIs, databases and AI models.

---

# 1. What is an API?

API stands for:

**Application Programming Interface**

An API allows two software applications to communicate with each other.

For example:

```text
Python Application
       ↓
      API
       ↓
    Server
       ↓
    Response
       ↓
Python Application
```

### Real-world example

A weather application can request weather information from a weather API.

```text
Weather App
     ↓
Weather API
     ↓
Weather Server
     ↓
Weather Data
     ↓
Weather App
```

The application doesn't need to know how the weather data is generated. It only needs to know how to communicate with the API.

---

# 2. What is HTTP?

HTTP stands for:

**HyperText Transfer Protocol**

HTTP defines how applications communicate over a network.

Basic flow:

```text
CLIENT
  |
  | HTTP Request
  ↓
SERVER
  |
  | HTTP Response
  ↓
CLIENT
```

A Python program can act as the client.

---

# 3. HTTP Methods

HTTP provides different methods for different actions.

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Retrieve data         |
| POST   | Send/create data      |
| PUT    | Update data           |
| PATCH  | Partially update data |
| DELETE | Delete data           |

The two most important methods to understand initially are:

```text
GET  → Get data
POST → Send data
```

---

# 4. GET Request

A GET request is used to retrieve data from a server.

Example:

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/6"
)

print(response.status_code)
print(response.json())
```

### Flow

```text
requests.get()
      ↓
Python sends GET request
      ↓
Server receives request
      ↓
Server processes it
      ↓
Server sends response
      ↓
Python receives response
```

---

# 5. `requests` Library

Python has a popular library called `requests` for making HTTP requests.

Install:

```bash
pip install requests
```

Import:

```python
import requests
```

GET:

```python
requests.get(url)
```

POST:

```python
requests.post(url)
```

---

# 6. Response Object

When we write:

```python
response = requests.get(url)
```

`response` contains information returned by the server.

For example:

```python
response.status_code
```

and:

```python
response.json()
```

---

# 7. Status Codes

HTTP status codes tell us what happened with the request.

Common status codes:

```text
200 → Success
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Server Error
```

Example:

```python
if response.status_code == 200:
    print("Success")
else:
    print("Something went wrong")
```

---

# 8. JSON Response

APIs commonly return data in JSON format.

Example:

```json
{
    "id": 6,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "example@email.com"
}
```

We can convert the JSON response into Python data using:

```python
response.json()
```

Example:

```python
data = response.json()

print(data["name"])
print(data["email"])
```

---

# 9. Parameters

Parameters allow us to send additional information with a request.

Example:

```python
import requests

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.status_code)
print(response.json())
```

The request conceptually becomes:

```text
https://example.com/posts?userId=1
```

Using `params` is cleaner than manually building the URL.

---

# 10. POST Request

POST is commonly used to send data to a server.

Example:

```python
import requests

data = {
    "title": "Learning APIs",
    "body": "I am learning HTTP requests.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.json())
```

### Flow

```text
Python
  ↓
POST request
  ↓
Send JSON data
  ↓
Server
  ↓
Process data
  ↓
Response
  ↓
Python
```

---

# 11. Request Body

The data sent with a POST request is commonly called the **request body**.

Example:

```python
data = {
    "name": "Ramesha",
    "skill": "Python"
}
```

Then:

```python
requests.post(url, json=data)
```

The dictionary is sent as JSON.

---

# 12. Headers

Headers contain additional information about an HTTP request.

For example:

```python
headers = {
    "Authorization": "Bearer TOKEN",
    "Content-Type": "application/json"
}
```

Then:

```python
response = requests.get(
    url,
    headers=headers
)
```

Headers are commonly used for:

* Authentication
* Authorization
* Content type
* API-specific information

---

# 13. API Keys & Environment Variables

API keys are secret credentials.

Do **not** hardcode them in public code.

### Bad

```python
API_KEY = "my-secret-key"
```

### Better

`.env`

```text
API_KEY=my-secret-key
```

Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
```

Also make sure `.env` is included in `.gitignore`.

```text
.env
```

---

# 14. Complete API Mental Model

When working with an API, think about these parts:

```text
URL
 ↓
Where are we sending the request?

METHOD
 ↓
What do we want to do?

PARAMETERS
 ↓
Extra information in the URL

HEADERS
 ↓
Authentication / extra request information

BODY
 ↓
Data sent to the server

STATUS CODE
 ↓
Did the request succeed?

JSON RESPONSE
 ↓
Data returned by the server
```

---

# 15. Why APIs Matter for AI Engineers

AI engineers frequently work with APIs.

For example:

```text
Python Application
       ↓
Backend API
       ↓
LLM API
       ↓
AI Model
       ↓
Response
       ↓
Python Application
```

APIs are used in:

* LLM applications
* AI chatbots
* RAG systems
* AI agents
* Data pipelines
* Automation
* Backend applications
* External services

Understanding APIs is therefore a fundamental AI engineering skill.

---

# 🧠 Quick Revision

```text
API
→ Allows applications to communicate.

HTTP
→ Protocol used for communication over the web.

GET
→ Retrieve data.

POST
→ Send/create data.

requests
→ Python library for HTTP requests.

status_code
→ Tells us what happened.

response.json()
→ Reads JSON response as Python data.

params
→ Sends query parameters.

headers
→ Sends additional request information.

body
→ Data sent to the server.

.env
→ Stores secret configuration such as API keys.
```

---

# ✅ Day 10 Completed

I learned how to communicate with APIs from Python using HTTP requests.

**Next:** [Day 11 — Type Hints & Async Basics →](./DAY_11.md)
