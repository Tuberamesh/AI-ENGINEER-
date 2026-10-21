# Day 43 — FastAPI Fundamentals and Endpoints

## Objective
Build and run a basic FastAPI application and understand how HTTP requests reach Python functions.

## Topics Learned
- FastAPI application setup
- Routes and GET endpoints
- Path parameters
- Query parameters
- Running a local API using Uvicorn
- Testing endpoints using Swagger UI
- Understanding how FastAPI converts Python dictionaries into JSON responses

## Project Structure

```text
week_7/
├── app/
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── README.md
└── day_43.md
```

## Endpoints Implemented

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Check API health |
| GET | `/hello/{name}` | Return a personalized greeting |
| GET | `/square` | Calculate the square of a number using a query parameter |

## Key Concepts

### Path Parameters
Path parameters are values included directly in a URL path.

Example: `/hello/Ramesha`

FastAPI passes `Ramesha` to the function as the `name` parameter.

### Query Parameters
Query parameters are supplied after `?` in a URL.

Example: `/square?number=5`

FastAPI reads `number` as an integer and returns its square.

### Swagger UI
FastAPI automatically generates interactive API documentation at `/docs`. It allows developers to inspect endpoints, submit requests, and examine responses.

### Running the Application

```bash
source .venv/bin/activate
python -m uvicorn app.main:app --reload
```

Local server: `http://127.0.0.1:8000`

Interactive documentation: `http://127.0.0.1:8000/docs`

## Outcome
Created and ran a working FastAPI application, tested endpoints, and learned how path and query parameters pass data into Python functions.

## Next
Day 44 — Request bodies, Pydantic schemas, and POST endpoints.
