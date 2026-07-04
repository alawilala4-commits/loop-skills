# Skill Composition Examples

## Feature Complete Workflow

**Goal:** Deliver complete feature from concept to production

**Skill Sequence:**
```
orchestrator (start)
  ↓
planning (break into: design, backend, frontend, test, deploy)
  ↓
decomposer (each into subtasks)
  ↓
router (dispatch to executor or skill-specific paths)
  ↓
[parallel: backend path → frontend path → testing path]
  ↓
quality (all green?)
  ↓
code-review (before merge)
  ↓
security (before deploy)
  ↓
deploy (to staging first)
  ↓
observability (monitor)
  ↓
synthesis (combine results)
  ↓
memory (save what we learned)
```

## Hotfix Emergency Workflow

**Goal:** Fix critical production issue ASAP

**Skill Sequence:**
```
incident-response (page on-call, assess)
  ↓
debugging (find root cause fast)
  ↓
fallback (rollback or feature flag off)
  ↓
[parallel if needed: retry or replanner]
  ↓
executor (apply fix)
  ↓
testing (smoke test)
  ↓
deploy (canary only, not full rollout)
  ↓
observability (watch metrics closely)
  ↓
memory (incident report + action items)
```

## Security Sprint Workflow

**Goal:** Audit and fix security issues

**Skill Sequence:**
```
orchestrator (scope audit)
  ↓
audit (run tools: SAST, dependency, secret)
  ↓
security (analyze results, prioritize)
  ↓
planning (plan fixes by severity)
  ↓
decomposer (per vulnerability)
  ↓
[parallel: fix & code-review]
  ↓
deploy (with security gate)
  ↓
quality (verify fixes work)
  ↓
memory (security improvements)
```
