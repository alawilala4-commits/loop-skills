# Systematic Debugging Process

## Phase 1: Reproduce (5-15 min)

### Understand the Symptom
- What exactly is broken?
- How to trigger it (steps to reproduce)?
- Does it happen every time or intermittently (flaky)?
- When did it start (recent deploy)?

### Collect Environment Info
- OS, Python/Node version
- Browser (if UI issue)
- Load conditions (heavy? idle?)
- Related recent changes

### Try Reproduce Locally
- Same code version
- Same data/configuration
- Document exact reproduction steps

## Phase 2: Isolate (10-20 min)

### Narrow Down Scope
- Component level: frontend vs backend vs database?
- Layer level: API vs business logic vs DB?
- Code path: which functions involved?

### Gather Evidence
- Logs: full stacktrace, nearby events
- Metrics: latency spike, error rate jump
- System state: CPU, memory, disk at failure time
- Recent changes: git log, deploy history

### Binary Search
- Remove components one by one
- Test after each removal
- Identify which component triggers issue

## Phase 3: Hypothesize (5-10 min)

### Possible Root Causes
1. Code bug (logic error, race condition)
2. Configuration (wrong env var, stale config)
3. Data (corrupted, missing, unexpected format)
4. External (API down, database locked)
5. Infrastructure (out of memory, disk full)

### Rank by Likelihood
- Recent code change? → Higher probability
- Configuration drift? → Medium probability
- Random cosmic ray? → Lower probability

## Phase 4: Test Hypothesis (15-30 min)

### Add Debugging
```python
# Bad: print statement
print(f"value: {value}")

# Good: structured logging with context
logger.debug(
    "Processing payment",
    extra={
        "user_id": user_id,
        "amount": amount,
        "trace_id": trace_id
    }
)
```

### Trace Execution
- Add log at entry/exit of suspected function
- Add log at key decision points
- Add log around external calls (API, DB)

### Add Instrumentation
- Metrics: timing, counts
- Watchpoints: variable changes
- Breakpoints: stop at specific line

## Phase 5: Fix (5-15 min)

### Apply Smallest Fix
- Don't refactor entire function
- Change only what's necessary
- Keep diff minimal

### Test Fix
- Reproducer should pass now
- No new errors in logs
- Performance unchanged

## Phase 6: Prevent Regressions (10-20 min)

### Add Test Case
```python
# Test the bug that was fixed
def test_payment_timeout_handling():
    # Reproduce original bug
    # Verify fix works
    # Verify it doesn't regress
```

### Add Monitoring
- Alert if metric spikes again
- Log boundary conditions
- Track similar patterns

### Document
- Root cause in commit message
- Prevention strategy
- Related issues tagged
