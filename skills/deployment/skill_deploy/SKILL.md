---
name: skill_deploy
description: "Deployment atau publikasi hasil ke target (Sheets, DB, server)."
version: 1.0.0
author: user
tags: [deployment, publish, release]
prerequisites: []
---

# Skill Deploy

Deployment atau publikasi hasil ke target environment.

## Trigger

- Review approved
- User minta deploy / "deploy ke production"
- User bilang "deploy", "publish", "release", "upload"

## Output Format

```
## Deploy Report: [Release]

### Target: [staging / production]
### Version: [v1.0.0]
### Timestamp: [ISO timestamp]

### Steps Executed
1. [Step 1] ✓
2. [Step 2] ✓
3. [Step 3] ✓

### Verification
- [ ] Health check passes
- [ ] Smoke test passes
- [ ] Rollback plan ready

### Status: [SUCCESS / FAILED / ROLLED_BACK]
```

## Process

1. **Pre-deploy Check** — confirm review passed, backup ready
2. **Deploy** — execute deployment steps
3. **Verify** — health check, smoke test
4. **Document** — log deployment details
5. **Notify** — inform stakeholders

## Deploy Targets

- **Google Sheets** — update data via API
- **Database** — run migrations / insert data
- **Server/FTP** — upload files
- **GitHub** — push / create release
- **API endpoint** — POST/PUT data

## Constraints

- `requires_production_access: true` — butuh akses ke target
- `environment: ["staging", "production"]` — support staging dan production
- Harus ada rollback plan sebelum deploy
- Never deploy on Friday (unless urgent)

## Integration

- `depends_on: ["skill_review"]` — setelah review approve
- `next_on_success: ["skill_automation_orchestration"]` — jika sukses, bisa automate
- `next_on_failure: []` — jika gagal, rollback dan investigate

## Pitfalls

- Jangan deploy tanpa backup
- Jangan deploy tanpa verification step
- Jangan skip staging test untuk production deploy
- Selalu siapkan rollback plan

## Upgrade Notes

- v1.0.0: basic deploy workflow
- Future: tambah blue-green deploy, canary release, CI/CD pipeline integration
