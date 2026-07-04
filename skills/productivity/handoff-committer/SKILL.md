---
name: handoff-committer
description: "Serah-terima final untuk pipeline produksi. Package result, summarize, prepare clean handoff to user. Terminal stage of multi-agent-orchestrator produksi pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [handoff, completion, summary, packaging, delivery, output]
    related_skills: [builder-drafter, quality-linter, github-pr-workflow]
---

# Handoff-Committer — Final Packaging Protocol

## Purpose
Serah-terima final untuk pipeline produksi. Package result, summarize, prepare clean handoff to user.

## When to Use
- User completes any task, workflow, or multi-agent pipeline
- After quality-linter passes, ready to deliver
- Need clean summary of what was done

## Do
- Present final result concise and usable
- Include only information needed for handoff
- Mention unresolved risks, caveats, next actions clearly
- Say directly if ready, or state exactly what remains
- Keep handoff neat, final, easy to copy or execute

## Don't
- Include internal process details (tool calls, debug logs)
- Skip risk disclosure
- Leave user unclear on next steps
- Mark DONE when tests fail

## Output Format
```
## ✅ TASK COMPLETE

**What was done:**
[2-3 sentences]

**Files changed:**
- `path/to/file.py` — [what changed]

**Verification:**
- Tests: X/Y pass
- Lint: PASS
- Review: PASS

**Commit:** `abc123f`

**Next steps:**
- [What user should do next]

---

## ⚠️ PARTIAL (if applicable)
**Completed:** [what's done]
**Remaining:** [what's left]
**To complete:** [commands to finish]
```

## Pipeline Position
Terminal stage of multi-agent-orchestrator produksi pipeline.

---

## Core Rules

1. **Present the final result in a concise, usable form.**
2. **Include only the information needed for the handoff.**
3. **Mention any unresolved risk, caveat, or next action clearly.**
4. **If the result is ready, say so directly.**
5. **If the result is partial, state exactly what remains.**
6. **Keep the handoff neat, final, and easy to copy or execute.**

---

## Daftar Isi

1. [Handoff Dimensions](#handoff-dimensions)
2. [Result Classification](#result-classification)
3. [Handoff Structure](#handoff-structure)
4. [Git Commit Protocol](#git-commit-protocol)
5. [Handoff Output Format](#handoff-output-format)
6. [Partial Result Handling](#partial-result-handling)
7. [Risk & Caveat Disclosure](#risk--caveat-disclosure)
8. [Handoff Recipes](#handoff-recipes)
9. [Pitfalls](#pitfalls)

---

## Handoff Dimensions

### What to Include

| Dimension | Content |
|-----------|---------|
| **Result** | What was produced (files, code, document) |
| **Status** | DONE / PARTIAL / BLOCKED |
| **Summary** | 2-3 sentences max |
| **Evidence** | Test results, verification, screenshots |
| **Risks** | Unresolved issues, caveats |
| **Next Steps** | What user should do next |

### What to Exclude

- Internal process details (user doesn't care what tool was used)
- Debug logs or intermediate steps
- Duplicate information
- Unverified claims (should be filtered earlier by quality-linter)

---

## Result Classification

### Status Definitions

| Status | Meaning | Handoff Style |
|--------|---------|---------------|
| **DONE** | Complete and verified | Clean delivery |
| **PARTIAL** | Some items incomplete | State what's done + what remains |
| **BLOCKED** | Cannot proceed | State blocker + unblock options |
| **FAILED** | Did not achieve goal | State why + recovery options |

### Completion Checklist

```
Before handoff, verify:
☐ Result matches original goal
☐ Quality-linter passed (no FAIL items)
☐ All files in expected locations
☐ Tests pass (if applicable)
☐ References valid (no broken links)
� Uncertainties clearly marked
☐ Git state clean (if applicable)
```

---

## Handoff Structure

### Standard Handoff Template

```
## ✅ TASK COMPLETE

**What was done:**
[2-3 sentences]

**Files changed:**
- `path/to/file.py` — [what changed]
- `path/to/file2.py` — [what changed]

**Verification:**
- Tests: X/Y pass
- Lint: PASS
- Review: PASS (if applicable)

**Commit:** `abc123f` (if git)

**Next steps:**
- [What user should do next, if anything]

---

## PARTIAL / BLOCKED (if applicable)
[If not DONE, explain what remains]
```

### Minimal Handoff (for simple tasks)

```
## ✅ Done

[One sentence result]

File: `path/to/file.py`
Tests: PASS (X/Y)
```

### Detailed Handoff (for complex workflows)

```
## ✅ WORKFLOW COMPLETE

### Summary
[Paragraph describing what was achieved]

### Pipeline Results
| Stage | Status | Evidence |
|-------|--------|----------|
| Design | ✅ | Design doc created |
| Code | ✅ | 3 files, 450 lines |
| Tests | ✅ | 60/60 pass |
| Review | ✅ | PASS, 0 findings |
| Merge | ✅ | PR #42 merged |

### Artifacts
| Artifact | Path/Location |
|----------|---------------|
| Source code | `src/module.py` |
| Tests | `tests/test_module.py` |
| Documentation | `README.md` |
| PR | https://github.com/org/repo/pull/42 |

### Verification
```bash
# Run tests
python -m unittest discover tests/ -v

# Check lint
ruff check src/

# Verify commit
git log --oneline -3
```

### Risks & Caveats
- [Any unresolved issue]
- [Any assumption that needs confirmation]
- [Any TODO marker remaining]

### Next Steps
1. [Action item 1]
2. [Action item 2]

---

## GIT STATUS
```
On branch main
nothing to commit, working tree clean
```
```

---

## Git Commit Protocol

### Pre-Commit Verification

```bash
# 1. Check status
git status

# 2. Review diff
git diff

# 3. Run tests
python -m unittest discover tests/ -q

# 4. Run lint
ruff check .

# 5. Verify no secrets
grep -r "API_KEY\|PASSWORD\|TOKEN" --include="*.py" .
```

### Commit Message Format

```
<type>(<scope>): <short description>

<optional body: explain WHAT and WHY>
```

### Commit Types

| Type | When |
|------|------|
| `feat` | New feature added |
| `fix` | Bug fixed |
| `refactor` | Code restructured |
| `docs` | Documentation updated |
| `test` | Tests added/updated |
| `chore` | Maintenance, tooling |
| `ci` | CI/CD changes |

### Post-Commit Handoff

```bash
# Verify commit exists
git log --oneline -1

# Push if remote exists
git push origin main

# Create tag for releases
git tag -a v1.0.0 -m "Release v1.0.0"
```

---

## Handoff Output Format

### Format by Content Type

| Output Type | Handoff Style |
|-------------|---------------|
| **Code file** | Path + test result + lint result |
| **Document** | Path + sections list + word count |
| **PR** | URL + CI status + review status |
| **Report** | Key findings (max 5) + full report path |
| **Pipeline** | Stage-by-stage table + artifacts |
| **Research** | Verdict + strongest sources + gaps |

### Format by Audience

| Audience | Style |
|----------|-------|
| **Developer** | Technical details, file paths, test results |
| **Manager** | Summary, timeline, blockers, next steps |
| **Client** | What was delivered, how to use it |
| **Downstream agent** | Structured data, exact paths, verification commands |

---

## Partial Result Handling

### What Counts as Partial

- Some tests pass, some fail
- Code works but docs incomplete
- Design complete but implementation pending
- Tests pass but lint fails

### Partial Handoff Format

```
## ⚠️ PARTIAL

**Completed:**
- [X was done]
- [Y was done]

**Remaining:**
- [Z still needs to do]
- [W blocked by blocker]

**To complete:**
[Commands or steps to finish]

**Current state:**
[Where things stand — what works, what doesn't]
```

### Blocked Handoff Format

```
## � BLOCKED

**Goal:** [What was being attempted]

**Blocker:** [What prevents completion]

**Unblock options:**
1. [Option 1 — what user needs to do]
2. [Option 2 — alternative approach]

**Partial output:**
[What was achieved before getting blocked]
```

---

## Risk & Caveat Disclosure

### Risk Classification

| Level | Type | Disclosure |
|-------|------|------------|
| 🔴 High | Could break production | MUST disclose |
| � Medium | Could affect reliability | Should disclose |
| � Low | Minor, acceptable | May omit |
| � Info | FYI only | Optional |

### Caveat Types

| Caveat | Template |
|--------|----------|
| Unverified claim | `[VERIFY]` — Source needed |
| Assumption | `[ASSUMPTION]` — Confirm with user |
| Time-sensitive | `[TIME]` — May be outdated |
| Platform-specific | `[PLATFORM]` — Tested on X only |
| Incomplete coverage | `[PARTIAL]` — X% tested |

### Risk Disclosure Format

```
### Risks
- � [Risk]: [Mitigation]
- 🔴 [Risk]: [Action needed from user]
- ⚪ [Info]: [Context]
```

---

## Handoff Recipes

### Recipe 1: Feature Complete

```
## ✅ Feature: [NAME]

**Files:**
- `src/feature.py` — implementation
- `tests/test_feature.py` — 25 tests, all pass

**Verification:**
```bash
python -m unittest tests/test_feature.py -v
ruff check src/feature.py
```

**Commit:** `abc123f`

**Ready to use:** Yes
```

### Recipe 2: Bug Fix Complete

```
## ✅ Bug Fix: [DESCRIPTION]

**Root cause:** [What caused it]
**Fix:** [What changed]
**Regression test:** `tests/test_x.py::test_y`

**Verification:**
```bash
python -m unittest tests/test_x.py -v  # PASS
```

**Tests:** 45/45 pass ✅
```

### Recipe 3: Research Complete

```
## ✅ Research: [TOPIC]

**Verdict:** STRONG | MODERATE | WEAK

**Key findings:**
1. [Fact — Tier 1 source]
2. [Fact — Tier 2 source]

**Sources:** 5 verified (3 Tier 1, 2 Tier 3)
**Full report:** `research/topic-report.md`

**Gaps:** [What we couldn't verify]
```

### Recipe 4: PR Ready

```
## ✅ PR Ready: [TITLE]

**Branch:** `feat/x`
**PR:** [URL] (created if ready)

**Status:**
- Tests: PASS (60/60)
- Lint: PASS
- Review: PASS

**CI:** � All checks pass

**To merge:**
```bash
gh pr merge --squash --delete-branch
```
```

### Recipe 5: Multi-Agent Pipeline Complete

```
## ✅ Pipeline: [GOAL]

| Stage | Agent | Status |
|-------|-------|--------|
| Design | Architect | ✅ |
| Code | Coder | ✅ |
| Test | Tester | ✅ |
| Review | Reviewer | ✅ |
| Docs | Documenter | ✅ |
| Deploy | Deployer | ✅ |

**Final artifacts:**
- `src/` — 5 files
- `tests/` — 45 tests
- `README.md` — updated
- PR #42 — merged

**Total time:** 23 minutes
**Issues found:** 1 (fixed during Test stage)
```

---

## Pitfalls

### 1. Including Unnecessary Detail
**Masalah:** Handoff includes internal tool calls, debug output
**Fix:** Include only what user needs to proceed

### 2. Missing Risk Disclosure
**Masalah:** Output looks perfect but has hidden caveats
**Fix:** Always check for unverified claims, assumptions, gaps

### 3. Vague Next Steps
**Masalah:** "Review the code" tanpa specify what to review
**Fix:** Specific action: "Run `python -m unittest tests/test_x.py -v`"

### 4. Partial Without Explanation
**Masalah:** User doesn't know what's incomplete
**Fix:** Explicit checklist: completed + remaining + to-complete

### 5. Wrong Status
**Masalah:** Marking DONE when tests fail
**Fix:** Honest status — PARTIAL is better than false DONE

### 6. No Verification Command
**Masalah:** User can't verify the result independently
**Fix:** Always include exact command to verify

### 7. Duplicate Information
**Masalah:** Same content in handoff + files + commit message
**Fix:** Handoff references files, doesn't duplicate content

---

## Quick Reference Card

```
STATUS:
  ✅ DONE     → Complete and verified
  ⚠️ PARTIAL  → Some items incomplete
  � BLOCKED  → Cannot proceed
  ❌ FAILED   → Did not achieve goal

HANDOFF MUST INCLUDE:
  - What was done (concise)
  - Where the output is
  - How to verify (command)
  - What remains (if partial)
  - Risks (if any)

HANDOFF FORMAT:
  Status → Summary → Files → Verify → Risks → Next Steps

GIT:
  ☐ Tests pass
  ☐ No secrets leaked
  � Commit message conventional
  � Push if remote exists
```

---

Sumber: Hermes Agent handoff workflow pattern
Created — 2026-06-28
