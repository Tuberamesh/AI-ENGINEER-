# Day 7 — Engineering Python Foundations

> **Goal:** Learn how to write reusable Python code and organize it properly using **functions, modules, packages, pip, and virtual environments.**

---

## 📚 What I Learned

* Functions
* Parameters and arguments
* Default arguments
* `*args`
* `**kwargs`
* Modules
* `import`
* Packages
* `pip`
* Virtual environments
* `venv`

---

# 1. Functions

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code again and again, we create a function and call it whenever needed.

### Example

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total


result = calculate_total(100, 3)

print(result)
```

Output:

```text
300
```

### Important

`return` sends a value back from the function.

```python
def add(a, b):
    return a + b
```

We can store the returned value:

```python
result = add(10, 20)
print(result)
```

### `return` vs `print`

```python
print()
```

Displays something on the screen.

```python
return
```

Sends a value back to the code that called the function.

---

# 2. Parameters and Arguments

### Parameter

A parameter is the variable written when defining a function.

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a **parameter**.

### Argument

An argument is the actual value passed when calling the function.

```python
greet("Ramesh")
```

Here, `"Ramesh"` is an **argument**.

### Multiple Parameters

```python
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
30
```

---

# 3. Default Arguments

A function parameter can have a default value.

```python
def greet(name, message="Hello"):
    print(message, name)
```

We can use the default:

```python
greet("Ramesh")
```

Output:

```text
Hello Ramesh
```

Or provide our own value:

```python
greet("Ramesh", "Good Morning")
```

Output:

```text
Good Morning Ramesh
```

### Key idea

If an argument is not provided, Python uses the default value.

---

# 4. `*args`

`*args` allows a function to accept **any number of positional arguments**.

```python
def add(*args):
    total = 0

    for number in args:
        total += number

    return total
```

Now we can pass any number of values:

```python
print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))
```

### What happens?

```python
add(10, 20, 30, 40)
```

Inside the function:

```python
args = (10, 20, 30, 40)
```

`args` is a **tuple**.

The loop takes each value one by one:

```python
for number in args:
```

---

# 5. `**kwargs`

`**kwargs` allows a function to accept **any number of keyword arguments**.

```python
def create_user(**kwargs):
    print(kwargs)


create_user(
    name="Ramesh",
    age=20,
    city="Bengaluru"
)
```

Output:

```text
{'name': 'Ramesh', 'age': 20, 'city': 'Bengaluru'}
```

`kwargs` is a **dictionary**.

We can access the key and value:

```python
def show_user(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
```

### Key idea

```text
*args       → multiple positional arguments → tuple

**kwargs    → multiple keyword arguments   → dictionary
```

---

# 6. Modules

A **module** is simply a Python `.py` file containing reusable code.

Instead of putting everything into one large file, we can separate our code into different modules.

### Example

```text
project/
├── main.py
└── utils.py
```

`utils.py`

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

`main.py`

```python
from utils import add, multiply

print(add(10, 20))
print(multiply(5, 4))
```

Output:

```text
30
20
```

### Key idea

```text
Module = one Python .py file
```

---

# 7. Import

`import` allows us to use code from another module.

### Example

```python
from utils import add

result = add(10, 20)

print(result)
```

Here:

```text
utils → module
add   → function
```

The import tells Python:

> Get the `add` function from the `utils` module.

---

# 8. Packages

A **package** is a folder used to organize related Python modules.

Example:

```text
utils_package/
├── __init__.py
└── math_utils.py
```

`math_utils.py`

```python
def square(number):
    return number * number


def cube(number):
    return number * number * number
```

We can import these functions:

```python
from utils_package.math_utils import square, cube

print(square(5))
print(cube(3))
```

Output:

```text
25
27
```

### Import path

```text
utils_package
      ↓
math_utils.py
      ↓
square()
```

### Remember

```text
Module  → a single .py file

Package → a folder containing related Python modules
```

---

# 9. `pip`

`pip` is Python's **package installer and manager**.

It allows us to install external Python packages.

For example:

```bash
pip install requests
```

After installing it, we can use it in Python:

```python
import requests
```

### Useful commands

Check pip:

```bash
pip --version
```

See installed packages:

```bash
pip list
```

### Key idea

```text
pip = tool used to install and manage Python packages
```

---

# 10. Virtual Environments

A **virtual environment** creates an isolated Python environment for a project.

This is useful because different projects may require different package versions.

### Without a virtual environment

```text
Project A ─┐
Project B ─┼──> Same Python environment
Project C ─┘
```

This can cause package/version conflicts.

### With virtual environments

```text
Project A → venv → its own packages

Project B → venv → its own packages

Project C → venv → its own packages
```

Each project can have its own dependencies.

---

# 11. Creating a Virtual Environment

Inside the project folder:

```bash
python3 -m venv venv
```

This creates:

```text
venv/
```

inside the project.

Example:

```text
day7/
├── main.py
├── utils.py
├── utils_package/
│   ├── __init__.py
│   └── math_utils.py
└── venv/
```

---

# 12. Activating a Virtual Environment

On macOS/Linux:

```bash
source venv/bin/activate
```

After activation, the terminal usually shows:

```text
(venv)
```

This means the terminal is now using the project's virtual environment.

We can verify the Python being used:

```bash
which python
```

---

# 13. Deactivating a Virtual Environment

When finished working:

```bash
deactivate
```

This leaves the virtual environment and returns to the normal environment.

### Remember

```text
activate
   ↓
Work inside project environment
   ↓
deactivate
   ↓
Leave project environment
```

---

# 14. Final Project Structure

My Day 7 practice project:

```text
day7/
├── main.py
├── utils.py
├── utils_package/
│   ├── __init__.py
│   └── math_utils.py
└── venv/
```

---

# 15. Complete Example

### `utils.py`

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def greet(name, message="Hello"):
    return f"{message}, {name}!"
```

### `math_utils.py`

```python
def square(number):
    return number * number


def cube(number):
    return number * number * number
```

### `main.py`

```python
from utils import add, multiply, greet
from utils_package.math_utils import square, cube


print(add(10, 20))
print(multiply(5, 4))
print(greet("Ramesh"))

print(square(5))
print(cube(3))
```

Output:

```text
30
20
Hello, Ramesh!
25
27
```

---

# 🧠 Quick Revision

| Concept          | Meaning                                |
| ---------------- | -------------------------------------- |
| Function         | Reusable block of code                 |
| Parameter        | Variable defined in a function         |
| Argument         | Value passed to a function             |
| Default argument | Parameter with a default value         |
| `*args`          | Multiple positional arguments          |
| `**kwargs`       | Multiple keyword arguments             |
| Module           | A `.py` file containing reusable code  |
| `import`         | Used to bring code from another module |
| Package          | Folder containing related modules      |
| `pip`            | Installs and manages Python packages   |
| `venv`           | Creates an isolated Python environment |
| `activate`       | Enter the virtual environment          |
| `deactivate`     | Leave the virtual environment          |

---

# 🔗 The Big Picture

The concepts connect like this:

```text
FUNCTION
   ↓
Reusable piece of code

MODULE
   ↓
Organize functions into .py files

PACKAGE
   ↓
Organize related modules into folders

PIP
   ↓
Install external Python packages

VIRTUAL ENVIRONMENT
   ↓
Keep project dependencies isolated
```

### One-line memory trick

> **Functions organize code → Modules organize functions → Packages organize modules → pip manages packages → venv isolates the project.**

---

## ✅ Day 7 Outcome

After completing Day 7, I can:

* Create reusable Python functions
* Use parameters and return values
* Work with default arguments
* Use `*args` and `**kwargs`
* Create and import my own modules
* Organize modules inside packages
* Understand and use `pip`
* Create and use virtual environments
* Understand why project isolation matters

**Day 7 complete — Engineering Python Foundations 🚀**
