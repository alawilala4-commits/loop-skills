# Incident Response Playbook

## Detection Phase

### Alert Triggered
Possible sources:
- Monitoring alert (error rate, latency, disk space)
- Customer report (support ticket, email, call)
- Internal observation (team member notice)

### Severity Assessment (SLA)
- **P1 Critical:** Service down, data loss, customer cannot use
  - Response SLA: 5 min
  - Resolution SLA: 1 hour
  
- **P2 High:** Major feature broken, significant degradation
  - Response SLA: 15 min
  - Resolution SLA: 4 hours
  
- **P3 Medium:** Minor feature issue, workaround available
  - Response SLA: 1 hour
  - Resolution SLA: 1 day

## Response Phase (First 15 min)

### Step 1: Page On-Call (< 2 min)
- Incident commander paged automatically (if P1/P2)
- Message: "@oncall-incident SEV-1: [Service] [Symptom]"
- War room link posted

### Step 2: Initial Assessment (< 5 min)
- Collect: error logs, metrics graph, recent deploys
- Scope: affected users, systems, data
- Impact: customer-facing? paid feature? payment system?

### Step 3: Mitigation (< 10 min)
- Immediate action: rollback, feature flag off, scale up, etc
- Goal: stop the bleeding (not full fix yet)
- Communicate: status to stakeholders

## Investigation Phase (10-60 min)

### Root Cause Analysis
1. Timeline: when did error start?
2. Recent change: code deploy? infra? dependency?
3. Reproduce: can you trigger issue locally?
4. Logs: error stacktrace, surrounding events?
5. Metrics: where does spike start (backend/DB/cache)?

### Decision Tree
- Code issue? → Rollback or hotfix
- Infrastructure? → Scale, restart, or failover
- Database? → Query, lock, or migration issue
- External? → Third-party API down
- Unknown? → Continue investigation

## Resolution Phase

### Implement Fix
- Hotfix branch if needed
- Code review (lightweight, focused)
- Deploy to staging
- Smoke test
- Deploy to production

### Verify Resolution
- Error rate returns to baseline
- Customer flow working
- Performance normalized
- No new errors in logs

## Communication Template

```
@channel Initial report:
SEV-1: Checkout service down, customers cannot complete payment
Impact: 5% of users affected
ETA fix: 30 min
Updates in #incident channel
```

```
@channel Update (10 min):
Root cause: Database connection pool exhausted
Mitigation: Rolled back to v1.2.3
Status: Service recovering, error rate dropping
Next: Investigate why v1.2.4 caused exhaustion
```

```
@channel Resolved:
Issue resolved at 16:47 UTC
Root cause: N+1 query in checkout endpoint (new in v1.2.4)
Resolution: Rolled back, hotfix prepared
Post-mortem: Tomorrow 2pm with team
```

## Post-Incident (Next Day)

### Post-Mortem Meeting (30 min)
Attendees: incident commander, deploy lead, backend team, on-call

Agenda:
1. Timeline: what happened & when
2. Root cause: why did it happen
3. Detection: why did we catch it / miss it
4. Resolution: how did we fix it
5. Prevention: how to prevent next time

### Action Items
Each item: owner, deadline, status
Examples:
- Add test case (prevents regression)
- Add monitoring alert (catch sooner)
- Code review process improvement
- Update runbook

### Publish Results
- Post-mortem doc in wiki
- Key learnings to team
- Update incident dashboard
