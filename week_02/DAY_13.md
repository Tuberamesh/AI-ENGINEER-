# 🚀 DAY 13 — HTTP + GET Properly

> **Week 3 — APIs Properly | Day 13 of 17**

Welcome to **Day 13 of my AI Engineering journey!** 🚀

In the previous days, I worked on engineering-style Python, including:

* Functions and modules
* Dictionaries and JSON
* File handling
* Exception handling
* Environment variables
* HTTP requests
* Type hints
* Async concepts
* Building an **AI Text Utility**

Now I am moving from **Python fundamentals → API engineering**.

APIs are extremely important for AI Engineers because modern AI applications constantly communicate with external services such as:

* LLM APIs
* Embedding APIs
* Vector databases
* Cloud services
* Authentication services
* Data APIs
* Internal backend services

The goal of Day 13 is not just to learn:

```python
requests.get(url)
```

The goal is to understand **what actually happens when that line runs.**

---

## 🎯 Today's Goal

By the end of Day 13, I should understand:

* Client
* Server
* HTTP
* Request
* Response
* URL
* Endpoint
* GET
* Status codes
* Response headers
* Response body
* JSON responses
* Query parameters
* `requests.get()`
* `response.status_code`
* `response.text`
* `response.json()`
* `response.headers`

Most importantly, I should understand this flow:

```text
Python Client
      ↓
HTTP Request
      ↓
API
      ↓
Server
      ↓
HTTP Response
      ↓
Python
      ↓
Process Data
```

---

# 1. What is an API?

An **API (Application Programming Interface)** provides a way for different software systems to communicate with each other.

For example, suppose my Python application needs user information.

Instead of directly accessing another application's database, my program can communicate through an API.

```text
Python Program
      ↓
     API
      ↓
   Server
      ↓
   Database
      ↓
   Server
      ↓
     API
      ↓
Python Program
```

The API acts as a communication interface between systems.

---

# 2. Client and Server

## Client

The **client** is the system making the request.

In my case:

```text
Python program
```

## Server

The **server** receives the request, processes it, and sends a response.

So the basic communication looks like:

```text
             HTTP REQUEST
Python ------------------------> Server
       "Give me user 5"

Python <------------------------ Server
             HTTP RESPONSE
       {"id": 5, "name": "..."}
```

### Simple mental model

```text
Client = asks
Server = responds
```

---

# 3. What is HTTP?

**HTTP = HyperText Transfer Protocol**

HTTP is a set of rules that allows clients and servers to communicate.

The basic flow is:

```text
Client
  │
  │ HTTP Request
  ↓
Server
  │
  │ HTTP Response
  ↓
Client
```

When I write:

```python
requests.get(url)
```

Python is making an **HTTP GET request** to the specified URL.

---

# 4. What is a URL?

Consider this URL:

```text
https://jsonplaceholder.typicode.com/users/5
```

We can break it down:

```text
https://
   ↓
Protocol

jsonplaceholder.typicode.com
   ↓
Domain / Server

/users/5
   ↓
Path
```

So:

```text
https://jsonplaceholder.typicode.com/users/5
│      │                              │
│      │                              └── Path
│      └───────────────────────────────── Domain
└──────────────────────────────────────── Protocol
```

---

# 5. What is an Endpoint?

An **endpoint** is a specific location provided by an API where a client can make a request.

Examples:

```text
/users
/products
/orders
/users/5
/products/10
```

For example:

```text
https://jsonplaceholder.typicode.com/users/5
```

The endpoint/path is:

```text
/users/5
```

It represents a specific API resource.

---

# 6. HTTP Methods

HTTP provides different methods for communicating with APIs.

The main methods I will learn during Week 3 are:

```text
GET
POST
PUT
DELETE
```

For Day 13, I focus on:

```text
GET
```

GET generally means:

> **Give me / retrieve data.**

Examples:

```text
GET /users
```

means:

```text
Give me users.
```

And:

```text
GET /users/5
```

means:

```text
Give me user 5.
```

Simple mental model:

```text
GET
 ↓
READ / FETCH DATA
```

---

# 7. Making a GET Request with Python

Python can make HTTP requests using the `requests` library.

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

print(response)
```

The output looks similar to:

```text
<Response [200]>
```

---

# 8. What Actually Happens?

When this line runs:

```python
response = requests.get(url)
```

the following happens:

```text
Python Program
      ↓
requests.get(url)
      ↓
HTTP GET Request
      ↓
Internet
      ↓
API Server
      ↓
Server processes request
      ↓
Server finds requested data
      ↓
HTTP Response
      ↓
Python receives response
      ↓
response object
```

So `response` is an object containing information about the HTTP response.

---

# 9. HTTP Status Codes

Every HTTP response contains a **status code**.

For example:

```python
print(response.status_code)
```

Output:

```text
200
```

`200` means:

```text
OK
```

In simple words:

> The request was successful.

Some important status codes:

| Status Code | Meaning               |
| ----------- | --------------------- |
| `200`       | OK / Successful       |
| `201`       | Created               |
| `400`       | Bad Request           |
| `401`       | Unauthorized          |
| `403`       | Forbidden             |
| `404`       | Not Found             |
| `500`       | Internal Server Error |

The important idea is:

```text
HTTP Status Code
       ↓
Tells me what happened to my request
```

---

# 10. `response.status_code`

This:

```python
response.status_code
```

returns the HTTP status code.

Example:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

print(response.status_code)
```

Output:

```text
200
```

---

# 11. `response.text`

Now I can inspect the response as text:

```python
print(response.text)
```

The API may return something similar to:

```json
{
  "id": 5,
  "name": "Chelsey Dietrich",
  "username": "Kamren",
  "email": "..."
}
```

`response.text` gives me the response body as text.

Conceptually:

```text
Server
   ↓
Response body
   ↓
response.text
   ↓
Python string
```

---

# 12. `response.json()`

APIs commonly return JSON.

Instead of treating the response only as text, I can convert the JSON response into Python data:

```python
data = response.json()
```

For example, JSON:

```json
{
    "id": 5,
    "name": "Chelsey Dietrich",
    "email": "example@email.com"
}
```

can become a Python dictionary:

```python
{
    "id": 5,
    "name": "Chelsey Dietrich",
    "email": "example@email.com"
}
```

So the important difference is:

```text
response.text
      ↓
String / text

response.json()
      ↓
Python dictionary/list/etc.
```

This is extremely important because API data usually needs to be processed inside Python.

---

# 13. Extracting Data from JSON

Once I have:

```python
data = response.json()
```

I can access fields:

```python
print(data["name"])
print(data["email"])
```

For example:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

data = response.json()

print(data["name"])
print(data["email"])
```

The flow is:

```text
GET Request
     ↓
HTTP Response
     ↓
response.json()
     ↓
Python Dictionary
     ↓
data["name"]
data["email"]
```

---

# 14. `response.headers`

HTTP responses also contain headers.

I can inspect them using:

```python
print(response.headers)
```

Headers contain metadata about the HTTP request or response.

Examples include information such as:

```text
Content-Type
Content-Length
Date
Server
```

Think of headers as:

> Information ABOUT the request or response.

---

# 15. Headers vs Body

This distinction is very important.

An HTTP message can contain:

```text
HTTP Request
│
├── Headers
│     ↓
│   Information about the request
│
└── Body
      ↓
    Data being sent
```

For example:

```text
Headers
→ Content-Type
→ Authorization
→ User-Agent

Body
→ Actual data being sent
```

For GET requests, I will commonly retrieve data without sending a meaningful request body.

---

# 16. Query Parameters

Sometimes an API needs additional information in the URL.

For example:

```text
/users?page=2&limit=10
```

Here:

```text
page=2
limit=10
```

are **query parameters**.

They provide additional instructions or filters to the API.

---

# 17. Sending Query Parameters with `requests`

Instead of manually constructing the URL, I can use `params`.

```python
params = {
    "page": 2,
    "limit": 10
}

response = requests.get(
    url,
    params=params
)
```

The `requests` library builds the query string for me.

Conceptually:

```text
Python

params = {
    "page": 2,
    "limit": 10
}

        ↓

?page=2&limit=10

        ↓

API
```

I can inspect the final URL using:

```python
print(response.url)
```

---

# 18. Complete GET Example

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/5"

params = {
    "page": 2
}

response = requests.get(
    url,
    params=params
)

print("Status:", response.status_code)
print("URL:", response.url)

print("Response Text:")
print(response.text)

data = response.json()

print("Name:", data["name"])
print("Email:", data["email"])

print("Headers:")
print(response.headers)
```

The important flow is:

```text
Python
  ↓
requests.get()
  ↓
GET Request
  ↓
API
  ↓
Server
  ↓
HTTP Response
  ↓
status_code
text
headers
json()
  ↓
Python Data
```

---

# 19. The Most Important Line of Day 13

This:

```python
response = requests.get(url)
```

should no longer feel like magic.

I should understand it as:

```text
requests.get(url)
        ↓
Create HTTP GET request
        ↓
Send request to URL
        ↓
Server receives request
        ↓
Server processes request
        ↓
Server sends HTTP response
        ↓
requests receives response
        ↓
response object
```

---

# 20. Day 13 Mini Practice

I built a small Python program that:

1. Imports `requests`
2. Makes a GET request
3. Checks the status code
4. Reads the response
5. Converts JSON into Python data
6. Extracts fields
7. Inspects response headers
8. Uses query parameters

Example structure:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

print("Name:", data["name"])
print("Email:", data["email"])
```

---

# 🧠 Day 13 Mental Model

I should now be able to visualize API communication like this:

```text
                  PYTHON CLIENT
                       │
                       │
                 requests.get()
                       │
                       ↓
                 HTTP REQUEST
                       │
                       ↓
                      API
                       │
                       ↓
                    SERVER
                       │
                  finds data
                       │
                       ↓
                 HTTP RESPONSE
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      status_code     text       headers
          │
          ↓
   response.json()
          │
          ↓
   Python dict/list
          │
          ↓
     Process Data
```

This is the foundation for working with APIs as an AI Engineer.

---

# 📝 Day 13 Key Takeaways

### HTTP

```text
Rules for communication between client and server
```

### Client

```text
The system making the request
```

### Server

```text
The system receiving and processing the request
```

### API

```text
Interface that allows software systems to communicate
```

### Endpoint

```text
Specific API location/resource
```

### GET

```text
Used mainly to retrieve data
```

### Status Code

```text
Tells me the result of the HTTP request
```

### Headers

```text
Metadata/information about the request or response
```

### `response.text`

```text
Response body as text
```

### `response.json()`

```text
Converts JSON response into Python data
```

### Query Parameters

```text
Additional values passed through the URL
```

### `params=`

```text
Used to send query parameters with requests
```

---

# 🎯 Day 13 Checkpoint

Before moving forward, I should be able to explain:

* What is an API?
* What is a client?
* What is a server?
* What is HTTP?
* What is a URL?
* What is an endpoint?
* What does GET mean?
* What does `requests.get()` do?
* What is a response object?
* What does `response.status_code` mean?
* What is the difference between `response.text` and `response.json()`?
* What are headers?
* What are query parameters?
* What does `params=` do?

If I can explain these concepts in my own words, **Day 13 is complete.** ✅

---

# 🚀 Why This Matters for AI Engineering

APIs are one of the foundations of modern AI applications.

Later, the same basic flow will look like:

```text
Python Application
       ↓
HTTP Request
       ↓
AI API
       ↓
LLM / AI Server
       ↓
JSON Response
       ↓
Python
       ↓
Process AI Output
       ↓
Application
```

For example:

```text
Python
   ↓
OpenAI / Gemini / other AI API
   ↓
LLM
   ↓
JSON response
   ↓
Python
   ↓
Extract generated content
   ↓
Use it inside application
```

So learning GET properly is not just an HTTP exercise.

It is the beginning of understanding **how AI applications communicate with external services.**

---

# 📁 Day 13 Files

My Week 3 structure now looks like:

```text
week_03/
│
├── DAY_13.md
└── day13_get.py
```

---

# 🔗 Learning Progress

```text
Week 1
Python + APIs Fundamentals
        ↓
Week 2
Engineering-style Python
        ↓
Day 10
HTTP Requests
        ↓
Day 11
Async + Type Hints
        ↓
Day 12
AI Text Utility
        ↓
Day 13
HTTP + GET Properly ✅
        ↓
Day 14
POST + Body + Headers
        ↓
Day 15
PUT + DELETE
        ↓
Day 16
Authentication + API Security
        ↓
Day 17
API Project 🚀
```

---

# 🎉 DAY 13 COMPLETE!

Today I learned how Python communicates with a server using HTTP and how to retrieve and process JSON data from an API.

I am no longer just writing:

```python
requests.get(url)
```

I understand the flow behind it:

```text
Python
   ↓
HTTP GET Request
   ↓
API
   ↓
Server
   ↓
HTTP Response
   ↓
JSON
   ↓
Python
   ↓
Process Data
```

That's an important step toward becoming an **AI Engineer.** 🚀

---

# 🚀 NEXT: DAY 14

In Day 14, I will learn how to **send data to an API**, not just retrieve it.

I will learn:

```text
POST
Request Body
JSON Body
Headers
Content-Type
requests.post()
```

And build:

```text
Python
   ↓
POST Request
   ↓
API
   ↓
Server
   ↓
JSON Response
   ↓
Python
```

The next question is:

> **"I know how to GET data. But how do I SEND data to an API?"**

That's exactly what **Day 14 — POST + Request Body + Headers** will answer.

**Day 13 → Done ✅**
