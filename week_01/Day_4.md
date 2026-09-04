# 🚀 Day 4 — API Keys, `.env` & Environment Variables

> **Welcome to Day 4 of my 50-Day AI Engineering Journey! 👋**
>
> Today I learned something that looks small but is **extremely important in real-world development**:
>
> 🔐 **How to safely handle API keys and secrets in Python projects.**
>
> If you're following this journey with me, don't just read the code. **Understand why we're doing each step.**

---

## 📚 Missed Day 3?

If you haven't gone through Day 3 yet, I recommend starting there first.

👉 **[Go to Day 3 — APIs & Python Requests](./DAY_3.md)**

In Day 3, I learned how a Python program can communicate with an API.

Today, we're going one step further:

> **How do we authenticate with an API without exposing our API key?**

---

# 🎯 What I Learned Today

By the end of Day 4, I understood:

* 🔑 What an API key is
* 🔐 Why API keys should never be hard-coded
* 📄 What a `.env` file is
* 🐍 How Python reads environment variables
* 📦 What `python-dotenv` does
* ⚙️ What `load_dotenv()` does
* 🔍 What `os.getenv()` does
* 🚫 What `.gitignore` does
* 🌳 How Git handles ignored files
* 💾 The difference between untracked, staged and committed files
* 🚀 How to safely push a project to GitHub without pushing secrets

---

# 1️⃣ First: What Is an API Key?

When we use an API, the API provider needs to know:

> **"Who is making this request?"**

An **API key** is commonly used to identify and/or authenticate an application making API requests.

For example:

```text
Python Program
      ↓
   API Request
      ↓
   API Key 🔑
      ↓
   API Provider
      ↓
   Response
```

The API key tells the provider:

> "This request is associated with this application/account."

Depending on the API provider, the key may also control access, permissions, quotas, or billing.

---

# 2️⃣ 🚨 The Problem With Hard-Coding API Keys

Imagine I get a real API key.

A beginner might write:

```python
API_KEY = "sk-actual-secret-key"
```

This works.

### But there is a BIG problem.

If I push this code to GitHub:

```text
Python Code
     ↓
API Key inside code
     ↓
git add
     ↓
git commit
     ↓
git push
     ↓
GitHub 🌍
```

Now my secret may be exposed.

Someone could potentially use the key.

That could result in:

* ❌ Unauthorized API usage
* ❌ Quota being consumed
* ❌ Unexpected charges
* ❌ Security problems

### ❌ DON'T DO THIS

```python
API_KEY = "actual-secret-key"
```

---

# 3️⃣ ✅ The Better Approach

Instead of putting the secret directly inside Python code:

```text
Python Code
      ❌
API Key directly inside code
```

we separate the secret from the code:

```text
Python Code
      ↓
Environment Variable
      ↓
Secret stored separately
```

One common approach during development is using a `.env` file.

---

# 4️⃣ What Is `.env`?

A `.env` file is a simple text file where we can store environment variables.

For example:

```env
API_KEY=your_key_here
```

Think of it as:

> **A place to keep configuration/secrets outside your Python source code.**

Our project now looks like:

```text
AI-ENGINEER-
│
├── .env 🔐
├── .gitignore
├── README.md
│
└── week_01/
    ├── Day_1.md
    ├── Day_2.md
    ├── Day_3.md
    ├── Day_4.md
    └── env_test.py
```

### Important ⚠️

The `.env` file is **not meant to be pushed to GitHub** when it contains secrets.

---

# 5️⃣ Installing `python-dotenv`

Python doesn't automatically read a `.env` file just because it exists.

So I installed:

```bash
pip install python-dotenv
```

`python-dotenv` helps Python load variables from a `.env` file.

---

# 6️⃣ Creating `env_test.py`

Inside:

```text
week_01/env_test.py
```

I wrote:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)
```

Let's understand this **line by line**.

---

## 🔹 Line 1

```python
import os
```

Python's `os` module allows us to interact with things related to the operating system.

Here, we'll use it to access environment variables.

---

## 🔹 Line 2

```python
from dotenv import load_dotenv
```

This means:

> **Import the `load_dotenv` function from the `dotenv` package.**

Important:

This line **does not execute the function**.

It only brings the function into our Python program.

Think:

```text
from dotenv import load_dotenv
              ↓
       Bring the function
```

---

## 🔹 Line 3

```python
load_dotenv()
```

Now we actually **call the function**.

The `()` means we're executing it.

`load_dotenv()` looks for the `.env` file and loads the variables from it into the environment available to our Python process.

So:

```text
.env
│
│ API_KEY=your_key_here
↓
load_dotenv()
↓
Environment variable available
```

### Remember this:

```python
from dotenv import load_dotenv
```

= **Bring the function**

```python
load_dotenv()
```

= **Use/call the function**

We are **not calling it twice**.

---

# 7️⃣ What Does `os.getenv()` Do?

Now we have:

```python
api_key = os.getenv("API_KEY")
```

This asks Python:

> **"Give me the value of the environment variable called `API_KEY`."**

Our `.env` contains:

```env
API_KEY=your_key_here
```

So:

```python
os.getenv("API_KEY")
```

returns:

```text
your_key_here
```

Therefore:

```python
api_key = os.getenv("API_KEY")
```

means:

```text
Get API_KEY
     ↓
Store its value
     ↓
Inside the variable api_key
```

---

# 🔄 Complete `.env` Flow

This is one of the most important things I learned today:

```text
             .env
              │
              │ API_KEY=your_key_here
              ↓
        load_dotenv()
              │
              ↓
    Environment Variable
              │
              ↓
     os.getenv("API_KEY")
              │
              ↓
          api_key
              │
              ↓
       Python Program
              │
              ↓
         API Request
```

---

# 8️⃣ Testing It

I ran:

```bash
python week_01/env_test.py
```

And got:

```text
your_key_here
```

That confirmed that Python successfully loaded the value from `.env`.

### ✅ What I proved

```text
.env
  ↓
load_dotenv()
  ↓
os.getenv("API_KEY")
  ↓
Python receives the value
```

---

# 9️⃣ But There Is Still One Problem...

We have successfully separated our API key from the Python code.

But what happens if I push the `.env` file to GitHub?

```text
.env
  ↓
contains secret 🔐
  ↓
git add .env
  ↓
git push
  ↓
GitHub 😨
```

That's exactly what we **don't** want.

So we need to tell Git:

> **"Ignore `.env`."**

That's where `.gitignore` comes in.

---

# 🔟 What Is `.gitignore`?

`.gitignore` is a file that tells Git:

> **"Don't track these files or folders."**

I created/updated my `.gitignore`:

```gitignore
.venv/
.env
__pycache__/
```

Let's understand each one.

### `.venv/`

Ignores the Python virtual environment.

```text
.venv/
```

We don't normally push the entire virtual environment to GitHub.

---

### `.env`

```text
.env
```

This is the important one today.

It tells Git:

> 🔐 **Don't track my `.env` file.**

---

### `__pycache__/`

```text
__pycache__/
```

Python can create cached files while running programs.

We generally don't need to push those generated files to GitHub.

---

# 🔐 The Security Flow

Now the setup looks like this:

```text
.env
│
│ contains secret
↓
.gitignore
│
│ "Ignore .env"
↓
Git
│
├── ❌ Don't track .env
├── ❌ Don't stage .env
└── ❌ Don't commit .env
```

Meanwhile:

```text
Day_4.md       → ✅ Track
env_test.py    → ✅ Track
.gitignore     → ✅ Track
.env           → 🔐 Ignore
```

---

# 1️⃣1️⃣ How Did I Verify `.env` Was Ignored?

I ran:

```bash
git check-ignore .env
```

Git returned:

```text
.env
```

That confirmed:

> `.env` is being ignored by Git.

I also learned about:

```bash
git check-ignore -v .env
```

The `-v` means **verbose**.

It showed:

```text
.gitignore:2:.env       .env
```

This tells me:

```text
.gitignore
    ↓
Line 2
    ↓
.env rule
    ↓
.env is ignored
```

So:

```bash
git check-ignore .env
```

= **Is this file ignored?**

```bash
git check-ignore -v .env
```

= **Is this file ignored, and which rule is causing it?**

---

# 1️⃣2️⃣ Understanding `git status`

Next I checked:

```bash
git status
```

Git showed:

```text
Changes not staged for commit:

    modified: .gitignore

Untracked files:

    week_01/Day_4.md
    week_01/env_test.py
```

Notice something very important:

```text
.env
```

was **NOT shown**.

Why?

Because `.env` is ignored.

---

# 🧠 Untracked vs Ignored

This was an important Git concept for me.

### Untracked

Git sees the file but isn't tracking it yet.

Example:

```text
week_01/Day_4.md
week_01/env_test.py
```

### Ignored

Git has been explicitly told not to track the file.

Example:

```text
.env
```

So:

```text
Untracked
    ↓
Git knows the file exists
    ↓
But isn't tracking it yet
```

while:

```text
Ignored
    ↓
Git has been told
"Don't track this"
    ↓
.env
```

---

# 1️⃣3️⃣ Staging the Correct Files

I then staged the files that should be committed:

```bash
git add .gitignore week_01/Day_4.md week_01/env_test.py
```

Notice:

```text
.env
```

was **not included**.

Then:

```bash
git status
```

showed:

```text
Changes to be committed:

    modified: .gitignore
    new file: week_01/Day_4.md
    new file: week_01/env_test.py
```

Again:

```text
.env ❌
```

It wasn't staged.

That's exactly what we wanted.

---

# 1️⃣4️⃣ Commit

Once everything looked correct, I committed the changes:

```bash
git commit -m "Complete Day 4 environment variables setup"
```

Git created a commit:

```text
[main 78e520a] Complete Day 4 environment variables setup
```

A **commit** is basically a saved checkpoint of our project.

Think:

```text
Working files
     ↓
git add
     ↓
Staging area
     ↓
git commit
     ↓
Saved checkpoint 📸
```

---

# 1️⃣5️⃣ Push to GitHub

Finally:

```bash
git push
```

This pushed my commit to GitHub.

The important part is:

```text
.env
```

was **never committed**.

So my repository contains the code and documentation, but not my secret `.env` file.

---

# 🧩 Day 4 Complete Workflow

Here is the entire concept in one picture:

```text
                 API KEY 🔑
                     │
                     ↓
                   .env
                     │
                     ↓
              load_dotenv()
                     │
                     ↓
            Environment Variable
                     │
                     ↓
          os.getenv("API_KEY")
                     │
                     ↓
               Python Code
                     │
                     ↓
               API Request
                     │
                     ↓
               API Provider
                     │
                     ↓
                 Response


        🔐 SECURITY SIDE

                 .env
                   │
                   ↓
              .gitignore
                   │
                   ↓
              Git ignores it
                   │
                   ↓
            ❌ No GitHub secret
```

---

# 🧠 My Day 4 Mental Model

If I forget everything else, I want to remember this:

```text
.env
=
Where I store local environment values/secrets

load_dotenv()
=
Load values from .env

os.getenv("API_KEY")
=
Read the API_KEY value

.gitignore
=
Tell Git what NOT to track
```

And the most important rule:

> 🔐 **Never hard-code real API keys in your source code or commit real secrets to GitHub.**

---

# 📌 Quick Revision

| Concept         | What it does                                                  |
| --------------- | ------------------------------------------------------------- |
| API Key         | Identifies/authenticates an API request depending on provider |
| `.env`          | Stores environment variables locally                          |
| `python-dotenv` | Helps Python load variables from `.env`                       |
| `load_dotenv()` | Loads `.env` variables                                        |
| `os.getenv()`   | Reads an environment variable                                 |
| `.gitignore`    | Tells Git what not to track                                   |
| `git status`    | Shows Git's current state                                     |
| `git add`       | Stages changes                                                |
| `git commit`    | Saves a checkpoint                                            |
| `git push`      | Sends commits to remote repository                            |

---

# ⚠️ Important Security Note

If you accidentally expose a **real API key** on GitHub:

### Don't just delete the line and assume you're safe.

The key may already exist in Git history.

Instead:

1. **Revoke/rotate the exposed key immediately.**
2. Remove the secret from the repository.
3. Check the provider's security/billing dashboard.
4. Review Git history if necessary.

The safest approach is:

```text
Secret
  ↓
.env
  ↓
.gitignore
  ↓
Never commit it
```

---

# 🎯 Day 4 Deliverables

Today I completed:

* [x] Understand API keys
* [x] Understand why secrets shouldn't be hard-coded
* [x] Create `.env`
* [x] Install `python-dotenv`
* [x] Use `load_dotenv()`
* [x] Use `os.getenv()`
* [x] Create/update `.gitignore`
* [x] Ignore `.env`
* [x] Verify `.env` with `git check-ignore`
* [x] Understand Git status
* [x] Stage the correct files
* [x] Commit the changes
* [x] Push the project to GitHub

---

# 💡 What I Can Now Explain

After Day 4, I should be able to explain this code without memorizing it:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
```

Because I now understand **what each line is doing and WHY it is there.**

---

# 🚀 What's Next?

Day 4 taught me how to **securely manage configuration and API keys**.

Now I'm ready to continue building on top of this foundation.

### 🔥 Day 5 coming next...

> **The goal isn't just to finish 50 days.**
>
> **The goal is to become capable of building real AI/data applications.**

---

## 🤝 If You're Following This Journey

Don't just copy my commands.

Try them yourself.

Break something.

Get an error.

Search for why it happened.

Fix it.

That's where the real learning happens.

If this documentation helped you understand the concept, ⭐ **star the repository** and follow along with the next day.

**See you on Day 5! 👋**

> — **Decoder Space | AI Engineering Journey**
