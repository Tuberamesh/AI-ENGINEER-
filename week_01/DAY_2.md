# 🚀 DAY 2 — Python Environment, Virtual Environment & pip

> Welcome to **Day 2 of my AI Engineering journey!**
>
> If you missed Day 1, don't jump directly into this one. I first learned the basic AI Engineering concepts like **AI Engineering, LLMs, Generative AI, APIs, REST APIs, HTTP, JSON, SDKs, API keys and Git/GitHub basics**.
>
> 👉 **Start here:** [Day 1 — AI Engineering Foundations](./DAY_1.md)

---

## 🎯 What I Am Learning Today

Today I am learning something that may look simple, but is extremely important in real-world Python and AI projects:

* Python environment
* Virtual environments (`venv`)
* Activating a virtual environment
* `pip`
* Python packages
* Dependencies
* Installing `requests`
* Checking installed packages
* `.gitignore`
* Basic project structure
* Running Python files
* Git + GitHub workflow

The goal is not just to memorize commands.

I want to understand **why we use them**.

---

# 1. First: What is a Python Environment?

Before understanding `venv`, I need to understand what an **environment** means.

A Python environment is basically the place where my Python program runs along with the Python version and packages it needs.

For example, my project might need:

```text
Python 3.12
requests
pandas
numpy
fastapi
```

Another project might need different versions of these packages.

This creates a problem.

---

# 2. Why Do We Need a Virtual Environment?

Imagine I have two projects.

### Project A

```text
Project A
    Python 3.12
    pandas 2.x
    requests
```

### Project B

```text
Project B
    Python 3.12
    pandas 1.x
    requests
```

Both projects need `pandas`, but they need **different versions**.

If I install everything globally on my computer, the projects can start fighting with each other.

This is called a:

> **Dependency conflict**

For example:

```text
Project A → pandas 2.x
Project B → pandas 1.x
              ↓
          Conflict ❌
```

A virtual environment solves this problem.

---

# 3. What is `venv`?

`venv` stands for:

> **Virtual Environment**

It creates an isolated Python environment for a project.

Think of it like giving every project its **own Python workspace**.

Instead of:

```text
My Computer
    ↓
One Python
    ↓
All Projects
    ↓
All Packages
```

I can have:

```text
My Computer
│
├── Project A
│   └── .venv
│       ├── Python
│       └── Packages
│
├── Project B
│   └── .venv
│       ├── Python
│       └── Packages
│
└── Project C
    └── .venv
        ├── Python
        └── Packages
```

Now each project can have its own dependencies.

### Why is this important for AI Engineering?

AI projects use many libraries.

For example, later I may work with:

```text
FastAPI
OpenAI SDK
Pandas
NumPy
SQLAlchemy
LangChain
Pydantic
```

Different projects may require different versions.

So learning virtual environments now is important because I will use them repeatedly in real AI projects.

---

# 4. Creating a Virtual Environment

I created my environment from the **repository root**.

My project structure is:

```text
AI-ENGINEER-/
```

I ran:

```bash
python3 -m venv .venv
```

Let's understand this command instead of blindly memorizing it.

### `python3`

Use Python 3.

### `-m`

Tell Python to run a module.

### `venv`

Use Python's built-in virtual environment module.

### `.venv`

The name of the environment folder.

So:

```bash
python3 -m venv .venv
```

basically means:

> "Python, create a virtual environment called `.venv` in this project."

After running it, I got:

```text
AI-ENGINEER-/
│
├── .venv/
├── README.md
└── week_01/
```

---

# 5. Activating the Virtual Environment

Creating the environment and using the environment are two different things.

I created it with:

```bash
python3 -m venv .venv
```

Then I activated it:

```bash
source .venv/bin/activate
```

After activation, my terminal showed:

```text
(.venv) (base) ramesha@... AI-ENGINEER- %
```

The important part is:

```text
(.venv)
```

That tells me the virtual environment is currently active.

---

# 6. How Do I Know My `.venv` Is Actually Being Used?

I don't want to simply trust the terminal prompt.

I can verify it.

Run:

```bash
which python
```

and:

```bash
which pip
```

My result was similar to:

```text
/Users/ramesha/Desktop/AI-ENGINEER-/.venv/bin/python
```

and:

```text
/Users/ramesha/Desktop/AI-ENGINEER-/.venv/bin/pip
```

This is important.

It proves that:

```text
python → my project's .venv
pip    → my project's .venv
```

So when I install packages, they are installed into my project environment rather than randomly into my global Python installation.

---

# 7. What is `pip`?

Now we come to another important word:

> **pip**

`pip` is Python's package installer/package manager.

Python itself comes with many built-in features, but developers don't want to write everything from scratch.

For example, if I want to make HTTP requests, I can use a library called:

```text
requests
```

I can install it using:

```bash
pip install requests
```

So:

```text
Python
   ↓
pip
   ↓
Install Python packages
```

Think of `pip` like a **package manager for Python**.

It allows me to:

```text
install packages
upgrade packages
remove packages
check installed packages
```

---

# 8. Useful `pip` Commands

### Check pip version

```bash
pip --version
```

Example:

```text
pip 24.x ... (python 3.12)
```

This tells me which pip I am using.

---

### Install a package

```bash
pip install requests
```

---

### See installed packages

```bash
pip list
```

---

### Show information about a package

```bash
pip show requests
```

This can show things like:

```text
Name
Version
Location
Dependencies
```

---

### Upgrade a package

```bash
pip install --upgrade requests
```

---

### Uninstall a package

```bash
pip uninstall requests
```

---

# 9. What is a Python Package?

A Python package is reusable code written by developers that I can install and use in my project.

Instead of writing everything myself, I can use existing libraries.

For example:

```text
requests → HTTP/API communication
numpy    → numerical computing
pandas   → data manipulation
fastapi  → APIs/backend
```

This is extremely important in AI Engineering because modern applications depend heavily on existing libraries and SDKs.

---

# 10. What is `requests`?

Today I installed:

```bash
pip install requests
```

`requests` is a Python library used for making **HTTP requests**.

Remember Day 1?

I learned:

```text
Client
   ↓
HTTP Request
   ↓
Server / API
   ↓
HTTP Response
```

`requests` helps my Python program communicate with APIs.

For example:

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
```

Here:

```python
requests.get(...)
```

sends an HTTP GET request.

The server sends a response back.

---

# 11. Why is `requests` Important for AI Engineering?

Because AI applications don't work in isolation.

A real AI application may communicate with:

```text
Weather API
Payment API
Database API
GitHub API
OpenAI API
Google API
Internal company APIs
```

For example:

```text
User
  ↓
My AI Application
  ↓
API Request
  ↓
External API
  ↓
JSON Response
  ↓
My Application
```

Later, I will use more specialized SDKs and frameworks, but understanding HTTP requests is still fundamental.

---

# 12. What are Dependencies?

When I installed:

```bash
pip install requests
```

I didn't only get `requests`.

My environment also contained packages such as:

```text
requests
urllib3
certifi
charset-normalizer
idna
```

Why?

Because `requests` depends on other packages.

Think about it like this:

```text
requests
   │
   ├── urllib3
   ├── certifi
   ├── charset-normalizer
   └── idna
```

These are called:

> **Dependencies**

A dependency is a package that another package needs to work correctly.

So when I install a package, pip can automatically install the packages it depends on.

---

# 13. Checking Installed Packages

I used:

```bash
pip list
```

and saw packages similar to:

```text
Package             Version
------------------- ---------
certifi             ...
charset-normalizer  ...
idna                ...
pip                 ...
requests            ...
urllib3             ...
```

This is useful because I can quickly see what is installed in my current environment.

---

# 14. Why `.venv` Should NOT Go to GitHub

After creating my environment, I ran:

```bash
git status
```

Git showed:

```text
.venv/
```

as an untracked folder.

At first I might think:

> "I created this folder, so shouldn't I push it?"

No.

I should **not** push `.venv` to GitHub.

Why?

Because `.venv` contains the local Python environment and installed packages.

It can contain a huge number of files.

Another developer doesn't need my local environment.

They can create their own environment.

So:

```text
My computer
    ↓
.venv
    ↓
LOCAL ONLY ❌
```

while:

```text
Source code
README
DAY_2.md
.gitignore
    ↓
GitHub ✅
```

---

# 15. What is `.gitignore`?

`.gitignore` is a special file that tells Git:

> "Ignore these files or folders. Don't track them."

I created:

```text
.gitignore
```

and added:

```text
.venv/
```

Now Git knows:

```text
.venv/
   ↓
IGNORE ❌
```

while my actual project files can still be tracked:

```text
week_01/DAY_2.md
week_01/hello.py
.gitignore
   ↓
TRACK ✅
```

---

# 16. Why is `.gitignore` Important?

Because real projects contain files that should not be committed.

Examples:

```text
.venv/
__pycache__/
.env
*.pyc
.DS_Store
```

Some files are unnecessary.

Some can contain secrets.

For example:

```text
.env
```

may contain:

```text
OPENAI_API_KEY=xxxxxxxx
DATABASE_PASSWORD=xxxxxxxx
```

I should **never commit API keys or passwords to GitHub**.

So `.gitignore` becomes extremely important in AI Engineering.

A common `.gitignore` for Python projects may contain:

```text
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

---

# 17. `.gitignore` Does NOT Delete Files

This is important.

If I write:

```text
.venv/
```

inside `.gitignore`, Git doesn't delete `.venv`.

It simply tells Git:

> "Don't track this folder."

The folder still exists on my Mac.

```text
Mac
│
├── .venv/       ← still exists
├── .gitignore
└── week_01/
```

Only Git ignores it.

---

# 18. Creating and Running a Python File

Inside:

```text
week_01/
```

I created:

```text
hello.py
```

The file contains:

```python
print("AI Engineering Journey - Day 2")
```

I can run it using:

```bash
python hello.py
```

Output:

```text
AI Engineering Journey - Day 2
```

This confirms that Python is able to execute my file.

---

# 19. One Mistake I Made Today 😅

At one point I accidentally put this:

```text
echo 'print("AI Engineering Journey - Day 2")' > hello.py
```

inside `hello.py`.

Python then gave me:

```text
SyntaxError
```

Why?

Because:

```text
echo
```

is a **terminal command**, not Python code.

The terminal command:

```bash
echo 'print("Hello")' > hello.py
```

creates/writes the file.

But the actual Python file should contain:

```python
print("Hello")
```

This distinction is important:

```text
Terminal command ≠ Python code
```

---

# 20. My Final Project Structure

After today's work, my repository looks like:

```text
AI-ENGINEER-/
│
├── README.md
├── .gitignore
│
├── .venv/              # Local only — NOT pushed
│
└── week_01/
    ├── DAY_1.md
    ├── DAY_2.md
    └── hello.py
```

---

# 21. Git Workflow I Used Today

After creating my files, I checked:

```bash
git status
```

Then I added the files:

```bash
git add .gitignore week_01/DAY_2.md week_01/hello.py
```

I created a commit:

```bash
git commit -m "Day 2 - Python Environment and pip"
```

And finally pushed to GitHub:

```bash
git push
```

My push succeeded:

```text
main -> main
```

So Day 2 is now saved on GitHub.

---

# 22. The Complete Day 2 Workflow

This is the workflow I want to remember.

### Step 1 — Go to project

```bash
cd AI-ENGINEER-
```

### Step 2 — Create environment

```bash
python3 -m venv .venv
```

### Step 3 — Activate it

```bash
source .venv/bin/activate
```

### Step 4 — Verify Python and pip

```bash
which python
which pip
```

Both should point to:

```text
AI-ENGINEER-/.venv/
```

### Step 5 — Install packages

```bash
pip install requests
```

### Step 6 — Check packages

```bash
pip list
```

### Step 7 — Write Python code

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
```

### Step 8 — Create `.gitignore`

```text
.venv/
.env
__pycache__/
*.pyc
.DS_Store
```

### Step 9 — Check Git

```bash
git status
```

### Step 10 — Add files

```bash
git add .
```

### Step 11 — Commit

```bash
git commit -m "Day 2 - Python Environment and pip"
```

### Step 12 — Push

```bash
git push
```

---

# 🧠 The Most Important Concepts From Today

If I forget everything else, I should remember these:

| Concept            | Simple Meaning                           |
| ------------------ | ---------------------------------------- |
| Python environment | Where my Python project runs             |
| `venv`             | Creates an isolated Python environment   |
| `.venv`            | The folder containing that environment   |
| Activate           | Tell my terminal to use that environment |
| `pip`              | Installs and manages Python packages     |
| Package            | Reusable Python code                     |
| Dependency         | A package required by another package    |
| `requests`         | Python library for HTTP requests         |
| `.gitignore`       | Tells Git what NOT to track              |
| Git                | Tracks changes in my project             |
| GitHub             | Stores/shares my Git repository online   |

---

# 🔥 One Simple Mental Model

I can remember Day 2 like this:

```text
Python
  ↓
Create .venv
  ↓
Activate .venv
  ↓
pip install packages
  ↓
Write Python code
  ↓
.gitignore protects unnecessary/secrets files
  ↓
Git tracks my code
  ↓
GitHub stores my project
```

Or even shorter:

> **venv isolates → pip installs → packages help → code uses them → .gitignore protects → Git tracks → GitHub stores**

---

# 🤖 Why This Matters for My AI Engineering Journey

Today may look like basic Python setup.

But this is the foundation for everything that comes next.

When I eventually build:

```text
AI Application
      ↓
Python
      ↓
Virtual Environment
      ↓
AI/ML Libraries
      ↓
APIs
      ↓
Database
      ↓
LLM
      ↓
Deployment
```

I will repeatedly use the same environment and package-management concepts.

So I am not just learning:

```text
pip install requests
```

I am learning the **professional workflow for building Python applications**.

---

## ✅ Day 2 Checklist

* [x] Understand Python environments
* [x] Understand virtual environments
* [x] Create `.venv`
* [x] Activate `.venv`
* [x] Verify Python and pip
* [x] Understand `pip`
* [x] Install `requests`
* [x] Understand packages
* [x] Understand dependencies
* [x] Create and run `hello.py`
* [x] Understand `.gitignore`
* [x] Keep `.venv` out of GitHub
* [x] Commit changes
* [x] Push changes to GitHub

---

# 🎯 Day 2 Complete!

I now understand **why** Python projects use virtual environments, packages, pip and `.gitignore`.

More importantly, I actually created an environment, installed a package, ran Python code and pushed the project to GitHub.

**Day 2 → DONE ✅**

➡️ Next: **Day 3**
