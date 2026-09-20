
# DAY 18 — LLM Fundamentals + Tokens + Context

> **Week 4 — LLMs + AI APIs**
>
> Day 18 focuses on understanding the core concepts behind Large Language Models before working with LLM APIs.

---

## 📅 Day 18 Goals

By the end of Day 18, I should understand:

* What an LLM is
* Training vs inference
* How ChatGPT-like systems generate responses
* LLM vs traditional software
* LLM vs ML model
* What tokens are
* Why tokens are not exactly words
* Input tokens vs output tokens
* What context means
* What a context window is
* Why long conversations and documents matter
* The basic LLM request/response flow
* What exactly happens when text is sent to an LLM

---

# 1. What is an LLM?

**LLM = Large Language Model**

An LLM is a type of machine-learning model trained on a very large amount of data so that it can learn patterns in language and generate text.

Examples of applications using LLMs include ChatGPT-like assistants, coding assistants, document analysis systems, chatbots, and AI agents.

The important idea is:

> An LLM generates text by processing its input and predicting what tokens should come next.

---

# 2. LLM vs Traditional Software

## Traditional Software

In traditional software, the developer explicitly defines the rules and logic.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

The flow is:

```text
Input
  ↓
Programmed rules
  ↓
Output
```

The programmer defines what should happen for different conditions.

---

## LLM Application

With an LLM application, the developer provides an input/prompt and the model generates an output.

```text
Input / Prompt
      ↓
   Context
      ↓
     LLM
      ↓
Generated output
```

The developer does not manually write every possible sentence the model can generate.

---

# 3. LLM vs ML Model

An LLM is itself a type of machine-learning model.

Conceptually:

```text
Machine Learning
       │
       ├── Classification
       ├── Regression
       ├── Recommendation
       │
       └── Language Models
              │
              └── Large Language Models
```

So:

> **LLM ⊂ Machine Learning**

A traditional ML model might predict:

```text
House price = ₹85 lakh
```

An LLM can generate:

```text
Explain why house prices increase.
```

and produce a natural-language response.

---

# 4. Training vs Inference

This is an important distinction for AI Engineering.

## Training

During training, the model learns patterns from a very large amount of data.

Simplified:

```text
Training Data
     ↓
   Tokens
     ↓
Neural Network
     ↓
Learn Patterns
     ↓
Trained Model
```

During training, the model's internal parameters are adjusted.

---

## Inference

Inference happens when an already-trained model is used to generate an answer.

For example, when I send a prompt to an LLM API, I am normally using the model for **inference**.

```text
User Prompt
     ↓
   Tokens
     ↓
Trained LLM
     ↓
Generated Tokens
     ↓
Response
```

### Easy way to remember

```text
TRAINING
= Model learns

INFERENCE
= Model uses what it learned
```

---

# 5. How ChatGPT-like Systems Generate Responses

Suppose I send:

```text
What is an API?
```

The simplified process is:

```text
"What is an API?"
        ↓
    Tokenizer
        ↓
      Tokens
        ↓
       LLM
        ↓
Predict next token
        ↓
Predict next token
        ↓
Predict next token
        ↓
      ...
        ↓
Final response
```

The model generates the response progressively.

For example, conceptually:

```text
"An API is"
       ↓
predict → "a"

"An API is a"
       ↓
predict → "way"

"An API is a way"
       ↓
predict → "for"

"An API is a way for"
       ↓
predict → "software"
```

This continues until the model produces the response.

---

# 6. What is a Token?

A **token is a unit of text that an LLM processes.**

A token can represent:

* A complete word
* Part of a word
* Punctuation
* Numbers
* Symbols
* Other pieces of text

The important point:

> **A token is not necessarily one word.**

For example, conceptually:

```text
"Hello world!"
```

could be represented approximately as:

```text
["Hello", " world", "!"]
```

The exact tokenization depends on the tokenizer and model.

---

# 7. Text → Tokens → Model

LLMs do not directly process text in the same way humans read text.

A simplified pipeline is:

```text
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
Token IDs / Numerical Representation
 ↓
LLM
```

For example:

```text
"Hello"
   ↓
Token
   ↓
Token ID
   ↓
Numerical representation
   ↓
LLM
```

The exact token IDs depend on the tokenizer/model.

---

# 8. Why Tokens Are Not Exactly Words

Consider:

```text
"unbelievable"
```

A tokenizer may split a word into multiple pieces.

Conceptually:

```text
unbelievable
      ↓
un + believable
```

Another word might remain as a single token.

Punctuation can also be represented as tokens.

Therefore:

```text
1 word ≠ necessarily 1 token
```

This is why token counts can differ from normal word counts.

---

# 9. Input Tokens

The tokens representing what I send to the model are **input tokens**.

Example:

```text
Explain APIs in simple terms.
```

The text is tokenized:

```text
Text
 ↓
Tokenizer
 ↓
Input Tokens
 ↓
LLM
```

Input tokens are important because LLM APIs commonly measure usage based partly on input token count.

---

# 10. Output Tokens

The tokens generated by the model are **output tokens**.

Example:

```text
Input:
Explain APIs in simple terms.

       ↓
      LLM
       ↓

Output Tokens:
An API is a way for software
applications to communicate...
```

The flow is:

```text
Input Text
    ↓
Input Tokens
    ↓
   LLM
    ↓
Output Tokens
    ↓
Output Text
```

---

# 11. Input Tokens + Output Tokens

Suppose an application uses:

```text
Input tokens  = 100
Output tokens = 200
```

Then:

```text
Total token usage = 300 tokens
```

This concept becomes important later when learning:

* LLM API pricing
* Usage limits
* Rate limits
* Context windows
* Performance optimization

---

# 12. What is Context?

**Context is the information available to the model when generating a response.**

It can include:

* System instructions
* Previous conversation
* Current user message
* Retrieved documents
* Other application-provided information

For example:

```text
System instructions
        +
Conversation history
        +
Current user message
        +
Retrieved information
        ↓
      Context
        ↓
       LLM
        ↓
    Response
```

---

# 13. What Can Be Inside Context?

## 1. System Instructions

For example:

```text
You are a helpful AI assistant.
Explain technical concepts simply.
```

---

## 2. Previous Conversation

For example:

```text
User:
What is an API?

Assistant:
An API allows software applications
to communicate with each other.

User:
What about authentication?
```

The previous conversation can be part of the context.

---

## 3. Current User Message

For example:

```text
Explain authentication simply.
```

This is part of the current request.

---

## 4. Retrieved Documents

In a RAG application, relevant information can be retrieved from documents and provided to the LLM.

```text
Documents
    ↓
Retrieval
    ↓
Relevant information
    ↓
Context
    ↓
LLM
```

RAG will be studied later.

---

## 5. Application Data

An application might provide information such as:

```text
Customer:
Name: Ramesh
Plan: Premium
```

That information can also be provided as context to the model.

---

# 14. What is a Context Window?

A **context window** is the amount of tokenized information a model can handle as context for a request.

It is not unlimited.

Conceptually:

```text
┌─────────────────────────────┐
│       CONTEXT WINDOW        │
│                             │
│ System instructions         │
│ Conversation history        │
│ Current prompt              │
│ Retrieved information       │
│ Documents                   │
│ Other context               │
│                             │
└─────────────────────────────┘
                 ↓
                LLM
```

Different models can have different context-window capacities.

Always check the documentation for the specific model when context limits matter.

---

# 15. Why Long Conversations Matter

Imagine a conversation:

```text
Message 1
Message 2
Message 3
Message 4
...
Message 100
Message 101
```

If an application keeps sending large amounts of conversation history as context, the number of tokens can become very large.

Therefore, AI applications need to manage context.

Possible strategies include:

* Summarization
* Chunking
* Retrieval
* RAG
* Selecting only relevant information
* Conversation history management

These concepts become especially important when building real AI applications.

---

# 16. Basic LLM Architecture Concept

The basic mental model is:

```text
User
  ↓
Prompt
  ↓
Tokens
  ↓
LLM
  ↓
Output Tokens
  ↓
Response
```

A slightly more detailed version:

```text
                 USER
                   │
                   ↓
                PROMPT
                   │
                   ↓
               TOKENIZER
                   │
                   ↓
               INPUT TOKENS
                   │
                   │
             + CONTEXT
                   │
                   ↓
             ┌───────────┐
             │    LLM    │
             │           │
             │   Model   │
             └───────────┘
                   │
                   ↓
             OUTPUT TOKENS
                   │
                   ↓
              TEXT RESPONSE
                   │
                   ↓
                  USER
```

---

# 17. What Happens When I Send Text to an LLM?

This is the most important question of Day 18.

Suppose I send:

```text
Explain APIs simply.
```

## Step 1 — My application sends a request

```text
Python Application
       ↓
    LLM API
```

The API is the interface through which the application communicates with the model service.

---

## Step 2 — The text is tokenized

```text
"Explain APIs simply."
          ↓
      Tokenizer
          ↓
       Tokens
```

---

## Step 3 — Context is included

Depending on the application, the request can contain:

```text
System instructions
+
Conversation history
+
Current prompt
+
Other relevant information
```

---

## Step 4 — The LLM processes the input

```text
Input Tokens
     +
Context
     ↓
    LLM
```

The LLM uses patterns and representations learned during training.

---

## Step 5 — The LLM generates output tokens

The model generates tokens progressively.

Conceptually:

```text
Token 1
   ↓
Token 2
   ↓
Token 3
   ↓
Token 4
   ↓
...
```

This is based on predicting what token should come next given the current context.

---

## Step 6 — Output tokens become text

```text
Output Tokens
      ↓
Text Response
```

The application receives the generated response.

---

# 18. Complete Request → Response Flow

The full simplified flow is:

```text
              USER
                │
                ↓
          Text / Prompt
                │
                ↓
            Tokenizer
                │
                ↓
           Input Tokens
                │
                +
              Context
                │
                ↓
               LLM
                │
                ↓
       Predict Next Token
                │
                ↓
       Predict Next Token
                │
                ↓
       Predict Next Token
                │
                ↓
          Output Tokens
                │
                ↓
          Text Response
                │
                ↓
              USER
```

---

# 19. Important Correction: API vs LLM

The **API and LLM are not the same thing**.

Think of it like:

```text
Your Python Program
       ↓
    LLM API
       ↓
      LLM
       ↓
    Response
```

The API is the communication interface.

The LLM is the actual model that processes the input and generates output.

For example, when using an SDK/API from Python:

```python
response = client.some_llm_method(...)
```

The Python application communicates with the API, and the API provides access to the model.

---

# 20. Important Mental Model

Remember these three different things:

```text
TOKENIZER
= Converts text ↔ tokens

API
= Communication interface between application and model service

LLM
= Model that processes the input/context and generates tokens
```

Simplified:

```text
Python
  ↓
API
  ↓
Tokenizer / Model system
  ↓
LLM
  ↓
Output
```

The exact internal implementation can vary by provider, but this is the useful conceptual model for an AI Engineer.

---

# 21. Tokens and Context Together

A useful way to think about an LLM request is:

```text
             REQUEST
                │
                ↓
     ┌─────────────────────┐
     │       CONTEXT       │
     │                     │
     │ System instructions │
     │ Conversation        │
     │ Current prompt      │
     │ Retrieved data      │
     └─────────────────────┘
                │
                ↓
             TOKENS
                │
                ↓
              LLM
                │
                ↓
         OUTPUT TOKENS
                │
                ↓
         TEXT RESPONSE
```

---

# 22. Day 18 Practice

Take these sentences:

```text
Hello
```

```text
Hello world
```

```text
I am learning AI Engineering.
```

```text
Python can call an LLM API.
```

For each sentence, understand that:

```text
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
LLM
```

Remember:

> The exact tokenization depends on the tokenizer/model.

The goal today is not to memorize exact token counts.

The goal is to understand:

```text
TEXT
 ↓
TOKENS
 ↓
LLM
 ↓
OUTPUT TOKENS
 ↓
TEXT
```

---

# 23. Common Misunderstandings

## ❌ "One token always equals one word."

No.

```text
1 word ≠ always 1 token
```

A word can be split into multiple tokens, and punctuation can also be represented as tokens.

---

## ❌ "The API is the LLM."

No.

```text
API = communication interface

LLM = machine-learning model
```

---

## ❌ "Inference means training the model."

No.

```text
Training
= Model learns from training data

Inference
= Trained model generates output
```

---

## ❌ "The model generates the whole response at once."

Conceptually, generation happens through repeated next-token prediction.

```text
Token 1
 ↓
Token 2
 ↓
Token 3
 ↓
...
```

---

## ❌ "Context means only my current message."

Not necessarily.

Context can include:

```text
System instructions
+
Conversation history
+
Current message
+
Retrieved information
+
Other application data
```

---

## ❌ "Context is unlimited."

No.

Models have context-window limits, and the limit depends on the model.

---

# 24. Key Terms

| Term           | Meaning                                                           |
| -------------- | ----------------------------------------------------------------- |
| LLM            | Large Language Model                                              |
| Training       | Process where a model learns from training data                   |
| Inference      | Using a trained model to generate output                          |
| Token          | Unit of text processed by the model                               |
| Input Token    | Token representing information sent to the model                  |
| Output Token   | Token generated by the model                                      |
| Tokenizer      | System that converts text into tokens and tokens back into text   |
| Context        | Information available to the model for generating a response      |
| Context Window | Maximum amount of context a model can process for a request       |
| LLM API        | Interface used by applications to communicate with an LLM service |

---

# 25. Day 18 Self-Test

I should now be able to answer these questions without looking at my notes.

### Q1. What does LLM stand for?

**Large Language Model.**

### Q2. Is an LLM a machine-learning model?

**Yes. An LLM is a type of machine-learning model.**

### Q3. What is training?

**Training is the process through which the model learns patterns from training data and its parameters are adjusted.**

### Q4. What is inference?

**Inference is using a trained model to process input and generate output.**

### Q5. What is a token?

**A token is a unit of text processed by an LLM. It is not necessarily a complete word.**

### Q6. What are input tokens?

**Tokens representing the information sent to the model.**

### Q7. What are output tokens?

**Tokens generated by the model as its response.**

### Q8. What is context?

**The information available to the model when generating a response.**

### Q9. What is a context window?

**The amount of tokenized information a model can handle as context for a request.**

### Q10. Does one word always equal one token?

**No. A word can be represented by multiple tokens, and tokens can also represent pieces of words or punctuation.**

### Q11. What does the API do?

**The API provides the communication interface through which an application sends requests to and receives responses from an LLM service.**

### Q12. What happens when I send text to an LLM?

**The text is tokenized, the request can include relevant context, the LLM processes the input and predicts output tokens progressively, and those output tokens are converted into the final text response.**

---

# 26. My Final Day 18 Understanding

The answer I should remember:

> When I send text to an LLM, the text is converted into tokens. The LLM API sends those tokens, along with any available context, to the LLM. The LLM uses patterns and representations learned during training to predict the next token and continues generating tokens until the response is complete. The generated output tokens are then converted back into text and returned as the response.

The core flow:

```text
My Text
   ↓
Tokenizer
   ↓
Input Tokens
   +
Context
   ↓
LLM
   ↓
Predict Next Token
   ↓
Predict Next Token
   ↓
Predict Next Token
   ↓
Output Tokens
   ↓
Text Response
```

---

# 27. What I Learned Today

* [x] What is an LLM?
* [x] Training vs inference
* [x] LLM vs traditional software
* [x] LLM vs ML model
* [x] How LLMs generate responses
* [x] What tokens are
* [x] Tokens are not exactly words
* [x] Input tokens
* [x] Output tokens
* [x] What context means
* [x] Context window
* [x] Why long conversations matter
* [x] Basic LLM architecture
* [x] Text → tokens → LLM → output tokens → text
* [x] What happens when text is sent to an LLM

---

# 28. Day 18 Summary

```text
LLM
= Large Language Model

TRAINING
= Model learns patterns from training data

INFERENCE
= Trained model generates output

TOKEN
= Unit of text processed by the model

INPUT TOKENS
= Tokens sent to the model

OUTPUT TOKENS
= Tokens generated by the model

CONTEXT
= Information available to the model

CONTEXT WINDOW
= Amount of tokenized context the model can handle

API
= Communication interface between application and LLM service
```

### The most important flow:

```text
User
 ↓
Prompt
 ↓
Tokenizer
 ↓
Input Tokens
 ↓
Context + Input
 ↓
LLM
 ↓
Next-token prediction
 ↓
Output Tokens
 ↓
Text
 ↓
Response
```

