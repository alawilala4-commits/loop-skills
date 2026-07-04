---
name: loop-hotfix-emergency
description: "Meta-skill: Crisis response for critical production incidents."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, meta-skill, hotfix, emergency, incident, recovery]
    composed_skills: [incident-response, debugging, fallback, retry, replanner, deploy]
---

# Loop Hotfix Emergency

## Purpose
Rapid response for critical production issues: detect → mitigate → fix → verify.

## Use When
- Production error rate > 5%
- Customer impact (service down)
- Data integrity issue
- Security breach detected
- P1 severity incident

## Workflow Sequence (Total: ~30 min)

### Phase 1: Response (0-5 min)
1. **loop-incident-response** — Page on-call, assess severity
   - Severity level (P1/P2/P3)
   - Affected users & systems
   - Business impact

### Phase 2: Mitigation (5-10 min)
2. **loop-fallback** — Deploy immediate mitigation
   - Rollback to last known good version (fastest)
   - OR disable feature with feature flag
   - OR scale resources
   - Goal: Stop bleeding immediately

### Phase 3: Diagnosis (10-20 min)
3. **loop-debugging** — Find root cause
   - Gather logs, metrics, reproduce
   - Identify affected component
   - Isolate root cause

### Phase 4: Fix & Verify (20-30 min)
4. **loop-executor** — Apply targeted fix
   - Minimal change (not refactor)
   - Code review (lightweight, fast)
   - Deploy to staging
5. **loop-retry** — Verify fix works
   - Smoke test in staging
   - Reproduce issue → verify fixed
   - Deploy to prod (canary rollout only)

### Phase 5: Monitor & Document
6. **loop-observability** — Real-time monitoring
   - Error rate trending down
   - Latency normalizing
   - User complaints stopping

## Output
- Incident resolved within SLA (< 1 hour for P1)
- Root cause identified
- Fix deployed & verified
- Incident ticket closed

## Timeline
- Mitigation: < 5 min
- Fix: < 20 min
- Deploy: < 5 min
- Total: ~30 min

## Key Decisions

**Error Rate > 5%?** → Rollback immediately (don't debug)
**Latency p99 > 2x?** → Rollback or scale up
**Auth failing?** → Rollback + check token service
**Database locked?** → Rollback + investigate
**Unknown cause?** → Feature flag OFF while investigating

## Canary Deployment Strategy
- Deploy to 10% traffic first
- Monitor for 5 min
- If OK, deploy to 100%
- If issue, rollback to 0% immediately

## Post-Incident (Next Day)
- Post-mortem meeting (30 min)
- Root cause analysis
- Prevention mechanism added
- Action items tracked