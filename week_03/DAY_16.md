# 🚀 DAY 16 — Authentication + REST + API Design

> **Week 3 — APIs Properly**
>
> Day 16 focuses on authentication, REST concepts, and how a real-world API communicates between a client, API, server, and database.

---

## 🎯 Goal

By the end of Day 16, I should understand:

- Why APIs need authentication
- API Keys
- Bearer Tokens
- Authorization Headers
- Why secrets should not be hard-coded
- `.env` for protecting API credentials
- What REST means
- Resources
- Endpoints
- HTTP methods
- Stateless requests
- JSON representations
- Basic API architecture
- Client → API → Server → Database → Response

---

# 🔐 1. Authentication

## What is Authentication?

Authentication is the process of identifying who is making a request.

An API may require authentication before allowing access to protected data or functionality.

### Simple flow

```text
Python
   ↓
HTTP Request + Credential
   ↓
API
   ↓
Credential Checked
   ↓
Server
   ↓
Response
````

### Authentication vs Authorization

**Authentication:**

> Who are you?

**Authorization:**

> What are you allowed to access or do?

Example:

```text
Authentication:
"Are you Ramesh?"

Authorization:
"Is Ramesh allowed to access this data?"
```

---

# 🔑 2. API Key

An API Key is a credential provided by an API service.

It can be used to identify or authenticate an application making API requests.

Example:

```text
API_KEY = "abc123xyz789"
```

Think of an API key as a secret credential similar to a password, but it is specifically used for API access.

### Important

An API key is **not the HTTP header itself**.

The API key is the credential that can be placed inside a header.

```text
API Key
   ↓
Credential / Secret
   ↓
Placed inside
   ↓
HTTP Header
```

---

# 🎫 3. Bearer Token

A Bearer Token is a token commonly sent using the HTTP `Authorization` header.

Example:

```text
Authorization: Bearer abc123xyz789
```

The important parts are:

```text
Authorization → Header name

Bearer → Authentication scheme

abc123xyz789 → Token / credential
```

### Mental model

```text
Token
  ↓
Bearer
  ↓
Authorization Header
  ↓
HTTP Request
  ↓
API
```

---

# 📦 4. Authorization Header

Authentication credentials are commonly placed inside an HTTP header.

Python example:

```python
headers = {
    "Authorization": f"Bearer {API_KEY}"
}
```

Then:

```python
response = requests.get(
    "https://api.example.com/users",
    headers=headers
)
```

### What does `headers=headers` mean?

It tells the `requests` library:

> Include the headers stored in the `headers` dictionary in the HTTP request.

So:

```python
headers = {
    "Authorization": f"Bearer {API_KEY}"
}
```

creates the headers.

And:

```python
requests.get(url, headers=headers)
```

sends those headers along with the HTTP request.

### Flow

```text
API Key / Token
      ↓
HTTP Header
      ↓
Authorization
      ↓
API
      ↓
Server checks credential
      ↓
Response
```

---

# 🚨 5. Never Hard-Code Secrets

Avoid:

```python
API_KEY = "abc123secret"
```

If this code is pushed to GitHub, the secret may become publicly visible.

Instead, store secrets in a `.env` file.

### `.env`

```text
API_KEY=abc123secret
```

### Python

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
```

Then:

```python
headers = {
    "Authorization": f"Bearer {API_KEY}"
}
```

### Complete flow

```text
.env
 ↓
API_KEY
 ↓
Python
 ↓
Authorization Header
 ↓
API
 ↓
Server
```

The `.env` file should also be included in `.gitignore`.

Example:

```text
.env
```

### Why use `.env`?

Because secrets such as API keys should not be directly written into source code.

This reduces the chance of accidentally exposing credentials when sharing code or pushing it to GitHub.

---

# 🌐 6. REST

REST stands for:

> **Representational State Transfer**

REST is an architectural style for designing APIs.

The most important practical idea is:

> **REST organizes APIs around resources and uses HTTP methods to operate on those resources.**

---

# 📦 7. Resources

A resource is a thing or data that an API manages.

Examples:

```text
Users
Products
Orders
Students
Courses
```

They can be represented through endpoints such as:

```text
/users
/products
/orders
/students
/courses
```

Think:

```text
Resource        Endpoint

Users      →    /users
Products   →    /products
Orders     →    /orders
```

---

# 🔗 8. Endpoints

An endpoint is a specific URL through which an API provides access to a resource or operation.

Examples:

```text
/users
/users/5

/products
/products/10

/orders
/orders/25
```

For example:

```text
/users
```

can represent the collection of users.

```text
/users/5
```

can represent a specific user.

### Collection vs Specific Resource

```text
/users
   ↓
All users / users collection
```

```text
/users/5
   ↓
One specific user
```

---

# 🔄 9. HTTP Methods + REST

The HTTP method tells the server what operation we want to perform.

For example:

```text
GET /users/5
```

means:

> Retrieve User 5.

```text
PUT /users/5
```

means:

> Update or replace User 5.

```text
DELETE /users/5
```

means:

> Delete User 5.

Notice:

```text
GET    /users/5
PUT    /users/5
DELETE /users/5
```

The resource is the same.

The HTTP method changes the operation.

### Important REST idea

Don't think:

```text
GET endpoint
POST endpoint
DELETE endpoint
```

Instead think:

```text
RESOURCE
   ↓
/users/5
   ↓
HTTP METHOD decides the operation
```

---

# ➕ 10. POST in REST

POST is commonly used to create a new resource.

Example:

```text
POST /users
```

Request body:

```json
{
    "name": "Ramesh",
    "age": 21
}
```

The server may create a new user such as:

```text
/users/6
```

So:

```text
POST /users
```

→ Create a new user

while:

```text
GET /users/6
```

→ Retrieve User 6

### REST CRUD Mental Model

```text
Operation    HTTP Method    Example

Create       POST           POST /users
Read         GET            GET /users/5
Update       PUT            PUT /users/5
Delete       DELETE         DELETE /users/5
```

---

# 🔄 11. Stateless Requests

Statelessness is an important REST concept.

### Stateless means:

> **Each request should contain the information needed by the server to process that request.**

The server should not depend on remembering the previous request.

Example:

```text
Request 1
GET /users/5
Authorization: Bearer ABC123

Request 2
GET /users/10
Authorization: Bearer ABC123

Request 3
GET /users/20
Authorization: Bearer ABC123
```

Each request can be processed independently.

Think:

```text
Request 1 → Server → Response

Request 2 → Server → Response

Request 3 → Server → Response
```

The server does not need to rely on the previous request to understand the current one.

### One-line definition

> **Stateless = Each request is independent and contains the information needed to process it.**

---

# 📄 12. JSON Representations

REST APIs commonly exchange data using JSON.

For example:

```text
/users/5
```

The server may return:

```json
{
    "id": 5,
    "name": "Ramesh",
    "age": 21
}
```

This JSON is a **representation of User 5**.

The actual resource may exist inside a database, but the client receives a representation of that resource.

### Flow

```text
Database
   ↓
User 5
   ↓
API
   ↓
JSON Representation
   ↓
Python
```

---

# 🐍 13. JSON in Python

Using the `requests` library:

```python
response = requests.get(url)

data = response.json()
```

`response.json()` converts the JSON response into Python data such as a dictionary or list.

Example:

```python
data = response.json()

print(data["name"])
```

### Flow

```text
Server
   ↓
JSON
   ↓
HTTP Response
   ↓
requests
   ↓
response.json()
   ↓
Python dictionary/list
```

---

# 🏗️ 14. API Architecture

A real API request can involve multiple components.

```text
             HTTP Request
Python ─────────────────────→ API
Client                         │
                               ↓
                             Server
                               │
                               ↓
                           Database
                               │
                               ↓
                          JSON Response
                               │
                               ↓
Python ←───────────────────────┘
```

---

## Step 1 — Python Client

The Python program is the client.

Example:

```python
response = requests.get(url)
```

Python wants data from another system.

---

## Step 2 — HTTP Request

The `requests` library creates and sends an HTTP request.

Example:

```text
GET /users/5
```

The request can contain:

```text
Method
URL
Headers
Parameters
Body
```

depending on the request.

---

## Step 3 — API

The API is the interface through which the application communicates with another system.

Examples:

```text
GET /users
POST /users
GET /users/5
DELETE /users/5
```

Think:

> **API = Interface/rules for communicating with another system.**

---

## Step 4 — Server

The request reaches a server/application that handles the request.

For example:

```text
GET /users/5
       ↓
Server:
"Find user with ID 5"
```

The server contains the application logic required to process the request.

---

## Step 5 — Database

The server may communicate with a database to retrieve or modify information.

Example:

```text
Server
   ↓
Database
   ↓
Find User 5
```

The database might contain:

```text
id    name       age
5     Ramesh     21
```

---

## Step 6 — JSON Response

The server sends the result back to the client.

Example:

```json
{
    "id": 5,
    "name": "Ramesh",
    "age": 21
}
```

---

## Step 7 — Python Processes the Response

Python receives the HTTP response:

```python
response = requests.get(url)
```

Then:

```python
data = response.json()
```

Python can now process, filter, display, or save the data.

---

# 🧠 15. Complete API Mental Model

```text
Python
  │
  │ HTTP Request
  ↓
API
  │
  ↓
Server
  │
  │ asks for data
  ↓
Database
  │
  │ returns data
  ↓
Server
  │
  │ JSON Response
  ↓
API
  │
  ↓
Python
```

### Important

An API is an **interface**.

The server/application handles the logic behind that interface and may communicate with a database.

A useful mental model is:

```text
Your Python Application
        ↓
       HTTP
        ↓
   API Interface
        ↓
Server/Application Logic
        ↓
     Database
```

---

# 🔥 16. Complete Week 3 API Flow

The concepts learned so far can be connected like this:

```text
Python Client
      ↓
HTTP Request
      ↓
HTTP Method
      ↓
Endpoint
      ↓
Headers / Parameters / Body
      ↓
Authentication
      ↓
API
      ↓
Server
      ↓
Database
      ↓
Server processes result
      ↓
HTTP Response
      ↓
JSON
      ↓
Python
```

---

# 🧠 17. Day 16 Revision

## 1. What is an API?

An API is an interface that allows one application to communicate with another system using defined rules.

---

## 2. What is HTTP?

HTTP is the protocol used to send requests and responses between clients and servers.

---

## 3. What is an endpoint?

An endpoint is a specific API URL used to access or perform an operation on a resource.

---

## 4. GET vs POST?

GET is generally used to retrieve data.

POST is generally used to create or send new data.

---

## 5. PUT vs DELETE?

PUT is generally used to update or replace a resource.

DELETE is used to remove a resource.

---

## 6. Header vs Body?

A header contains metadata or instructions about the request or response.

The body contains the actual data being sent.

Example:

```text
Header:
Authorization: Bearer ABC123

Body:
{
    "name": "Ramesh",
    "age": 21
}
```

---

## 7. Parameter vs Body?

Parameters provide additional information through the URL, such as query parameters or path parameters.

The body carries data inside the HTTP request.

Example path parameter:

```text
/users/5
```

Here:

```text
5
```

identifies a specific user and can be treated as a path parameter.

Example query parameter:

```text
/users?age=21
```

Here:

```text
age=21
```

is a query parameter.

A body could contain:

```json
{
    "name": "Ramesh",
    "age": 21
}
```

---

## 8. What does 401 mean?

```text
401 Unauthorized
```

The request does not have valid authentication credentials or the credentials were not accepted.

---

## 9. What does 404 mean?

```text
404 Not Found
```

The requested resource or endpoint could not be found.

---

## 10. Why use `.env`?

`.env` helps keep sensitive information such as API keys outside the source code.

This reduces the chance of accidentally exposing secrets when sharing or pushing code to GitHub.

---

# 📝 18. Key Takeaways

```text
API
→ Interface between applications/systems

HTTP
→ Protocol used for request/response communication

Endpoint
→ Specific API URL

API Key
→ Credential used for API access

Bearer Token
→ Token commonly sent through Authorization header

Authorization Header
→ Header used to carry authentication information

REST
→ Architectural style for designing APIs around resources

Resource
→ Data/entity managed by an API

Stateless
→ Each request is independent

JSON
→ Common format for representing/transferring data

.env
→ Keeps secrets/configuration outside source code
```

---

# 🚀 19. Final Mental Model

```text
                 HTTP REQUEST
Python ─────────────────────────→ API
Client                              │
                                    ↓
                              Authentication
                                    │
                                    ↓
                                  Server
                                    │
                                    ↓
                                Database
                                    │
                                    ↓
                              JSON RESPONSE
                                    │
                                    ↓
Python ←────────────────────────────┘
```

---

# 🎯 DAY 16 COMPLETED ✅

Today I learned:

* Authentication
* API Keys
* Bearer Tokens
* Authorization Headers
* `.env`
* REST
* Resources
* Endpoints
* HTTP methods
* Stateless requests
* JSON representations
* API architecture
* Client → API → Server → Database → Response

---

# 🔗 Previous Day

[← Day 15 — PUT, DELETE & Status Codes](./DAY_15.md)

---

# 💡 Final Thought

> **Don't just learn how to call an API. Understand what happens behind the request.**

```text
Python
   ↓
HTTP
   ↓
API
   ↓
Server
   ↓
Database
   ↓
JSON
   ↓
Python
```

This mental model is the foundation for building real-world applications with APIs.

---



> **Learn → Build → Understand → Repeat.**

