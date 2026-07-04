# Task Decomposition Examples

## Example 1: Build User Auth System

**Original Task:** "Build authentication system"

**Decomposed:**
1. Design JWT token structure & expiry
2. Implement token generation endpoint
3. Implement token validation middleware
4. Implement password hashing (bcrypt)
5. Implement login endpoint
6. Implement logout endpoint
7. Add rate limiting on login
8. Add audit logging
9. Test happy path & error cases
10. Deploy & monitor

## Example 2: Fix Performance Bug

**Original Task:** "Checkout is slow"

**Decomposed:**
1. Reproduce issue: baseline latency p99
2. Profile: identify slow component (API? DB? Frontend?)
3. If DB: identify slow query, add index or optimize
4. If API: identify bottleneck (N+1? missing cache?)
5. If Frontend: identify rendering lag or large bundle
6. Apply fix
7. Verify: latency back to normal
8. Add test to prevent regression
9. Add monitoring alert
10. Deploy

## Example 3: Migrate Database Schema

**Original Task:** "Migrate from SQLite to PostgreSQL"

**Decomposed:**
1. Design new schema in PostgreSQL
2. Create migration script (data transformation)
3. Test migration on prod-like data
4. Implement dual-write (old + new DB)
5. Run migration on staging
6. Verify data integrity
7. Run migration on production (during low traffic)
8. Verify queries work
9. Deprecate old DB connection
10. Monitor for issues

## Decomposition Rules

### Do
- Break into ~10-15 subtasks (each 1-3 days)
- Order by dependency (design → implement → test)
- Each subtask has single responsibility
- Subtask can be worked on independently

### Don't
- Too granular (100+ subtasks is a list, not a plan)
- Vague subtasks ("fix stuff", "make it work")
- Missing dependencies (parallel tasks should be marked)
- Overlapping subtasks (duplication)
