---
name: loop-security
description: "Cek keamanan: vulnerability, secret exposure, auth, injection, compliance."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, security, vulnerability, OWASP, compliance]
---

# Loop Security

## Purpose
Cek keamanan: vulnerability, secret exposure, auth, injection, compliance.

## Use When
- Sebelum production deploy.
- Saat ada perubahan auth/input handling.
- Saat dependency update.
- Regular security audit (monthly/quarterly).

## Steps
1. Run SAST (static analysis): semgrep, bandit.
2. Check dependency: pip audit, npm audit, cargo audit.
3. Check secrets: scan untuk API key, password, token.
4. Check auth: JWT validation, session management, CORS.
5. Check injection: SQL, XSS, command injection.
6. Check data flow: encryption in transit & at rest.
7. Review compliance: GDPR, HIPAA, PCI jika applicable.

## Output
- Security issues list (Critical/High/Medium/Low).
- Dependency vulnerabilities & patch availability.
- Secret exposure incidents.
- Compliance status.

## Pitfalls
- Jangan ignore low severity issues — bisa chain attack.
- Jangan deploy dengan known vulnerability.
- Jangan hardcode secret di code.
- Jangan skip dependency update.

## Verification
- No Critical/High security issue.
- Dependencies up-to-date.
- No secret exposed.
- Compliance checklist passed.