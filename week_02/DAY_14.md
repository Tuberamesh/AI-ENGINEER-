# 🚀 DAY 14 — POST + Request Body + Headers

> **Week 2 — APIs Properly | Day 14 **

## 👋 Welcome to Day 14

Yesterday in **Day 13**, I learned how Python communicates with an API using **HTTP GET requests**.

I learned the basic flow:

```text
Python Client
     ↓
HTTP Request
     ↓
API / Server
     ↓
JSON Response
     ↓
Python
```

Today, I moved from **receiving data** to **sending data**.

I learned how to use:

* POST
* Request body
* JSON data
* Request headers
* `json=data`
* `response.json()`
* HTTP status code `201`
* `Content-Type`
* `Accept`
* GET vs POST

This is an important step toward becoming an **AI Engineer**, because AI applications constantly send data to APIs.

---

# 🎯 Day 14 Goal

By the end of Day 14, I should understand:

```text
Python
   ↓
POST Request
   ↓
Headers + JSON Body
   ↓
API
   ↓
Server
   ↓
Response
   ↓
Status Code + JSON
   ↓
Python
```

---

# 1️⃣ GET vs POST

## GET

GET is mainly used to **retrieve data**.

```python
response = requests.get(url)
```

Mental model:

```text
"Give me some data."
```

---

## POST

POST is mainly used to **send data** to an API, often to create a new resource.

```python
response = requests.post(url, json=data)
```

Mental model:

```text
"Here is some data. Process/create something with it."
```

### Simple comparison

| Method | Purpose          |
| ------ | ---------------- |
| GET    | Retrieve data    |
| POST   | Send/create data |

---

# 2️⃣ What is a Request Body?

When sending data through POST, the actual data is usually placed inside the **request body**.

Example:

```json
{
    "name": "Ramesha",
    "email": "ramesha@example.com",
    "role": "AI Engineer"
}
```

This is the data that we are sending to the server.

Think:

```text
POST REQUEST

URL
 ↓
Where should the request go?

Headers
 ↓
Information about the request

Body
 ↓
Actual data being sent
```

---

# 3️⃣ What are Headers?

Headers contain additional information about an HTTP request or response.

For example:

```text
Content-Type: application/json
```

This tells the server:

```text
"The data I am sending is JSON."
```

A request can contain:

```text
Method
URL
Headers
Body
```

Example:

```text
POST /users

Headers:
Content-Type: application/json

Body:
{
    "name": "Ramesha",
    "role": "AI Engineer"
}
```

---

# 4️⃣ Python Dictionary → JSON Request

In Python, I can create the data as a dictionary:

```python
data = {
    "name": "Ramesha",
    "email": "ramesha@example.com",
    "role": "AI Engineer"
}
```

Then send it as JSON:

```python
requests.post(url, json=data)
```

The flow is:

```text
Python Dictionary
       ↓
   json=data
       ↓
JSON Request Body
       ↓
      API
       ↓
    Server
```

The `requests` library handles the JSON encoding for me when I use `json=data`.

---

# 5️⃣ My First POST Request

I used JSONPlaceholder as a public testing API.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "AI Engineer",
    "body": "Learning APIs properly",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

I ran it using:

```bash
python day14_post.py
```

The response was similar to:

```text
201
{
    'title': 'AI Engineer',
    'body': 'Learning APIs properly',
    'userId': 1,
    'id': 101
}
```

---

# 6️⃣ Understanding `requests.post()`

The most important line is:

```python
response = requests.post(url, json=data)
```

It contains two important things:

```python
requests.post(
    url,
    json=data
)
```

### `url`

Tells Python where to send the request.

```python
url
```

### `json=data`

Tells Python what JSON data should be sent in the request body.

So:

```text
requests.post()
       ↓
URL + JSON data
       ↓
HTTP POST Request
       ↓
Server
```

---

# 7️⃣ What does `json=data` mean?

Suppose:

```python
data = {
    "name": "Ramesha",
    "role": "AI Engineer"
}
```

Then:

```python
requests.post(url, json=data)
```

sends this information as JSON.

Conceptually:

```text
Python Dictionary
        ↓
     json=data
        ↓
JSON
        ↓
HTTP Request Body
        ↓
API
```

This is a very common pattern when working with APIs.

---

# 8️⃣ Request Headers

I can also explicitly provide headers:

```python
headers = {
    "Content-Type": "application/json"
}
```

Then:

```python
response = requests.post(
    url,
    json=data,
    headers=headers
)
```

Complete example:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "AI Engineer",
    "body": "Learning APIs properly",
    "userId": 1
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    json=data,
    headers=headers
)

print(response.status_code)
print(response.json())
```

### Important note

When using:

```python
json=data
```

the `requests` library already handles the JSON encoding and normally sets the appropriate `Content-Type`.

I included the header here because understanding headers is important for API engineering.

Later, headers become especially important for things such as:

```text
Authorization
API keys
Content-Type
Accept
```

---

# 9️⃣ Content-Type

One important header is:

```text
Content-Type: application/json
```

It tells the server:

```text
"The body of my request is JSON."
```

Mental model:

```text
Content-Type
      ↓
"What format am I sending?"
```

---

# 🔟 Accept

Another common header is:

```text
Accept: application/json
```

This means:

```text
"I would like the response in JSON format."
```

So:

```text
Content-Type
      ↓
Format I am sending

Accept
      ↓
Format I want back
```

Example:

```python
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
```

---

# 1️⃣1️⃣ Request Headers vs Response Headers

These are different.

## Request Headers

They travel:

```text
Python → Server
```

Example:

```python
headers = {
    "Content-Type": "application/json"
}
```

---

## Response Headers

They travel:

```text
Server → Python
```

I can inspect them using:

```python
print(response.headers)
```

So:

```text
REQUEST

Python
  ↓
Request Headers
  ↓
Server


RESPONSE

Server
  ↓
Response Headers
  ↓
Python
```

---

# 1️⃣2️⃣ HTTP Status Code 201

After sending the POST request:

```python
print(response.status_code)
```

I may receive:

```text
201
```

`201` generally means:

```text
Created
```

It is commonly returned when a POST request successfully creates a resource.

Basic comparison:

```text
200 → Successful request
201 → Resource created
```

---

# 1️⃣3️⃣ Reading the Response

After the server responds:

```python
response
```

contains the HTTP response.

I can check the status:

```python
response.status_code
```

And I can convert the JSON response into a Python object:

```python
response.json()
```

Flow:

```text
Server
  ↓
JSON Response
  ↓
response.json()
  ↓
Python Dictionary
```

---

# 1️⃣4️⃣ Mini Project — Send User Data

I created a simple program that takes user input and sends it using POST.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

name = input("Enter your name: ")
email = input("Enter your email: ")
role = input("Enter your role: ")

data = {
    "name": name,
    "email": email,
    "role": role
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    json=data,
    headers=headers
)

print("Status:", response.status_code)
print("Response:", response.json())
```

Example:

```text
Enter your name: Ramesha
Enter your email: ramesha@gmail.com
Enter your role: AI Engineer

Status: 201
Response: {...}
```

---

# 🔍 1️⃣5️⃣ Code Execution Flow

Suppose I enter:

```text
Ramesha
ramesha@gmail.com
AI Engineer
```

### Step 1

```python
name = input("Enter your name: ")
```

Python waits for input.

After entering:

```text
Ramesha
```

we have:

```python
name = "Ramesha"
```

---

### Step 2

```python
email = input("Enter your email: ")
```

After entering:

```text
ramesha@gmail.com
```

we have:

```python
email = "ramesha@gmail.com"
```

---

### Step 3

```python
role = input("Enter your role: ")
```

After entering:

```text
AI Engineer
```

we have:

```python
role = "AI Engineer"
```

---

### Step 4

Python creates the dictionary:

```python
data = {
    "name": name,
    "email": email,
    "role": role
}
```

Now:

```python
data = {
    "name": "Ramesha",
    "email": "ramesha@gmail.com",
    "role": "AI Engineer"
}
```

---

### Step 5

Python executes:

```python
response = requests.post(
    url,
    json=data,
    headers=headers
)
```

The POST request is sent.

Conceptually:

```text
Python
  ↓
POST
  ↓
URL
  ↓
Headers
  ↓
JSON Body
  ↓
API
  ↓
Server
```

---

### Step 6

The server sends a response.

```python
response
```

now contains the response.

---

### Step 7

I check:

```python
response.status_code
```

Result:

```text
201
```

---

### Step 8

I execute:

```python
response.json()
```

The JSON response becomes a Python object.

```text
JSON
 ↓
response.json()
 ↓
Python Dictionary
```

---

# 🧠 1️⃣6️⃣ Complete Mental Model

This is the most important thing I learned today:

```text
                PYTHON CLIENT
                     │
                     │
                     │ POST
                     ↓
          ┌─────────────────────┐
          │    HTTP REQUEST     │
          │                     │
          │ URL                 │
          │ Headers             │
          │ Body                │
          │                     │
          │ JSON DATA           │
          └─────────────────────┘
                     │
                     ↓
                    API
                     │
                     ↓
                   SERVER
                     │
                     ↓
          ┌─────────────────────┐
          │   HTTP RESPONSE     │
          │                     │
          │ Status Code         │
          │ Headers             │
          │ JSON Body           │
          └─────────────────────┘
                     │
                     ↓
                  PYTHON
                     │
                     ↓
             response.json()
```

---

# 🤖 1️⃣7️⃣ Why POST Matters for AI Engineering

POST is extremely important in AI engineering.

AI applications frequently need to **send data to APIs**.

For example:

```text
User Input
    ↓
Python Application
    ↓
POST Request
    ↓
API
    ↓
AI Service
    ↓
JSON Response
    ↓
Python
    ↓
Application Output
```

The exact APIs and request formats will vary, but the underlying HTTP concept is the same.

Understanding POST means I am learning the communication layer that many AI applications depend on.

---

# ⚠️ 1️⃣8️⃣ JSONPlaceholder Note

JSONPlaceholder is a testing API.

When I send a POST request, it can simulate creating a resource and return a successful response such as:

```text
201
```

But I should not treat it as a real database where my newly created data will permanently exist.

It is being used here purely to practice HTTP and API communication.

---

# 📝 Day 14 Key Takeaways

### HTTP Methods

```text
GET
↓
Retrieve data

POST
↓
Send/create data
```

### Request Body

```text
Actual data being sent
```

### Headers

```text
Additional information about the request
```

### `json=data`

```text
Send Python data as JSON
```

### `response.status_code`

```text
Check HTTP result
```

### `201`

```text
Created
```

### `response.json()`

```text
JSON response → Python object
```

### Content-Type

```text
Describes the format being sent
```

### Accept

```text
Describes the response format I prefer
```

---

# ✅ Day 14 Checkpoint

Before moving forward, I should be able to explain these:

* What is the difference between GET and POST?
* What is a request body?
* What are HTTP headers?
* What does `json=data` do?
* What is `Content-Type`?
* What is `Accept`?
* What does status code `201` mean?
* What does `response.json()` do?
* What is the difference between request headers and response headers?

If I can explain these concepts in my own words, **Day 14 is complete.**

---

# 📁 Day 14 Files

My Week 2 structure:

```text
week_02/
│
├── DAY_13.md
├── day13_get.py
│
├── DAY_14.md
└── day14_post.py
```

# 🎉 DAY 14 COMPLETE!

Today I moved from simply **requesting data** to actually **sending data through HTTP**.

The core idea I want to remember is:

```text
GET
→ "Give me data."

POST
→ "Here is some data."
```

And the engineering flow is:

```text
Python
   ↓
POST Request
   ↓
Headers + JSON Body
   ↓
API
   ↓
Server
   ↓
Response
   ↓
Status Code + JSON
   ↓
Python
```

This is another important building block in my journey toward becoming an **AI Engineer**.

---

# 🚀 NEXT — DAY 15

In **Day 15**, I will learn:

```text
PUT
DELETE
```

I will learn how APIs can:

```text
Create
  ↓
POST

Read
  ↓
GET

Update
  ↓
PUT

Delete
  ↓
DELETE
```

This will complete the basic **CRUD + HTTP methods** foundation.

## 🚀 Keep Building. Keep Shipping. Become the Engineer.

**Day 14 → DONE ✅**

**Next stop → Day 15: PUT + DELETE 🔥**

