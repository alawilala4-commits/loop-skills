# Security Audit Tools & Configuration

## Static Analysis (SAST)

### Semgrep (OSS)
```bash
# Install
pip install semgrep

# Run
semgrep --config=p/owasp-top-ten src/

# Common checks
semgrep --config=p/python src/
semgrep --config=p/security-audit src/
```

### Bandit (Python)
```bash
# Install
pip install bandit

# Run
bandit -r src/

# Ignore specific issue
bandit -r src/ -s B101  # Ignore assert_used
```

### SonarQube (Enterprise)
Self-hosted scanner for code quality + security

## Dependency Scanning

### NPM Audit
```bash
# Check vulnerabilities
npm audit

# Fix automatically
npm audit fix

# Fix with breaking changes
npm audit fix --force
```

### Pip Audit (Python)
```bash
# Install
pip install pip-audit

# Scan
pip-audit

# Generate report
pip-audit --format json > audit.json
```

### Snyk (Commercial)
```bash
# Install
npm install -g snyk

# Authenticate
snyk auth

# Test
snyk test
```

## Secret Scanning

### Git-Secrets
```bash
# Install
git clone https://github.com/awslabs/git-secrets.git
cd git-secrets && make install

# Setup patterns
git secrets --register-aws --global

# Scan
git secrets --scan
```

### TruffleHog (OSS)
```bash
# Install
pip install truffleHog

# Scan
truffleHog filesystem /path/to/repo
truffleHog github --repo https://github.com/user/repo
```

## Container Scanning

### Trivy (OSS)
```bash
# Install
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh

# Scan image
trivy image my-app:latest

# Scan filesystem
trivy fs /path/to/app
```

## Audit Report Template

```
# Security Audit Report
Date: 2026-07-04
Scope: All Python code in src/

## Summary
- Total issues: 15
- Critical: 0
- High: 2
- Medium: 5
- Low: 8

## Critical Issues
None

## High Issues
1. SQL Injection in user_service.py:45
   - Recommendation: Use parameterized query
   - Severity: HIGH
   - Status: To fix

2. Hardcoded secret in config.py:12
   - Recommendation: Move to .env
   - Severity: HIGH
   - Status: To fix

## Remediation Timeline
- Critical: Fix within 24h
- High: Fix within 1 week
- Medium: Fix within 2 weeks
- Low: Fix next sprint

## Compliance
- OWASP Top 10: 2 issues found (A1, A2)
- PCI DSS: Pass (no card data exposed)
- GDPR: Pass (no unencrypted PII)
```
