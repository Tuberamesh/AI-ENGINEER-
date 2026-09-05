Yep bro — understood. You want **ONE single copy-paste Markdown block**, no separate code blocks inside it, and **under 1000 lines**.

```markdown
# 🚀 Day 5 — REST API, SDK & Postman

Hey everyone! 👋

Welcome to **Day 5** of my journey toward becoming an **AI-Ready Data Engineer**.

Today I learned:

- REST API
- HTTP Methods
- Resources & Endpoints
- SDK
- Postman
- HTTP Requests & Responses
- Status Codes
- Headers
- JSON → Python Dictionary
- Calling APIs using Python

> 🎯 **Goal:** Understand how APIs work, test them using Postman, and call them using Python.

---

## 🔙 Missed Day 4?

👉 [📖 Day 4 — API Keys & Environment Variables](./Day_4.md)

---

## 1️⃣ What is a REST API?

A **REST API** is a way for applications to communicate with each other using HTTP.

### Simple Flow

    Python / Client
          ↓
    HTTP Request
          ↓
         API
          ↓
    HTTP Response
          ↓
         JSON

Think of an API like a waiter:

    You       → Request
    Waiter    → API
    Kitchen   → Server
    Food      → Response

You ask for something → API sends the request → server processes it → server sends back the response.

---

## 2️⃣ What is a Resource?

A **resource** is the thing we are working with.

    /users

Represents the users resource.

    /users/1

Represents user with ID `1`.

---

## 3️⃣ HTTP Methods

HTTP methods tell the server **what action we want to perform**.

| Method | Meaning | Example |
|---|---|---|
| GET | Read data | `GET /users` |
| POST | Create data | `POST /users` |
| PUT | Update data | `PUT /users/1` |
| DELETE | Delete data | `DELETE /users/1` |

### Easy Memory Trick

    GET     → Give me
    POST    → Create
    PUT     → Update
    DELETE  → Remove

---

## 4️⃣ What is an Endpoint?

An **endpoint** is the path used to access a resource.

Example:

    /users/1

The path alone doesn't tell us the action.

The HTTP method tells us what we want to do.

    GET /users/1
    → Get user 1

    PUT /users/1
    → Update user 1

    DELETE /users/1
    → Delete user 1

### Remember

    URL / Path → WHICH resource?
    Method     → WHAT action?

---

## 5️⃣ REST API Flow

    CLIENT
       |
       | HTTP Request
       ↓
    API SERVER
       |
       | HTTP Response
       ↓
    CLIENT

Example:

    Python
       |
       | GET /users/1
       ↓
    API Server
       |
       | 200 OK + JSON
       ↓
    Python

---

## 6️⃣ What is an SDK?

**SDK = Software Development Kit**

An SDK is a collection of tools and libraries that makes it easier to work with a service.

### Without SDK

    Python
       ↓
    HTTP Request
       ↓
    API

### With SDK

    Python
       ↓
    SDK
       ↓
    HTTP Request
       ↓
    API

### API vs SDK

    API → Interface/service we communicate with

    SDK → Tools that make communicating with that service easier

They are **not the same thing**.

Both ultimately help our application communicate with a service.

---

## 7️⃣ What is Postman?

**Postman** is a tool used to test APIs.

Instead of writing Python code first, we can send requests directly from Postman.

Example:

    Method:
    GET

    URL:
    https://jsonplaceholder.typicode.com/users/1

Click **Send** and Postman shows the response from the server.

---

## 8️⃣ My First API Request in Postman

I used:

    GET
    https://jsonplaceholder.typicode.com/users/1

After clicking **Send**, the API returned user information.

The response contained JSON data.

---

## 9️⃣ HTTP Response

When we send a request, the server sends a response.

A response mainly contains:

    HTTP RESPONSE
    │
    ├── Status Code
    ├── Headers
    └── Body

Example:

    200 OK

The body contains the actual response data.

---

## 🔟 HTTP Status Codes

Status codes tell us what happened with our request.

| Status Code | Meaning |
|---|---|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

### Easy Memory

    200 → Success
    404 → Not Found
    500 → Server Error

---

## 1️⃣1️⃣ Testing 200 OK

I requested:

    GET /users/1

The server returned:

    200 OK

Meaning:

    Request successfully processed
    User data received

---

## 1️⃣2️⃣ Testing 404 Not Found

Then I changed the URL to:

    https://jsonplaceholder.typicode.com/users/999999

The server returned:

    404 Not Found

Why?

Because the requested user/resource does not exist.

### Important Difference

    400 → Request itself is invalid

    404 → Requested resource does not exist

---

## 1️⃣3️⃣ Headers

Headers contain extra information about an HTTP request or response.

Example:

    Content-Type: application/json

Another example:

    Authorization: Bearer xyz

Think of headers as **metadata**.

### Easy Memory Trick

    URL       → WHERE?
    Method    → WHAT ACTION?
    Headers   → EXTRA INFORMATION
    Body      → DATA

---

## 1️⃣4️⃣ JSON Response

The server commonly sends data in **JSON** format.

Example:

    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret"
    }

Postman displays this JSON in a readable format.

---

## 1️⃣5️⃣ JSON vs Python Dictionary

JSON and Python dictionaries look very similar, but they are not exactly the same thing.

When Python receives a JSON response, we can convert it into a Python object using:

    response.json()

Example:

    data = response.json()

For a JSON object, Python normally gives us a dictionary.

### Flow

    Server
       ↓
      JSON
       ↓
    response.json()
       ↓
    Python Dictionary

---

## 1️⃣6️⃣ Calling an API Using Python

I used the `requests` library.

    import requests

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    print("Status Code:", response.status_code)

    print("\nResponse Headers:")
    print(response.headers)

    data = response.json()

    print("\nResponse Body:")
    print(data)

---

## 1️⃣7️⃣ Understanding the Python Code

### Import requests

    import requests

The `requests` library helps Python send HTTP requests.

### Store the API URL

    url = "https://jsonplaceholder.typicode.com/users/1"

This stores the API endpoint.

### Send GET Request

    response = requests.get(url)

Python sends a GET request to the API.

### Check Status Code

    print(response.status_code)

This tells us whether the request was successful.

Example:

    200

means success.

### Get Response Headers

    print(response.headers)

This shows extra information sent with the response.

### Convert JSON

    data = response.json()

This converts the JSON response into a Python object.

For a JSON object, this will normally be a dictionary.

---

## 1️⃣8️⃣ Complete API Flow

    Python
       ↓
    requests.get()
       ↓
    HTTP GET Request
       ↓
    API Server
       ↓
    HTTP Response
       ↓
    ┌─────────────────┐
    │ Status Code 200 │
    │ Headers         │
    │ JSON Body       │
    └─────────────────┘
       ↓
    response.json()
       ↓
    Python Dictionary

---

## 1️⃣9️⃣ Postman vs Python

### Postman

    Postman
       ↓
    GET Request
       ↓
    API
       ↓
    JSON Response

### Python

    Python
       ↓
    requests.get()
       ↓
    API
       ↓
    JSON Response
       ↓
    response.json()
       ↓
    Python Dictionary

### Difference

**Postman** → Quickly test APIs manually.

**Python** → Use APIs inside applications and programs.

---

## 2️⃣0️⃣ My Two API Tests

### Test 1 — Existing User

Request:

    GET
    https://jsonplaceholder.typicode.com/users/1

Response:

    200 OK

Meaning:

    Request successful
    User data received

### Test 2 — Non-existing User

Request:

    GET
    https://jsonplaceholder.typicode.com/users/999999

Response:

    404 Not Found

Meaning:

    Requested resource does not exist

---

## 2️⃣1️⃣ Quick Revision

### REST API

    A way for applications to communicate using HTTP.

### Resource

    The thing we are working with.

Examples:

    /users
    /users/1

### HTTP Methods

    GET     → Read
    POST    → Create
    PUT     → Update
    DELETE  → Delete

### Endpoint

    The path used to access a resource.

### SDK

    Tools/libraries that make working with a service easier.

### Postman

    Tool used to test APIs.

### Status Code

    Tells us what happened with the request.

### Headers

    Extra information about the request/response.

### Body

    Contains the actual data.

### JSON

    Common format used to exchange data between applications.

### response.json()

    Converts the JSON response into a Python object.

---

## 2️⃣2️⃣ Most Important Concepts

### API Request → Response

    API
    ↓
    Receives HTTP Request
    ↓
    Processes Request
    ↓
    Sends HTTP Response
    ↓
    Status Code + Headers + Body

### HTTP Methods

    GET    → Read
    POST   → Create
    PUT    → Update
    DELETE → Delete

### JSON Conversion

    JSON Response
         ↓
    response.json()
         ↓
    Python Dictionary

---

## 2️⃣3️⃣ Day 5 Practice

I tested the API in Postman.

### Test 1

    GET /users/1
    → 200 OK

### Test 2

    GET /users/999999
    → 404 Not Found

I also called the same API using Python.

---

## 2️⃣4️⃣ Files Created

Inside my `week_01` folder:

    DAY_5.md
    day5_api_test.py

---

## 🎯 Day 5 Deliverable

> An API receives a request over HTTP and returns a response, commonly in JSON. I can test APIs using Postman and call them from Python.

---

## ✅ What I Can Do After Day 5

- Understand what a REST API is
- Understand GET, POST, PUT and DELETE
- Understand resources and endpoints
- Understand API vs SDK
- Send GET requests using Postman
- Read HTTP status codes
- Understand basic headers
- Understand JSON responses
- Convert JSON responses into Python objects
- Call an API using Python
- Understand the request → response flow

---

# 🚀 Day 5 Complete!

Another step completed in my **AI-Ready Data Engineer** journey.

The goal is not to memorize everything.

The goal is to understand the flow:

    Request
       ↓
      API
       ↓
    Response
       ↓
      JSON
       ↓
    Application

---

## 🔜 Next

👉 **Day 6 — Continue building the AI Engineering foundation**

---

## 💡 Final Revision

If I forget everything from today, remember these 5 things:

    1. API → Allows applications to communicate

    2. GET → Read data

    3. POST → Create data

    4. Status Code → Tells what happened

    5. JSON → Common format for API data

That's enough for today's foundation. 🚀

---

## ⭐ Follow My Journey

I'm documenting my learning journey step by step.

If you're also learning **Data Engineering, AI Engineering, APIs or Python**, feel free to follow along.

**Learn → Build → Document → Repeat. 🚀**
```
