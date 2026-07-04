# Code Review Checklist (Detailed)

## LOGIC & FUNCTIONALITY

### Correctness
- [ ] Algorithm correct for stated requirement
- [ ] Edge cases handled (null, empty, 0, negative, large values)
- [ ] Boundary conditions checked (off-by-one, overflow)
- [ ] Error paths explicit (not silent fail)
- [ ] State transitions valid

### Complexity
- [ ] Time complexity acceptable (no O(n²) in loop)
- [ ] Space complexity acceptable (no memory leak)
- [ ] Readable: can you understand logic without heavy thinking?
- [ ] Testable: can unit test verify behavior?

### No Shortcuts
- [ ] No TODOs left behind
- [ ] No debug code (print, console.log)
- [ ] No hardcoded values (use constants/config)
- [ ] No dead code (unused variable, unreachable branch)

## SECURITY

### Input Validation
- [ ] User input validated (not trusted)
- [ ] Type checked before use
- [ ] Length/size constraints enforced
- [ ] SQL injection prevented (parameterized query)
- [ ] XSS prevented (output escaped)

### Authentication & Authorization
- [ ] Auth token verified (not expired)
- [ ] Permission checked (not just role name)
- [ ] Admin-only endpoints protected
- [ ] Cross-tenant access prevented

### Data Protection
- [ ] Sensitive data not logged
- [ ] Password/secret not in error message
- [ ] No PII in URL query param
- [ ] Encryption used for sensitive data at rest

## STYLE & CONSISTENCY

### Naming
- [ ] Variable names clear & descriptive
- [ ] Function names reflect what they do (verb)
- [ ] Constants UPPERCASE
- [ ] Private methods prefixed (_, private, __dunder)
- [ ] No single-letter variable (except loop counter i, j)

### Structure
- [ ] Function length < 30 lines (prefer smaller)
- [ ] Class/module responsibility single
- [ ] Indentation consistent (2 or 4 spaces)
- [ ] Line length < 100 characters (readability)

### Comments
- [ ] Comments explain WHY not WHAT
- [ ] No commented-out code (use git history)
- [ ] Docstring on public functions
- [ ] Complex logic commented

## TESTING

### Coverage
- [ ] Happy path tested
- [ ] Error path tested
- [ ] Edge cases tested
- [ ] Test name describes behavior
- [ ] Assertion message clear

### Test Quality
- [ ] Test independent (no side effects)
- [ ] Test not flaky (deterministic)
- [ ] Test not testing framework (test actual logic)
- [ ] Cleanup after test (mock reset, file delete)

## PERFORMANCE

### Detection
- [ ] No N+1 query (loop with query inside)
- [ ] No unnecessary copy (pass by reference if possible)
- [ ] No blocking operation on hot path
- [ ] Cache used appropriately
- [ ] Inefficient algorithm replaced (e.g., O(n²) → O(n log n))

### Monitoring Ready
- [ ] Latency metric tracked
- [ ] Error metric tracked
- [ ] Unusual call pattern logged

## DATABASE

### Migrations
- [ ] Migration backward-compatible (if needed)
- [ ] Index created for foreign key
- [ ] Data migration tested with production-like data
- [ ] Rollback tested

### Query
- [ ] Query uses index (explain analyze)
- [ ] Join not producing cartesian product
- [ ] Batch fetch (select ... where id in (...)) not per-record

## REVIEW WORKFLOW

### As Author
1. Self-review first (catch obvious issues)
2. PR description clear & reference ticket
3. Link to related PRs
4. Call out areas needing focus

### As Reviewer
1. Understand requirement first (read ticket)
2. Check logic & correctness
3. Check security & data protection
4. Check style consistency
5. Run locally if significant change
6. Approve or request changes (be specific)

### Comment Tone
❌ "This is wrong"
✓ "I think this could be O(n) instead of O(n²). What do you think?"

❌ "Bad variable name"
✓ "Can we rename `tmp` to `processed_items` for clarity?"

### Approval
- [ ] Author addressed all feedback
- [ ] Tests passing in CI
- [ ] Commit history clean (if requested)
- [ ] Ready to merge
