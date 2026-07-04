# API Design Template (Minimal)

## Endpoint Structure

```
Method: POST
Path: /api/v1/users
Request:
  {
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user"
  }

Response (200):
  {
    "id": "uuid-123",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user",
    "created_at": "2026-07-04T16:46:00Z"
  }

Response (400):
  {
    "code": "VALIDATION_ERROR",
    "message": "Email already exists",
    "details": {
      "field": "email",
      "constraint": "unique"
    }
  }

Response (401):
  {
    "code": "UNAUTHORIZED",
    "message": "Invalid or missing authentication token"
  }

Response (500):
  {
    "code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred",
    "trace_id": "abc-123-def"
  }
```

## HTTP Status Mapping
- 200 OK: Success
- 201 Created: Resource created
- 400 Bad Request: Validation error
- 401 Unauthorized: Auth missing/invalid
- 403 Forbidden: Auth valid but no permission
- 404 Not Found: Resource not found
- 429 Too Many Requests: Rate limit hit
- 500 Internal Server Error: Server error
- 503 Service Unavailable: Temporary outage

## Request Validation
- Type check: string, number, array, object
- Required fields explicit
- Length constraints: min/max
- Format constraints: email, UUID, ISO date
- Enum validation: allowed values only

## Response Format
- Always JSON
- Include request trace_id for debugging
- Consistent error structure
- No sensitive data in error message

## Authentication
- Bearer token in Authorization header
- JWT claims include user_id, scope, exp
- Token refresh endpoint (expires in 1h)
- Logout endpoint clear server-side session

## Pagination
- Query param: page (1-indexed), limit (max 100)
- Response includes: total, page, limit, has_next
- Sort param: field name with +/- prefix (+name, -created_at)
