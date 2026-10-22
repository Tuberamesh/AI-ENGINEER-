# Day 45 — Swagger, OpenAPI and Error Handling

## Topics
- Swagger UI at `/docs`
- ReDoc at `/redoc`
- OpenAPI specification at `/openapi.json`
- HTTP status codes: 200, 201, 400, 404, 422, 500
- `HTTPException` for intentional errors
- Global exception handler for unexpected errors
- Safe error messages and private logging

## Build
- Added `GET /documents/{document_id}`
- Returned 404 for missing documents
- Tested request validation through `/ask`
- Practiced unexpected error handling with a temporary endpoint

## Key takeaway
FastAPI generates API documentation automatically and supports predictable error responses through HTTP exceptions and custom exception handlers.

## Next
Day 46 — File uploads and background tasks, according to the roadmap.
