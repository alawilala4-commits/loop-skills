---
name: loop-feature-complete
description: "Meta-skill: Full feature development workflow from design to production."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, meta-skill, feature, workflow, complete]
    composed_skills: [orchestrator, planning, decomposer, backend, frontend, testing, code-review, deploy, observability]
---

# Loop Feature Complete

## Purpose
Orchestrate full feature development workflow: design → implement → test → review → deploy → monitor.

## Use When
- Building new feature (not hotfix)
- Cross-functional work (backend + frontend)
- Requires multiple review cycles
- Production deployment needed

## Workflow Sequence

### Phase 1: Planning (Day 1)
1. **loop-orchestrator** — Initialize feature, set scope
2. **loop-planning** — Create step-by-step plan
3. **loop-decomposer** — Break into backend, frontend, testing tasks

### Phase 2: Development (Days 2-4)
4. **loop-backend** — Implement API, database, auth
5. **loop-frontend** — Build component, styling, integration
   (4 & 5 can run in parallel)
6. **loop-testing** — Write unit & integration tests

### Phase 3: Review & QA (Day 5)
7. **loop-quality** — Check quality gate passed
8. **loop-critic** — Review for weaknesses
9. **loop-code-review** — Peer review for logic & security

### Phase 4: Deployment (Day 6)
10. **loop-deploy** — Deploy to staging → production
11. **loop-observability** — Monitor metrics, logs, alerts

### Phase 5: Closure
12. **loop-reflection** — Lessons learned
13. **loop-memory** — Save approach for similar features

## Output
- Feature deployed to production
- Tests passing & coverage ≥ 75%
- Monitoring setup & alerting active
- Team learnings documented

## Timeline
- Planning: 0.5 day
- Development: 2-3 days
- Review: 1 day
- Deployment: 0.5 day
- Total: ~4-5 days

## Key Checkpoints

✓ After Planning: Design approved
✓ After Dev: Code complete & locally tested
✓ After Review: All feedback addressed
✓ After Deploy: Smoke tests green, metrics normal
✓ After Closure: Retrospective complete

## Success Criteria
- [ ] Feature works as specified
- [ ] Tests ≥ 80% coverage
- [ ] Security audit passed
- [ ] Performance within targets
- [ ] Monitoring & alerting ready
- [ ] Documentation updated
- [ ] Team trained on changes