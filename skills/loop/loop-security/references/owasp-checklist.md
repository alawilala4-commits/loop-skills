# OWASP Top 10 Security Checklist

## A1: Broken Access Control
- [ ] Authorization checks on every endpoint (not just frontend)
- [ ] No hardcoded role checks — use permission model
- [ ] CORS properly configured (no wildcard * unless internal)
- [ ] API key rotation implemented
- [ ] Token expiry enforced

## A2: Cryptographic Failures
- [ ] Sensitive data encrypted at rest (DB, cache, backup)
- [ ] HTTPS/TLS enforced (HSTS header set)
- [ ] No hardcoded secrets in code/config
- [ ] Password hashing: bcrypt/argon2 (not MD5/SHA1)
- [ ] API keys >= 32 characters, random

## A3: Injection (SQL, NoSQL, Command, Template)
- [ ] SQL: Use parameterized queries, no string concatenation
- [ ] NoSQL: Validate & sanitize input before query
- [ ] Command: Avoid shell execution, use library API
- [ ] Template: Auto-escape output (Jinja2, ERB, etc)
- [ ] Validate input: whitelist, type check, length limit

## A4: Insecure Design
- [ ] Threat model documented (common attack vectors)
- [ ] Security requirements in spec (not afterthought)
- [ ] Rate limiting implemented (prevent brute force)
- [ ] Account lockout after N failed login
- [ ] Session timeout configured

## A5: Security Misconfiguration
- [ ] Dev/test database not accessible from prod
- [ ] Debug mode disabled in production
- [ ] Default credentials changed
- [ ] Error messages don't expose implementation details
- [ ] Security headers set (CSP, X-Frame-Options, etc)

## A6: Vulnerable & Outdated Components
- [ ] Dependencies scanned for CVE (pip audit, npm audit)
- [ ] Patch applied within 30 days of release
- [ ] No end-of-life libraries used
- [ ] Dependency lock file in version control
- [ ] Unused dependencies removed

## A7: Authentication Failures
- [ ] Password policy: min 12 chars, complexity required
- [ ] MFA available for critical accounts
- [ ] Session management: secure cookie flags (HttpOnly, Secure, SameSite)
- [ ] Failed login attempts logged & monitored
- [ ] Password reset link expires in 15 min

## A8: Software & Data Integrity Failures
- [ ] CI/CD pipeline security hardened (no unauthorized changes)
- [ ] Software signed or checksummed
- [ ] Deployment package verified before install
- [ ] Database backups encrypted & tested
- [ ] Change log maintained

## A9: Logging & Monitoring Failures
- [ ] Successful/failed auth logged with timestamp
- [ ] Access logs include: user, action, resource, result
- [ ] No PII/password in logs
- [ ] Logs forwarded to centralized system
- [ ] Alert on repeated failed login / unusual activity

## A10: SSRF (Server-Side Request Forgery)
- [ ] Don't fetch user-provided URLs without validation
- [ ] Whitelist allowed domains
- [ ] Firewall rules block internal network access from app
- [ ] Validate IP range (no 127.0.0.1, 10.0.0.0/8, etc)

## Tools to Run
- SAST: semgrep, bandit, SonarQube
- Dependency: pip audit, npm audit, Snyk
- DAST: OWASP ZAP, Burp Suite (paid)
- Container: Trivy (scan Docker images)

## Compliance Notes
- GDPR: Data minimization, encryption, access control
- PCI DSS: No raw card data, encrypted transmission
- HIPAA: Audit logs, encryption, role-based access
