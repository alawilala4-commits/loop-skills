---
name: loop-incident-response
description: "Handle production incident: detection, triage, mitigation, resolution, retrospective."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, incident, production, crisis, recovery]
---

# Loop Incident Response

## Purpose
Handle production incident: detection, triage, mitigation, resolution, retrospective.

## Use When
- Production alert triggered.
- Customer-reported issue.
- Data integrity detected.
- Performance degradation > threshold.

## Steps
1. Detect: alert fired, customer report, or metric spike.
2. Triage: severity (P1 critical, P2 high, P3 medium, P4 low).
3. Page on-call: notify incident commander & relevant team.
4. Assess: gather logs, metrics, reproduce issue.
5. Mitigate: temporary fix atau rollback to stabilize.
6. Investigate: root cause analysis.
7. Fix: permanent solution deployed & verified.
8. Communicate: status update ke stakeholders.
9. Retrospective: post-mortem & action items.

## Output
- Incident ticket created & tracked.
- Timeline recorded.
- Root cause identified.
- Fix deployed & verified.
- Post-mortem completed.

## Pitfalls
- Jangan panic — follow playbook.
- Jangan skip communication ke stakeholder.
- Jangan skip post-mortem.
- Jangan revert tanpa understanding cause.

## Verification
- Incident resolved < SLA.
- Root cause documented.
- Prevention mechanism added.
- Team learnings captured.