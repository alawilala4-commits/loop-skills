---
name: loop-code-review
description: "Review kode sebelum merge: logic, style, security, performance."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, code-review, PR-review, quality-gate]
---

# Loop Code Review

## Purpose
Review kode sebelum merge: logic, style, security, performance.

## Use When
- PR/MR siap untuk review.
- Sebelum merge ke main/staging.
- Saat ada perubahan critical path.

## Steps
1. Scan diff: understand change scope.
2. Check logic: algoritma benar, edge case handled.
3. Check style: consistent dengan codebase.
4. Check security: no injection, auth verified, secrets safe.
5. Check performance: no N+1, no memory leak, no unnecessary copy.
6. Check test: coverage adequate, test meaningful.
7. Comment & request change jika perlu.
8. Approve setelah semua resolved.

## Output
- Review status (approved/changes-requested/comment).
- List issues per category (logic, style, security, perf, test).
- Actionable feedback & suggestions.
- Approval status.

## Pitfalls
- Jangan nitpick style — use linter.
- Jangan approve tanpa memahami change.
- Jangan comment hostile — professional tone.
- Jangan skip security check.

## Verification
- Author addressed all feedback.
- Test coverage maintained or improved.
- No critical issue missed.
- Review feedback recorded.