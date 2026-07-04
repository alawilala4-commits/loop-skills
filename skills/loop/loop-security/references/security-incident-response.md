# Security Incident Response Checklist

## Upon Discovering Security Issue

### IMMEDIATE (First 15 minutes)

- [ ] **Identify severity level**
  - P1 (Critical): Active exploit, data breach, RCE
  - P2 (High): Security vulnerability, weak auth
  - P3 (Medium): Policy violation, config issue
  - P4 (Low): Security hardening, documentation

- [ ] **Isolate affected systems**
  - Take affected service offline if P1
  - Enable read-only mode if possible
  - Block known attack vectors

- [ ] **Notify team**
  - Page security lead
  - Notify management (P1 only)
  - Create incident ticket

### SHORT TERM (Next 1 hour)

- [ ] **Investigate root cause**
  - Check logs (access, error, auth)
  - Identify entry point
  - Determine scope of exposure

- [ ] **Collect evidence**
  - Screenshots of logs
  - Database backups
  - Network captures
  - Save all forensic data

- [ ] **Contain the issue**
  - Reset compromised credentials
  - Revoke API keys
  - Update firewall rules
  - Deploy security patches

### MEDIUM TERM (Next 24 hours)

- [ ] **Assess damage**
  - What data was exposed?
  - How many users affected?
  - Business impact analysis

- [ ] **Notify affected parties**
  - Send user notification email
  - Update status page
  - Prepare PR statement (if public)

- [ ] **Deploy permanent fix**
  - Patch vulnerable code
  - Add security controls
  - Review similar systems

### LONG TERM (Next week)

- [ ] **Post-incident review**
  - Root cause analysis
  - Timeline reconstruction
  - Preventive measures

- [ ] **Improve processes**
  - Add monitoring alerts
  - Update documentation
  - Training for team

- [ ] **Report & follow-up**
  - Executive summary
  - Recommendations
  - Schedule follow-ups

## Detection Rules

### Watch for:
- Unusual login activity (IPs, times)
- Database access patterns
- API rate limiting triggers
- Memory/CPU spikes
- Unusual outbound traffic
- Error rate increases
