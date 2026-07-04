---
name: claude-code
description: "Delegate coding to Claude Code CLI. Skill spesialis agent — tidak bagian dari pipeline riset/produksi. Use when user asks to build, fix, refactor, or review code via Claude Code."
version: 3.0.0
author: Hermes Agent (Lala Alawi rebuild)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Claude, Anthropic, Code-Review, Refactoring, PTY, Automation, CLI]
    related_skills: [codex, hermes-agent, test-driven-development, systematic-debugging]
---

# Claude Code — General Agent Execution

## Purpose
Delegate coding to Claude Code CLI. Skill spesialis agent — tidak bagian dari pipeline riset/produksi.

## When to Use
- User asks to build, fix, refactor, or review code via Claude Code
- Multi-turn iterative coding sessions
- Complex multi-file changes
- Need Claude's autonomous coding capabilities

## Do
- Prefer print mode (`-p`) for one-shot tasks
- Use tmux + background=true for interactive/multi-turn
- Always set `--max-turns` in print mode
- Set `--allowedTools` to minimum needed
- Handle workspace trust dialog on first launch
- Use `--dangerously-skip-permissions` with caution
- Monitor cost with `total_cost_usd`

## Don't
- Use interactive mode for one-shot tasks
- Skip `--max-turns` (risk runaway loops)
- Use `--dangerously-skip-permissions` on production without review
- Ignore workspace trust dialog (session will get stuck)
- Forget to cleanup tmux sessions

## Output Format
```
## Claude Code Task: [DESCRIPTION]

**Mode:** Print | Interactive
**Status:** SUCCESS | FAIL | PARTIAL

### Result
- Session ID: [id]
- Turns: N
- Cost: $X.XX
- Time: Xs

### Files Changed
- path/to/file.py — [what changed]

### Next Steps
- [What to do next]
```

## Pipeline Position
Skill spesialis agent. Digunakan via delegate_task dengan role="Claude Code" di multi-agent-orchestrator.

---

## Two Orchestration Modes

### Mode 1: Print (`-p`) — PREFERRED
```
claude -p "task" --max-turns 10 --allowedTools "Read,Edit"
```
- One-shot, auto-exits
- No dialog handling
- JSON output available

### Mode 2: Interactive (tmux)
```
tmux + claude
```
- Multi-turn conversational
- Requires dialog handling
- Real-time monitoring via capture-pane

### Install Claude Code CLI

```bash
# macOS / Linux / Termux
npm install -g @anthropic-ai/claude-code

# Verifikasi
claude --version  # harus v2.x+

# Update ke latest
claude update
```

### Authentication — Pilih Salah Satu

| Metode | Command | Kapan Pakai |
|--------|---------|-------------|
| OAuth (Pro/Max) | `claude auth login` | Punya subscription Claude Pro/Max |
| API Key (pay-as-you-go) | Set `export ANTHROPIC_API_KEY=sk-ant-...` | Ingin bayar per-token |
| Console auth | `claude auth login --console` | Enterprise |
| SSO | `claude auth login --sso` | Team resmi |

### Post-Install Verification

```bash
# Cek auth status
claude auth status          # JSON output
claude auth status --text   # human-readable

# Health check
claude doctor               #cek auto-updater + installation health

# Test basic invocation
claude -p "Say hello" --max-turns 1
```

**Completion criterion:** `claude --version` mengembalikan v2.x+, `claude auth status` menunjukkan "authenticated".

---

## Konsep Inti: Dua Mode Orkestrasi

Claude Code bisa di-orchestrasi lewat Hermes dalam **dua mode fundamental**. Salah pilih mode = session gagal atau boros cost.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Claude Code Orchestration                     │
├──────────────────────────┬──────────────────────────────────────┤
│   MODE 1: Print (-p)     │   MODE 2: Interactive PTY (tmux)     │
├──────────────────────────┼──────────────────────────────────────┤
│ • One-shot task          │ • Multi-turn conversation            │
│ • Auto-exits when done   │ • Persists until /exit               │
│ • No dialog handling     │ • Perlu dialog handling              │
│ • JSON output available  │ • Real-time monitoring via tmux      │
│ • CI/CD friendly         │ • Human-in-the-loop decisions        │
│ • RECOMMENDED for most   │ • For exploratory/complex work       │
└──────────────────────────┴──────────────────────────────────────┘
```

**Decision tree:**
```
Task single, clear scope?  →  MODE PRINT (-p)
Need follow-up questions?  →  MODE INTERACTIVE (tmux)
Need structured JSON?      →  MODE PRINT (-p --output-format json)
Need slash commands?       →  MODE INTERACTIVE
Cost is primary concern?   →  MODE PRINT (avg 40% cheaper)
```

---

## Mode Print (`-p`) — One-Shot Tasks

Flag `-p` menjalankan **single task dan auto-exit**. Ini jalur terbersih untuk automasi dan kebanyakan task coding.

### Basic Pattern

```bash
claude -p "Add input validation to api/auth.py" \
  --allowedTools "Read,Edit" \
  --max-turns 5 \
  --output-format json
```

### Flag Wajib Mode Print

| Flag | Fungsi | Default |
|------|--------|---------|
| `--max-turns N` | Batasi agentic loop | Unlimited (bahaya!) |
| `--allowedTools "Read,Edit"` | Whitelist tools | Semua tools |
| `--output-format json` | Structured output | text |
| `--fallback-model haiku` | Fallback saat overloaded | none |

### Structured JSON Output

```bash
claude -p "List all Python functions in src/" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  --max-turns 5
```

Output JSON memiliki field kritis:
- `session_id` — untuk resume session
- `total_cost_usd` — tracking biaya
- `num_turns` — berapa kali Claude loop
- `subtype` — "success", "error_max_turns", "error_budget"
- `result` — text output dari Claude

### Streaming JSON (Real-time)

```bash
claude -p "Write a README for this project" \
  --output-format stream-json \
  --verbose \
  --include-partial-messages
```

Parse stream events dengan jq:
```bash
claude -p "Explain this" --output-format stream-json --verbose \
  | jq -rj 'select(.type == "stream_event" and .event.delta.type? == "text_delta") | .event.delta.text'
```

### Pipe Input

```bash
# Analisis file tertentu
cat src/main.py | claude -p "Find bugs in this code" --max-turns 1

# Review git diff
git diff HEAD~3 | claude -p "Review these changes" --max-turns 1

# Multiple files
cat src/*.py | claude -p "Find all TODO comments" --max-turns 1
```

### Bare Mode (CI/CD / Scripting)

```bash
claude --bare -p "Run tests" --allowedTools "Read,Bash"
```

`--bare` skip: hooks, plugins, MCP discovery, CLAUDE.md loading, OAuth. Fastest startup — requires API key.

### Completion Criterion

- Claude mengembalikan output `subtype: "success"` atau `result` yang diharapkan
- `total_cost_usd` < budget yang ditentukan
- File terverifikasi berubah sesuai task
- Exit code 0

---

## Mode Interaktif (PTY via tmux) — Multi-Turn Sessions

Mode interaktif memerlukan **tmux sebagai orchestration layer**. Hermes send-keys untuk kirim prompt, capture-pane untuk monitoring.

### Session Lifecycle

```
1. CREATE   → tmux new-session -d -s <name> -x 140 -y 40
2. LAUNCH   → tmux send-keys -t <name> 'cd /path && claude' Enter
3. TRUST    → tmux send-keys -t <name> Enter        (handle dialog)
4. WORK     → tmux send-keys -t <name> 'task prompt' Enter
5. MONITOR  → tmux capture-pane -t <name> -p -S -50
6. FOLLOWUP → tmux send-keys -t <name> 'more changes' Enter
7. EXIT     → tmux send-keys -t <name> '/exit' Enter
8. CLEANUP  → tmux kill-session -t <name>
```

### Launch Template

```bash
# Step 1: Create detached tmux session
tmux new-session -d -s claude-work -x 140 -y 40

# Step 2: Launch Claude Code
tmux send-keys -t claude-work 'cd /path/to/project && claude' Enter

# Step 3: Wait for startup + handle trust dialog (3-5 detik)
sleep 5 && tmux send-keys -t claude-work Enter

# Step 4: Send task
sleep 2 && tmux send-keys -t claude-work 'Refactor auth to use JWT' Enter

# Step 5: Monitor progress
sleep 30 && tmux capture-pane -t claude-work -p -S -60
```

### Monitoring Indicators

Capture output mengandung visual markers:

| Marker | Artinya | Action |
|--------|---------|--------|
| `❯` | Claude menunggu input | Kirim prompt baru atau `/exit` |
| `●` | Claude aktif pakai tools | Tunggu — jangan interrupt |
| `⏵⏵ bypass permissions on` | Permission bypass aktif | OK, lanjut monitoring |
| `◐ medium · /effort` | Current effort level | Ganti dengan Shift+T kalau perlu |
| `ctrl+o to expand` | Output terpotong | Non-blocking |

### Context Window Health

> **CRITICAL**: Di atas **70%** context usage, Claude mulai kehilangan presisi. Di atas **85%**, hallucination risk naik drastis.

Monitoring:
- Ketik `/context` di interactive mode — muncul colored grid
- Kalau > 70% → `/compact` immediately
- Kalau > 85% → `/compact` atau `/clear` (fresh start)

### Completion Criterion

- Semua task items selesai (check `/todos`)
- `tmux capture-pane` menunjukkan `❯` (Claude idle)
- Output/ perubahan terverifikasi
- Session di-kill setelah selesai (kecuali mau resume)

---

## Dialog Handling (CRITICAL)

Claude Code menampilkan **hingga 3 dialog** di startup. Hermes harus handle via tmux send-keys.

### Dialog 1: Workspace Trust

```
  ❯ 1. Yes, I trust this folder     ← DEFAULT (benar — tekan Enter)
    2. No, exit
```

**Handling:**
```bash
sleep 5 && tmux send-keys -t <session> Enter
```

**Muncul sekali per direktori** setelah trust dialog diterima.

### Dialog 2: Permission Bypass Confirmation (hanya dengan `--dangerously-skip-permissions`)

```
    1. No, exit                    ← DEFAULT (salah!)
  ❯ 2. Yes, I accept               ← harus pilih ini
```

**Handling:**
```bash
sleep 3 && tmux send-keys -t <session> Down && sleep 0.3 && tmux send-keys -t <session> Enter
```

**Muncul setiap session** saat pakai `--dangerously-skip-permissions`.

### Dialog 3: First-Run Telemetry Consent

```
  ❯ 1. Yes, help improve Claude Code    ← DEFAULT
    2. No, thanks
```

**Handling:** `tmux send-keys -t <session> Enter` (default OK)

### Robust Dialog Handler Pattern

```bash
# Launch dengan permission bypass
tmux send-keys -t work 'cd /project && claude --dangerously-skip-permissions "task"' Enter

# Handle trust dialog
sleep 4 && tmux send-keys -t work Enter

# Handle permission dialog (Down then Enter)
sleep 3 && tmux send-keys -t work Down && sleep 0.3 && tmux send-keys -t work Enter

# Wait for Claude to start working
sleep 10 && tmux capture-pane -t work -p -S -30
```

### Completion Criterion

- Tidak ada dialog yang "stuck" di capture-pane
- Claude mulai menampilkan tool usage (`●` lines)
- Task prompt terkirim dan di-proses

---

## Session Management & Resumption

### Session Persistence

Session tersimpan di `~/.claude/projects/<project-path-hash>/`. Default TTL: **5 jam**.

### Resume Patterns

```bash
# Resume session terakhir di direktori saat ini
claude -c

# Resume session spesifik by ID
claude -r <session-id>

# Fork session (new ID, keep history)
claude -r <id> --fork-session

# Continue dengan task baru
claude -c "Add tests for the refactored code"
```

### Print Mode Session Continuation

```bash
# Start task, simpan session ID
claude -p "Start refactoring database layer" \
  --output-format json --max-turns 10 > /tmp/session.json

# Resume dengan session ID
SESSION_ID=$(cat /tmp/session.json | python3 -c 'import json,sys; print(json.load(sys.stdin)["session_id"])')
claude -p "Continue and add connection pooling" --resume $SESSION_ID --max-turns 5
```

### Session Cleanup

```bash
# Hapus session files lama (hemat disk)
rm -rf ~/.claude/projects/*/

# Atau biarkan auto-expire (5 jam)
```

### Completion Criterion

- `claude -c` atau `claude -r <id>` berhasil load previous context
- Session history terlihat di awal session
- Task lanjutan bisa merujuk ke pekerjaan sebelumnya

---

## Model Selection, Cost & Performance

### Model Tiers

| Model | Alias | Cost | Best For |
|-------|-------|------|----------|
| Claude Opus 4 | `opus` | $$$$ | Complex multi-step, architecture decisions |
| Claude Sonnet 4 | `sonnet` | $$ | Daily coding, balanced speed/quality |
| Claude Haiku 3.5 | `haiku` | $ | Simple tasks, fast iteration |

### Effort Levels

| Level | Thinking Depth | Use Case |
|-------|----------------|----------|
| `low` | Minimal | Simple edits, formatting |
| `medium` | Standard | Default — most tasks |
| `high` | Deep | Complex refactoring, debugging |
| `max` | Maximum | Architecture decisions, hard bugs |
| `auto` | Claude decides | Let Claude optimize |

### Cost Control Flags

```bash
# Cap total spend
claude -p "task" --max-budget-usd 0.50

# Limit agentic loops
claude -p "task" --max-turns 10

# Fallback model saat overloaded
claude -p "task" --fallback-model haiku

# Effort level
claude -p "task" --effort high
```

### Cost Optimization Rules

1. **`--max-turns` selalu di-set di print mode** — cegah runaway loops
2. **`--max-budget-usd` untuk safety net** — minimum ~$0.05 (system prompt cache)
3. **`haiku` untuk simple tasks** — 5x cheaper dari sonnet
4. **`--bare` untuk CI** — skip plugin overhead
5. **`/compact` di interactive mode** — hemat context window
6. **Pipe input** vs baca file — hemat tokens untuk analisis
7. **Session baru per task berbeda** — context fresh lebih efisien

### Completion Criterion

- `total_cost_usd` dalam result < budget yang ditentukan
- Task selesai dalam `num_turns` yang reasonable (< 15 untuk print mode)
- Tidak ada `error_budget` atau `error_max_turns` di output

---

## Permission & Security

### Permission Modes

| Mode | Flag | Behavior |
|------|------|----------|
| Default | (none) | Confirm setiap tool use |
| Accept Edits | `--permission-mode acceptEdits` | Auto-approve file edits |
| Plan | `--permission-mode plan` | Hanya planning, no execution |
| Auto | `--permission-mode auto` | Auto-approve most tools |
| Bypass | `--dangerously-skip-permissions` | Auto-approve SEMUA tools |

### Tool Whitelist/Blacklist

```bash
# Hanya Read + Edit
claude -p "task" --allowedTools "Read,Edit"

# Semua tools kecuali Bash
claude -p "task" --disallowedTools "Bash"

# Pattern matching
claude -p "task" --allowedTools "Bash(git *)"  # hanya git commands
claude -p "task" --allowedTools "Bash(npm run lint:*)"  # hanya lint scripts
```

### Tool Name Syntax

```
Read                    # Semua file reading
Edit                    # Edit existing files
Write                   # Create new files
Bash                    # Semua shell commands
Bash(git *)             # Hanya git commands
Bash(git commit *)      # Hanya git commit
Bash(npm run lint:*)    # Pattern matching
WebSearch               # Web search
WebFetch                # Web page fetch
mcp__<server>__<tool>   # Specific MCP tool
```

### Security Best Practices

1. **Jangan pakai `--dangerously-skip-permissions` di production repo** — tanpa review
2. **Set `--allowedTools` minimal** — principle of least privilege
3. **Pakai PreToolUse hooks** untuk block dangerous commands
4. **Jangan hardcode secrets** — Claude bisa read .env files
5. **Review changes sebelum commit** — Claude bisa salah

### Completion Criterion

- Tools yang dipakai sesuai whitelist
- Tidak ada `Bash(rm -rf *)` atau `Bash(git push --force)` tanpa review
- File .env tidak terbaca oleh Claude
- Changes terverifikasi sebelum commit

---

## CLAUDE.md — Persistent Project Context

Claude Code auto-load `CLAUDE.md` dari project root. Ini adalah **single source of truth** untuk project context.

### Hierarchy (priority tinggi ke rendah)

1. **Global:** `~/.claude/CLAUDE.md` — berlaku untuk semua project
2. **Project:** `./CLAUDE.md` — project-specific (git-tracked)
3. **Local:** `.claude/CLAUDE.local.md` — personal overrides (gitignored)

### Template CLAUDE.md

```markdown
# Project: Nama Project

## Architecture
- FastAPI backend + SQLAlchemy ORM
- PostgreSQL database, Redis cache
- pytest untuk testing, target 90% coverage

## Key Commands
- `make test` — run full test suite
- `make lint` — ruff + mypy
- `make dev` — start dev server di :8000

## Code Standards
- Type hints di semua public functions
- Docstrings Google style
- 2-space indentation untuk YAML, 4-space untuk Python
- No wildcard imports
- Error messages jangan leak sensitive data

## Project Structure
- `src/api/` — API routes
- `src/models/` — Database models
- `src/services/` — Business logic
- `tests/` — Test files (mirror src structure)
```

### Rules Directory (Modular)

Untuk project besar, jangan cram semua ke satu CLAUDE.md:

```
.claude/
├── CLAUDE.md              # Entry point (short)
└── rules/
    ├── api.md             # API conventions
    ├── testing.md         # Testing standards
    ├── security.md        # Security rules
    └── database.md        # DB conventions
```

Setiap `.md` di `rules/` auto-loaded sebagai additional context.

### Auto-Memory

Claude otomatis menyimpan learned context di `~/.claude/projects/<project>/memory/`:
- Limit: 25KB atau 200 lines per project
- Terpisah dari CLAUDE.md — ini catatan internal Claude
- Survive `/clear` — persist across sessions

### Completion Criterion

- `CLAUDE.md` ada di project root
- Berisi: architecture, key commands, code standards, project structure
- Spesifik (bukan "write good code" tapi "use 2-space indentation")
- Rules directory terpisah untuk project besar

---

## Custom Agents & Subagents

### Agent Locations (priority order)

1. **Project:** `.claude/agents/<name>.md` — team-shared, git-tracked
2. **CLI flag:** `--agents '<json>'` — session-specific, dynamic
3. **User:** `~/.claude/agents/<name>.md` — personal

### Agent File Format

```markdown
# .claude/agents/security-reviewer.md
---
name: security-reviewer
description: Security-focused code review
model: opus
tools: [Read, Bash]
---

You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication/authorization flaws
- Hardcoded secrets
- Unsafe deserialization
- Missing input validation
```

### Invoke Agent

```bash
# Via @ mention di interactive mode
@security-reviewer review the auth module

# Via CLI flag (dynamic)
claude --agents '{"reviewer":{"description":"Reviews code","prompt":"You are a code reviewer focused on performance"}}' \
  -p "Use @reviewer to check auth.py"
```

### Multi-Agent Orchestration

Claude bisa orchestrate multiple agents:
> "Use @db-expert to optimize queries, then @security to audit the changes, then @perf to benchmark."

### Completion Criterion

- Agent file ada di `.claude/agents/` atau `~/.claude/agents/`
- Frontmatter valid (name, description, model, tools)
- Agent bisa di-invoke via @ mention
- Output sesuai specialization agent

---

## MCP Integration

MCP (Model Context Protocol) menambah external tools ke Claude Code.

### Add MCP Server

```bash
# GitHub integration
claude mcp add -s user github -- npx @modelcontextprotocol/server-github

# PostgreSQL queries
claude mcp add -s local postgres -- npx @anthropic-ai/server-postgres \
  --connection-string postgresql://localhost/mydb

# Puppeteer untuk web testing
claude mcp add puppeteer -- npx @anthropic-ai/server-puppeteer
```

### MCP Scopes

| Flag | Scope | Storage |
|------|-------|---------|
| `-s user` | Global (semua project) | `~/.claude.json` |
| `-s local` | Project ini (personal) | `.claude/settings.local.json` (gitignored) |
| `-s project` | Project ini (team-shared) | `.claude/settings.json` (git-tracked) |

### MCP in Print/CI Mode

```bash
claude --bare -p "Query database" --mcp-config mcp-servers.json --strict-mcp-config
```

`--strict-mcp-config` ignore semua MCP config kecuali yang di `--mcp-config`.

### MCP Limits

- Tool descriptions: 2KB cap per server
- Result size: default capped, bisa di-naikkan ke 500K chars via `maxResultSizeChars`
- Output tokens: `export MAX_MCP_OUTPUT_TOKENS=50000`

### Completion Criterion

- `claude mcp list` menunjukkan server terdaftar
- MCP tools muncul di available tools
- Server bisa di-invoke tanpa error

---

## Hooks — Automation pada Events

Hooks menjalankan shell commands pada specific events di Claude Code lifecycle.

### Hook Configuration

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(*.py)",
      "hooks": [{"type": "command", "command": "ruff check --fix $CLAUDE_FILE_PATHS"}]
    }],
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command", "command": "if echo \"$CLAUDE_TOOL_INPUT\" | grep -q 'rm -rf'; then echo 'Blocked!' && exit 2; fi"}]
    }],
    "Stop": [{
      "hooks": [{"type": "command", "command": "echo 'Done' >> /tmp/claude-activity.log"}]
    }]
  }
}
```

### All 8 Hook Types

| Hook | Trigger | Common Use |
|------|---------|------------|
| `UserPromptSubmit` | Sebelum Claude proses prompt | Input validation, logging |
| `PreToolUse` | Sebelum tool dijalankan | Security gates (exit 2 = block) |
| `PostToolUse` | Setelah tool selesai | Auto-format, run linters |
| `Notification` | Permission request / input wait | Desktop notifications |
| `Stop` | Claude selesai response | Completion logging |
| `SubagentStop` | Subagent selesai | Agent orchestration |
| `PreCompact` | Sebelum context di-compress | Backup transcripts |
| `SessionStart` | Session dimulai | Load dev context |

### Hook Environment Variables

| Variable | Content |
|----------|---------|
| `CLAUDE_PROJECT_DIR` | Current project path |
| `CLAUDE_FILE_PATHS` | Files being modified |
| `CLAUDE_TOOL_INPUT` | Tool parameters as JSON |

### Security Hook Example

```json
{
  "PreToolUse": [{
    "matcher": "Bash",
    "hooks": [{"type": "command", "command": "if echo \"$CLAUDE_TOOL_INPUT\" | grep -qE 'rm -rf|git push.*--force|:(){ :|:& };:'; then echo 'Dangerous command blocked!' && exit 2; fi"}]
  }]
}
```

### Completion Criterion

- Hooks terdaftar di `.claude/settings.json` atau `~/.claude/settings.json`
- Exit code 2 di PreToolUse = block command
- PostToolUse hooks jalan otomatis setelah tool use
- Security hooks block dangerous commands

---

## Slash Commands Reference

### Session & Context

| Command | Fungsi |
|---------|--------|
| `/help` | Show all commands |
| `/compact [focus]` | Compress context (CLAUDE.md survives) |
| `/clear` | Wipe conversation history |
| `/context` | Visualize context usage |
| `/cost` | Token usage + cache-hit breakdown |
| `/resume` | Switch/resume different session |
| `/rewind` | Revert to previous checkpoint |
| `/btw <question>` | Side question tanpa cost tambahan |
| `/status` | Version, connectivity, session info |
| `/todos` | List tracked action items |
| `/exit` atau `Ctrl+D` | End session |

### Development & Review

| Command | Fungsi |
|---------|--------|
| `/review` | Code review current changes |
| `/security-review` | Security analysis current changes |
| `/plan [description]` | Enter Plan mode |
| `/loop [interval]` | Schedule recurring tasks |
| `/batch` | Auto-create worktrees untuk parallel changes |

### Configuration & Tools

| Command | Fungsi |
|---------|--------|
| `/model [model]` | Switch model mid-session |
| `/effort [level]` | Set reasoning effort |
| `/init` | Create CLAUDE.md |
| `/memory` | Edit CLAUDE.md |
| `/config` | Interactive settings |
| `/permissions` | View/update tool permissions |
| `/agents` | Manage subagents |
| `/mcp` | Manage MCP servers |
| `/add-dir` | Add working directories |
| `/usage` | Plan limits + rate limit status |
| `/voice` | Push-to-talk voice mode |

### Custom Slash Commands

Buat `.claude/commands/<name>.md` (project) atau `~/.claude/commands/<name>.md` (personal):

```markdown
# .claude/commands/deploy.md
Run deploy pipeline:
1. Run all tests
2. Build Docker image
3. Push to registry
4. Update $ARGUMENTS environment (default: staging)
```

Usage: `/deploy production` — `$ARGUMENTS` auto-replace.

---

## Keyboard Shortcuts

### General Controls

| Key | Action |
|-----|--------|
| `Ctrl+C` | Cancel current input/generation |
| `Ctrl+D` | Exit session |
| `Ctrl+R` | Reverse search command history |
| `Ctrl+B` | Background a running task |
| `Ctrl+V` | Paste image |
| `Ctrl+O` | Transcript mode (see thinking) |
| `Ctrl+G` / `Ctrl+X Ctrl+E` | Open prompt in external editor |
| `Esc Esc` | Rewind conversation/code state |

### Mode Toggles

| Key | Action |
|-----|--------|
| `Shift+Tab` | Cycle permission modes |
| `Alt+P` | Switch model |
| `Alt+T` | Toggle thinking mode |
| `Alt+O` | Toggle Fast Mode |

### Multiline Input

| Key | Action |
|-----|--------|
| `\` + `Enter` | Quick newline |
| `Shift+Enter` | Newline (alt) |
| `Ctrl+J` | Newline (alt) |

### Input Prefixes

| Prefix | Action |
|--------|--------|
| `!` | Execute bash directly (bypass AI) |
| `@` | Reference files/directories |
| `#` | Quick add to CLAUDE.md |
| `/` | Slash commands |

### "ultrathink" Keyword

Kata kunci **"ultrathink"** di prompt = maximum reasoning effort untuk turn tersebut, terlepas dari setting `/effort` saat ini.

---

## Error Mapping & Troubleshooting

### Error Types

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `error_max_turns` | `--max-turns` terlalu kecil | Naikkan `--max-turns` atau simplify task |
| `error_budget` | `--max-budget-usd` terlampaui | Naikkan budget atau simplify task |
| `rate_limit` | API rate limit hit | Tunggu 60s, coba lagi |
| `billing_error` | API key invalid / no credit | Cek `ANTHROPIC_API_KEY` |
| `authentication_error` | OAuth expired | `claude auth login` ulang |
| `context_overflow` | Context window full | `/compact` atau `/clear` |
| `tool_error` | Tool execution failed | Cek tool input/path |

### Common Issues

| Gejala | Diagnosis | Fix |
|--------|-----------|-----|
| Claude stuck di dialog | Trust/permission dialog tidak di-handle | Kirim Enter/Down+Enter via tmux |
| Claude output tidak muncul | Session belum ready | Tambah `sleep` sebelum capture |
| Session tidak bisa resume | TTL expired (5 jam) | Start session baru |
| Claude pakai `python` bukan `python3` | No `python` symlink | Claude self-corrects, atau buat symlink |
| Cost naik drastis | `--max-turns` tidak di-set | Selalu set `--max-turns` di print mode |
| Claude lupa context | Context window > 85% | `/compact` atau `/clear` |

### Completion Criterion

- Error ter-map ke solusi yang benar
- Session bisa di-recover dari error
- Cost tetap dalam budget
- Task selesai setelah retry

---

## Pola Harian—Recipes Siap Pakai

### 1. Quick Fix (Print Mode)

```bash
claude -p "Fix the TypeError in src/api/auth.py line 42" \
  --allowedTools "Read,Edit" \
  --max-turns 3 \
  --output-format json
```

### 2. Feature Development (Interactive + Worktree)

```bash
tmux new-session -d -s feature-x -x 140 -y 40
tmux send-keys -t feature-x 'cd /project && claude -w feature-x' Enter
sleep 5 && tmux send-keys -t feature-x Enter
sleep 2 && tmux send-keys -t feature-x 'Add user profile page with avatar upload' Enter
```

### 3. Code Review (Print Mode)

```bash
git diff main...feature-branch | claude -p \
  "Review this diff for: bugs, security issues, style problems, missing tests. Be thorough." \
  --max-turns 1
```

### 4. PR Review dari Number

```bash
claude -p "Review this PR thoroughly" --from-pr 42 --max-turns 10
```

### 5. Parallel Tasks (3 Simultaneous)

```bash
# Task 1: Backend fix
tmux new-session -d -s t1 && tmux send-keys -t t1 'cd /p && claude -p "Fix auth bug" --allowedTools "Read,Edit" --max-turns 10' Enter

# Task 2: Tests
tmux new-session -d -s t2 && tmux send-keys -t t2 'cd /p && claude -p "Write API tests" --allowedTools "Read,Write,Bash" --max-turns 15' Enter

# Task 3: Docs
tmux new-session -d -s t3 && tmux send-keys -t t3 'cd /p && claude -p "Update README" --allowedTools "Read,Edit" --max-turns 5' Enter

# Monitor all
sleep 30 && for s in t1 t2 t3; do echo "=== $s ==="; tmux capture-pane -t $s -p -S -5; done
```

### 6. Deep Refactoring (Interactive)

```bash
tmux new-session -d -s refactor && tmux send-keys -t refactor 'cd /p && claude' Enter
sleep 5 && tmux send-keys -t refactor Enter
tmux send-keys -t refactor 'Refactor the entire database layer to use connection pooling. Plan first, then implement incrementally.' Enter
```

### 7. Security Audit

```bash
claude -p "Audit this codebase for security vulnerabilities: SQL injection, XSS, hardcoded secrets, unsafe deserialization" \
  --allowedTools "Read" \
  --max-turns 15 \
  --output-format json
```

### Completion Criterion per Recipe

- Quick Fix: File berubah, tests pass
- Feature Dev: Worktree terbuat, feature berjalan
- Code Review: Review output mencakup bugs + security + style
- PR Review: Review komprehensif dengan actionable feedback
- Parallel Tasks: Semua 3 task selesai
- Deep Refactoring: Incremental changes, tests tetap pass
- Security Audit: Report mencakup semua kategori vulnerability

---

## Anti-Patterns & Pitfalls

### 1. Tanpa `--max-turns` di Print Mode
**Masalah:** Runaway loop, cost membengkak
**Fix:** Selalu set `--max-turns 5-15` untuk print mode

### 2. Pakai Interactive Mode untuk Task Single
**Masalah:** Overhead tmux, lebih lambat, lebih mahal
**Fix:** Pakai print mode (`-p`) untuk task one-shot

### 3. Lupa Handle Trust Dialog
**Masalah:** Session stuck di trust dialog
**Fix:** Selalu kirim `Enter` 5 detik setelah launch

### 4. Context Window > 85%
**Masalah:** Claude mulai hallucinate, output tidak reliable
**Fix:** Monitor dengan `/compact`, `/clear` kalau > 85%

### 5. Hardcode Secrets di Prompt
**Masalah:** Secrets tersimpan di session history
**Fix:** Pakai env vars atau `.env` file, reference by name

### 6. Skip Review untuk `--dangerously-skip-permissions`
**Masalah:** Claude bisa hapus/modify file tanpa konfirmasi
**Fix:** Review changes sebelum commit, atau jangan pakai bypass

### 7. Session Accumulation
**Masalah:** Disk penuh dengan session files lama
**Fix:** `rm -rf ~/.claude/projects/*/` secara periodic

### 8. Salah Pilih Model
**Masalah:** Opus untuk simple task = boros; Haiku untuk complex = gagal
**Fix:** Sonnet default, Haiku untuk simple, Opus untuk architecture

### 9. Tidak Pakai CLAUDE.md
**Masalah:** Claude tidak tahu project conventions
**Fix:** Buat CLAUDE.md minimal dengan architecture + commands + standards

### 10. Expect 100% Accuracy
**Masalah:** Claude bisa salah — terutama di context > 70%
**Fix:** Review output, run tests, jangan blind trust

---

## Verification Checklist

Sebelum menutup session atau memulai task baru:

- [ ] Task output sesuai yang diminta
- [ ] `total_cost_usd` dalam budget
- [ ] File changes terverifikasi (cek dengan `git diff`)
- [ ] Tests pass (kalau ada test suite)
- [ ] Tidak ada secrets terbuka di output
- [ ] Session di-kill (interactive mode) atau output disimpan (print mode)
- [ ] CLAUDE.md terupdate kalau ada conventions baru
- [ ] tmux sessions dibersihkan

---

## Environment Variables Reference

| Variable | Effect |
|----------|--------|
| `ANTHROPIC_API_KEY` | API key auth (alternative to OAuth) |
| `CLAUDE_CODE_EFFORT_LEVEL` | Default effort: low/medium/high/max/auto |
| `MAX_THINKING_TOKENS` | Cap thinking tokens (0 = disable) |
| `MAX_MCP_OUTPUT_TOKENS` | Cap MCP server output |
| `CLAUDE_CODE_NO_FLICKER=1` | Alt-screen rendering (no flicker) |
| `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` | Strip credentials from sub-processes |

---

## Quick Reference Card

```
INSTALL    → npm install -g @anthropic-ai/claude-code
AUTH       → claude auth login
VERSION    → claude --version
HEALTH     → claude doctor
UPDATE     → claude update

PRINT MODE → claude -p "task" --max-turns 10 --output-format json
INTERACTIVE→ tmux + claude (see Mode Interactive section)
RESUME     → claude -c / claude -r <id>
REVIEW     → git diff | claude -p "review" --max-turns 1
MCP ADD    → claude mcp add -s user <name> -- <cmd>
STATUS     → claude auth status
```

---

Sumber: https://code.claude.com/docs/en/cli-reference
Rebuild untuk Hermes Agent workflow — 2026-06-28
