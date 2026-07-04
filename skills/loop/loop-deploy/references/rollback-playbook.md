# Rollback Playbook

## Decision Tree

### Error Rate Spike (> 5% above baseline)
**Decision:** IMMEDIATE ROLLBACK
**Action:** Page incident commander, trigger rollback procedure
**Timing:** < 5 minutes

### Latency Regression (p99 > 2x baseline)
**Decision:** Evaluate (1-2 min window)
- If customer complaints: ROLLBACK
- If isolated to specific endpoint: Feature flag OFF (if available)
- If trending worse: ROLLBACK
**Timing:** < 10 minutes

### Authentication Failures (> 1%)
**Decision:** IMMEDIATE ROLLBACK
**Reason:** Auth issues compound quickly, customer impact high
**Timing:** < 3 minutes

### Database Errors (connection, lock, migration)
**Decision:** ROLLBACK + CHECK MIGRATIONS
**Action:** Revert code, verify migration rolled back
**Timing:** < 5 minutes

### Feature Broken (detected by smoke test)
**Decision:** 
- If critical path: ROLLBACK
- If edge case: Feature flag OFF, investigate
- If non-critical: Log, fix in hotfix branch
**Timing:** Depends on severity

### Data Integrity Issue
**Decision:** ROLLBACK + INVESTIGATE
**Action:** Pull data snapshot, identify anomaly, rollback if needed
**Timing:** < 15 minutes (may need forensics)

## Rollback Procedure (5 Steps)

### Step 1: Alert (< 1 min)
```
1. Declare SEV-1 incident in #incident channel
2. Tag: incident commander, oncall-backend, oncall-infra
3. Message: "Rolling back [version] due to [reason]. ETA 5 min."
4. Start incident war room (video link)
```

### Step 2: Revert (< 2 min)
```bash
# Option A: Re-deploy previous version
git checkout v1.2.4  # last known good
make deploy env=prod

# Option B: Kubernetes rollback
kubectl rollout undo deployment/api -n prod

# Option C: Feature flag toggle
POST /internal/feature-flags
  {"feature": "new_checkout", "enabled": false}
```

### Step 3: Monitor (2-5 min)
- Error rate returns to baseline
- Latency p99 normalizes
- Auth/payment flow working
- Database connections stable
- No logs showing new errors

### Step 4: Communicate (< 3 min)
```
@channel: Deployment rolled back to v1.2.4 due to high error rate.
Service recovering. Will post RCA in #incident in 1h.
```

### Step 5: Post-Mortem (Next day)
- When: 1:1 meeting with on-call & deploy lead
- Duration: 30 min
- Output: 
  - What happened
  - Why detection missed it
  - How to prevent next time
  - Action item assigned

## Pre-Rollback Checklist

Before rollback, ensure:
- [ ] Last backup verified & accessible
- [ ] Previous version tag known
- [ ] Rollback tested in staging (weekly)
- [ ] On-call has access keys
- [ ] Database migration can be reversed
- [ ] CDN cache can be cleared

## Post-Rollback Checklist

After rollback:
- [ ] Service responding normally
- [ ] No data loss reported
- [ ] Metrics recovered
- [ ] Team notified
- [ ] Incident ticket created
- [ ] Review blocked (new deploy paused 30 min)

## Prevention

For each rollback incident:
1. Add test case to catch issue
2. Add monitoring alert
3. Review code change (why did it pass?)
4. Update deployment checklist
5. Share learnings with team

## Escalation Path

- Incident Commander: decides rollback
- On-call Backend: executes rollback
- Infrastructure: monitors & supports
- Manager: notified of SEV-1
- Post-mortem attendees: incident lead + all impacted teams
