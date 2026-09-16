
# 🚀 DAY 15 — PUT + DELETE + Status Codes

> **Week 3 — APIs Properly**
>
> **Goal:** Understand the full CRUD API cycle, HTTP status codes, and basic API error handling.

---

# 🎯 What I Learned Today

Today I learned:

- CRUD
- POST
- GET
- PUT
- DELETE
- HTTP status codes
- `response.status_code`
- `response.raise_for_status()`
- API error handling with `try/except`

---

# 1️⃣ CRUD

CRUD represents the four basic operations we commonly perform on data.

| Operation | HTTP Method | Meaning |
|---|---|---|
| Create | POST | Create new data |
| Read | GET | Retrieve data |
| Update | PUT | Update existing data |
| Delete | DELETE | Remove data |

Think about a user:

```text
CREATE USER → POST
GET USER    → GET
UPDATE USER → PUT
DELETE USER → DELETE
````

---

# 2️⃣ POST — Create

POST is generally used when we want to create a new resource.

```python
import requests

data = {
    "name": "Ramesha",
    "email": "ramesha@gmail.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print(response.status_code)
print(response.json())
```

The important part:

```python
requests.post(
    url,
    json=data
)
```

`json=data` contains the information we want to send to the API.

Expected status:

```text
201 Created
```

---

# 3️⃣ GET — Read

GET is used to retrieve data.

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)
print(response.json())
```

Think:

```text
GET /users/1
      ↓
"Give me user 1"
```

Expected status:

```text
200 OK
```

---

# 4️⃣ PUT — Update

PUT is used to update an existing resource.

Example:

```python
data = {
    "name": "Ramesha Updated",
    "email": "updated@gmail.com"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=data
)

print(response.status_code)
print(response.json())
```

The important part:

```python
requests.put(
    url,
    json=data
)
```

Think:

```text
PUT /users/1
      ↓
Update user 1
      ↓
with this data
```

The URL identifies the resource.

The HTTP method tells the server what operation we want to perform.

---

# 5️⃣ DELETE — Delete

DELETE is used to remove a resource.

```python
response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)
```

Think:

```text
DELETE /users/1
       ↓
Delete user 1
```

A DELETE request does not necessarily need a JSON body.

Depending on the API, a successful DELETE may return:

```text
200 OK
```

or:

```text
204 No Content
```

---

# 6️⃣ HTTP Status Codes

After sending an HTTP request, the server sends an HTTP response.

The response contains a status code.

```text
Python
   ↓
HTTP Request
   ↓
Server
   ↓
HTTP Response
   ↓
Status Code
```

---

# 🟢 2xx — Success

```text
200 → OK
201 → Created
204 → No Content
```

### 200 — OK

The request was successful.

Example:

```text
GET /users/1
     ↓
200 OK
```

### 201 — Created

A new resource was successfully created.

Example:

```text
POST /users
     ↓
201 Created
```

### 204 — No Content

The request was successful, but the server has no response body to return.

Example:

```text
DELETE /users/1
     ↓
204 No Content
```

---

# 🟡 4xx — Client / Request Problem

```text
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
429 → Too Many Requests
```

### 400 — Bad Request

The request sent by the client is invalid or cannot be processed.

```text
400 → "Your request is not valid."
```

### 401 — Unauthorized

Valid authentication is required.

```text
401 → "You need valid authentication."
```

For example, an API may require an API key or token.

### 403 — Forbidden

The server understands the request, but the client does not have permission to perform the action.

```text
403 → "You're not allowed to do this."
```

### 404 — Not Found

The requested resource or endpoint could not be found.

```text
GET /users/999999
        ↓
404 Not Found
```

### 429 — Too Many Requests

The client has sent too many requests within a certain period.

```text
429 → "Slow down. Too many requests."
```

---

# 🔴 5xx — Server Problem

```text
500 → Internal Server Error
502 → Bad Gateway
503 → Service Unavailable
```

### 500 — Internal Server Error

Something went wrong on the server.

```text
500 → Server-side error
```

### 502 — Bad Gateway

A server acting as a gateway/proxy received an invalid response from another server.

### 503 — Service Unavailable

The server is temporarily unable to handle the request.

---

# 🧠 Status Code Groups

The easiest way to remember status codes:

```text
2xx → Success
4xx → Client / request problem
5xx → Server problem
```

---

# 7️⃣ Checking Status Codes in Python

We can access the status code using:

```python
response.status_code
```

Example:

```python
response = requests.get(url)

print(response.status_code)
```

We can also check specific codes:

```python
if response.status_code == 200:
    print("Success")

elif response.status_code == 404:
    print("Not found")
```

---

# 8️⃣ `raise_for_status()`

Instead of manually checking every error status, `requests` provides:

```python
response.raise_for_status()
```

It checks the HTTP response.

If the response indicates an unsuccessful HTTP status, it raises an exception.

Example:

```python
response = requests.get(url)

response.raise_for_status()

data = response.json()
```

If the response is:

```text
200
```

then:

```text
raise_for_status()
        ↓
No exception
        ↓
Program continues
```

If the response is:

```text
404
```

then:

```text
raise_for_status()
        ↓
Exception
        ↓
Error handling
```

### Simple memory:

```text
raise_for_status()
        ↓
"Did the HTTP request fail?"
        ↓
Yes → Raise exception
No  → Continue
```

---

# 9️⃣ Combining `try/except` with API Requests

This connects today's API knowledge with the exception handling learned in Week 2.

```python
try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

Flow:

```text
try
 ↓
Send request
 ↓
Receive response
 ↓
raise_for_status()
 ↓
 ├── Success → Continue
 │
 └── Error → Exception
                ↓
              except
```

`RequestException` is used to catch request-related errors from the `requests` library.

---

# 🔟 Complete CRUD Example

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"

# GET
response = requests.get(f"{url}/1")

print("GET")
print("Status:", response.status_code)
print("Response:", response.json())


# POST
data = {
    "name": "Ramesha",
    "email": "ramesha@gmail.com"
}

response = requests.post(
    url,
    json=data
)

print("\nPOST")
print("Status:", response.status_code)
print("Response:", response.json())


# PUT
data = {
    "name": "Ramesha Updated",
    "email": "updated@gmail.com"
}

response = requests.put(
    f"{url}/1",
    json=data
)

print("\nPUT")
print("Status:", response.status_code)
print("Response:", response.json())


# DELETE
response = requests.delete(
    f"{url}/1"
)

print("\nDELETE")
print("Status:", response.status_code)
```

---

# 1️⃣1️⃣ CRUD Flow

```text
             CRUD
              │
     ┌────────┼────────┐
     ↓        ↓        ↓
  CREATE    READ     UPDATE
    POST     GET       PUT
              │
              ↓
            DELETE
```

A more practical view:

```text
POST /users
     ↓
Create user

GET /users/1
     ↓
Read user

PUT /users/1
     ↓
Update user

DELETE /users/1
     ↓
Delete user
```

---

# 🧠 Important Concepts to Remember

### HTTP Method

Tells the server **what operation we want to perform**.

```text
GET
POST
PUT
DELETE
```

### Endpoint

Identifies the resource we are interacting with.

```text
/users
/users/1
/products
/products/10
```

### JSON Body

Contains data we want to send.

```python
json=data
```

### Status Code

Tells us what happened with the request.

```text
200 → Success
201 → Created
404 → Not Found
500 → Server Error
```

### `raise_for_status()`

Automatically raises an exception when the response has an unsuccessful HTTP status.

---

# 🧪 Day 15 Practice

Created:

```text
day15_crud.py
```

Performed:

```text
GET
POST
PUT
DELETE
```

Printed:

```text
Method
Status Code
Response
```

---

# ✅ Day 15 Summary

Today I learned the complete CRUD cycle:

```text
CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE
```

I also learned how to understand HTTP status codes:

```text
2xx → Success
4xx → Client / request problem
5xx → Server problem
```

And learned how:

```python
response.raise_for_status()
```

works together with:

```python
try:
    ...
except requests.exceptions.RequestException:
    ...
```

This connects API requests with the exception handling concepts learned earlier.

---

# 🚀 What's Next?

## DAY 16 — Authentication + REST + API Design

Next I will learn:

* API Keys
* Bearer Tokens
* Authorization Headers
* `.env` for secrets
* REST
* Resources
* Endpoints
* Stateless requests
* JSON representations
* API architecture

The goal is to understand how **real-world APIs** work beyond simple public APIs.

---


> **Keep building. Don't just memorize APIs — understand how the request, server, response, and data flow work together. 🚀**

