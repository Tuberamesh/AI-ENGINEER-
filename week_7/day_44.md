# Day 44 — Request Models, Response Models & Validation

## What I learned
- Pydantic `BaseModel`
- Request bodies and JSON
- Required fields and default values
- Field validation using `Field()`
- `response_model` in FastAPI
- Automatic validation errors (HTTP 422)

## Models
- `AskRequest`: question (3–500 characters), top_k (default 3, range 1–10)
- `AskResponse`: question, answer, top_k

## Endpoint
`POST /ask`

Accepts a question and returns a placeholder answer in a consistent JSON structure.

## Testing
- Valid input: HTTP 200
- Question shorter than 3 characters: HTTP 422
- top_k greater than 10: HTTP 422

## Key takeaway
FastAPI parses and validates incoming JSON using Pydantic and validates the response structure using `response_model`.

## Next
Day 45 — Error handling and configuration.
