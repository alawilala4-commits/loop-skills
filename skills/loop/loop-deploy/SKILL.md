---
name: loop-deploy
description: "Deploy ke production: pre-flight checks, rollout strategy, monitoring, rollback."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, deploy, production, release, infrastructure]
---

# Loop Deploy

## When to Use
Gunakan sebelum push ke production, saat release versi baru, atau saat update infrastruktur.

## Inputs
- Deployment target (dev/staging/prod).
- Release notes & changelog.
- Pre-flight checklist.
- Rollout strategy (blue-green, canary, rolling).
- Rollback plan.
- Health check endpoints.
- Monitoring & alerting.
- Stakeholder notification list.

## Procedure
1. Run pre-flight checks (build, tests, security).
2. Create release notes & tag versioning.
3. Plan rollout strategy & timing window.
4. Backup current state (database snapshot, config).
5. Deploy ke staging environment terlebih dahulu.
6. Run smoke tests di staging.
7. Get sign-off dari stakeholder jika perlu.
8. Execute production deployment sesuai strategy.
9. Monitor metrics & logs real-time.
10. Verify functionality & performance.
11. If issue: trigger rollback plan.

## Output
- Successful deployment logged & versioned.
- Release notes published.
- Rollback plan documented & tested.
- Post-deploy monitoring active.
- Issue tracking (if any).

## Pitfalls
- Jangan deploy Jumat sore tanpa on-call coverage.
- Jangan deploy tanpa rollback plan.
- Jangan trust manual checklist — automate pre-flight.
- Jangan deploy saat traffic spike.
- Jangan disable monitoring during deploy.
- Jangan skip staging environment.

## Verification
- Pre-flight checks all green.
- Smoke tests passed di staging.
- Production health checks passing.
- Metrics normal (latency, error rate, throughput).
- User-facing feature working in production.
- Database migration (if any) applied successfully.
- Rollback tested & ready.

## Pre-Flight Checklist
✓ All tests passing locally & in CI
✓ Code reviewed & approved
✓ Security audit passed
✓ Database migrations prepared & tested
✓ Environment variables set correctly
✓ Secrets rotated (if needed)
✓ Config changes verified
✓ Feature flags configured
✓ Logging & monitoring ready
✓ On-call engineer assigned
✓ Stakeholder notified

## Deployment Strategies
1. **Rolling**: Gradual replacement, zero downtime
2. **Blue-Green**: Full switch between environments
3. **Canary**: Deploy to small % users first, monitor
4. **Feature Flag**: Deploy to prod but gate feature