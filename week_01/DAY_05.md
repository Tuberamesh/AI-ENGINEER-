i m trying direct web version for light weight 
im not finding any get somehting here

Absolutely bro 🔥 Here is your complete DAY_5.md, written as if you are teaching someone who visits your GitHub repo.

I kept it:

Beginner-friendly
Step-by-step
Revision-friendly
With important diagrams
With practical code
With Postman practice
With a Day 4 link placeholder
With CTA at the end

Copy everything below directly into DAY_5.md:

# 🚀 Day 5 — REST APIs, SDKs & Postman

Hey everyone! 👋

Welcome to **Day 5** of my journey toward becoming an **AI-Ready Data Engineer**.

Yesterday, I learned about API requests, responses, JSON, and how to work with APIs using Python.

👉 **Missed Day 4? Check it here:**  
[📖 Day 4 — API Keys & Environment Variables](./Day_4.md)

Today, I wanted to understand something very important:

> **How do APIs actually work, how can I test them, and what is the difference between an API and an SDK?**

Let's learn it step by step.

---

# 📌 Today's Learning Goals

By the end of Day 5, I should understand:

- What is a REST API?
- What is a resource?
- What is an endpoint?
- GET, POST, PUT and DELETE
- What is an SDK?
- API vs SDK
- What is Postman?
- HTTP Request
- HTTP Response
- Status codes
- Response body
- Headers
- Calling an API using Python

---

# 1️⃣ What is a REST API?

Let's start with the simplest definition.

**REST API** is a common way of designing APIs using HTTP methods and URLs to work with resources.

For example, imagine we have a server containing users.

```text
/users

This represents the users resource.

If I want a specific user:

/users/1

This represents user with ID 1.

2️⃣ What is a Resource?

A resource is the thing we want to work with.

Examples:

/users
/products
/orders
/students
/movies

For example:

/users

means the collection of users.

And:

/users/1

means one specific user.

Think of it like:

/users
   ↓
All users

/users/1
   ↓
User with ID 1
3️⃣ HTTP Methods

HTTP methods tell the server what action we want to perform.

The four important methods are:

Method	Meaning	Example
GET	Read data	GET /users
POST	Create data	POST /users
PUT	Update data	PUT /users/1
DELETE	Delete data	DELETE /users/1
Easy way to remember
GET     → Give me
POST    → Create this
PUT     → Update this
DELETE  → Remove this
4️⃣ Understanding Endpoint + Method

One thing that confused me initially was:

/users/1

What does it do?

By itself, it only identifies a resource.

The HTTP method + URL together tell us what we want.

GET /users/1

→ Get user 1

PUT /users/1

→ Update user 1

DELETE /users/1

→ Delete user 1

So:

/users/1 = resource
GET /users/1 = action on that resource

5️⃣ REST API Flow

A simple REST API interaction looks like this:

CLIENT
  │
  │ HTTP Request
  │
  ▼
SERVER / API
  │
  │ HTTP Response
  │
  ▼
CLIENT

The request contains things like:

HTTP Request
│
├── Method
├── URL
├── Headers
└── Body

The response contains:

HTTP Response
│
├── Status Code
├── Headers
└── Body
6️⃣ API vs SDK

Now let's understand SDK.

What is an SDK?

SDK = Software Development Kit

An SDK is a collection of tools/libraries provided to make it easier to work with a service.

The important thing I learned:

API and SDK are NOT the same thing.

Direct API call

I can make an HTTP request myself.

Python
   ↓
HTTP Request
   ↓
API
Using an SDK

The SDK handles many communication details for me.

Python Code
    ↓
   SDK
    ↓
HTTP Request
    ↓
   API

So the main idea is:

API → The interface/service I communicate with

SDK → Tools that make communicating with that service easier
7️⃣ What is Postman?

Postman is a tool that allows me to test APIs without writing code first.

Instead of immediately writing Python:

requests.get(...)

I can use Postman to send the request and inspect the response.

This is useful when developing and debugging APIs.

8️⃣ My First GET Request in Postman

I used this public API:

https://jsonplaceholder.typicode.com/users/1

In Postman:

Method:
GET

URL:
https://jsonplaceholder.typicode.com/users/1

Then I clicked:

Send

The server returned:

200 OK

and user data in the response body.

9️⃣ Understanding HTTP Response

When the server responds, there are different parts.

HTTP RESPONSE
│
├── Status Code
│      ↓
│     200 OK
│
├── Headers
│      ↓
│   Extra information
│
└── Body
       ↓
      JSON data
🔟 Status Codes

Status codes tell me what happened to my request.

The most important ones I learned today:

Status Code	Meaning
200	Success
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
500	Server Error

I don't need to memorize everything right now.

The most important ones for today are:

200 → Success ✅
404 → Not Found ❌
500 → Server Error ❌
1️⃣1️⃣ Understanding 404

I tested:

https://jsonplaceholder.typicode.com/users/999999

The user doesn't exist.

The server returned:

404 Not Found

This taught me an important difference.

400 vs 404
400 Bad Request
→ The request itself is invalid/bad.

404 Not Found
→ The server understood the request,
  but the requested resource doesn't exist.

For example:

GET /users/999999

The server understands that I want user 999999.

But that user doesn't exist.

Therefore:

404 Not Found
1️⃣2️⃣ What is a Response Body?

The response body contains the actual data returned by the server.

For example:

{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret"
}

This is JSON data.

So:

Status Code
    ↓
Tells me what happened

Response Body
    ↓
Contains the returned data
1️⃣3️⃣ What are Headers?

Headers are extra information/metadata attached to an HTTP request or response.

They are NOT part of the URL.

A request can look like:

HTTP REQUEST
│
├── Method
│    GET
│
├── URL
│    https://api.com/users/1
│
├── Headers
│    Extra information
│
└── Body
     Data being sent

For example:

Content-Type: application/json

This tells the server what type of data is being sent.

Another common example is:

Authorization: Bearer <token>

This can be used to provide authentication information.

Simple memory trick
URL     → WHERE?
Method  → WHAT ACTION?
Headers → EXTRA INFORMATION
Body    → DATA
1️⃣4️⃣ JSON → Python Dictionary

When an API sends JSON, Python can convert that JSON into a Python object.

For example:

data = response.json()

If the JSON response is:

{
  "id": 1,
  "name": "Leanne Graham"
}

Python can represent it as:

{
    "id": 1,
    "name": "Leanne Graham"
}

For a JSON object, this becomes a Python dictionary.

1️⃣5️⃣ Calling an API Using Python

Now let's connect everything I learned today.

Create:

day5_api_test.py

Inside my week_01 folder.

Code:

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Print response headers
print("\nResponse Headers:")
print(response.headers)

# Convert JSON response into Python object
data = response.json()

# Print response body
print("\nResponse Body:")
print(data)

Run it:

python day5_api_test.py

Expected result:

Status Code: 200

Response Headers:
{...}

Response Body:
{'id': 1, 'name': 'Leanne Graham', ...}
1️⃣6️⃣ What is Happening in the Python Code?

Let's break it down.

Step 1
import requests

Import the requests library.

Step 2
url = "https://jsonplaceholder.typicode.com/users/1"

Store the API URL.

Step 3
response = requests.get(url)

Send a GET request to the API.

Flow:

Python
  ↓
requests.get()
  ↓
HTTP GET Request
  ↓
API Server
Step 4
response.status_code

Check the HTTP status code.

For a successful request:

200
Step 5
response.headers

Get the response headers.

These contain extra information about the response.

Step 6
response.json()

Read the JSON response and convert it into a Python object.

For example:

JSON
 ↓
response.json()
 ↓
Python dictionary
1️⃣7️⃣ Complete API Flow

This is the most important diagram from today's learning.

                 CLIENT
          ┌─────────────────┐
          │ Python / Postman│
          └────────┬────────┘
                   │
                   │ HTTP Request
                   │
                   │ Method + URL
                   │ Headers + Body
                   ▼
          ┌─────────────────┐
          │    API SERVER   │
          └────────┬────────┘
                   │
                   │ HTTP Response
                   │
                   │ Status + Headers
                   │ Body
                   ▼
          ┌─────────────────┐
          │ Python / Postman│
          └─────────────────┘
1️⃣8️⃣ Postman vs Python

I also learned that Postman and Python can perform the same API request.

Postman
Postman
   ↓
GET request
   ↓
API
   ↓
JSON response
Python
Python
   ↓
requests.get()
   ↓
API
   ↓
JSON response

Postman is especially useful for testing and debugging.

Python is what I can use to integrate the API into my application.

🧪 1️⃣9️⃣ My Day 5 Experiment

I tested two URLs.

Test 1
https://jsonplaceholder.typicode.com/users/1

Result:

Status Code → 200
Body → User data

The user exists.

Test 2
https://jsonplaceholder.typicode.com/users/999999

Result:

Status Code → 404
Body → {}

The user doesn't exist.

This helped me understand the difference between:

200 → Resource found / request successful

404 → Resource not found
🧠 2️⃣0️⃣ Quick Revision

Before moving on, this is what I should remember from Day 5.

REST API
    ↓
Uses HTTP methods + URLs to work with resources

GET
    ↓
Read

POST
    ↓
Create

PUT
    ↓
Update

DELETE
    ↓
Delete

And:

URL
 ↓
Where?

Method
 ↓
What action?

Headers
 ↓
Extra information

Body
 ↓
Data

And:

200 → Success
404 → Not Found
500 → Server Error
🎯 2️⃣1️⃣ Day 5 Key Takeaways

Today I learned:

REST APIs use HTTP methods and URLs.
A resource can be represented by an endpoint such as /users/1.
GET is used to retrieve data.
POST is used to create data.
PUT is used to update data.
DELETE is used to delete data.
An SDK provides tools that make API interaction easier.
Postman can be used to test APIs without writing code.
HTTP responses contain status codes, headers and bodies.
JSON is commonly used as API response data.
response.json() converts JSON into a Python object.
200 means the request was successful.
404 means the requested resource was not found.
Headers contain additional information about a request or response.
💻 Files I Created

My Week 1 folder now looks like:

week_01/
│
├── README.md
├── DAY_1.md
├── DAY_2.md
├── DAY_3.md
├── Day_4.md
├── DAY_5.md
│
├── hello.py
├── api_test.py
├── env_test.py
└── day5_api_test.py
🏁 Day 5 Deliverable

An API receives a request over HTTP and returns a response, commonly in JSON. I can test APIs using Postman and call them from Python.

🔥 What I Can Do Now

After Day 5, I can:

Understand an API
       ↓
Identify its endpoint
       ↓
Choose HTTP method
       ↓
Send request using Postman
       ↓
Check status code
       ↓
Inspect headers
       ↓
Read JSON response
       ↓
Call the same API using Python

That's a big step toward building real AI applications.

🚀 Day 5 COMPLETE!

One more day completed in my AI-Ready Data Engineer journey.

I'm not just learning syntax.

I'm trying to understand:

What happens behind the code?

That's the mindset I want to build throughout this journey.

📌 Continue the Journey

👉 Previous: Day 4 — API Keys & Environment Variables

👉 Next: Day 6 — Coming Soon 🚀

⭐ If this helped you

If you're also learning Data Engineering, AI, APIs or Python:

⭐ Star this repository
👀 Follow the journey
💬 Share your learning progress
🚀 Use these notes to learn alongside me

See you on Day 6! 🔥

#AI #DataEngineering #Python #APIs #RESTAPI #Postman #SoftwareEngineering #LearningInPublic


### Small correction before you paste

Your **Day 4 filename is `Day_4.md`** according to the structure you've been using, so I used:

```md
[📖 Day 4 — API Keys & Environment Variables](./Day_4.md)

That way the GitHub link should work correctly.

bro i want all in one markdown to copy paste directly. u giving topic topic separate . i domt want all topics should be in one markdown. please i beg you give in one markdown not seprate separte. i told multiple times still giivng same issue to me and i need simple dont want complex theory full. just make it for revision . give less than 1000lines and all in one markdown. if not in one markdown then dont generate it

Bro 😭 understood. One single Markdown. Nothing separated. No complex theory. Revision-focused. Under 1000 lines.

Copy-paste this directly into DAY_5.md:

# 🚀 Day 5 — REST API, SDK & Postman

Hey everyone! 👋

Welcome to **Day 5** of my journey toward becoming an **AI-Ready Data Engineer**.

Today I learned the basics of:

- REST API
- HTTP Methods
- Endpoint
- SDK
- Postman
- HTTP Response
- Status Codes
- Headers
- JSON → Python Dictionary
- Calling an API using Python

> 🎯 Goal: Understand how APIs work and learn how to test and call them.

---

## 🔙 Missed Day 4?

👉 [📖 Day 4 — API Keys & Environment Variables](./Day_4.md)

---

# 1️⃣ What is a REST API?

A **REST API** is a way for applications to communicate with each other using HTTP.

Simple example:

```text
My Python Program
       ↓
    HTTP Request
       ↓
      API
       ↓
   HTTP Response
       ↓
     JSON Data

Think of an API like a waiter:

You → Request
Waiter → API
Kitchen → Server
Food → Response

You ask for something → API sends the request to the server → server sends back the response.

2️⃣ What is a Resource?

A resource is the thing we are working with.

Example:

/users

means the users resource.

/users/1

means user with ID 1.

3️⃣ HTTP Methods

HTTP methods tell the server what action we want to perform.

Method	Meaning	Example
GET	Read data	GET /users
POST	Create data	POST /users
PUT	Update data	PUT /users/1
DELETE	Delete data	DELETE /users/1
Easy way to remember
GET     → Give me
POST    → Create
PUT     → Update
DELETE  → Remove
4️⃣ Endpoint

An endpoint is the URL/path where we access a particular resource.

Example:

/users
/users/1

But remember:

/users/1

only tells us which resource.

The HTTP method tells us what we want to do.

For example:

GET /users/1

→ Get user 1

PUT /users/1

→ Update user 1

DELETE /users/1

→ Delete user 1

5️⃣ REST API Flow
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
6️⃣ What is an SDK?

SDK = Software Development Kit

An SDK is a set of tools/libraries that makes it easier to work with a service.

Without SDK:

Python
   ↓
HTTP Request
   ↓
API

With SDK:

Python
   ↓
SDK
   ↓
HTTP Request
   ↓
API
API vs SDK
API → The interface/service we communicate with

SDK → Tools that make communicating with that service easier

So they are not the same thing.

Both eventually communicate with the API.

7️⃣ What is Postman?

Postman is a tool used to test APIs.

Instead of writing Python code first, we can directly send requests using Postman.

For example:

GET
https://jsonplaceholder.typicode.com/users/1

Click Send.

Postman shows the server response.

8️⃣ My First API Request in Postman

I used:

Method:
GET

URL:
https://jsonplaceholder.typicode.com/users/1

Then I clicked:

Send

The API returned user information.

9️⃣ HTTP Response

When we send a request, the server sends a response.

A response mainly contains:

HTTP RESPONSE
│
├── Status Code
├── Headers
└── Body

Example:

200 OK

and the body contains JSON data.

🔟 Status Code

The status code tells us what happened with our request.

Important ones:

Status	Meaning
200	Success
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
500	Server Error

For now, I mainly remember:

200 → Success
404 → Not Found
500 → Server Error
1️⃣1️⃣ Testing 200 OK

I requested:

GET /users/1

The server returned:

200 OK

This means:

The request was successfully processed.

1️⃣2️⃣ Testing 404 Not Found

Then I changed the URL to:

https://jsonplaceholder.typicode.com/users/999999

The server returned:

404 Not Found

Why?

Because that user/resource does not exist.

Important difference
400 → The request itself is bad

404 → The requested resource was not found
1️⃣3️⃣ Headers

Headers contain extra information about an HTTP request or response.

Example:

Content-Type: application/json

or:

Authorization: Bearer xyz

Think of headers as metadata.

1️⃣4️⃣ Request
again same issue brooo. give all in one caopy paste markdown not multiple

Bro 😭 my bad. I understand exactly now.

You want ONE SINGLE ```markdown code block from # Day 5 to the end.
No separate markdown blocks. No topic-by-topic outside the block. Just copy → paste into DAY_5.md.

# 🚀 Day 5 — REST API, SDK & Postman

Hey everyone! 👋

Welcome to **Day 5** of my journey toward becoming an **AI-Ready Data Engineer**.

Today I learned the basics of:

- REST API
- HTTP Methods
- Endpoint
- SDK
- Postman
- HTTP Response
- Status Codes
- Headers
- JSON → Python Dictionary
- Calling an API using Python

> 🎯 Goal: Understand how APIs work and learn how to test and call them.

---

## 🔙 Missed Day 4?

👉 [📖 Day 4 — API Keys & Environment Variables](./Day_4.md)

---

## 1️⃣ What is a REST API?

A REST API is a way for applications to communicate with each other using HTTP.

Simple flow:

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

A resource is the thing we are working with.

Example:

    /users

This represents the users resource.

    /users/1

This represents user with ID 1.

---

## 3️⃣ HTTP Methods

HTTP methods tell the server what action we want to perform.

| Method | Meaning | Example |
|---|---|---|
| GET | Read data | `GET /users` |
| POST | Create data | `POST /users` |
| PUT | Update data | `PUT /users/1` |
| DELETE | Delete data | `DELETE /users/1` |

### Easy way to remember

    GET     → Give me
    POST    → Create
    PUT     → Update
    DELETE  → Remove

---

## 4️⃣ Endpoint

An endpoint is the path we use to access a resource.

Example:

    /users/1

But the path alone doesn't tell us the action.

The HTTP method tells us what we want to do.

    GET /users/1
    → Get user 1

    PUT /users/1
    → Update user 1

    DELETE /users/1
    → Delete user 1

### Remember

    URL / Path   → WHICH resource?
    Method       → WHAT action?

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

SDK = Software Development Kit

An SDK is a collection of tools/libraries that makes it easier to work with a service.

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

They are not the same thing.

Both ultimately help our application communicate with the API.

---

## 7️⃣ What is Postman?

Postman is a tool used to test APIs.

Instead of writing Python code first, we can send requests directly from Postman.

For example:

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

## 🔟 Status Codes

Status codes tell us what happened with our request.

| Status Code | Meaning |
|---|---|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

For now, I mainly remember:

    200 → Success
    404 → Not Found
    500 → Server Error

---

## 1️⃣1️⃣ Testing 200 OK

I requested:

    GET /users/1

The server returned:

    200 OK

This means the request was successfully processed.

---

## 1️⃣2️⃣ Testing 404 Not Found

Then I changed the URL to:

    https://jsonplaceholder.typicode.com/users/999999

The server returned:

    404 Not Found

Why?

Because the requested user/resource does not exist.

### Important difference

    400 → Request itself is invalid

    404 → Requested resource does not exist

---

## 1️⃣3️⃣ Headers

Headers contain extra information about an HTTP request or response.

Example:

    Content-Type: application/json

Another example:

    Authorization: Bearer xyz

Think of headers as metadata.

### Easy memory trick

    URL       → WHERE?
    Method    → WHAT ACTION?
    Headers   → EXTRA INFORMATION
    Body      → DATA

---

## 1️⃣4️⃣ JSON Response

The server commonly sends data in JSON format.

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

For a JSON object, Python gives us a dictionary.

Flow:

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

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status Code:", response.status_code)

print("\nResponse Headers:")
print(response.headers)

data = response.json()

print("\nResponse Body:")
print(data)
1️⃣7️⃣ Understanding the Python Code
Import requests
import requests

The requests library helps Python send HTTP requests.

Store the API URL
url = "https://jsonplaceholder.typicode.com/users/1"

This stores the API endpoint.

Send GET request
response = requests.get(url)

Python sends a GET request to the API.

Check status code
print(response.status_code)

This tells us whether the request was successful.

For example:

200

means success.

Get response headers
print(response.headers)

This shows extra information sent with the response.

Convert JSON
data = response.json()

This converts the JSON response into a Python object.

For a JSON object, this will normally be a dictionary.

1️⃣8️⃣ Complete API Flow

The complete flow I learned today:

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
1️⃣9️⃣ Postman vs Python
Postman
Postman
   ↓
GET Request
   ↓
API
   ↓
JSON Response
Python
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

Postman is useful for quickly testing an API.

Python is useful when we want to use the API inside our application.

2️⃣0️⃣ My Two API Tests
Test 1 — Existing User

Request:

GET
https://jsonplaceholder.typicode.com/users/1

Response:

200 OK

Meaning:

Request successful
User data received
Test 2 — Non-existing User

Request:

GET
https://jsonplaceholder.typicode.com/users/999999

Response:

404 Not Found

Meaning:

Requested resource does not exist
2️⃣1️⃣ Quick Revision
REST API
A way for applications to communicate using HTTP.
Resource
The thing we are working with.

Example:

/users
/users/1
HTTP Methods
GET     → Read
POST    → Create
PUT     → Update
DELETE  → Delete
Endpoint
The path used to access a resource.
SDK
Tools/libraries that make working with a service easier.
Postman
Tool used to test APIs.
Status Code
Tells us what happened with the request.
Headers
Extra information about the request/response.
Body
Contains the actual data.
JSON
Common format used to exchange data between applications.
response.json()
Converts the JSON response into a Python object.
2️⃣2️⃣ The Most Important Things I Learned
API
↓
Receives HTTP Request
↓
Processes Request
↓
Sends HTTP Response
↓
Status Code + Headers + Body

And:

GET    → Read
POST   → Create
PUT    → Update
DELETE → Delete

And:

JSON Response
     ↓
response.json()
     ↓
Python Dictionary
2️⃣3️⃣ Day 5 Practice

I tested the API in Postman:

GET /users/1
→ 200 OK

Then:

GET /users/999999
→ 404 Not Found

I also called the same API using Python.

2️⃣4️⃣ Files Created

Inside my week_01 folder:

DAY_5.md
day5_api_test.py
🎯 Day 5 Deliverable

An API receives a request over HTTP and returns a response, commonly in JSON. I can test APIs using Postman and call them from Python.

✅ What I Can Do After Day 5

I can now:

Understand what a REST API is
Understand GET, POST, PUT and DELETE
Understand resources and endpoints
Understand API vs SDK
Send GET requests using Postman
Read HTTP status codes
Understand basic headers
Understand JSON responses
Convert JSON responses into Python objects
Call an API using Python
Understand the basic request → response flow
🚀 Day 5 Complete!

Another step completed in my AI-Ready Data Engineer journey.

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
🔜 Next

👉 Day 6 — Continue building the AI Engineering foundation

💡 Final Revision

If I forget everything from today, remember these 5 things:

1. API → Allows applications to communicate

2. GET → Read data

3. POST → Create data

4. Status Code → Tells what happened

5. JSON → Common format for API data

That's enough for today's foundation. 🚀

⭐ Follow My Journey

I'm documenting my learning journey step by step.

If you're also learning Data Engineering, AI Engineering, APIs or Python, feel free to follow along.

Learn → Build → Document → Repeat. 🚀