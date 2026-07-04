---
name: loop-security-sprint
description: "Meta-skill: Comprehensive security audit and remediation sprint."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, meta-skill, security, audit, compliance, sprint]
    composed_skills: [audit, security, planning, code-review, deploy]
---

# Loop Security Sprint

## Purpose
Dedicated security sprint: audit → identify → fix → verify → deploy with security gate.

## Use When
- Scheduled security audit (quarterly)
- After dependency update with CVEs
- Before major release
- Post-incident security review
- Compliance requirement (PCI, HIPAA, GDPR)

## Workflow Sequence

### Phase 1: Audit (Day 1-2)
1. **loop-audit** — Run comprehensive tools
   - SAST: semgrep, bandit
   - Dependency: pip audit, npm audit
   - Secret: TruffleHog
   - Config: yamllint
   - Output: Severity-prioritized report

2. **loop-security** — Analyze findings
   - Categorize by OWASP Top 10
   - Assess business impact
   - Prioritize: Critical → High → Medium → Low

### Phase 2: Planning (Day 2)
3. **loop-planning** — Create sprint plan
   - Critical: Fix within 24h
   - High: Fix within 1 week
   - Medium: Fix within 2 weeks
   - Low: Fix next sprint

4. **loop-decomposer** — Break into fix tasks
   - Each issue → actionable task
   - Owner assigned
   - Timeline set

### Phase 3: Development (Day 3-7)
5. **loop-executor** — Implement fixes
   - Minimal fix (address specific issue)
   - No unnecessary refactoring
   - Comprehensive testing

### Phase 4: Review & Gate (Day 8)
6. **loop-code-review** — Security-focused review
   - Verify fix addresses root cause
   - Check no new vulnerabilities introduced
   - Verify testing adequate

7. **loop-quality** — Security gate check
   - No high/critical remaining
   - All dependencies patched
   - No secrets exposed
   - Compliance checklist passed

### Phase 5: Deploy (Day 8-9)
8. **loop-deploy** — Deploy with security gate
   - Pre-flight: SAST + dependency scan
   - Staging: Verify fixes work
   - Production: Monitored rollout

## Output
- All critical/high issues fixed
- Compliance checklist passed
- Security report published
- Team trained on improvements

## Timeline
- Audit: 1 day
- Planning: 0.5 day
- Development: 3-5 days
- Review: 1 day
- Deploy: 1 day
- Total: ~1 week

## Issues Severity

### Critical (P1) — Fix within 24h
- Remote code execution (RCE)
- SQL injection
- Authentication bypass
- Data exposure

### High (P2) — Fix within 1 week
- Cross-site scripting (XSS)
- Insecure deserialization
- Hardcoded secrets
- Weak cryptography

### Medium (P3) — Fix within 2 weeks
- Missing input validation
- Weak password policy
- Missing HTTPS
- Outdated dependencies

### Low (P4) — Fix next sprint
- Security headers missing
- Logging insufficient
- Documentation incomplete

## Compliance Checklist

✓ OWASP Top 10: No P1/P2 issues
✓ Dependencies: All up-to-date, no CVE
✓ Secrets: None exposed in code
✓ GDPR: Data minimization, encryption
✓ PCI DSS: If payment processing involved
✓ HIPAA: If healthcare data involved

## Post-Sprint
- Security findings published
- Training for team on common issues
- Update security guidelines
- Plan quarterly audits