---
name: skill_automation_orchestration
description: "Mengubah proses yang sudah stabil menjadi workflow otomatis (mis. n8n, CLI)."
version: 1.0.0
author: user
tags: [automation, orchestration, n8n, cron, workflow]
prerequisites: []
---

# Skill Automation Orchestration

Mengubah proses yang sudah stabil menjadi workflow otomatis.

## Trigger

- Deploy berhasil, user mau automate
- User bilang "automatiskan", "jadwalkan", "setiap hari/minggu"
- Proses berjalan manual yang sudah stabil dan perlu di-automate

## Output Format

```
## Automation: [Process Name]

### Platform: [n8n / bash / cron]
### Schedule: [cron expression / trigger type]

### Workflow
1. Trigger → [apa yang trigger]
2. Step 1 → [aksi]
3. Step 2 → [aksi]
4. Output → [hasil]

### Monitoring
- Health check: [cara monitor]
- Alert: [jika gagal, notify ke mana]

### Status: [ACTIVE / PAUSED / DISABLED]
```

## Process

1. **Identify** — identifikasi proses yang sudah stabil dan repeatable
2. **Design** — rancang workflow (trigger → steps → output)
3. **Implement** — buat automation script/workflow
4. **Test** — jalankan manual untuk verify
5. **Schedule** — set up cron atau n8n trigger
6. **Monitor** — set up health check dan alerting

## Platforms

### n8n
- Visual workflow editor
- Good untuk: API integrations, multi-step webhooks
- Trigger: schedule, webhook, event

### Bash + Cron
- Simple, reliable
- Good untuk: file processing, backups, reports
- Trigger: cron schedule

### Hermes Cronjob
- Integrated dengan Hermes Agent
- Good untuk: agent-driven workflows, data collection
- Trigger: schedule, context-based

## Constraints

- `allowed_platforms: ["n8n", "bash", "cron"]`
- Harus ada error handling
- Harus ada logging
- Harus bisa di-pause/disable

## Integration

- `depends_on: ["skill_deploy"]` — setelah deploy stabil
- `next_on_success: []` — terminal stage
- `next_on_failure: []` — jika gagal, simplify atau manual fallback

## Pitfalls

- Jangan automate proses yang belum stabil
- Jangan skip error handling
- Jangan lupa monitoring — "set and forget" berbahaya
- Selalu test dengan dry-run dulu

## Upgrade Notes

- v1.0.0: basic automation setup
- Future: tambah monitoring dashboard, alerting integration, auto-retry logic
