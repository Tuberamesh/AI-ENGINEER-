# 🚀 DAY 3 — HTTP + APIs + JSON

> 👋 **Hey! Welcome to Day 3 of my AI Engineering journey.**
>
> Today we're going to understand something you'll use almost everywhere in AI Engineering:
>
> **How applications communicate with APIs.**
>
> If you missed Day 2, start here:
>
> 👉 [📚 Day 2 — Python Environment & Packages](./DAY_2.md)
>
> Don't just read this. **Run the code yourself and understand the flow.**

---

## 🎯 What I Learned Today

By the end of Day 3, I understood:

* What HTTP is
* What an API is
* What an API endpoint is
* HTTP methods

  * GET
  * POST
  * PUT
  * DELETE
* CRUD operations
* HTTP status codes
* What a request contains
* What a response contains
* What JSON is
* Python Dictionary vs JSON
* `response.json()`
* Query parameters
* How Python communicates with an API

---

# 1️⃣ What is HTTP?

**HTTP = HyperText Transfer Protocol**

It is a set of rules that allows applications to communicate with each other over a network.

For example:

```text
My Python Program
       │
       │ HTTP Request
       ↓
     Server
       │
       │ HTTP Response
       ↓
My Python Program
```

Whenever we use an API, HTTP is commonly involved in this communication.

---

# 2️⃣ What is an API?

**API = Application Programming Interface**

An API allows one application to communicate with another application or service.

Think about a restaurant:

```text
You → Waiter → Kitchen
```

You don't directly enter the kitchen.

You tell the waiter what you want.

The waiter takes your request to the kitchen and brings the result back.

Similarly:

```text
Your Application
       ↓
      API
       ↓
    Server
       ↓
      Data
```

The API acts as the communication interface.

---

# 3️⃣ What is an API Endpoint?

An **endpoint** is a specific URL/path where we send an API request.

For example:

```text
https://jsonplaceholder.typicode.com/users/1
```

Let's break it down:

```text
https://
   ↓
Protocol

jsonplaceholder.typicode.com
   ↓
Server / Domain

/users/1
   ↓
Endpoint / Path
```

Here:

```text
/users/1
```

means:

> Give me the user whose ID is 1.

---

# 4️⃣ My First API Request

I used Python's `requests` library.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)
print(response.json())
```

Output:

```text
200
{'id': 1, 'name': 'Leanne Graham', ...}
```

---

## 🔍 What happened?

```text
Python
   │
   │ GET /users/1
   ↓
API Server
   │
   │ Finds user 1
   ↓
Response
   │
   ├── Status Code → 200
   └── JSON Data
```

So my Python program asked:

> "Give me user 1."

The server replied:

> "Here is user 1."

---

# 5️⃣ HTTP Methods

HTTP methods tell the server **what we want to do**.

The four important methods I learned today:

| Method | Purpose     |
| ------ | ----------- |
| GET    | Read data   |
| POST   | Create data |
| PUT    | Update data |
| DELETE | Delete data |

Easy way to remember:

```text
GET     → Give me data
POST    → Create something
PUT     → Update something
DELETE  → Remove something
```

---

# 6️⃣ CRUD

These HTTP methods map nicely to CRUD operations.

```text
CRUD

C → Create → POST
R → Read   → GET
U → Update → PUT
D → Delete → DELETE
```

This is a very important connection to remember.

---

# 7️⃣ GET — Read Data

GET is used when we want to retrieve data.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/3"
)

print(response.status_code)
print(response.json())
```

If the request succeeds:

```text
200
```

The response contains the requested user.

### Think:

```text
GET /users/3
```

Means:

> Give me user 3.

---

# 8️⃣ POST — Create Data

POST is used when we want to create a new resource.

Example:

```python
import requests

data = {
    "name": "John Doe",
    "username": "johndoe",
    "email": "john.doe@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print(response.status_code)
print(response.json())
```

Output:

```text
201
{'id': 11, 'name': 'John Doe', ...}
```

---

## 🔍 What happened?

We sent:

```json
{
  "name": "John Doe",
  "username": "johndoe",
  "email": "john.doe@example.com"
}
```

The server created a resource and returned:

```text
201 Created
```

It also gave us an ID:

```json
{
  "id": 11,
  "name": "John Doe"
}
```

---

# 9️⃣ Is `11` a Default ID?

**No.**

`11` is NOT a default number.

In this particular test API, existing users already had IDs like:

```text
1
2
3
...
10
```

So the newly created resource received:

```text
11
```

In real applications, IDs can be generated in different ways.

For example:

```text
Sequential ID
1, 2, 3, 4...

UUID
550e8400-e29b-41d4-a716-446655440000

Other generated IDs
```

So:

> **Never assume that the next ID will always be 11.**

The server/database is responsible for generating the ID.

If the API returns:

```python
result = response.json()

user_id = result["id"]
```

we should use that returned ID.

---

# 🔟 PUT — Update Data

PUT is used to update an existing resource.

For example:

```python
import requests

data = {
    "name": "Ramesh",
    "username": "decoder"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/3",
    json=data
)

print(response.status_code)
print(response.json())
```

Notice the endpoint:

```text
/users/3
```

Why?

Because we are updating a **specific user**.

```text
POST
/users
 ↓
Create a new user


PUT
/users/3
 ↓
Update user 3
```

---

# 1️⃣1️⃣ DELETE — Remove Data

DELETE is used to delete an existing resource.

```python
import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/3"
)

print(response.status_code)
print(response.json())
```

A successful DELETE may return:

```text
200
```

or:

```text
204
```

---

# 1️⃣2️⃣ What is HTTP Status Code?

A status code tells us **what happened to our request**.

The first digit tells us the category:

```text
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error
```

### Important status codes

| Status | Meaning               |
| ------ | --------------------- |
| `200`  | OK / Successful       |
| `201`  | Created               |
| `204`  | Success, no content   |
| `400`  | Bad Request           |
| `401`  | Unauthorized          |
| `404`  | Not Found             |
| `500`  | Internal Server Error |

---

## 🤔 Why 200 and not 300?

Because HTTP status codes have **standard meanings**.

```text
200 → Success
300 → Redirection
```

So if my GET request successfully retrieves data:

```text
200 OK
```

is appropriate.

We don't randomly choose `300`.

---

# 1️⃣3️⃣ Understanding 404

Suppose I request:

```text
/users/999999
```

and the resource doesn't exist.

The server can return:

```text
404
```

`404 Not Found` means:

> The requested resource could not be found.

It doesn't necessarily mean my Python code is broken.

The request reached the server, but the requested resource/path wasn't found.

---

# 1️⃣4️⃣ Request vs Response

This is one of the most important concepts from today.

## REQUEST

What **we send to the server**.

```text
REQUEST
│
├── URL
├── METHOD
├── HEADERS
├── QUERY PARAMETERS
└── BODY
```

## RESPONSE

What **the server sends back to us**.

```text
RESPONSE
│
├── STATUS CODE
├── HEADERS
└── BODY
```

Complete flow:

```text
                 REQUEST
Python ─────────────────────────→ Server
       URL
       Method
       Headers
       Query Params
       Body


                 RESPONSE
Python ←───────────────────────── Server
       Status Code
       Headers
       Body
```

---

# 1️⃣5️⃣ What is the Request URL?

The URL tells the application **where to send the request**.

Example:

```text
https://jsonplaceholder.typicode.com/users/3
```

Think:

```text
URL
 ↓
WHERE should I send this request?
```

---

# 1️⃣6️⃣ What is the Request Method?

The method tells the server **what we want to do**.

```text
GET
POST
PUT
DELETE
```

Think:

```text
METHOD
 ↓
WHAT do I want to do?
```

---

# 1️⃣7️⃣ What is the Request Body?

The body contains the **data we send to the server**.

For example:

```python
data = {
    "name": "Ramesh",
    "username": "decoder"
}
```

Then:

```python
requests.post(
    url,
    json=data
)
```

The body contains:

```json
{
  "name": "Ramesh",
  "username": "decoder"
}
```

Think:

```text
BODY
 ↓
WHAT DATA am I sending?
```

---

# 1️⃣8️⃣ What are Headers?

Headers contain **additional information about the request or response**.

For example:

```python
headers = {
    "Content-Type": "application/json"
}
```

This tells the server:

> The data I'm sending is JSON.

Headers can also contain other information such as authentication details, but we'll learn those when we reach API authentication.

Think:

```text
HEADERS
 ↓
EXTRA INFORMATION
```

---

# 1️⃣9️⃣ Query Parameters

Query parameters are extra values added to the URL to control or filter the request.

Example:

```text
/users?id=3
```

Here:

```text
/users
 ↓
Endpoint

?
 ↓
Starts query parameters

id=3
 ↓
Parameter
```

So:

```text
/users?id=3
```

can mean:

> Give me the user with ID 3.

---

## Multiple Query Parameters

```text
/users?limit=10&page=2
```

Here:

```text
limit = 10
page  = 2
```

---

## Python Example

Instead of manually writing:

```python
url = "https://example.com/users?id=3"
```

we can use:

```python
params = {
    "id": 3
}

response = requests.get(
    "https://example.com/users",
    params=params
)
```

Python constructs the query string for us.

Think:

```text
QUERY PARAMETERS
 ↓
HOW / WHICH DATA do I want?
```

---

# 2️⃣0️⃣ What is JSON?

**JSON = JavaScript Object Notation**

JSON is a standard format used to exchange data between applications.

Example:

```json
{
  "id": 1,
  "name": "Ramesh",
  "username": "decoder"
}
```

JSON is extremely common in APIs.

---

# 2️⃣1️⃣ Python Dictionary vs JSON

They can look very similar, but they are not exactly the same thing.

Python:

```python
data = {
    "id": 1,
    "name": "Ramesh"
}
```

JSON:

```json
{
  "id": 1,
  "name": "Ramesh"
}
```

Think of it like this:

```text
Python Dictionary
       ↓
   Convert/send
       ↓
      JSON
       ↓
     Server
```

And when receiving:

```text
Server
   ↓
 JSON
   ↓
response.json()
   ↓
Python object
```

---

# 2️⃣2️⃣ What Does `response.json()` Do?

This was an important concept I learned.

When the server sends JSON data, we can use:

```python
response.json()
```

to convert the JSON response into a Python object that we can work with.

Example:

Server sends:

```json
{
  "id": 1,
  "name": "Ramesh"
}
```

Python:

```python
data = response.json()
```

Now:

```python
print(data["name"])
```

Output:

```text
Ramesh
```

So remember:

```text
SERVER
  ↓
JSON
  ↓
response.json()
  ↓
Python dictionary/list
```

### Important:

`response.json()` is **not used to "make something JSON"**.

It is used to **read/parse JSON received from the server into a Python object**.

---

# 2️⃣3️⃣ Sending JSON vs Receiving JSON

This distinction is very important.

## Sending

```python
data = {
    "name": "Ramesh"
}

requests.post(
    url,
    json=data
)
```

Conceptually:

```text
Python Dictionary
       ↓
      JSON
       ↓
     Server
```

## Receiving

```python
data = response.json()
```

Conceptually:

```text
Server
   ↓
 JSON
   ↓
response.json()
   ↓
Python object
```

### Easy memory trick

```text
SEND
dict → JSON → Server

RECEIVE
Server → JSON → response.json() → Python
```

---

# 2️⃣4️⃣ JSON Data Types

JSON supports common data types:

```text
String
Number
Boolean
Null
Object
Array
```

Example:

```json
{
  "name": "Ramesh",
  "age": 21,
  "student": true,
  "skills": ["Python", "SQL", "AI"],
  "address": {
    "city": "Bengaluru"
  }
}
```

One small difference:

JSON:

```text
true
false
null
```

Python:

```text
True
False
None
```

---

# 2️⃣5️⃣ Complete API Flow

Now let's connect everything I've learned.

```text
                    CLIENT
               Python Application
                       │
                       │ HTTP REQUEST
                       │
             ┌─────────┴─────────┐
             │                   │
           URL                 METHOD
             │                   │
             │              GET / POST /
             │              PUT / DELETE
             │
        HEADERS
             │
       QUERY PARAMS
             │
           BODY
             │
             ↓
                    API SERVER
                       │
                       │
                  Process Request
                       │
                       ↓
                    RESPONSE
                       │
             ┌─────────┴─────────┐
             │                   │
        STATUS CODE             BODY
             │                   │
          200 / 201              JSON
          400 / 404
          500
```

---

# 🧠 The Most Important Mental Model

If you remember only one diagram from Day 3, remember this:

```text
REQUEST
│
├── URL        → WHERE?
├── METHOD     → WHAT?
├── HEADERS    → EXTRA INFO?
├── PARAMETERS → WHICH/HOW?
└── BODY       → WHAT DATA?
        │
        ↓
      SERVER
        │
        ↓
RESPONSE
│
├── STATUS CODE → WHAT HAPPENED?
├── HEADERS     → EXTRA INFO
└── BODY        → DATA / JSON
```

---

# 🛠️ My Day 3 Practice

I actually tested these operations using Python.

```python
import requests

# GET
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)
print(response.json())


# POST
data = {
    "name": "John Doe",
    "username": "johndoe",
    "email": "john.doe@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print(response.status_code)
print(response.json())


# PUT
data = {
    "name": "Ramesh",
    "username": "decoder"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/3",
    json=data
)

print(response.status_code)
print(response.json())


# DELETE
response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/3"
)

print(response.status_code)
print(response.json())
```

---

# 📌 Quick Revision

| Concept           | Remember                           |
| ----------------- | ---------------------------------- |
| HTTP              | Rules for communication            |
| API               | Interface between applications     |
| Endpoint          | Specific API URL/path              |
| GET               | Read                               |
| POST              | Create                             |
| PUT               | Update                             |
| DELETE            | Delete                             |
| CRUD              | Create, Read, Update, Delete       |
| 200               | Success                            |
| 201               | Created                            |
| 204               | Success, no content                |
| 400               | Bad request                        |
| 401               | Unauthorized                       |
| 404               | Not found                          |
| 500               | Server error                       |
| JSON              | Data exchange format               |
| `response.json()` | JSON response → Python object      |
| Query Params      | Extra values in URL                |
| Headers           | Extra request/response information |
| Body              | Data being sent                    |

---

# 🎤 Interview Questions I Should Be Able To Answer

### What is an API?

> An API is an interface that allows different applications or systems to communicate with each other.

### What is an endpoint?

> An endpoint is a specific URL/path where an API request is sent.

### Difference between GET and POST?

> GET is generally used to retrieve data, while POST is generally used to create/send data.

### Why did POST return 201?

> `201 Created` means the server successfully created a new resource.

### Is ID 11 a default?

> No. In this test API, 11 was assigned because the existing users already had IDs 1–10. In real applications, IDs can be generated in different ways.

### What does 404 mean?

> The requested resource or endpoint was not found.

### Why 200 instead of 300?

> HTTP status codes are standardized. 200 represents success, while 300 belongs to the redirection category.

### What does `response.json()` do?

> It parses the JSON response received from the server into a Python object that I can work with.

### What is the difference between request and response?

> A request is what the client sends to the server. A response is what the server sends back to the client.

---

# 🚀 Day 3 Takeaway

Before Day 3, an API URL looked like just a complicated link.

Now I can look at:

```text
https://example.com/users/3
```

and understand:

```text
HTTPS
  ↓
Protocol

/users/3
  ↓
Endpoint

GET
  ↓
Operation

200
  ↓
Successful response

JSON
  ↓
Data format
```

That's the foundation I need before working with **real-world APIs and AI APIs**.

---

## 🔥 Challenge Before Moving to Day 4

Don't just copy the code.

Try changing:

```text
GET user 1 → user 5
```

Then try:

```text
POST a different user
```

Then:

```text
PUT user 5
```

And finally:

```text
DELETE user 5
```

After running them, explain the flow to yourself:

```text
Request
   ↓
Server
   ↓
Response
```

If you can explain that without looking at these notes, **Day 3 is done.** ✅

---

# 📅 Day 3 Completed

```text
HTTP             ✅
API              ✅
Endpoints        ✅
GET              ✅
POST             ✅
PUT              ✅
DELETE           ✅
CRUD             ✅
Status Codes     ✅
Requests         ✅
Responses        ✅
Headers          ✅
Body             ✅
Query Parameters ✅
JSON             ✅
response.json()  ✅
API Flow         ✅
```

> **Day 3 complete. 🚀**
>
> **Next stop → Day 4**
>
> Keep building. Keep breaking things. Keep learning.
>
> **One day at a time. One concept at a time.**
>
> — **Decoder Space | AI Engineering Journey**
