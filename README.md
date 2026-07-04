════════════════════════════════════════════════════════════════
                    LOOP SKILLS FRAMEWORK
                        MASTER INDEX
                 Production Ready | v1.0.0 | 2026-07-04
════════════════════════════════════════════════════════════════

## QUICK NAVIGATION

### Command Cheatsheet
```bash
# List all skills
skills_list(category='loop')

# View any skill + references
skill_view(name='loop-backend')

# Validate all skills
bash ~/.hermes/scripts/loop-validate.sh

# Generate report
bash ~/.hermes/scripts/loop-report.sh summary

# Run workflow scheduler
bash ~/.hermes/scripts/loop-workflow-scheduler.sh status
```

## SKILLS INVENTORY (33 Total)

### CORE (8 Skills)
- loop-orchestrator ........ Routing & sequencing
- loop-planning ........... Decomposition & planning
- loop-decomposer ......... Task breakdown
- loop-router ............. Skill/tool selection
- loop-executor ........... Execute workflow
- loop-verifier ........... QA & validation
- loop-critic ............. Review weaknesses
- loop-quality ............ Quality gates

### EXECUTION (6 Skills)
- loop-backend ............ API & database
- loop-frontend ........... Component & UI
- loop-testing ............ Validation tests
- loop-debugging .......... Error diagnosis
- loop-code-review ........ PR review
- loop-deploy ............. Production deployment

### RECOVERY (4 Skills)
- loop-fallback ........... Alternative paths
- loop-retry .............. Retry with strategy
- loop-replanner .......... Replan on failure
- loop-incident-response .. Crisis handling

### ASSURANCE (3 Skills)
- loop-audit .............. Code audit
- loop-security ........... Security check
- loop-observability ...... Monitoring setup

### CONTEXT (6 Skills)
- loop-memory ............. Save state
- loop-reflection ......... Evaluate iterative
- loop-research ........... Gather info
- loop-context-management  Organize context
- loop-handoff ............ Delegate work
- loop-synthesis .......... Combine results

### ADVANCED (3 Skills)
- loop-tool-use ........... Tool management
- loop-safety ............. Risk guard
- loop-budget ............. Token/time limit

### META-SKILLS (3 Skills)
- loop-feature-complete ... Full dev workflow
- loop-hotfix-emergency ... Crisis response
- loop-security-sprint .... Security audit

## AUTOMATION SCRIPTS (5 Total)

Location: ~/.hermes/scripts/

1. **loop-validate.sh** — Validate all 33 skills
   Usage: bash loop-validate.sh [skill-filter]

2. **loop-run.sh** — Execute skill workflow
   Usage: bash loop-run.sh loop-backend

3. **loop-report.sh** — Generate status reports
   Usage: bash loop-report.sh [summary|json|markdown]

4. **loop-integration-test.sh** — Test automation
   Usage: bash loop-integration-test.sh

5. **loop-workflow-scheduler.sh** — Task scheduler (Termux-compatible)
   Usage: bash loop-workflow-scheduler.sh [validate|report|audit|all|status]

## REFERENCE FILES (17 Total)

CORE:
- orchestrator-routing.md
- orchestrator-skill-composition.md
- planning-template.md
- quality-standards.md
- decomposition-examples.md
- fallback-strategies.md

EXECUTION:
- api-design-minimal.md
- component-checklist.md
- test-pyramid.md
- code-review-detailed.md
- debugging-process.md

ASSURANCE:
- audit-tools.md
- owasp-checklist.md
- observability-setup.md
- rollback-playbook.md
- deploy-checklist.md
- incident-playbook.md

## DOCUMENTATION (5 Total)

~/.hermes/

1. LOOP_FINAL_REPORT.md ............ Complete status report
2. LOOP_SKILLS_MAP.md ............. Taxonomy & architecture
3. LOOP_UPGRADE_ROADMAP.md ........ 5-phase roadmap
4. LOOP_SKILLS_DEPLOYMENT.md ...... Deployment checklist
5. PHASE2_COMPLETION_SUMMARY.md ... This phase summary

## WORKFLOW EXAMPLES

### Feature Development (4-5 days)
loop-feature-complete
  → planning, decomposer
  → backend, frontend, testing (parallel)
  → code-review, security
  → deploy, observability

### Production Crisis (<30 min)
loop-hotfix-emergency
  → incident-response, debugging
  → fallback, retry
  → executor, deploy

### Security Sprint (1 week)
loop-security-sprint
  → audit, security
  → planning, code-review
  → deploy, quality

## DIRECTORY STRUCTURE

~/.hermes/
├── skills/loop/
│   ├── loop-audit/
│   ├── loop-backend/
│   ├── loop-frontend/
│   ├── ... (30 more skills)
│   └── loop-security-sprint/ (meta-skill)
├── scripts/
│   ├── loop-validate.sh
│   ├── loop-run.sh
│   ├── loop-report.sh
│   ├── loop-integration-test.sh
│   ├── loop-workflow-scheduler.sh
│   └── loop-cron-setup.sh
├── logs/
│   └── (automation logs)
├── LOOP_FINAL_REPORT.md
├── LOOP_SKILLS_MAP.md
├── LOOP_UPGRADE_ROADMAP.md
├── LOOP_SKILLS_DEPLOYMENT.md
└── PHASE2_COMPLETION_SUMMARY.md

════════════════════════════════════════════════════════════════
                        NEXT STEPS
════════════════════════════════════════════════════════════════

OPTIONAL Phase 3: Templates
- API endpoint scaffold (TypeScript)
- React component template
- Python test template
- Docker compose config

OPTIONAL Phase 4: Versioning
- Feedback collection (3 months)
- Bug fixes & patches (v1.1)
- Major redesign (v2.0)

OPTIONAL Phase 5: CI/CD Integration
- Wire into GitHub Actions / GitLab CI
- Slack notifications
- Dashboard widget
- Auto-scheduling

════════════════════════════════════════════════════════════════
