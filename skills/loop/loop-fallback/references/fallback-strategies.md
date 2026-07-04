# Fallback Strategies

## When Primary Path Fails

### Code Issue (Bug)
**Primary:** Fix code & deploy
**Fallback 1:** Revert to last known good version (fastest, safest)
**Fallback 2:** Disable feature with feature flag
**Fallback 3:** Scale resources (if resource-constrained)

### Database Issue (Query Slow)
**Primary:** Optimize query with index
**Fallback 1:** Use cached result if available
**Fallback 2:** Denormalize & pre-compute
**Fallback 3:** Route to read replica

### Infrastructure Issue (Service Down)
**Primary:** Restart service
**Fallback 1:** Failover to backup region
**Fallback 2:** Scale down gracefully (queue requests)
**Fallback 3:** Manual intervention (page on-call)

### External Dependency Issue (API Down)
**Primary:** Retry with backoff
**Fallback 1:** Use cached response
**Fallback 2:** Degrade gracefully (show stale data)
**Fallback 3:** Offline mode (queue for later)

## Fallback Checklist

- [ ] Fallback path tested & working
- [ ] Fallback doesn't introduce new issues
- [ ] Fallback clearly documented
- [ ] Team knows how to trigger fallback
- [ ] Fallback has monitoring/alerting
- [ ] Plan to restore primary path

## Common Fallbacks

| Failure | Fallback | Time to Execute |
|---------|----------|-----------------|
| New code | Rollback | 1-5 min |
| Slow query | Read replica | 10 min |
| Service crash | Restart | 1-3 min |
| Database down | Backup DB | 15-30 min |
| API rate limited | Cache | Immediate |
| High latency | Scale up | 5-10 min |
