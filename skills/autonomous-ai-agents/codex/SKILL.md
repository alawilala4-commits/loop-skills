---
name: codex
description: "Delegate coding to OpenAI Codex CLI. Skill spesialis agent — tidak bagian dari pipeline riset/produksi. Use when user asks to build, fix, refactor, or review code via Codex."
version: 2.0.0
author: Hermes Agent (Lala Alawi rebuild)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Codex, OpenAI, Code-Review, Refactoring, PTY, Automation, CLI]
    related_skills: [claude-code, hermes-agent, test-driven-development, systematic-debugging]
---

# Codex — Coding Agent Execution

## Purpose
Delegate coding to OpenAI Codex CLI. Skill spesialis agent — tidak bagian dari pipeline riset/produksi.

## When to Use
- User asks to build, fix, refactor, or review code via Codex
- Need GPT-4/GPT-5 backend instead of Claude
- Batch PR review
- Parallel worktree execution

## Do
- Use `exec` mode for one-shot tasks
- Use `--full-auto` for build tasks
- Use `--sandbox danger-full-access` on Termux/Android
- Run inside git repository (mandatory)
- Monitor with process(poll/log) in background mode

## Don't
- Run outside git repository (Codex refuses)
- Use `--yolo` on production without review
- Forget bubblewrap fails on Android (use danger-full-access)
- Skip reviewing Codex changes before commit

## Output Format
```
## Codex Task: [DESCRIPTION]

**Mode:** exec | review | interactive
**Status:** SUCCESS | FAIL | PARTIAL

### Result
- Files changed: N
- Tests: X/Y pass

### Next Steps
- [What to do next]
```

## Pipeline Position
Skill spesialis agent. Digunakan via delegate_task dengan role="Codex" di multi-agent-orchestrator.

---

## Three Execution Modes

### Mode 1: One-Shot (`exec`)
```
codex exec "task" --full-auto
```
- Auto-exits when done
- CI/CD friendly

### Mode 2: Interactive REPL
```
codex (pty=true)
```
- Multi-turn conversation
- Requires PTY

### Mode 3: Review
```
codex review --base origin/main
```
- Native PR review
- Batch capable

```
┌──────────────────────────────────────────────────────────────┐
│                    Codex CLI Architecture                     │
├──────────────────────────────────────────────────────────────┤
│  CLI Layer     → codex exec / codex review / codex (REPL)    │
│  Agent Loop    → Read → Reason → Execute → Verify → Repeat   │
│  Sandbox Layer → bubblewrap / user-namespaces / full-access  │
│  Model Layer   → GPT-4o / GPT-5 (via OpenAI API)             │
│  Transport     → Responses API (OpenAI)                      │
└──────────────────────────────────────────────────────────────┘
```

**Key differences dari Claude Code:**
- Codex **harus** di dalam git repository (Claude Code tidak)
- Codex pakai **sandbox** by default (Claude Code pakai permission system)
- Codex support **batch PR review** native
- Codex support **parallel worktree** execution

---

## Prasyarat & Instalasi

### System Requirements
- Node.js >= 18
- Git >= 2.30 (mandatory — Codex refuse run outside git repo)
- RAM minimal 4GB
- Storage: ~300MB untuk install + cache

### Install Codex CLI

```bash
# macOS / Linux / Termux
npm install -g @openai/codex

# Verifikasi
codex --version

# Update ke latest
codex update
```

### Authentication — Pilih Salah Satu

| Metode | Command | Kapan Pakai |
|--------|---------|-------------|
| API Key | `export OPENAI_API_KEY=***` | Pay-as-you-go, paling reliable |
| Codex OAuth | `codex login` | Free tier / ChatGPT Pro subscriber |
| Hermes-managed | `hermes auth add openai-codex` | Kalau pakai Hermes Gateway |

### Post-Install Verification

```bash
# Cek auth status
codex auth status

# Test basic invocation
codex exec "Say hello" --dry-run

# Cek sandbox
codex exec "echo test" --sandbox read-only
```

**Completion criterion:** `codex --version` returns version, `codex auth status` shows authenticated.

---

## Konsep Inti: Agent Loop & Sandbox

### Agent Loop

Codex menjalankan **iterative agent loop**:

```
1. READ    → Baca file yang relevan
2. REASON  → Analisis dan plan action
3. EXECUTE → Jalankan tool (edit file, run command)
4. VERIFY  → Cek hasil (run tests, lint)
5. REPEAT  → Loop sampai task selesai atau max-turns
```

### Sandbox Model

Codex menjalankan setiap task di **isolated sandbox**:

| Sandbox | Isolation | Network | Write |
|---------|-----------|---------|-------|
| `read-only` | bubblewrap | No | No |
| `workspace-write` (default) | bubblewrap | No | Yes, hanya workspace |
| `danger-full-access` | No sandbox | Yes | Yes, full system |

> **IMPORTANT**: Di Termux/Android, `workspace-write` sering gagal karena bubblewrap tidak support user-namespace di Android. Pakai `danger-full-access` sebagai fallback.

---

## Tiga Mode Eksekusi

### Mode 1: One-Shot (`exec`) — RECOMMENDED untuk most tasks

```bash
codex exec "Add dark mode toggle to settings"
```

- Auto-exits when done
- No PTY needed (bisa jalan di background)
- Support `--dry-run` untuk preview

### Mode 2: Interactive REPL

```bash
codex
```

- Full TUI experience
- Multi-turn conversation
- Requires `pty=true` di Hermes

### Mode 3: Review Mode

```bash
codex review --base origin/main
```

- Native PR review
- Output structured review comments
- Bisa batch multiple PRs

### Decision Tree

```
Task single, clear scope?  →  MODE EXEC
Need follow-up questions?  →  MODE REPL (pty=true)
Need PR review?            →  MODE REVIEW
Batch work?                →  MODE EXEC + worktrees
```

---

## One-Shot Tasks — `codex exec`

### Basic Pattern

```bash
codex exec "Add input validation to api/auth.py"
```

### Flag Wajib

| Flag | Fungsi | Default |
|------|--------|---------|
| `--full-auto` | Auto-approve file changes | No |
| `--yolo` | No sandbox, no approvals | No |
| `--sandbox <model>` | Pilih sandbox mode | workspace-write |
| `--dry-run` | Preview tanpa eksekusi | No |

### Auto-Approve Modes

```bash
# Full auto — auto-approve semua file changes (masih sandboxed)
codex exec --full-auto "Refactor auth module"

# YOLO — no sandbox, no approvals (fastest, most dangerous)
codex exec --yolo "Fix all lint errors"

# Default — minta approval untuk setiap change
codex exec "Add new feature"
```

### Dry Run (Preview)

```bash
# Lihat apa yang akan dilakukan tanpa execute
codex exec --dry-run "Refactor database layer"
```

### Scratch Work (Non-Project)

Codex **harus** di dalam git repo. Untuk scratch work:

```bash
cd $(mktemp -d) && git init && codex exec "Build a snake game in Python"
```

### Completion Criterion

- Exit code 0
- File berubah sesuai task
- Tidak ada error di output
- Tests pass (kalau ada test suite)

---

## Interactive Sessions — PTY + Background

### Basic Interactive

```bash
# Di Hermes terminal
terminal(command="codex", workdir="/path/to/project", pty=true)
```

### Background Mode (Long Tasks)

```bash
# Start di background
terminal(command="codex exec --full-auto 'Refactor the auth module'", 
  workdir="/path/to/project", 
  background=true, pty=true
)
# Returns session_id

# Monitor progress
process(action="poll", session_id="<id>")
process(action="log", session_id="<id>")

# Send input kalau Codex tanya
process(action="submit", session_id="<id>", data="yes")

# Kill kalau perlu
process(action="kill", session_id="<id>")
```

### Monitoring Indicators

| Marker | Artinya | Action |
|--------|---------|--------|
| `>` | Codex menunggu input | Kirim prompt baru |
| `...` | Codex sedang proses | Tunggu |
| `✓` | Task selesai | Review output |
| `✗` | Error terjadi | Cek log |

### Completion Criterion

- Session selesai (exit code 0)
- Output sesuai yang diminta
- Session di-kill setelah selesai

---

## Sandbox Models & Security

### Sandbox Comparison

| Model | Use Case | Risk Level |
|-------|----------|------------|
| `read-only` | Review, analysis | Low |
| `workspace-write` | Building features | Medium |
| `danger-full-access` | System-level changes | High |

### Termux/Android Special Case

Di Android/Termux, bubblewrap sering gagal:

```
Error: setting up uid map: Permission denied
Error: loopback: Failed RTM_NEWADDRESS: Operation not permitted
```

**Fix:**
```bash
codex exec --sandbox danger-full-access "task"
```

Atau set default di config:
```bash
echo 'sandbox_mode = "danger-full-access"' >> ~/.codex/config.toml
```

### Security Best Practices

1. **Jangan `--yolo` di production repo** — tanpa review
2. **Pakai `workspace-write` by default** — balance safety/speed
3. **Review changes sebelum commit** — Codex bisa salah
4. **Jangan expose API keys** — sandbox bisa baca env vars
5. **Clean git status sebelum launch** — avoid conflicts

### Completion Criterion

- Sandbox mode sesuai risk level task
- Tidak ada `danger-full-access` untuk task simple
- Changes terverifikasi sebelum commit
- API keys tidak terbuka di output

---

## Batch & Parallel Execution

### Parallel Issue Fixing

```bash
# Create worktrees
git worktree add -b fix/issue-78 /tmp/issue-78 main
git worktree add -b fix/issue-99 /tmp/issue-99 main

# Launch Codex di setiap worktree
terminal(command="codex exec --full-auto 'Fix issue #78: <description>. Commit when done.'", 
  workdir="/tmp/issue-78", background=true, pty=true)
terminal(command="codex exec --full-auto 'Fix issue #99: <description>. Commit when done.'", 
  workdir="/tmp/issue-99", background=true, pty=true)

# Monitor
process(action="list")

# After completion, push dan create PRs
cd /tmp/issue-78 && git push -u origin fix/issue-78
gh pr create --repo user/repo --head fix/issue-78 --title "fix: ..." --body "..."

# Cleanup
git worktree remove /tmp/issue-78
git worktree remove /tmp/issue-99
```

### Batch PR Reviews

```bash
# Fetch semua PR refs
git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'

# Review multiple PRs in parallel
terminal(command="codex exec 'Review PR #86. git diff origin/main...origin/pr/86'", 
  workdir="/project", background=true, pty=true)
terminal(command="codex exec 'Review PR #87. git diff origin/main...origin/pr/87'", 
  workdir="/project", background=true, pty=true)

# Post results
gh pr comment 86 --body "<review>"
gh pr comment 87 --body "<review>"
```

### Completion Criterion

- Semua worktree tasks selesai
- PRs tercreate dengan benar
- Worktree dibersihkan setelah selesai
- Review comments terpost

---

## PR Review Workflow

### Single PR Review

```bash
# Clone ke temp directory
REVIEW=$(mktemp -d) && git clone https://github.com/user/repo.git $REVIEW
cd $REVIEW && gh pr checkout 42

# Run review
codex review --base origin/main
```

### Batch PR Review

```bash
# Fetch all PR refs
git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'

# Review specific PRs
codex exec "Review PR #86. git diff origin/main...origin/pr/86"
codex exec "Review PR #87. git diff origin/main...origin/pr/87"
```

### Review Output Format

Codex review menghasilkan structured output:
- **Bugs**: Logic errors, race conditions
- **Security**: Injection, auth flaws, secrets
- **Style**: Naming, formatting, conventions
- **Tests**: Missing test coverage
- **Performance**: Inefficiencies, N+1 queries

### Completion Criterion

- Review mencakup: bugs, security, style, tests
- Actionable feedback dengan line references
- Review terpost ke PR (kalau diminta)

---

## Worktree Isolation

### Why Worktrees?

Worktrees memberikan **isolasi penuh** untuk parallel tasks:
- Setiap task di branch terpisah
- Tidak ada conflict antar task
- Bisa run simultaneously
- Easy cleanup

### Worktree Lifecycle

```bash
# 1. Create
git worktree add -b feature-x /tmp/feature-x main

# 2. Work
cd /tmp/feature-x && codex exec --full-auto "Implement feature X"

# 3. Push
git push -u origin feature-x

# 4. PR
gh pr create --head feature-x --title "feat: X" --body "..."

# 5. Cleanup
git worktree remove /tmp/feature-x
```

### Completion Criterion

- Worktree terbuat dengan branch benar
- Task selesai di worktree
- Push dan PR berhasil
- Worktree dihapus setelah merge

---

## Error Mapping & Troubleshooting

### Error Types

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `Not a git repository` | Di luar git repo | `git init` atau cd ke repo |
| `Permission denied (bubblewrap)` | Sandbox tidak support | `--sandbox danger-full-access` |
| `Authentication error` | API key invalid | Cek `OPENAI_API_KEY` |
| `Rate limit` | Terlalu banyak request | Tunggu 60s, coba lagi |
| `Context overflow` | File terlalu besar | Split task, gunakan specific paths |
| `Sandbox write denied` | Coba write di luar workspace | Pindah ke workspace atau ganti sandbox |

### Common Issues

| Gejala | Diagnosis | Fix |
|--------|-----------|-----|
| Codex tidak mau start | Bukan git repo | `git init` dulu |
| Bubblewrap error | Android/Termux | `--sandbox danger-full-access` |
| Codex tanya terus | Task terlalu vague | Spesifikkan task + paths |
| Cost naik drastis | Task terlalu besar | Split jadi sub-tasks |
| Changes tidak tersimpan | Sandbox read-only | Ganti ke `workspace-write` |

### Completion Criterion

- Error ter-map ke solusi yang benar
- Session bisa di-recover dari error
- Task selesai setelah retry

---

## Pola Harian—Recipes Siap Pakai

### 1. Quick Fix (One-Shot)

```bash
codex exec "Fix the TypeError in src/api/auth.py line 42"
```

### 2. Feature Development (Background)

```bash
terminal(command="codex exec --full-auto 'Add user profile page with avatar upload'", 
  workdir="/project", background=true, pty=true)
# Monitor dengan process(action="poll", session_id="<id>")
```

### 3. Code Review

```bash
git diff main...feature-branch | codex exec "Review this diff for bugs, security, style"
```

### 4. Batch Issue Fixing (Parallel)

```bash
# Setup worktrees
git worktree add -b fix/78 /tmp/fix-78 main
git worktree add -b fix/99 /tmp/fix-99 main

# Launch parallel
codex exec --full-auto "Fix #78"  # di /tmp/fix-78
codex exec --full-auto "Fix #99"  # di /tmp/fix-99
```

### 5. Full Refactoring

```bash
codex exec --full-auto "Refactor the entire database layer to use connection pooling. Plan first, then implement incrementally."
```

### 6. Security Audit

```bash
codex exec --sandbox read-only "Audit this codebase for security vulnerabilities"
```

### 7. Test Generation

```bash
codex exec --full-auto "Add unit tests for all functions in src/api/auth.py"
```

### Completion Criterion per Recipe

- Quick Fix: File berubah, tests pass
- Feature Dev: Feature berjalan, tidak break existing
- Code Review: Review komprehensif dengan actionable feedback
- Batch Fix: Semua issues terfix, PRs tercreate
- Refactoring: Incremental changes, tests tetap pass
- Security Audit: Report mencakup semua kategori
- Test Generation: Coverage naik, tests pass

---

## Codex vs Claude Code — Kapan Pilih Mana

| Aspek | Codex CLI | Claude Code CLI |
|-------|-----------|-----------------|
| **Model** | GPT-4/GPT-5 (OpenAI) | Claude Sonnet/Opus (Anthropic) |
| **Sandbox** | bubblewrap/user-ns | Permission system |
| **Git requirement** | Mandatory | Optional |
| **Batch PR review** | Native support | Via workarounds |
| **Parallel worktree** | Built-in | Via `-w` flag |
| **MCP support** | Limited | Full MCP |
| **CLAUDE.md** | Tidak ada | Auto-load |
| **Cost** | OpenAI pricing | Anthropic pricing |
| **Termux support** | Perlu `danger-full-access` | Lebih compatible |

### Decision Tree

```
Butuh batch PR review?         →  CODEX
Butuh MCP integration?         →  CLAUDE CODE
Butuh CLAUDE.md context?       →  CLAUDE CODE
Di Termux/Android?             →  CLAUDE CODE (lebih mudah)
Butuh parallel worktrees?      →  CODEX (lebih native)
Budget constraint?             →  Bandingkan pricing
Prefer OpenAI ecosystem?       →  CODEX
Prefer Anthropic ecosystem?    →  CLAUDE CODE
```

### Completion Criterion

- Pilihan agent sesuai task requirements
- Cost dalam budget
- Output quality memenuhi standar

---

## Anti-Patterns & Pitfalls

### 1. Jalankan di Luar Git Repo
**Masalah:** Codex refuse start dengan error "Not a git repository"
**Fix:** `git init` dulu atau cd ke existing repo

### 2. Lupa `--full-auto` untuk Build Tasks
**Masalah:** Codex minta approval untuk setiap file change
**Fix:** Pakai `--full-auto` untuk build/refactor tasks

### 3. Bubblewrap di Android
**Masalah:** `Permission denied` error di Termux
**Fix:** `--sandbox danger-full-access`

### 4. Task Terlalu Vague
**Masalah:** Codex tanya terus atau salah paham
**Fix:** Spesifikkan file paths + expected behavior

### 5. Tidak Review Changes
**Masalah:** Codex bisa salah — terutama untuk complex logic
**Fix:** Review `git diff` sebelum commit

### 6. Parallel Tanpa Worktree
**Masalah:** Conflict antar parallel tasks
**Fix:** Selalu pakai `git worktree` untuk isolation

### 7. Expose API Keys
**Masalah:** Sandbox bisa baca env vars
**Fix:** Pakai `.env` file, jangan hardcode di prompt

### 8. Expect 100% Accuracy
**Masalah:** Model bisa salah — terutama GPT-4o vs Opus
**Fix:** Review output, run tests, jangan blind trust

---

## Verification Checklist

Sebelum menutup session atau memulai task baru:

- [ ] Task output sesuai yang diminta
- [ ] File changes terverifikasi (cek dengan `git diff`)
- [ ] Tests pass (kalau ada test suite)
- [ ] Tidak ada secrets terbuka di output
- [ ] Session di-kill (background mode) atau output disimpan
- [ ] Worktree dibersihkan (kalau pakai parallel)
- [ ] PR tercreate (kalau task selesai)
- [ ] Cost dalam budget

---

## Quick Reference Card

```
INSTALL    → npm install -g @openai/codex
AUTH       → codex login / export OPENAI_API_KEY
VERSION    → codex --version
STATUS     → codex auth status

EXEC MODE  → codex exec "task"
REVIEW MODE→ codex review --base origin/main
REPL MODE  → codex (pty=true)

FLAGS:
  --full-auto              → auto-approve changes
  --yolo                   → no sandbox, no approvals
  --sandbox read-only      → review only
  --sandbox workspace-write→ build (default)
  --sandbox danger-full-access → no isolation
  --dry-run                → preview only

TERMUX FIX → --sandbox danger-full-access
BATCH      → git worktree + parallel exec
REVIEW     → codex review --base origin/main
```

---

Sumber: https://github.com/openai/codex
Rebuild untuk Hermes Agent workflow — 2026-06-28
