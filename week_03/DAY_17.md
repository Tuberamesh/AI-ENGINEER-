
# DAY 17 — Public API Data Processor

## 🎯 Goal

Build a complete Python program that:

Python → HTTP Request → Public API → JSON Response → Python → Processing → Useful Output → `result.json`

The goal is to combine everything learned in Week 3:

- HTTP requests
- APIs
- GET
- JSON
- Status codes
- Error handling
- Functions
- Data processing
- Saving JSON files

---

## 1. Project

Project name:

    api-data-processor

Project structure:

    api-data-processor/
    ├── main.py
    ├── api.py
    ├── processor.py
    ├── result.json
    ├── requirements.txt
    └── .gitignore

### Purpose of each file

| File | Purpose |
|---|---|
| `main.py` | Controls the overall program flow |
| `api.py` | Communicates with the API |
| `processor.py` | Processes and cleans API data |
| `result.json` | Stores the final processed output |
| `requirements.txt` | Stores project dependencies |
| `.gitignore` | Prevents unnecessary files from being committed |

---

## 2. API Used

We used JSONPlaceholder:

    https://jsonplaceholder.typicode.com/users

This is a public API that returns user data in JSON format.

The API returns 10 users.

Example response:

    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }

The actual response also contains:

- address
- phone
- website
- company

---

## 3. Requests Library

The project uses the Python `requests` library.

Check whether it is installed:

    python -m pip show requests

`requirements.txt`:

    requests

---

# 4. API Layer — api.py

The responsibility of `api.py` is to communicate with the external API.

    import requests

    API_URL = "https://jsonplaceholder.typicode.com/users"


    def fetch_data():
        try:
            response = requests.get(API_URL, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the API.")

        except requests.exceptions.Timeout:
            print("Error: The API request timed out.")

        except requests.exceptions.HTTPError as error:
            print(f"HTTP error: {error}")

        except requests.exceptions.JSONDecodeError:
            print("Error: The API returned invalid JSON.")

        return None

---

# 5. Understanding `requests.get()`

    response = requests.get(API_URL, timeout=10)

This sends an HTTP GET request to the API.

The flow is:

    Python program
          ↓
    requests.get()
          ↓
    Internet
          ↓
    API server
          ↓
    Response

### `API_URL`

    API_URL = "https://jsonplaceholder.typicode.com/users"

This tells Python where to send the request.

### `timeout=10`

    timeout=10

This means Python will wait up to 10 seconds for the request before raising a timeout error.

It does NOT mean the API must respond in exactly 10 seconds.

---

# 6. What is `response`?

When we write:

    response = requests.get(API_URL)

`response` contains the server's response.

It can contain:

- status code
- response body
- headers
- JSON data

For example:

    response.status_code

could return:

    200

---

# 7. `raise_for_status()`

    response.raise_for_status()

This checks whether the HTTP response indicates an error.

Examples:

    200 → OK
    201 → Created
    204 → No Content

    400 → Bad Request
    401 → Unauthorized
    403 → Forbidden
    404 → Not Found
    429 → Too Many Requests

    500 → Internal Server Error
    502 → Bad Gateway
    503 → Service Unavailable

If the response is an error such as 404 or 500, `raise_for_status()` raises an exception.

Example:

    404 Not Found
          ↓
    raise_for_status()
          ↓
    HTTPError

---

# 8. `response.json()`

    return response.json()

This converts the JSON response into normal Python data.

For example, JSON:

    [
        {
            "id": 1,
            "name": "Leanne Graham"
        }
    ]

becomes Python data:

    [
        {
            "id": 1,
            "name": "Leanne Graham"
        }
    ]

So:

    response.json()

means:

> Take the JSON received from the server and convert it into Python data that our program can work with.

---

# 9. Error Handling

We used `try/except` because API communication can fail.

Basic structure:

    try:
        # risky operation

    except SomeError:
        # handle the error

The `try` block contains operations that might fail.

The `except` block handles those errors.

---

# 10. ConnectionError

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")

This handles situations where Python cannot establish a connection to the server.

Flow:

    Python
       ↓
    requests.get()
       ↓
    Cannot connect
       ↓
    ConnectionError
       ↓
    except ConnectionError

Important:

ConnectionError means the connection itself could not be established.

---

# 11. Timeout

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

This happens when the request takes longer than the allowed timeout.

Example:

    requests.get(API_URL, timeout=10)

If the request does not complete within the timeout period:

    10 seconds exceeded
           ↓
        Timeout
           ↓
    except Timeout

---

# 12. HTTPError

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

This handles HTTP errors such as:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable

We tested this by temporarily changing the URL to:

    https://jsonplaceholder.typicode.com/invalid

The API responded with:

    404 Client Error: Not Found

This proved that our HTTP error handling works.

---

# 13. JSONDecodeError

    except requests.exceptions.JSONDecodeError:
        print("Error: The API returned invalid JSON.")

This happens when the server responds, but the response cannot be converted into valid JSON.

We tested:

    response = requests.get("https://example.com")
    response.json()

The connection worked.

However, `example.com` returned HTML instead of JSON.

Therefore:

    Connection works
          ↓
    Response received
          ↓
    response.json()
          ↓
    Response is not valid JSON
          ↓
    JSONDecodeError

Important difference:

    ConnectionError
    = Could not connect to the server

    JSONDecodeError
    = Connected successfully, but the response was not valid JSON

---

# 14. Why `return None`?

At the end of `fetch_data()`:

    return None

If an API error happens, the function does not have valid data to return.

So it returns:

    None

`None` means:

> There is no usable data.

Example:

    API fails
       ↓
    print error
       ↓
    return None
       ↓
    main() receives None

---

# 15. Why Check `data is None`?

In `main.py`:

    if data is None:
        return

This is an early return.

It prevents invalid data from reaching the processor.

Without this check:

    processed_data = process_data(data)

could receive:

    None

Then `processor.py` would try:

    for user in None:

Python would raise:

    TypeError: 'NoneType' object is not iterable

So:

    if data is None:
        return

means:

> If there is no data, stop the function instead of continuing.

---

# 16. Why Is `return` Useful?

`return` allows us to stop a function early when continuing would not make sense.

Example:

    def main():
        data = fetch_data()

        if data is None:
            return

        processed_data = process_data(data)

If `data` is `None`:

    API fails
       ↓
    data = None
       ↓
    data is None?
       ↓
    YES
       ↓
    return
       ↓
    main() stops

If the API succeeds:

    API succeeds
       ↓
    data contains users
       ↓
    data is None?
       ↓
    NO
       ↓
    process_data(data)
       ↓
    Continue normally

This is called an early return.

---

# 17. Processor Layer — processor.py

The processor does NOT communicate with the API.

It only works with data that has already been received by Python.

    def process_data(data):
        processed_users = []

        for user in data:
            processed_user = {
                "id": user["id"],
                "name": user["name"],
                "username": user["username"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"]
            }

            processed_users.append(processed_user)

        return {
            "total_users": len(processed_users),
            "users": processed_users
        }

---

# 18. Where Does Data Come From?

The data comes from the API.

The complete flow is:

    api.py
       ↓
    fetch_data()
       ↓
    requests.get()
       ↓
    JSONPlaceholder API
       ↓
    JSON response
       ↓
    response.json()
       ↓
    Python data
       ↓
    main.py
       ↓
    process_data(data)
       ↓
    processor.py

The processor does NOT fetch data from the internet.

It receives data from `main.py`.

---

# 19. Passing Data Between Files

In `main.py`:

    data = fetch_data()

Now `data` contains the API response.

Then:

    processed_data = process_data(data)

This passes the data into `processor.py`.

Conceptually:

    fetch_data()
         ↓
    returns API data
         ↓
    data
         ↓
    process_data(data)
         ↓
    processor.py receives data

There is no new API request happening when `process_data(data)` is called.

---

# 20. Main Program — main.py

    import json

    from api import fetch_data
    from processor import process_data


    def save_data(data):
        with open("result.json", "w") as file:
            json.dump(data, file, indent=4)


    def main():
        data = fetch_data()

        if data is None:
            return

        processed_data = process_data(data)

        save_data(processed_data)


    if __name__ == "__main__":
        main()

---

# 21. Why Use Functions?

Instead of putting everything inside one huge `main()` function, we separated responsibilities.

    fetch_data()
         ↓
    Get API data

    process_data()
         ↓
    Process API data

    save_data()
         ↓
    Save final data

This makes the project:

- easier to understand
- easier to test
- easier to maintain
- easier to modify
- more reusable

---

# 22. Saving JSON

The `save_data()` function:

    def save_data(data):
        with open("result.json", "w") as file:
            json.dump(data, file, indent=4)

opens:

    result.json

in write mode:

    "w"

Then:

    json.dump(data, file, indent=4)

writes the Python data into the file as valid JSON.

---

# 23. `json.dump()` vs `json.dumps()`

### `json.dump()`

Writes JSON directly into a file.

    json.dump(data, file, indent=4)

### `json.dumps()`

Converts Python data into a JSON-formatted string.

    json_string = json.dumps(data)

For our project we use:

    json.dump()

because we are saving the result into:

    result.json

---

# 24. Python Dictionary vs JSON

Python may display a dictionary like:

    {'name': 'Ramesha', 'age': 21}

Python commonly displays strings with single quotes.

JSON requires double quotes:

    {
        "name": "Ramesha",
        "age": 21
    }

Therefore `json.dump()` converts the Python data into valid JSON format.

---

# 25. Final `result.json`

Our final file contains processed data similar to:

    {
        "total_users": 10,
        "users": [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "city": "Gwenborough",
                "company": "Romaguera-Crona"
            }
        ]
    }

There are 10 processed users.

---

# 26. View `result.json`

Simple:

    cat result.json

This displays the contents of the file exactly as they are stored.

Another useful command:

    python -m json.tool result.json

This can:

- validate JSON
- format JSON
- make JSON easier to read

For our project, because we already use:

    json.dump(data, file, indent=4)

the JSON file is already formatted.

Therefore `cat result.json` is enough for normal viewing.

---

# 27. Complete Program Flow

The complete project works like this:

    main.py
       ↓
    fetch_data()
       ↓
    api.py
       ↓
    requests.get(API_URL)
       ↓
    Public API
       ↓
    JSON Response
       ↓
    response.json()
       ↓
    Python data
       ↓
    main.py
       ↓
    process_data(data)
       ↓
    processor.py
       ↓
    Processed data
       ↓
    save_data()
       ↓
    result.json

---

# 28. Error Flow

If something goes wrong:

    requests.get()
         │
         ├── Connection problem
         │       ↓
         │   ConnectionError
         │
         ├── Takes too long
         │       ↓
         │     Timeout
         │
         ├── HTTP error
         │       ↓
         │    HTTPError
         │
         └── Invalid JSON
                 ↓
           JSONDecodeError

All of these are handled inside `api.py`.

---

# 29. Why `try/except` Is in `api.py`

`try/except` is placed around the operations that can fail while communicating with the API:

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

These operations can produce:

- ConnectionError
- Timeout
- HTTPError
- JSONDecodeError

Therefore the API layer handles API-related errors.

The responsibilities are:

    api.py
    ↓
    API request + API error handling

    processor.py
    ↓
    Data processing

    main.py
    ↓
    Program workflow

    result.json
    ↓
    Final output

---

# 30. Important Concepts Learned

## API

An API allows one program to communicate with another system.

## Endpoint

The specific URL used to access a resource.

Example:

    https://jsonplaceholder.typicode.com/users

## GET

Used to request data.

    requests.get(url)

## JSON

A common format for exchanging structured data.

## HTTP Status Code

Tells us what happened with the request.

## `raise_for_status()`

Raises an exception when the HTTP response indicates an error.

## `response.json()`

Converts a JSON response into Python data.

## `try/except`

Allows the program to handle errors instead of crashing immediately.

## `None`

Represents the absence of a usable value.

## Early Return

Stops a function when continuing would not make sense.

Example:

    if data is None:
        return

## `json.dump()`

Writes Python data as JSON into a file.

---

# 31. Final Architecture

The project follows this architecture:

    API Layer
        ↓
    Data Processing Layer
        ↓
    Application Control
        ↓
    Output Layer

More specifically:

    api.py
        ↓
    fetch_data()
        ↓
    main.py
        ↓
    process_data()
        ↓
    processor.py
        ↓
    main.py
        ↓
    save_data()
        ↓
    result.json

---

# 32. Day 17 Checklist

- [x] Created API data processor project
- [x] Used a public API
- [x] Sent GET request
- [x] Used `requests`
- [x] Used `timeout`
- [x] Checked HTTP status
- [x] Used `raise_for_status()`
- [x] Converted JSON response into Python data
- [x] Processed API data
- [x] Passed data between functions
- [x] Passed data between Python files
- [x] Saved processed data to JSON
- [x] Used `json.dump()`
- [x] Used functions
- [x] Added API error handling
- [x] Handled ConnectionError
- [x] Handled Timeout
- [x] Handled HTTPError
- [x] Handled JSONDecodeError
- [x] Learned why `return None` is used
- [x] Learned why early `return` is useful
- [x] Tested HTTP 404 error
- [x] Tested invalid JSON response
- [x] Verified final `result.json`

---

# 🎯 Day 17 Final Takeaway

The most important thing learned today is how a real Python program can consume an API, handle failures, process the received data, and save useful results.

The complete pipeline is:

    Python
       ↓
    HTTP Request
       ↓
    Public API
       ↓
    JSON Response
       ↓
    Python Data
       ↓
    Validation / Error Handling
       ↓
    Data Processing
       ↓
    Useful Output
       ↓
    JSON File

Day 17 combines the major API concepts learned throughout Week 3 into one complete working application.
