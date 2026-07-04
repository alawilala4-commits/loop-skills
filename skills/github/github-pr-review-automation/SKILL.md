---
name: github-pr-review-automation
description: "Automated PR review pipeline — analyze diff, verify risks, judge severity, lint review, post comment. Triggered on pull_request events."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [github, PR, review, automation, pilot, code-review]
    related_skills: [github-pr-workflow, research-verifier, judge, quality-linter, handoff-committer, multi-agent-orchestrator]
---

# PILOT — GitHub PR Review Automation

## Purpose
Jalankan review otomatis untuk setiap PR baru atau update PR, lalu berikan komentar ringkas, terstruktur, dan aman.

## When to Use
- `pull_request.opened` — PR baru dibuat
- `pull_request.synchronize` — PR diupdate (commit baru)
- `pull_request.reopened` — PR dibuka kembali

## Allowed Skills
- `multi-agent-orchestrator` — Routing + koordinasi
- `research-verifier` — Analisis diff + risiko
- `judge` — Severity + detail level
- `quality-linter` — Review kualitas komentar
- `handoff-committer` — Final packaging + posting
- `claude-code` — Deep code analysis (optional)
- `codex` — Alternative analysis (optional)

## Do
- Baca PR diff secara lengkap
- Analisis perubahan kode untuk risiko dan pola janggal
- Beri komentar yang jelas, singkat, dan actionable
- Putuskan severity: low, medium, high
- Post komentar sebagai review (bukan merge)

## Don't
- Merge PR
- Auto-fix kode
- Mengubah file repo
- Beri komentar redundant atau terlalu panjang
- Review di luar scope PR

## Output Format
```text
Verdict: low | medium | high

Findings:
- ...
- ...

Notes:
- ...

Suggested next action:
- ...
```

## Pipeline Position
GitHub automation pipeline. Triggered by PR events. Coordinated by multi-agent-orchestrator.

---

## Expected Flow

### Stage 1: multi-agent-orchestrator
```
Input: PR event (opened/synchronize/reopened)
Action: Terima event, routing ke skill review
Output: PR metadata + diff
```

### Stage 2: research-verifier
```
Input: PR diff
Action: Periksa isi diff, cari risiko/konflik/pola janggal
Output: Findings + risk assessment
```

### Stage 3: judge
```
Input: Findings dari verifier
Action: Putuskan severity (low/medium/high)
         Tentukan komentar umum vs detail
Output: Severity + review strategy
```

### Stage 4: quality-linter
```
Input: Draft review
Action: Cek kejelasan, singkat, non-redundant
         Pastikan actionable
Output: Lint-clean review
```

### Stage 5: handoff-committer
```
Input: Final review
Action: Package + post ke PR
Output: Posted review comment
```

---

## Severity Criteria

| Level | Criteria | Action |
|-------|----------|--------|
| **low** | Minor style, naming, atau dokumentasi | Komentar singkat |
| **medium** | Logic issue, missing test, edge case | Komentar detail + suggestion |
| **high** | Security, breaking change, data loss risk | Komentar detail + block merge |

## Review Checklist

- [ ] Code logic correct?
- [ ] Tests cover changes?
- [ ] No security vulnerabilities?
- [ ] No breaking changes undocumented?
- [ ] Naming conventions followed?
- [ ] No hardcoded secrets?
- [ ] Error handling present?
- [ ] Documentation updated?

## Trigger Events

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
```

## Integration

```bash
# Manual trigger for testing
gh pr diff <NUMBER> | pilot-review

# Post review
gh pr review <NUMBER> --body "review content"
```

---

Sumber: Hermes Agent GitHub automation pattern
Created — 2026-06-28
