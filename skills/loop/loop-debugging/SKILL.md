---
name: loop-debugging
description: "Diagnosa & perbaiki error dari test atau production."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, debugging, troubleshooting, error-analysis]
---

# Loop Debugging

## Purpose
Diagnosa & perbaiki error dari test atau production dengan sistematik.

## Use When
- Test failure tiba-tiba.
- Exception di production.
- Feature tidak bekerja sesuai harapan.
- Performance degradation.

## Steps
1. Reproduksi error: understand symptoms & context.
2. Collect data: logs, stacktrace, metrics, state.
3. Isolate: narrow down scope (component, layer, path).
4. Hypothesize: candidates root cause.
5. Test hypothesis: add debugging, trace execution.
6. Fix: apply smallest change yang resolve root cause.
7. Verify: test reproduce, monitor production.

## Output
- Root cause identified.
- Fix applied & tested.
- Prevention strategy (test, monitoring, guard).
- Post-mortem jika production incident.

## Pitfalls
- Jangan symptoms-driven — find root cause.
- Jangan apply random fixes.
- Jangan skip adding test untuk prevent regresi.
- Jangan ignore similar patterns elsewhere.

## Verification
- Error tidak terulang.
- Fix tidak introduce regresi.
- Test added untuk prevent future.
- Team aware of fix & rationale.