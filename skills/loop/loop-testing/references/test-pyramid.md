# Test Pyramid Strategy

## Structure (Top to Bottom)

### E2E Tests (10-15%)
What: Real browser, full user flow
When: After backend + frontend integrated
Cost: Slow (3-10s per test), flaky, expensive
Count: ~10-20 tests for critical paths

Examples:
- User signup → login → create item → share
- Admin dashboard → edit user → verify logs
- Payment flow → receipt → email notification

### Integration Tests (30-40%)
What: Multiple components/modules working together
When: After unit tests pass
Cost: Medium speed (100-500ms), more stable
Count: ~30-50 tests

Examples:
- API endpoint calls database & cache
- Frontend component calls API & updates UI
- Queue consumer processes message & persists

### Unit Tests (50-60%)
What: Single function/component isolated
When: Immediately during development
Cost: Fast (1-10ms), stable, cheap
Count: ~100-200 tests per module

Examples:
- Utils function: input → output
- Component: props → render output
- Service: method return value

## Coverage Targets

**Critical Path (must have tests):**
- Authentication & authorization
- Payment & billing logic
- Data validation & sanitization
- Error handling
- Target: 80-90% coverage

**Supporting Code:**
- UI rendering
- Helper utilities
- Data transformation
- Target: 60-80% coverage

**Nice to Have (optional):**
- CSS logic
- Build/config code
- Third-party wrappers
- Target: 20-40% coverage

## Running Tests

```bash
# Unit only (fast feedback)
npm test -- --testPathPattern=unit

# Unit + Integration (pre-PR)
npm test -- --testPathPattern="(unit|integration)"

# All tests (pre-deploy)
npm test

# With coverage
npm test -- --coverage

# Watch mode (development)
npm test -- --watch
```

## Test-Driven Development (TDD) Flow

1. RED: Write failing test (define behavior)
2. GREEN: Write minimal code to pass
3. REFACTOR: Clean up without breaking test
4. REPEAT: Add next feature

Benefits:
- Design emerges naturally
- Confidence in changes
- Documentation via tests
- Less debugging later
