# Day 47 — Logging, Configuration and Testing

## Today's Goal
Understand how to make a FastAPI project easier to configure, debug, test, and maintain.

## 1. Logging

**File:** `app/main.py`

Logging records important events and errors while the application runs.

- `logger.info()` records normal application events.
- `logger.exception()` records an error along with traceback details.
- Log messages help identify where a request failed.

Why it matters:
When an API fails, logs help developers investigate the cause instead of guessing.

## 2. Configuration

**Files:** `app/config.py`, `.env.example`, `.gitignore`

- `config.py` loads settings using `python-dotenv`.
- `.env.example` documents the environment variables the project expects.
- `.env` stores local configuration values.
- `.gitignore` prevents `.env` and `.venv` from being committed.

Why it matters:
Configuration can change without editing application logic. Secrets can also be kept outside the source code.

## 3. Automated Testing

**File:** `tests/test_api.py`

We used Pytest and FastAPI's TestClient to test the API.

Tests cover:
- Home and health endpoints.
- Hello endpoint.
- Missing documents and invalid requests.
- Successful RAG responses using a mock.
- RAG failure returning HTTP 503.

Result: 9 tests passed.

Why it matters:
Automated tests catch regressions when we modify code. Mocking lets us test API behavior without calling the actual LLM for every test.

## Commands

Run tests:

```bash
.venv/bin/python -m pytest -v
