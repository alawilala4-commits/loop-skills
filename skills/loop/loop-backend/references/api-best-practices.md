# API Design Best Practices

## REST Principles

### Correct Endpoint Design
```
GET    /api/users          → List all users
GET    /api/users/:id      → Get specific user
POST   /api/users          → Create user
PUT    /api/users/:id      → Update user
DELETE /api/users/:id      → Delete user
PATCH  /api/users/:id      → Partial update
```

### Status Codes
- 200: OK (success)
- 201: Created (POST success)
- 204: No Content (DELETE success)
- 400: Bad Request (invalid input)
- 401: Unauthorized (auth required)
- 403: Forbidden (permission denied)
- 404: Not Found
- 409: Conflict (duplicate/state issue)
- 500: Internal Server Error

### Request/Response Format
```json
// Request
POST /api/users
{
  "name": "John",
  "email": "john@example.com"
}

// Response (201)
{
  "status": "success",
  "data": {
    "id": "123",
    "name": "John",
    "email": "john@example.com",
    "createdAt": "2024-01-01T00:00:00Z"
  }
}

// Error Response (400)
{
  "status": "error",
  "code": "VALIDATION_ERROR",
  "message": "Invalid email format",
  "errors": [
    {
      "field": "email",
      "message": "Must be valid email"
    }
  ]
}
```

## API Versioning

### URL-based (Recommended)
```
GET /api/v1/users
GET /api/v2/users
```

### Header-based
```
GET /api/users
Accept: application/vnd.api+json;version=2
```

## Pagination

```json
GET /api/users?page=1&limit=10

Response:
{
  "status": "success",
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 42,
    "pages": 5
  }
}
```

## Filtering & Sorting

```
GET /api/users?role=admin&sort=-createdAt
GET /api/users?search=john&status=active
```

## Rate Limiting Headers

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1609459200
```

## Authentication

### Bearer Token
```
Authorization: Bearer eyJhbGc...
```

### API Key
```
X-API-Key: sk_live_1234567890
```

## Documentation
- Use OpenAPI/Swagger
- Document all endpoints
- Include examples
- Show error cases
