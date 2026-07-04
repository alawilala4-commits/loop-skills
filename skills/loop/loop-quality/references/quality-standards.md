# Quality Standards Definition

## Code Quality Metrics

### Coverage Threshold
- Critical path (auth, payment, data): 80-90%
- Standard features: 60-80%
- Support code: 40-60%
- Overall: >= 75%

### Complexity Limits
- Cyclomatic complexity per function: <= 10
- Function length: <= 50 lines
- Class length: <= 300 lines
- Method parameters: <= 4

### Performance Targets
- API p99 latency: < 200ms (standard), < 500ms (batch)
- Test suite: < 5 min (unit), < 15 min (integration)
- Build time: < 3 min
- Deploy time: < 10 min

## Defect Severity

### Critical (P1)
- Data loss or corruption
- Security vulnerability
- Service down
- Customer cannot complete transaction
- Fix within 24 hours

### High (P2)
- Major feature broken
- Significant performance degradation (p99 > 2x)
- Authentication/authorization issue
- Fix within 1 week

### Medium (P3)
- Minor feature bug
- UI rendering issue
- Minor performance issue
- Fix within sprint

### Low (P4)
- Documentation typo
- UI polish
- Optional optimization
- Fix as time permits

## Release Readiness Checklist

Before declaring ready for production:

```
Code Quality:
  ✓ All tests passing
  ✓ Linter clean (no warnings)
  ✓ Code coverage >= 75%
  ✓ No critical issues from SAST

Security:
  ✓ No high/critical vulnerabilities
  ✓ No hardcoded secrets
  ✓ Input validation on all endpoints
  ✓ Authentication required

Performance:
  ✓ Load tested (at least 1.5x traffic)
  ✓ Database query optimized
  ✓ No N+1 issues
  ✓ Cache strategy defined

Operations:
  ✓ Monitoring setup complete
  ✓ Alerting configured
  ✓ Runbook documented
  ✓ Rollback tested

Documentation:
  ✓ API spec updated
  ✓ README reflects changes
  ✓ Deployment notes clear
  ✓ Changelog entry added
```

## Enforcement

### Pre-Commit Hook
```bash
#!/bin/bash
# Run linter, type check, format
pylint src/
mypy src/
black --check src/
```

### CI Pipeline Gate
- All tests must pass
- Coverage >= 75%
- SAST zero critical/high
- Build completes < 3 min

### Code Review Gate
- At least 1 approval
- No unresolved comments
- CI green
