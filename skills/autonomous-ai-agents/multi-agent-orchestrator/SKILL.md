---
name: multi-agent-orchestrator
description: "Root supervisor for all multi-agent workflows. Orchestrates scout→search→verify→judge→draft→lint→handoff pipeline. Use when task benefits from staged execution, specialist delegation, or validation gates."
version: 3.0.0
author: Hermes Agent (Lala Alawi rebuild)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [orchestration, multi-agent, supervisor, pipeline, root, delegation]
    related_skills: [scout, search-engineering, research-verifier, judge, builder-drafter, quality-linter, handoff-committer, claude-code, codex, test-driven-development, systematic-debugging, github-pr-workflow]
---

# Multi-Agent Orchestrator — Root Supervisor

## Purpose
Root supervisor for all multi-agent workflows. Orchestrates scout→search→verify→judge→draft→lint→handoff pipeline.

## When to Use
- Task kompleks dengan multiple independent components
- Butuh staged execution dengan validation gates
- User explicitly bilang "orchestrator", "multi-agent", "delegate"
- Task benefit dari separation of concerns
- Ada pekerjaan yang bisa di-parallel

## Do
- Break goals into smallest useful work units
- Delegate to specialist roles — don't do all work yourself
- Prefer parallel work when tasks don't depend on each other
- Assign each step to the most appropriate role
- Track dependencies, blockers, and completion status
- Ask minimum clarifying question when ambiguous
- Provide concise final handoff when complete

## Don't
- Do all work yourself when specialist can do better
- Skip validation gates
- Retry blindly without specific feedback
- Over-orchestrate simple tasks (1-2 steps = kerjakan sendiri)
- Under-orchestrate complex tasks
- Ignore dependencies between steps
- Leave tmux sessions or temp files uncleaned

## Output Format
```
## WORKFLOW: [GOAL]

### Plan
| Step | Role | Status | Depends On |
|------|------|--------|------------|
| 1    | Scout| done   | —          |
| 2    | Search| done  | 1          |

### Result
- Status: DONE | PARTIAL | BLOCKED
- Files: [list]
- Tests: X/Y pass

### Next Steps
- [Action items]

### Blockers
- [Any blocking issues]
```

## Pipeline Position
ROOT SUPERVISOR — mengawasi seluruh pipeline (intel, produksi, engineering, agents).

---

## Two Sub-Pipelines

### Pipeline Intel (Research Flow)
```
scout → search-engineering → research-verifier → judge
```

### Pipeline Produksi (Output Flow)
```
builder-drafter → quality-linter → handoff-committer
```

---

## Hierarchy

```
multi-agent-orchestrator (ROOT SUPERVISOR)
│
├── PIPELINE INTEL (Research Flow)
│   ├── scout — Discovery awal
│   ├── search-engineering — Pencarian terfokus
│   ├── research-verifier — Validasi + konflik
│   └── judge — Keputusan + routing
│
├── PIPELINE PRODUKSI (Output Flow)
│   ├── builder-drafter — Susun draf
│   ├── quality-linter — Periksa kualitas
│   └── handoff-committer — Serah-terima final
│
└── SKILL SPESIALIS (Domain-Specific)
    ├── test-driven-development — TDD workflow
    ├── systematic-debugging — Debug 4-fase
    ├── github-pr-workflow — PR lifecycle
    ├── claude-code — Claude Code CLI agent
    └── codex — Codex CLI agent
```

---

## Core Rules

1. **Do not do all the work yourself** — delegate to specialist roles.
2. **Decompose complex goals** into clear, independent steps.
3. **Prefer parallel work** when tasks do not depend on each other.
4. **Assign each step** to the most appropriate role.
5. **Track dependencies, blockers, and completion status**.
6. **If ambiguous**, ask the minimum necessary clarifying question.
7. **If complete**, provide a concise final handoff.
8. **Keep the plan practical, short, and executable**.

---

## Pipeline Intel (Research Flow)

Gunakan pipeline ini untuk task riset/investigasi:

```
1. SCOUT     → Cari sinyal baru (broad discovery)
2. SEARCH    → Pencarian sumber terfokus
3. VERIFY    → Validasi + deteksi konflik
4. JUDGE     → Keputusan: accept/reject/defer
```

Setiap skill punya file sendiri — load sesuai kebutuhan:
- `scout` — Discovery protocol
- `search-engineering` — Query construction
- `research-verifier` — Evidence validation
- `judge` — Scoring + routing

---

## Pipeline Produksi (Output Flow)

Gunakan pipeline ini untuk task produksi output:

```
1. DRAFT     → Susun draf dari verified inputs
2. LINT      → Periksa kualitas (correctness, format, edge cases)
3. HANDOFF   → Package + serah-terima final
```

Setiap skill punya file sendiri:
- `builder-drafter` — Document production
- `quality-linter` — Output inspection
- `handoff-committer` — Final packaging

---

## Specialist Roles (Task Execution)

| Role | Responsibility | Toolsets | When to Use |
|------|---------------|----------|-------------|
| **Architect** | System design, API contracts | `["terminal", "file"]` | Perlu design dulu |
| **Coder** | Write code, implement features | `["terminal", "file"]` | Produksi code |
| **Tester** | Run tests, verify coverage | `["terminal"]` | Verifikasi code |
| **Reviewer** | Code quality, security | `["file"]` | Quality assurance |
| **Documenter** | Write docs, README | `["file"]` | Dokumentasi |
| **Deployer** | Git push, CI monitor | `["terminal"]` | Deployment ops |
| **Auditor** | Full audit (code+tests+git) | `["terminal", "file"]` | Final validation |

---

## Workflow Sequence

### Standard Pipeline (Full Research → Production)

```
1. Orchestrator receives task
2. → SCOUT (discovery)
3. ← Scout returns findings
4. → SEARCH (focused queries)
5. ← Search returns sources
6. → VERIFY (validation)
7. ← Verifier returns validated evidence
8. → JUDGE (decision)
9. ← Judge returns accepted/rejected + routing
10. → DRAFT (build output)
11. ← Drafter returns draft
12. → LINT (quality check)
13. ← Linter returns PASS/WARN/FAIL
14. → HANDOFF (final package)
15. ← Committer returns final result
16. Orchestrator reports to user
```

### Coding Pipeline (Feature/Bugfix)

```
1. Orchestrator receives task
2. → Architect (design, if needed)
3. → Coder (implement with TDD)
4. → Tester (run tests)
5. If FAIL → back to Coder (max 3 retries)
6. → Reviewer (code review)
7. → Documenter (update docs)
8. → Deployer (commit + push)
9. → Auditor (final check)
10. Orchestrator reports to user
```

### Parallel Pipeline

```
1. Orchestrator receives task
2. → Architect (design)
3. ← Architect returns spec
4. Orchestrator dispatches parallel:
   ├── → Coder A (feature X) ─┐
   ├── → Coder B (feature Y) ─┤ PARALLEL
   └── → Coder C (feature Z) ─┘
5. Wait for all Coders
6. → Tester (run all tests)
7. → Reviewer + Documenter (parallel)
8. → Deployer
9. Orchestrator reports to user
```

---

## Handoff Format

Setiap `delegate_task` call MENGHARUSKAN field ini di `context`:

```yaml
- goal: "apa yang harus dicapai (one sentence)"
- role: "Coder/Tester/Reviewer/Scout/Judge/dll"
- context: "konteks minimum yang dibutuhkan"
- constraints: "batasan (Python 3.13, no pytest, exactly N tests)"
- expected_output: "output yang harus dikembalikan agen"
- status: "status saat ini"
- acceptance_criteria: "kriteria spesifik yang harus dipenuhi"
- dependencies: "apa yang harus selesai dulu"
- previous_output: "output dari step sebelumnya"
```

---

## Dependency Tracking

```yaml
steps:
  - id: "1"
    role: "Scout"
    status: "completed"
    output: "5 findings discovered"
    
  - id: "2"
    role: "Search"
    status: "completed"
    depends_on: ["1"]
    output: "10 sources found"
    
  - id: "3"
    role: "Verify"
    status: "completed"
    depends_on: ["2"]
    output: "7 sources validated"
    
  - id: "4"
    role: "Judge"
    status: "completed"
    depends_on: ["3"]
    output: "5 accepted, 2 rejected"
    
  - id: "5"
    role: "Drafter"
    status: "in_progress"
    depends_on: ["4"]
    
  - id: "6"
    role: "Linter"
    status: "blocked"
    depends_on: ["5"]
    
  - id: "7"
    role: "Handoff"
    status: "blocked"
    depends_on: ["6"]
```

---

## Validation Gates

| Gate | From → To | Check |
|------|-----------|-------|
| Gate 1 | Scout → Search | Findings relevant? Not noise? |
| Gate 2 | Search → Verify | Sources authoritative? Current? |
| Gate 3 | Verify → Judge | Evidence sufficient? No contradictions? |
| Gate 4 | Judge → Draft | Accepted items clear? |
| Gate 5 | Draft → Linter | Draft complete? All inputs verified? |
| Gate 6 | Linter → Handoff | No FAIL items? |
| Gate 7 | Handoff → User | Result matches goal? |

---

## Retry Loop Rules

| Stage | Max Retry | On Retry Fail |
|-------|-----------|---------------|
| Coder → Tester | 3 | Escalate to user |
| Tester → Coder (fix) | 3 | Escalate to user |
| Reviewer → Coder (fix) | 2 | Escalate to user |
| Any intel stage | 2 | Skip that branch |

---

## Ambiguity Resolution

| Ambiguity | Clarifying Question |
|-----------|-------------------|
| Scope unclear | "Apakah ini untuk fitur X saja, atau termasuk Y?" |
| Tech stack unclear | "Python 3.13 + unittest, atau pytest?" |
| Bahasa output | "Doc dalam Bahasa Indonesia atau English?" |
| Git strategy | "Langsung commit ke main, atau buat branch?" |

---

## Anti-Patterns & Pitfalls

1. **Doing all work yourself** — Always delegate to specialist roles
2. **Skipping validation gates** — Always verify before handoff
3. **Retrying blindly** — Include specific feedback in retry
4. **Context loss between agents** — Include all necessary context
5. **Over-orchestrating simple tasks** — Simple = kerjakan sendiri
6. **Under-orchestrating complex tasks** — Complex = decompose + delegate
7. **Ignoring dependencies** — Track and respect order
8. **Not cleaning up** — Always cleanup after workflow
9. **Forgetting documentation** — Always end with Documenter
10. **Not escalating after max retries** — Max retries → escalate to user

---

## Verification Checklist

- [ ] Goal dipecah menjadi smallest useful work units
- [ ] Setiap step punya role assignment yang tepat
- [ ] Pipeline intel diikuti (scout→search→verify→judge) jika riset
- [ ] Pipeline produksi diikuti (draft→lint→handoff) jika output
- [ ] Dependencies teridentifikasi dan respected
- [ ] Parallel opportunities dimanfaatkan
- [ ] Validation gates dilewati sebelum handoff
- [ ] Retry loop diikuti (max 3 per stage)
- [ ] Context lengkap di-setiap handoff
- [ ] Acceptance criteria terpenuhi
- [ ] Final handoff diberikan ke user
- [ ] Cleanup dilakukan

---

## Quick Reference Card

```
HIERARCHY:
  multi-agent-orchestrator (ROOT)
  ├── INTEL: scout → search → verify → judge
  ├── PRODUKSI: draft → lint → handoff
  └── SPESIALIS: TDD, debugging, PR, claude-code, codex

PIPELINES:
  Research   → Scout → Search → Verify → Judge → Draft → Lint → Handoff
  Coding     → Architect → Coder → Tester → Reviewer → Doc → Deploy
  Quick Fix  → Coder → Tester → Deployer
  Parallel   → Architect → [Coder-X, Coder-Y] → Tester

ROLES:
  Architect, Coder, Tester, Reviewer, Documenter, Deployer, Auditor

RETRIES:
  Max 3 per stage
  Always include specific feedback
  Escalate to user after max
```

---

Sumber: Hermes Agent multi-agent workflow pattern
Rebuild v3.0.0 — 2026-06-28
