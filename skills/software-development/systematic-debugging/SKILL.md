---
name: systematic-debugging
description: "4-phase root cause debugging. Skill spesialis untuk coding pipeline — tidak bagian dari intel/produksi pipeline. Use when investigating test failures, unexpected behavior, or production bugs."
version: 2.0.0
author: Hermes Agent (Lala Alawi rebuild)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, troubleshooting, problem-solving, root-cause, investigation]
    related_skills: [test-driven-development, claude-code, codex, python-cli-app]
---

# Systematic Debugging — 4-Phase Root Cause Analysis

## Purpose
Root-cause analysis workflow. Skill spesialis untuk coding pipeline — tidak bagian dari intel/produksi pipeline.

## When to Use
- Test failures
- Unexpected behavior
- Production bugs
- Build failures
- Performance problems
- Under time pressure (emergencies make guessing tempting)

## Do
- Read error messages carefully — they often contain the solution
- Build a tight feedback loop (fast, deterministic, specific)
- Check recent changes (git diff, recent commits)
- Trace data flow to find source, not symptom
- Form 3-5 ranked hypotheses before testing
- Fix root cause, not symptom
- Create regression test after fix

## Don't
- Guess and check randomly
- Fix without understanding root cause
- Apply multiple fixes at once
- Skip test after fix
- Retry more than 3 times without questioning architecture
- Name files after stdlib modules

## Output Format
```
## Debug: [ISSUE]

### Phase 1: Root Cause
- Error: [message]
- Location: file.py:42
- Recent changes: [git diff summary]

### Phase 2: Pattern
- Working example: [similar code that works]
- Difference: [what's different]

### Phase 3: Hypothesis
1. [Hypothesis A] — Testing: [method]
2. [Hypothesis B] — Testing: [method]

### Phase 4: Fix
- Root cause: [what was wrong]
- Fix applied: [what changed]
- Regression test: tests/test_x.py::test_y
- Status: PASS (X/Y tests)
```

## Pipeline Position
Skill spesialis untuk coding pipeline. Digunakan oleh Coder/Tester role di multi-agent-orchestrator.

---

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

**Tiga pilar debugging:**
1. **Evidence** — Data-driven investigation, bukan tebakan
2. **Reproduction** — Bug harus bisa di-reproduce sebelum fix
3. **Verification** — Fix harus di-test dan terbukti bekerja

**The Feedback Loop:**
```
 reproduce → identify → fix → verify → repeat
     ↑                                    └──────┘
     └────────────────────────────────────────────┘
```

Fokus utama: **buat loop yang TIGHT** — cepat, deterministik, dan specific ke bug yang dihadapi.

---

## Kapan Menggunakan Proses Ini

### SELALUA gunakan proses ini:
- Test failures (unit, integration, e2e)
- Bugs di production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues
- CI failures

### TERUTAMA ketika:
- Ada time pressure (emergency membuat guessing menarik)
- "Satu quick fix sepertinya obvious"
- Sudah coba multiple fixes
- Fix sebelumnya tidak work
- Tidak fully understand the issue

### JANGAN skip ketika:
- Issue sepertinya simple (simple bugs tetap punya root cause)
- Kamu rushed (rushing guarantees rework)
- Someone wants it fixed NOW (systematic lebih cepat dari thrashing)

---

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

Jika kamu belum selesai Fase 1, kamu TIDAK BOLEH propose fixes.

---

## Fase 1: Root Cause Investigation

**Sebelum attempt APAPUN fix:**

### 1. Baca Error Message dengan Teliti

- Jangan skip errors atau warnings
- Sering kali error message contains the exact solution
- Baca stack traces secara lengkap
- Note: line numbers, file paths, error codes

**Tools:**
```bash
# Read source file
read_file path="src/problematic.py" offset=40 limit=20

# Search error string di codebase
search_files pattern="ErrorType" path="src/" file_glob="*.py"
```

### 2. Buat Tight Feedback Loop

Loop harus:
- **Fast** — bisa run berulang kali dalam detik
- **Deterministic** — selalu reproduce bug yang sama
- **Specific** — assert exact symptom, bukan generic failure
- **Automated** — could be run by agent tanpa human input

**Jenis loop (prioritas order):**

| # | Jenis | Kapan Pakai |
|---|-------|-------------|
| 1 | Failing test | Bug berada di function yang di-test |
| 2 | HTTP script/curl | Bug di API endpoint |
| 3 | CLI invocation | Bug di CLI argument handling |
| 4 | Headless browser script | Bug di UI behavior |
| 5 | Replay captured trace | Bug di network/request flow |
| 6 | Throwaway harness | Bug butuh minimal setup |
| 7 | Property/fuzz loop | Bug intermittent di broad input |
| 8 | Bisection harness | Bug muncul antara dua known states |
| 9 | Differential loop | Bug muncul saat compare two configs |
| 10 | Human-in-loop script | Last resort — automate human steps |

### 3. Tighten the Loop

Setelah loop ada:
- **Faster** — cache setup, narrow scope, skip unrelated init
- **Sharper signal** — assert exact symptom, bukan generic success
- **More deterministic** — pin time, seed randomness, isolate filesystem

**Untuk non-deterministic bugs:** Goal = higher reproduction rate, bukan perfection. 50% flake = debuggable. 1% flake = usually not.

### 4. Cek Perubahan Terbaru

```bash
# Recent commits
git log --oneline -10

# Uncommitted changes
git diff

# Changes in specific file
git log -p --follow src/problematic_file.py | head -100

# What changed in last session?
git diff HEAD~5 --stat
```

### 5. Gather Evidence di Multi-Component Systems

Ketika sistem punya multiple components (API → service → database):

**Sebelum propose fixes, add diagnostic instrumentation:**
- Log data yang MASUK component
- Log data yang KELUAR component
- Verify environment/config propagation
- Check state di setiap layer

**Run sekali** untuk gather evidence showing WHERE it breaks.
**ANALYZE** evidence untuk identify failing component.
**INVESTIGATE** component tersebut.

### 6. Trace Data Flow

Ketika error deep di call stack:
- Di mana bad value berasal?
- Siapa yang panggil function ini dengan bad value?
- Trace upstream sampai ketemu sumbernya
- **Fix at the source, bukan at the symptom**

**Tools:**
```python
# Find where function is called
search_files("function_name(", path="src/", file_glob="*.py")

# Find where variable is set
search_files(r"variable_name\s*=", path="src/", file_glob="*.py")
```

### Phase 1 Completion Checklist

- [ ] Error messages fully read dan dipahami
- [ ] Tight loop command exists dan sudah di-run minimal sekali
- [ ] Loop is red-capable: asserts exact symptom, bukan nearby failure
- [ ] Loop is deterministic, atau flaky bug punya reproduction rate tinggi
- [ ] Recent changes teridentifikasi dan direview
- [ ] Evidence gathered (logs, state, data flow)
- [ ] Problem terisolasi ke specific component/code
- [ ] Root cause hypotheses bisa stated dan tested

**STOP:** Jangan proceed ke Fase 2 sampai kamu understand WHY itu terjadi.

---

## Fase 2: Pattern Analysis

**Cari pattern sebelum fix:**

### 0. Minimize Reproduction

Setelah loop red, shrink repro ke smallest scenario yang masih red. Cut inputs, callers, config, data, steps **satu per satu**, re-running loop setelah each cut.

**Selesai ketika:** Removing any remaining element makes loop go green = minimal repro narrows hypothesis space dan sering menjadi cleanest regression test.

### 1. Find Working Examples

- Locate similar working code di same codebase
- Apa yang WORK yang similar dengan apa yang BROKEN?

```python
search_files("similar_working_pattern", path="src/", file_glob="*.py")
```

### 2. Compare Against References

- Kalau implement pattern, baca reference implementation secara LENGKAP
- Jangan skim — baca setiap line
- Understand pattern fully sebelum apply

### 3. Identify Differences

- Apa yang berbeda antara working dan broken?
- List setiap difference, sekecil apapun
- Jangan asumsi "that can't matter"

### 4. Understand Dependencies

- Component lain apa yang dibutuhkan?
- Settings, config, environment apa?
- Assumptions apa yang dibuat code?

### Phase 2 Completion Checklist

- [ ] Minimal reproduction exists
- [ ] Working examples found
- [ ] Differences between working/broken identified
- [ ] Dependencies understood
- [ ] Hypothesis could be formed

---

## Fase 3: Hypothesis dan Testing

**Scientific method:**

### 1. Form Ranked Falsifiable Hypotheses

- Generate **3-5 plausible hypotheses** sebelum test single one
- Rank by likelihood dan cheapness to falsify
- State prediction each hypothesis makes: "Jika X adalah cause, maka changing/observing Y harus membuat Z happen"
- Discard atau sharpen hypothesis yang tidak buat testable prediction

**Jika user hadir:** Show ranked list sebelum testing. Mereka mungkin punya domain knowledge yang instantly re-rank.
**Jika user AFK:** Proceed dengan ranking.

### 2. Test Minimally

- Test highest-ranked hypothesis dengan smallest possible probe
- Change **one variable at a time**
- Jangan fix multiple things sekaligus
- Prefer debugger/REPL inspection — one breakpoint beats ten logs
- Jika add logs, tag every temporary line dengan unique prefix: `[DEBUG-a4f2]`

### 3. Verify Before Continuing

- **Work?** → Fase 4
- **Tidak work?** → Form NEW hypothesis
- **Jangan** add more fixes on top

### 4. Ketika Kamu Tidak Tahu

- Katakan "Saya tidak understand X"
- Jangan pura-pura tanya
- Ask user untuk help
- Research lebih

### Phase 3 Completion Checklist

- [ ] 3-5 hypotheses formed
- [ ] Hypotheses ranked by likelihood
- [ ] Top hypothesis tested
- [ ] Result verified (confirmed atau disproven)
- [ ] New hypothesis formed (jika perlu)

---

## Fase 4: Implementation

**Fix root cause, BUKAN symptom:**

### 1. Create Failing Test Case

- Simplest possible reproduction
- Automated test jika mungkin
- **HARUS** ada sebelum fixing
- Gunakan `test-driven-development` skill

### 2. Implement Single Fix

- Address root cause yang di-identify
- **SATU change at a time**
- No "while I'm here" improvements
- No bundled refactoring

### 3. Verify Fix

```bash
# Run specific regression test
python -m unittest tests/test_module.py::TestModule.test_regression -v

# Run full suite — no regressions
python -m unittest discover tests/ -q
```

### 4. Jika Fix Tidak Work — The Rule of Three

- **STOP.**
- Count: Sudah berapa kali fix dicoba?
- Jika < 3: Return ke Fase 1, re-analyze dengan new information
- **Jika ≥ 3: STOP dan question architecture (step 5)**
- **JANGAN** attempt Fix #4 tanpa architectural discussion

### 5. Jika 3+ Fixes Gagal: Question Architecture

**Pattern indicating architectural problem:**
- Setiap fix reveals new shared state/coupling di tempat berbeda
- Fixes require "massive refactoring" untuk implement
- Setiap fix creates new symptoms elsewhere

**STOP dan question fundamentals:**
- Apakah pattern ini fundamentally sound?
- Apakah kita "sticking with it through sheer inertia"?
- Haruskah refactor architecture vs continue fixing symptoms?

**Diskusikan dengan user sebelum attempt lebih fixes.**

BUKAN failed hypothesis — ini adalah wrong architecture.

### Phase 4 Completion Checklist

- [ ] Failing test case created
- [ ] Single fix implemented
- [ ] Regression test passes
- [ ] All tests pass (no regressions)
- [ ] 3+ fixes questioned architecture (jika applicable)

---

## The Rule of Three

```
Fix attempt 1 → Gagal → Re-analyze → Fix attempt 2 → Gagal → Re-analyze → Fix attempt 3 → Gagal → STOP → Question Architecture
```

| Attempts | Action |
|----------|--------|
| 1-2 | Re-analyze dari Fase 1, coba pendekatan berbeda |
| 3+ | Question ARCHITECTURE, diskusikan dengan user |

**JANGAN attempt Fix #4 tanpa diskusi architectural.**

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process cepat untuk simple bugs. |
| "Emergency, no time for process" | Systematic debugging LEBIH CEPAT dari guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right dari awal. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first membuktikan fix. |
| "Multiple fixes at once saves time" | Tidak bisa isolate apa yang work. Creates new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Baca lengkap. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question pattern, jangan fix lagi. |

---

## Python-Specific Pitfalls

### 1. stdlib module name collision

**Symptom:** stdlib imports fail dengan `AttributeError` atau `ImportError` di tempat tidak terduga.

**Contoh:** File `calendar.py` menyebabkan `datetime.strptime()` crash dengan `AttributeError: module 'calendar' has no attribute 'day_abbr'` karena `datetime.strptime` internally import stdlib `calendar`, tapi menemukan project `calendar.py` kamu.

**Rule:** Jangan pernah nama file project sama dengan***@`. Gunakan prefix: `cal.py`, `myjson.py`, `app_os.py`.

**Quick check:** Kalau filename match dengan https://docs.python.org/3/library/ — rename it.

### 2. Mutable Default Arguments

**Symptom:** Function "remember" state antar calls.

**Wrong:**
```python
def add_item(item, items=[]):  # Mutable default!
    items.append(item)
    return items
```

**Right:**
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 3. Late Binding Closures

**Symptom:** All lambda/callback pakai value terakhir.

**Wrong:**
```python
functions = [lambda: i for i in range(3)]
# All return 2!
```

**Right:**
```python
functions = [lambda i=i: i for i in range(3)]
# Returns 0, 1, 2
```

### 4. is vs ==

**Symptom:** Comparison gagal untuk value yang sepertinya sama.

```python
# "is" checks identity (same object)
# "==" checks value equality

x = 256
y = 256
x is y  # True (cached)

x = 257
y = 257
x is y  # False (not cached)
x == y  # True
```

**Rule:** Selalu pakai `==` untuk value comparison.

### 5. Chained Comparison Trap

```python
# Wrong: Ini selalu True!
if 1 < x < 10:  # OK

# Wrong: Ini yang salah
flag = x == True  # Only True for x=1, bukan x=2, x=3
flag = bool(x)    # Correct
```

---

## Hermes Integration

### Investigation Tools di Hermes

| Tool | Kapan Pakai |
|------|-------------|
| `search_files` | Find error strings, trace function calls, locate patterns |
| `read_file` | Read source code dengan line numbers untuk precise analysis |
| `terminal` | Run tests, check git history, reproduce bugs |
| `web_search` | Research error messages, library docs |

### Debugging + delegate_task

Untuk complex multi-component debugging, dispatch investigation subagents:

```python
delegate_task(
    goal="Investigate why [specific test/behavior] fails",
    context="""
    Follow systematic-debugging skill:
    1. Read the error message carefully
    2. Reproduce the issue
    3. Trace the data flow to find root cause
    4. Report findings — do NOT fix yet

    Error: [paste full error]
    File: [path to failing code]
    Test command: [exact command]
    """,
    toolsets=['terminal', 'file']
)
```

### Debugging + TDD

Ketika fixing bugs:
1. Write test yang reproduce bug (RED)
2. Debug systematically untuk find root cause
3. Fix root cause (GREEN)
4. Test membuktikan fix dan prevent regression

**Jangan fix bugs tanpa test.**

---

## Error Mapping & Troubleshooting

### Common Python Errors

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `SyntaxError` | Invalid Python syntax | Cek indentation, brackets, colons |
| `IndentationError` | Mixed tabs/spaces | Convert all ke 4-space indent |
| `NameError` | Variable tidak defined | Cek scope, import, typo |
| `TypeError` | Operation di wrong type | Cek type, convert jika perlu |
| `ValueError` | Value tidak valid | Cek input, validasi |
| `KeyError` | Dictionary key tidak ada | Pakai `.get()` atau check key exists |
| `IndexError` | List index out of range | Cek length, guard dengan if |
| `AttributeError` | Object tidak punya attribute | Cek type, method name |
| `ImportError` | Module tidak ditemukan | Cek path, install dependency |
| `FileNotFoundError` | File tidak ditemukan | Cek path, buat file jika perlu |
| `JSONDecodeError` | JSON invalid/kosong | Cek isi file, handle empty/corrupt |
| `AssertionError` | Test assertion failed | Cek expected vs actual |
| `RecursionError` | Infinite recursion | Cek base case, stack depth |
| `UnboundLocalError` | Variable referenced before assignment | Init variable di function scope |

### Common Test Failures

| Failure | Penyebab | Solusi |
|---------|----------|--------|
| `AssertionError: X != Y` | Expected value salah | Cek test, fix expected |
| `ModuleNotFoundError` | File shadowing stdlib | Rename file |
| `FileNotFoundError` | Setup tidak buat file | Fix setUp() correcly |
| `JSONDecodeError` | File empty/corrupt | Fix test data preparation |
| `AttributeError: NoneType` | Function return None | Cek return value |

### Debug Workflow

```
Error terjadi
    │
    ▼
Baca error message lengkap
    │
    ▼
Identify file + line number
    │
    ▼
Read code di lokasi error
    │
    ▼
Identify root cause (Fase 1)
    │
    ▼
Form hypothesis (Fase 3)
    │
    ▼
Test hypothesis (isolate variable)
    │
    ▼
Implement fix (SATU change)
    │
    ▼
Verify fix (test pass + no regressions)
    │
    ▼
Commit + document
```

---

## Pola Harian—Recipes Siap Pakai

### 1. Test Failure Debug (5-15 menit)

```bash
# 1. Run failing test dengan verbose
python -m unittest tests/test_module.py -v

# 2. Baca error message dengan teliti
# 3. Read file di line yang error
# 4. Trace data flow ke atas
# 5. Identify root cause
# 6. Implement SATU fix
# 7. Verify test passes + no regressions
```

### 2. CLI App Bug (10-20 menit)

```bash
# 1. Reproduce bug dengan CLI command
python app.py command_that_fails

# 2. Identify error type (ValueError? TypeError? Crash?)
# 3. Read source di function yang error
# 4. Check input validation
# 5. Check JSON file state
# 6. Fix root cause
# 7. Test both success dan error paths
```

### 3. CI Failure (15-30 menit)

```bash
# 1. Run CI checks locally
python -m unittest discover tests/ -v

# 2. Check lint
# 3. Check type hints
# 4. Read CI logs jika unavailable locally
# 5. Fix specific failure
# 6. Re-run until all pass
```

### 4. Production Bug (30-60 menit)

```bash
# 1. Gather logs + error reports
# 2. Reproduce di local/dev
# 3. Write failing test that reproduces bug
# 4. Debug systematically (4 Fase)
# 5. Fix root cause
# 6. Verify fix + no regressions
# 7. Deploy + monitor
```

### Completion Criterion per Recipe

- Test Failure: Test passes, root cause understood, no regressions
- CLI App Bug: Bug fixed, both success + error paths tested
- CI Failure: All checks pass locally
- Production Bug: Bug reproduced, test exists, fix verified, deployed

---

## Anti-Patterns & Pitfalls

### 1. Guess-and-Check
**Masalah:** Coba fix random tanpa investigation
**Fix:** Selalu ikuti 4-fase process

### 2. Fix Symptom, Not Cause
**Masalah:** Error hilang tapi bug tetap ada
**Fix:** Trace ke root cause, fix di sumber

### 3. Multiple Fixes Sekaligus
**Masalah:** Tidak tahu apa yang work
**Fix:** SATU change per test

### 4. Skip Test After Fix
**Masalah:** Tidak ada regression prevention
**Fix:** Selalu tulis/update test

### 5. Ignore Warnings
**Masalah:** Warnings often become errors
**Fix:** Treat warnings sebagai errors

### 6. Debug di Production
**Masalah:** Risky, slow, no isolation
**Fix:** Reproduce locally dulu

### 7. Copy-Paste Fix dari Stack Overflow
**Masalah:** Tidak understand kenapa fix work
**Fix:** Understand root cause dulu, lalu implement

### 8. 3+ Fixes Tanpa Question Architecture
**Masalah:** Stuck di loop, waste time
**Fix:** Question architecture, diskusikan dengan user

---

## Verification Checklist

Sebelum marking debug complete:

- [ ] Error message fully read dan dipahami
- [ ] Root cause teridentifikasi (bukan symptom)
- [ ] Failing test exists (reproduces bug)
- [ ] Hypothesis formed dan tested
- [ ] Single fix implemented (root cause, bukan symptom)
- [ ] Regression test passes
- [ ] All tests pass (no regressions)
- [ ] No new bugs introduced
- [ ] Fix documented (commit message jelas)
- [ ] 3+ fixes questioned architecture (jika applicable)

**Tidak bisa check semua box? Kamu skip process. Mulai ulang dari Fase 1.**

---

## Quick Reference Card

```
DEBUGGING FLOW:
  1. READ    → Baca error message lengkap
  2. REPRODUCE → Buat tight feedback loop
  3. TRACE   → Trace data flow ke sumber
  4. HYPOTHESIZE → Form 3-5 ranked hypotheses
  5. TEST    → Test SATU variable per waktu
  6. FIX     → Implement SATU fix (root cause)
  7. VERIFY  → Test passes + no regressions

RULE OF THREE:
  Fix 1-2 gagal → Re-analyze, coba pendekatan berbeda
  Fix 3+ gagal → STOP, question architecture

COMMON ERRORS:
  TypeError       → Wrong type operation
  ValueError      → Invalid value
  KeyError        → Dict key tidak ada
  AttributeError  → Object tidak punya attribute
  FileNotFoundError → File tidak ada
  JSONDecodeError → JSON invalid/kosong
  AssertionError  → Test assertion failed

FILE NAMING:
  ✗ json.py, os.py, sys.py  (shadows stdlib)
  ✓ myjson.py, app_os.py    (safe)
```

---

Sumber: Adapted from obra/superpowers debugging workflow
Rebuild untuk Hermes Agent + Python CLI workflow — 2026-06-28
