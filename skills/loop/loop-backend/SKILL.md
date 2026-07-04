---
name: loop-backend
description: "Development backend: API, database, auth, business logic, error handling."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, backend, API, database, logic]
---

# Loop Backend

## When to Use
Gunakan saat mengerjakan endpoint API, database schema, business logic, auth flow, atau integration.

## Inputs
- API spec / OpenAPI.
- Database schema / migrations.
- Auth requirement (JWT, OAuth, session).
- Error handling pattern.
- Rate limiting, caching strategy.
- Logging & monitoring plan.
- Performance target (p99 latency, throughput).

## Procedure
1. Design API contract (method, path, request/response).
2. Design atau update database schema.
3. Implementasi business logic dengan error handling.
4. Add input validation & sanitization.
5. Implement authentication/authorization.
6. Add caching strategy (redis, in-memory).
7. Setup logging & structured output.
8. Implementasi rate limiting.
9. Test dengan realistic data volume.
10. Verify performance target.

## Output
- API endpoint tested & documented.
- Database migrations applied.
- Error handling comprehensive.
- Logging & monitoring setup.
- Performance verified.
- Security checks passed.

## Pitfalls
- Jangan query database di loop (N+1 problem).
- Jangan store sensitive data in plain text.
- Jangan trust client input — validate semua.
- Jangan fail silently — log dan respond dengan error.
- Jangan hardcode config — gunakan env vars.
- Jangan skip database backups setup.

## Verification
- All paths have error response defined.
- No SQL injection vulnerabilities.
- No unhandled exceptions.
- Auth working (valid token, expired token, no token).
- Database transactions consistent.
- Latency within target (e.g., p99 < 200ms).
- Load tested with concurrent requests.

## API Design Checklist
✓ RESTful conventions or GraphQL clear
✓ Request/response schema documented
✓ Error codes standardized
✓ Pagination implemented (for list endpoints)
✓ Filtering/sorting available
✓ Rate limiting configured
✓ CORS configured
✓ Request validation (schema, type, size)
✓ Response serialization optimized

## Database Best Practices
- Use migrations for all schema changes
- Index foreign keys & frequent queries
- Partition large tables if needed
- Backup strategy tested
- Connection pooling configured
- Slow query logging enabled

## Authentication & Authorization
- JWT/OAuth flow documented
- Token expiry & refresh mechanism
- Permission checks at endpoint level
- Admin/user role separation
- Audit log for auth events

## Error Handling Pattern
- All endpoints return consistent error format
- Error codes mapped to HTTP status
- Sensitive info not exposed in error
- Client-friendly error messages
- Detailed logging on server side