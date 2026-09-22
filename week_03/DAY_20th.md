
# DAY 20 — LLM APIs + Python

> **Goal:** Understand how Python applications communicate with LLMs through APIs, including authentication, requests/responses, model selection, token pricing, rate limits, and API errors.

---

## 1. What is an LLM API?

An **LLM API** is an interface that allows a software application to communicate with an AI/LLM model.

The general API flow learned in Week 3 was:

```text
Python
   ↓
HTTP Request
   ↓
API
   ↓
Server
   ↓
JSON Response
```

With an LLM API, the flow becomes:

```text
Python
   ↓
LLM API
   ↓
AI Model
   ↓
JSON Response
   ↓
Python
```

The important point is:

> **An API is not the LLM itself. The API is the communication interface that allows our application to use the LLM.**

For example, instead of manually using an AI website, our Python application can send input to an LLM API and receive the generated result.

### LLM API vs ChatGPT website

When using an AI website:

```text
User
 ↓
AI Website
 ↓
AI Infrastructure
 ↓
Model
 ↓
Response
```

When building an AI application:

```text
Your Application
 ↓
LLM API
 ↓
AI Model
 ↓
Response
```

This is why APIs are important for AI Engineers.

---

# 2. API Key

An **API key** is a secret credential provided by an API provider.

It allows the API provider to identify and authenticate requests from your application.

Conceptually:

```text
Python Application
       ↓
    API Key
       ↓
    LLM API
       ↓
 Authentication
       ↓
    AI Model
```

The API key should be treated as a secret.

### Never expose an API key

Avoid putting secrets directly into source code:

```python
api_key = "my-secret-api-key"
```

If this code is pushed to GitHub, the secret could be exposed.

Instead, store secrets outside your source code.

---

# 3. Authentication

**Authentication means verifying the credential used by a request.**

In simple terms:

> **Authentication = Who are you / is this credential valid?**

For example:

```text
Python
  ↓
API Key
  ↓
LLM API
  ↓
Is this credential valid?
  ↓
YES → Request can be processed
NO  → Authentication error
```

A common HTTP authentication pattern is:

```http
Authorization: Bearer YOUR_API_KEY
```

Here:

```text
Authorization → HTTP header name
Bearer        → Authentication scheme
YOUR_API_KEY  → Credential
```

The important point is that the header is called `Authorization`, but the credential inside it can be used to authenticate the request.

### Authentication vs Authorization

These concepts are related but different.

```text
Authentication
→ Is the credential valid?
→ Who/what is making the request?

Authorization
→ What is this credential allowed to access/do?
```

For example:

```text
API Key
   ↓
Authentication
   ↓
Credential is valid
   ↓
Authorization / permission checks
   ↓
Is this resource/action allowed?
```

For normal LLM API usage, we mainly need to understand **authentication with the API key**.

We do not necessarily write separate:

```python
authenticate()
authorize()
```

functions ourselves.

The API provider's server handles these checks.

---

# 4. Environment Variables

API keys are secrets, so they should not normally be hard-coded into the source code.

An **environment variable** is a value stored outside the source code that a program can read when it runs.

A common local-development approach is using a `.env` file.

Example:

```text
.env

API_KEY=your_secret_key
```

Then:

```text
.env
 ↓
Environment Variable
 ↓
Python
 ↓
API Request
```

The `.env` file keeps the secret separate from the application code.

### Important

Do **not** push `.env` to GitHub.

Add it to `.gitignore`:

```text
.env
```

Example project:

```text
ai-project/
│
├── main.py
├── .env
└── .gitignore
```

The `.env` file contains the secret locally, while `.gitignore` prevents Git from tracking it.

### Important distinction

```text
.env
→ Stores the secret locally

API Key
→ The credential used by the API

Authentication
→ The process of validating the credential
```

---

# 5. Request and Response

An LLM API follows the same fundamental request/response model learned in Week 3.

```text
Python
   ↓
HTTP Request
   ↓
LLM API
   ↓
AI Model
   ↓
HTTP Response
   ↓
Python
```

## Request

The request tells the API what we want to do.

Conceptually, an LLM request can contain:

```text
Request
├── Authentication
│      └── API key
│
├── Model
│      └── Which model to use?
│
└── Input
       └── What should the model process?
```

For example:

```text
Model: some-model

Input:
"Explain APIs simply."
```

The request is sent to the LLM API.

---

## What happens at the server?

The general process is:

```text
Python
  ↓
HTTP Request
  ↓
LLM API
  ↓
Authentication check
  ↓
Request processing
  ↓
Selected AI Model
  ↓
Model generates output
```

The model then produces an output.

---

# 6. Response

The API sends the result back to our Python application.

```text
AI Model
   ↓
Generated output
   ↓
LLM API
   ↓
HTTP Response
   ↓
Python
```

The response is usually structured data rather than just plain text.

For example, conceptually:

```json
{
  "output": "An API allows software systems to communicate."
}
```

The exact response structure depends on the API and SDK being used.

---

# 7. Why JSON?

JSON is a common format for exchanging structured data between applications.

Example:

```json
{
  "name": "Ramesh",
  "age": 21
}
```

An LLM API can return structured information such as:

```json
{
  "id": "response_123",
  "model": "some-model",
  "output": "An API allows software systems to communicate."
}
```

Our Python application can then extract the information it needs.

This connects directly to the JSON knowledge learned in Week 3.

---

# 8. Complete LLM API Flow

The overall flow is:

```text
┌─────────────────────────┐
│    Your Python Code     │
└────────────┬────────────┘
             │
             │ HTTP REQUEST
             │
             │ API Key
             │ Model
             │ Input
             ↓
┌─────────────────────────┐
│        LLM API          │
└────────────┬────────────┘
             │
             │ Authentication
             │ Request processing
             ↓
┌─────────────────────────┐
│       AI Model          │
└────────────┬────────────┘
             │
             │ Generates output
             ↓
┌─────────────────────────┐
│        LLM API          │
└────────────┬────────────┘
             │
             │ HTTP RESPONSE
             │ JSON
             ↓
┌─────────────────────────┐
│    Your Python Code     │
└─────────────────────────┘
```

---

# 9. Model Selection

An LLM API may provide multiple models.

Conceptually:

```text
LLM API
   │
   ├── Model A
   ├── Model B
   ├── Model C
   └── Model D
```

Our request specifies which model we want to use.

Conceptually:

```python
model = "some-model"
```

Different models can have different characteristics.

## Important model-selection factors

### 1. Capability

Some models are designed for more complex tasks such as:

* reasoning
* coding
* analysis
* complex instructions

### 2. Speed

Some models can provide responses faster than others.

### 3. Cost

Different models can have different prices.

### 4. Context size

Models can support different amounts of context/input.

This matters for:

* long documents
* conversations
* RAG
* large codebases
* reports

### 5. Output quality

Different models can produce different levels of quality depending on the task.

---

## AI Engineer mindset

Do not automatically think:

> "Use the biggest model."

Instead think:

```text
Task
 ↓
Required capability
 ↓
Required speed
 ↓
Required context
 ↓
Budget
 ↓
Choose an appropriate model
```

The best model depends on the task and application requirements.

---

# 10. Tokens and API Pricing

LLM APIs commonly charge based on token usage.

Tokens were introduced earlier in Day 18.

The basic process is:

```text
Your text
   ↓
Tokenizer
   ↓
Input tokens
   ↓
LLM
   ↓
Output tokens
   ↓
Response
```

---

## Input Tokens

**Input tokens** are the tokens sent to the model.

For example:

```text
"Explain APIs simply."
```

gets converted into tokens.

Those tokens become part of the model's input.

```text
Your prompt
    ↓
Input tokens
    ↓
LLM
```

---

## Output Tokens

The model generates a response.

Those generated tokens are **output tokens**.

```text
LLM
 ↓
Generated tokens
 ↓
Output
```

Therefore, one API request can have:

```text
Input tokens
+
Output tokens
```

---

# 11. Why do tokens affect cost?

Suppose, purely as an example:

```text
Input:  1,000 tokens
Output: 500 tokens
```

Then the request processed:

```text
1,000 input tokens
+
500 output tokens
=
1,500 tokens
```

However, pricing is not necessarily one single price for all tokens.

Providers can have separate rates for:

```text
Input tokens
Output tokens
```

The exact price depends on the provider and model.

---

# 12. Why Longer Prompts Can Cost More

Consider:

### Short request

```text
"Classify this review."
```

Small amount of input.

### Large request

```text
"Classify this review."

+
Company documentation

+
Customer history

+
Previous conversation

+
Product information

+
Long instructions
```

The second request contains significantly more input information and therefore potentially more input tokens.

```text
More input
   ↓
More input tokens
   ↓
Potentially higher cost
```

Output length also matters.

```text
Short answer
   ↓
Fewer output tokens

Long answer
   ↓
More output tokens
```

---

# 13. Why Model Choice Matters for Cost

Different models can have different pricing.

Therefore:

```text
Model selection
      ↓
Capability
Speed
Context
Quality
Cost
```

An AI Engineer should choose a model appropriate for the task rather than automatically choosing the most expensive model.

---

# 14. Context Window vs Pricing

Do not confuse these concepts.

### Context window

How much information the model can handle within its supported context.

### Pricing

How much the provider charges for token usage.

They are related to usage but are not the same thing.

A model having a large context window does not mean we should always send huge amounts of information.

---

# 15. API Rate Limits

An API cannot necessarily accept unlimited requests instantly.

Therefore, APIs use **rate limits**.

A rate limit controls how much API usage can happen within a certain period.

Examples can include:

```text
Requests per minute
Tokens per minute
Concurrent requests
```

---

# 16. Requests Per Minute — RPM

**RPM = Requests Per Minute**

Example:

```text
100 requests / minute
```

This means the application has a limit on how many requests it can make during the relevant rate-limit window.

Conceptually:

```text
Python
 ↓
Request
 ↓
Request
 ↓
Request
 ↓
...
 ↓
Rate limit
```

If too many requests are sent, the API can reject requests.

---

# 17. Tokens Per Minute — TPM

**TPM = Tokens Per Minute**

This limits token throughput over a period.

For example, an application could make relatively few requests but each request could contain a large amount of text.

Therefore:

```text
RPM
→ How many requests?

TPM
→ How many tokens?
```

Both can matter.

---

# 18. Why Rate Limits Exist

Rate limits can help:

* protect API infrastructure
* prevent abuse
* provide fair access to shared infrastructure
* control traffic
* prevent accidental excessive usage

---

# 19. Rate Limit Errors

When an application exceeds a rate limit, it can receive:

```text
429 Too Many Requests
```

This was already learned as an HTTP status code in Week 3.

Now we understand its meaning in an LLM API context.

```text
Application
    ↓
Too many requests
    ↓
LLM API
    ↓
429 Too Many Requests
```

---

# 20. Retry and Backoff

A production application should not blindly retry every failed request.

For a temporary rate-limit situation, an application may:

```text
Request
   ↓
429
   ↓
Wait
   ↓
Retry
```

A common strategy is **exponential backoff**:

```text
1 second
   ↓
2 seconds
   ↓
4 seconds
   ↓
8 seconds
```

The exact retry strategy should follow the API provider's guidance.

---

# 21. Payment vs Rate Limits

Paying for API usage and having rate limits are two different things.

### Payment

Answers:

> **How much does my usage cost?**

### Rate limit

Answers:

> **How much traffic can I send within a certain period?**

Therefore:

```text
Money available
      +
Rate limit exceeded
      =
Request can still be rejected
```

Paying for API usage does **not automatically mean unlimited requests per second/minute**.

Paid access can provide higher or different limits depending on the provider, account, model, and usage tier, but limits can still exist.

---

# 22. Why Pay for API Tokens?

When using an LLM API, our application is using the provider's computing infrastructure and AI model.

Conceptually:

```text
Your Application
      ↓
Input Tokens
      ↓
AI Infrastructure
      ↓
Model Processing
      ↓
Output Tokens
      ↓
Response
```

The provider charges for this usage according to its pricing model.

Think of it like a utility:

```text
More usage
   ↓
More resources consumed
   ↓
Potentially higher cost
```

But payment does not mean unlimited instantaneous traffic.

A useful analogy:

> Paying a highway toll allows you to use the highway, but it doesn't mean you can drive at unlimited speed or that the highway has unlimited capacity.

---

# 23. Paid API vs Free Access

The exact rules depend on the provider, but generally:

### Free / limited access

May have:

* lower usage limits
* fewer available models/features
* limited API access
* limited token/request throughput

### Paid API usage

Generally means:

* billable API usage is available
* requests can consume paid model resources
* usage is charged according to the provider's pricing
* rate limits still apply

Therefore:

```text
Paid
≠
Unlimited
```

---

# 24. ChatGPT Subscription vs API

A ChatGPT subscription and API usage can be separate products/billing systems.

Using an AI chat interface:

```text
You
 ↓
ChatGPT
 ↓
Model
```

Building your own application:

```text
Your Python Application
 ↓
LLM API
 ↓
Model
```

Access to a chat product does not automatically mean your Python application has unlimited API usage.

API access follows the provider's API access, billing, model, and rate-limit rules.

---

# 25. Basic LLM API Errors

LLM API requests can fail.

The important HTTP status codes to remember are:

```text
401
403
404
429
500
502
503
```

---

## 401 — Unauthorized

Usually indicates an authentication problem.

Possible causes:

* missing API key
* invalid API key
* incorrect credential
* credential not accepted

Flow:

```text
Python
 ↓
API key
 ↓
LLM API
 ↓
Authentication failed
 ↓
401
```

---

## 403 — Forbidden

Usually indicates a permission/authorization problem.

The server understands the request/credential but does not allow the requested action or resource.

Remember:

```text
401 → Authentication problem
403 → Permission/authorization problem
```

---

## 404 — Not Found

The requested resource or endpoint could not be found.

Example:

```text
/api/wrong-endpoint
```

could result in:

```text
404 Not Found
```

---

## 429 — Too Many Requests

Usually indicates a rate-limit problem.

```text
Too many requests
       ↓
429
```

The appropriate response may involve waiting and retrying according to the provider's guidance.

---

## 500 — Internal Server Error

A server-side problem occurred.

Important:

> A 500 error does not automatically mean our Python code is wrong.

The problem may be on the API provider's side.

---

## 502 — Bad Gateway

Can indicate a problem in communication between servers or infrastructure.

---

## 503 — Service Unavailable

Can indicate that a service is temporarily unavailable.

---

# 26. Don't Retry Every Error

Different errors require different handling.

```text
401
 ↓
Check authentication / API key
```

```text
403
 ↓
Check permissions/access
```

```text
404
 ↓
Check endpoint/resource
```

```text
429
 ↓
Wait / backoff / retry appropriately
```

```text
500 / 503
 ↓
Potentially retry if appropriate
```

A production application should understand the error instead of blindly retrying everything.

---

# 27. Complete Day 20 Mental Model

Everything we learned can now be connected:

```text
                    API KEY
                       ↓
               Authentication
                       ↓
┌─────────────────────────────────────┐
│          Python Application         │
└──────────────────┬──────────────────┘
                   │
                   │ HTTP REQUEST
                   │
                   │ Model
                   │ Input
                   │ Authentication
                   ↓
┌─────────────────────────────────────┐
│              LLM API                │
└──────────────────┬──────────────────┘
                   │
                   │ Rate limits
                   │ Request validation
                   ↓
┌─────────────────────────────────────┐
│             AI MODEL                │
└──────────────────┬──────────────────┘
                   │
                   │ Output tokens
                   ↓
┌─────────────────────────────────────┐
│              LLM API                │
└──────────────────┬──────────────────┘
                   │
                   │ JSON / HTTP Response
                   ↓
┌─────────────────────────────────────┐
│          Python Application         │
└─────────────────────────────────────┘
```

---

# 28. Day 20 Key Concepts

```text
LLM API
→ Interface that allows applications to use an LLM.

API Key
→ Secret credential used to authenticate an API request.

Authentication
→ Verifying the credential/request.

Authorization
→ Determining what an authenticated credential is allowed to access/do.

Environment Variable
→ Value stored outside source code and read by the application.

.env
→ Common local-development file for storing environment variables.

Request
→ Data sent from our application to the API.

Response
→ Data returned by the API.

JSON
→ Structured format commonly used for API data exchange.

Model Selection
→ Choosing a model based on capability, speed, context, quality, and cost.

Input Tokens
→ Tokens sent to the model.

Output Tokens
→ Tokens generated by the model.

Pricing
→ Cost associated with API usage.

RPM
→ Requests Per Minute.

TPM
→ Tokens Per Minute.

429
→ Too Many Requests / rate-limit response.

401
→ Authentication problem.

403
→ Permission/authorization problem.

404
→ Resource not found.

5xx
→ Server/service-side errors.
```

---

# 29. What I Should Be Able to Explain After Day 20

I should now be able to explain:

### What is an LLM API?

```text
An interface that allows my application to communicate with an AI model.
```

### How does authentication work?

```text
My application provides a credential such as an API key.
The API validates the credential before processing the request.
```

### Why use `.env`?

```text
To keep secrets/configuration outside the source code.
```

### What is a request?

```text
The information my application sends to the LLM API.
```

### What is a response?

```text
The information returned by the LLM API after processing the request.
```

### Why do tokens matter?

```text
They represent the text processed/generated by the model
and are commonly used for API usage and pricing.
```

### Why do rate limits exist?

```text
To control how much traffic or token usage an application can send
within a certain period.
```

### Why can a paid API still return 429?

```text
Because payment and rate limits are different.
Paid usage allows billable API use, but the API can still limit request/token throughput.
```

### What does this mean?

```python
response = client.responses.create(...)
```

At a high level:

```text
Python
   ↓
SDK/client
   ↓
API request
   ↓
Authentication
   ↓
LLM API
   ↓
Selected model
   ↓
Generated response
   ↓
Python
```

---

# DAY 20 COMPLETE ✅

