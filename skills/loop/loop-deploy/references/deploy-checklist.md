# Deployment Checklist & Monitoring

## Rollout Timeline
- Staging: 10-15 min
- Smoke tests: 5 min
- Sign-off: 5 min
- Production deploy: 15-30 min
- Post-deploy validation: 10 min
- Total: ~1 hour

## Monitoring During Deploy
- Error rate (track spikes)
- Latency p50/p99 (track regression)
- Database query time (track locks)
- Cache hit ratio (track degradation)
- Auth failures (track token issues)
- Business metrics (traffic, conversion, etc)

## Rollback Decision Tree
- Error rate > 5%? → Rollback immediately
- Latency p99 > 2x baseline? → Evaluate, then rollback
- Auth failing > 1%? → Rollback immediately
- Database errors? → Rollback + check migrations
- Feature broken? → Feature flag off (if available)

## Rollback Procedure
1. Alert on-call team.
2. Revert to last known good version.
3. Clear cache if needed.
4. Monitor metrics return to normal.
5. Post-mortem & log incident.
6. Communicate with stakeholders.

## Post-Deploy Checklist
✓ Key user flows tested
✓ Data integrity verified
✓ Performance metrics stable
✓ No error spike
✓ All services responding
✓ External integrations working
✓ Logging/monitoring all data flowing
✓ Release notes published
✓ Team notified of completion

## Communication Template
- Pre-deploy: "Deploying X at Y time, expect Z"
- During: Real-time status in #deploy channel
- Post: "Deployment complete, metrics: [link]"
- If rollback: "Issue detected, rolling back to [version]"

## Infrastructure Considerations
- Load balancer health check updated
- DNS/routing verified
- SSL certificate valid
- CDN cache invalidated
- Database connection pool sized
- Resource limits set (CPU, memory)
- Backup retention verified
