---
name: loop-observability
description: "Setup monitoring, logging, alerting untuk visibility production."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, observability, monitoring, logging, metrics]
---

# Loop Observability

## Purpose
Setup monitoring, logging, alerting untuk visibility production.

## Use When
- Setelah feature baru deploy.
- Saat infrastructure change.
- Setup environment baru.
- Quarterly observability audit.

## Steps
1. Define metrics: business & technical KPI.
2. Setup logging: structured logs, trace ID, context.
3. Setup metrics collection: Prometheus, CloudWatch, etc.
4. Setup alerting: thresholds, escalation, on-call routing.
5. Create dashboards: overview, per-service, per-team.
6. Setup log aggregation: centralized search & analysis.
7. Test alert: verify notification working.

## Output
- Metrics & logging configured.
- Alert rules defined.
- Dashboard accessible.
- On-call rotation setup.

## Pitfalls
- Jangan alert terlalu banyak — alert fatigue.
- Jangan log sensitive data (PII, secret).
- Jangan collect metrics dengan cardinality explosion.
- Jangan skip test alert.

## Verification
- All services shipping metrics & logs.
- Alert firing & notifying on-call.
- Dashboard real-time & accurate.
- No log data loss.