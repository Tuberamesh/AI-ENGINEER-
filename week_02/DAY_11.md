# DAY 11 — Type Hints & Async Basics

> Week 2 — Python for AI Engineering

## 📚 Navigation

* [← Back to Day 10 — HTTP Requests & APIs](./DAY_10.md)
* [Next → Day 12 — Classes & OOP](./DAY_12.md)

---

# 🎯 What I Learned

Today I learned two important Python concepts used heavily in modern software and AI engineering:

1. **Type Hints**
2. **Asynchronous Programming**

Topics covered:

* Function type hints
* Variable type hints
* List and dictionary hints
* Why developers use type hints
* What `async def` means
* What `await` means
* What `asyncio` does
* What `asyncio.run()` does
* What a coroutine is
* Calling async functions
* Why async is useful for I/O operations

---

# PART 1 — TYPE HINTS

# 1. What are Type Hints?

Type hints allow us to communicate what type of data a variable or function is expected to use.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

This tells us:

```text
a → expected int
b → expected int
return → expected int
```

---

# 2. Without Type Hints

```python
def add(a, b):
    return a + b
```

We don't immediately know what types the function expects.

---

# 3. With Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

Now the function clearly communicates its intention.

```text
add(
    a: int,
    b: int
)
    ↓
returns int
```

This becomes especially useful in large projects.

---

# 4. Variable Type Hints

We can also add type hints to variables.

```python
name: str = "Ramesha"

age: int = 21

price: float = 99.5

is_active: bool = True
```

Common types:

```text
str
int
float
bool
```

---

# 5. List Type Hints

Example:

```python
skills: list[str] = [
    "Python",
    "SQL",
    "APIs"
]
```

This communicates:

```text
skills
 ↓
list
 ↓
contains strings
```

Another example:

```python
numbers: list[int] = [1, 2, 3, 4]
```

---

# 6. Dictionary Type Hints

Basic:

```python
user: dict = {
    "name": "Ramesha",
    "age": 21
}
```

A more specific form:

```python
user: dict[str, int] = {
    "age": 21
}
```

The exact type-hint syntax can become more advanced later.

For now, remember:

> Type hints communicate what kind of data we expect.

---

# 7. Do Type Hints Enforce Types?

Usually, **no**.

Python is dynamically typed.

For example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

The type hints don't automatically prevent someone from passing other types.

Type hints mainly help:

* Developers
* IDEs
* Autocomplete
* Static type checkers
* Linters
* Code maintenance
* Readability

---

# 8. Why Developers Use Type Hints

Imagine a small project:

```text
100 lines
```

Type hints are helpful.

Now imagine:

```text
10,000+ lines
50 files
Multiple developers
APIs
Database
AI models
```

Type hints make it easier to understand what data moves between functions.

They improve:

```text
READABILITY
     ↓
UNDERSTANDING
     ↓
MAINTENANCE
     ↓
DEBUGGING
```

---

# 9. Type Hints in AI Engineering

A realistic AI/backend function could look like:

```python
def generate_response(prompt: str) -> dict:
    ...
```

This immediately communicates:

```text
prompt
 ↓
expected string

return value
 ↓
expected dictionary
```

Type hints are particularly useful when working with APIs, backend services and AI pipelines.

---

# PART 2 — ASYNC BASICS

# 10. What is Async?

Async means **asynchronous programming**.

The basic idea is:

> When a program has to wait for an I/O operation, it can use that waiting time to handle other eligible async work.

Common I/O operations include:

* API requests
* Network requests
* Database operations
* File operations
* External services

---

# 11. Synchronous vs Asynchronous

### Synchronous

```text
Task 1
  ↓
Wait
  ↓
Finish
  ↓
Task 2
  ↓
Wait
  ↓
Finish
```

### Asynchronous

```text
Task 1
  ↓
Waiting...
  ↓
Task 2 can run
  ↓
Task 1 finishes
```

The main benefit appears when programs spend significant time waiting for external operations.

---

# 12. `async def`

We use `async def` to define an asynchronous function.

Example:

```python
async def say_hello():
    print("Hello")
```

Compare:

```python
def say_hello():
    print("Hello")
```

The first one is an async function.

---

# 13. Defining an Async Function Does Not Run It

When Python sees:

```python
async def say_hello():
    print("Hello")
```

it only defines the function.

It does not immediately print:

```text
Hello
```

---

# 14. Calling an Async Function

If we write:

```python
say_hello()
```

Python creates a **coroutine object**.

Conceptually:

```text
say_hello()
     ↓
Coroutine object
```

The function body doesn't simply execute like a normal `def` function.

The coroutine needs to be awaited or scheduled as part of an async program.

---

# 15. What is `await`?

`await` tells Python:

> Run this async operation and wait for it to complete before this coroutine continues.

Example:

```python
async def main():
    await say_hello()
```

Flow:

```text
main()
  ↓
await say_hello()
  ↓
Run say_hello()
  ↓
Wait until it finishes
  ↓
Continue main()
```

### Important

`await` does **not** mean:

> Stop the entire program.

It pauses the **current coroutine** while waiting.

During an actual I/O wait, the event loop can handle other eligible async work.

---

# 16. Basic Async Example

```python
import asyncio

async def say_hello():
    print("Hello")

async def main():
    await say_hello()

asyncio.run(main())
```

---

# 17. Line-by-Line Execution

### Step 1

```python
import asyncio
```

Import Python's standard async library.

---

### Step 2

```python
async def say_hello():
    print("Hello")
```

Define an async function.

Nothing is printed yet.

---

### Step 3

```python
async def main():
    await say_hello()
```

Define another async function.

Inside it:

```python
await say_hello()
```

means:

```text
Run say_hello()
     ↓
Wait for it to finish
     ↓
Continue main()
```

---

### Step 4

```python
asyncio.run(main())
```

Start and run the async program.

Complete flow:

```text
asyncio.run(main())
        ↓
      main()
        ↓
await say_hello()
        ↓
say_hello()
        ↓
print("Hello")
        ↓
Hello
        ↓
say_hello finishes
        ↓
main finishes
        ↓
asyncio.run finishes
```

Output:

```text
Hello
```

---

# 18. Why Does `await` Look Continuous Here?

This is an important beginner point.

Our function only contains:

```python
print("Hello")
```

There is no real waiting operation.

Therefore:

```python
await say_hello()
```

finishes almost immediately.

So it looks like normal sequential execution.

This example mainly teaches the syntax and flow of:

```text
async def
await
asyncio.run()
```

---

# 19. What Happens Without `await`?

Consider:

```python
import asyncio

async def say_hello():
    print("Hello")

async def main():
    say_hello()

asyncio.run(main())
```

This does **not** properly execute `say_hello()`.

The line:

```python
say_hello()
```

creates a coroutine object.

Conceptually:

```text
main()
 ↓
say_hello()
 ↓
Create coroutine
 ↓
❌ Never awaited
```

The `print("Hello")` will not execute as intended.

Python may also show a warning:

```text
RuntimeWarning:
coroutine 'say_hello' was never awaited
```

---

# 20. Calling Async Functions Inside vs Outside Async Functions

## Inside an async function

Use:

```python
await say_hello()
```

Example:

```python
async def main():
    await say_hello()
```

---

## Outside an async function

You normally cannot simply write:

```python
await say_hello()
```

in ordinary synchronous code.

Instead:

```python
asyncio.run(say_hello())
```

Example:

```python
async def say_hello():
    print("Hello")

asyncio.run(say_hello())
```

Mental model:

```text
INSIDE async function
        ↓
      await
        ↓
  async function


OUTSIDE async function
        ↓
  asyncio.run()
        ↓
  async function
```

---

# 21. What is `asyncio`?

`asyncio` is Python's standard library for asynchronous programming.

It provides tools for running and managing asynchronous operations.

The main concepts learned today are:

```text
asyncio
   ↓
Python's async tools

asyncio.run()
   ↓
Starts/runs an async program

async def
   ↓
Defines an async function

await
   ↓
Waits for an async operation

coroutine
   ↓
Async operation represented by a coroutine object
```

---

# 22. Why Async Matters for AI Engineering

AI applications frequently communicate with external services.

For example:

```text
AI Application
      ↓
Send API Request
      ↓
Waiting for Server
      ↓
Receive Response
      ↓
Process Result
```

That waiting time is where asynchronous programming can become useful.

Examples:

* LLM API calls
* Web APIs
* Database requests
* Network operations
* External services
* AI agents making multiple tool calls

---

# 23. Async Does NOT Automatically Mean Faster

Important:

```text
async ≠ automatically faster
```

Async is especially useful for **I/O-bound** work.

For example:

```text
API request
Database request
Network request
```

These operations spend time waiting.

Async is not a magic solution for CPU-heavy calculations.

---

# 24. Type Hints + Async Together

Modern Python AI/backend code often combines both.

Example:

```python
async def generate_response(prompt: str) -> dict:
    ...
```

This communicates:

```text
async def
 ↓
Function is asynchronous

prompt: str
 ↓
prompt is expected to be a string

-> dict
 ↓
Function is expected to return a dictionary
```

This pattern is common in modern AI and backend applications.

---

# 🧠 Quick Revision

## Type Hints

```text
a: int
→ a is expected to be an integer

name: str
→ name is expected to be a string

list[str]
→ list containing strings

-> int
→ function is expected to return an integer
```

Remember:

> Type hints improve readability and tooling, but generally don't enforce types at runtime.

---

## Async

```text
async def
→ Define an async function

await
→ Wait for an async operation to complete

asyncio
→ Python's async library

asyncio.run()
→ Run an async program

coroutine
→ Object representing async work
```

Most important pattern:

```python
async def main():
    await some_async_function()

asyncio.run(main())
```

---

# 🚀 Final Mental Model

### Type Hints

```text
def function(
    name: str
) -> int:
```

Means:

```text
name
 ↓
expected string

return
 ↓
expected integer
```

### Async

```text
async def
    ↓
Define async work

await
    ↓
Wait for that async work

asyncio.run()
    ↓
Start the async program
```

---

# ✅ Day 11 Completed

Today I learned:

* Type hints
* Function annotations
* Variable annotations
* Async functions
* Coroutines
* `async def`
* `await`
* `asyncio`
* `asyncio.run()`
* Why async is useful for I/O-bound operations
* How async can be useful in AI/backend applications

**Next:** [Day 12 — Classes & OOP →](./DAY_12.md)

---

> **Learning principle:** Don't memorize `async` syntax. Understand what happens when the code runs.
