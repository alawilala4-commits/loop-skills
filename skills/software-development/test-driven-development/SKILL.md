---
name: test-driven-development
description: "TDD workflow: RED-GREEN-REFACTOR. Skill spesialis untuk coding pipeline — tidak bagian dari intel/produksi pipeline. Use when building features, fixing bugs, or refactoring code."
version: 2.0.0
author: Hermes Agent (Lala Alawi rebuild)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testing, tdd, development, quality, red-green-refactor, python, unittest]
    related_skills: [systematic-debugging, claude-code, codex, python-cli-app]
---

# Test-Driven Development (TDD) — RED-GREEN-REFACTOR

## Purpose
Code with tests workflow. Skill spesialis untuk coding pipeline — tidak bagian dari intel/produksi pipeline.

## When to Use
- Building new features
- Fixing bugs (write failing test first)
- Refactoring existing code
- Any behavior change

## Do
- Write failing test FIRST (RED)
- Watch it fail — verify it fails for the right reason
- Write minimal code to pass (GREEN)
- Refactor only after green
- Use vertical tracer bullets (one behavior per cycle)
- Delete code written before tests — start over

## Don't
- Write code before tests
- Skip watching the test fail
- Add features beyond what the test requires
- Test implementation details instead of behavior
- Keep "reference" code when restarting with TDD
- Name files after stdlib modules (json.py, os.py, calendar.py)

## Output Format
```
## TDD Cycle: [FEATURE]

### RED
- Test: tests/test_x.py::test_y
- Status: FAIL (expected — feature not implemented)

### GREEN
- Implementation: src/module.py
- Status: PASS (minimal code)

### REFACTOR
- Changes: [cleanup done]
- Status: PASS (all tests still green)

### Result
- Tests: X/Y pass
- Coverage: Z%
```

## Pipeline Position
Skill spesialis untuk coding pipeline. Digunakan oleh Coder role di multi-agent-orchestrator.

---

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

**Mengapa test-first:**
- Memaksa kamu memikirkan interface sebelum implementasi
- Menemukan edge case SEBELUM coding (bukan setelah)
- Menghasilkan dokumentasi executable (test = spec)
- Memungkinkan refactoring percaya diri (test catch regressions)
- Mencegah over-engineering (hanya code yang di-test yang ditulis)

**Tiga pilar TDD:**
1. **Verification** — Test membuktikan code bekerja
2. **Design** — Test-first memaksa interface yang baik
3. **Regression Prevention** — Test mencegah bug kembali

---

## Kapan TDD Wajib vs Opsional

### TDD WAJIB untuk:
- Fitur baru (apapun ukurannya)
- Bug fix (tulis test yang reproduce bug dulu)
- Refactoring (pastikan behavior tidak berubah)
- Perubahan behavior
- API endpoint baru
- Validasi input/output
- Edge case handling

### TDD OPSIONAL (tanya user dulu):
- Throwaway prototype / spike
- Generated code (boilerplate)
- Configuration files (JSON/YAML tanpa logic)
- One-time migration scripts
- Exploratory coding di REPL

### Decision Tree

```
Ada logic/behavior?
├── Ya → TDD WAJIB
│   ├── Fitur baru? → RED → GREEN → REFACTOR
│   ├── Bug fix? → Write failing test → Fix → Verify
│   └── Refactor? → Ensure tests pass → Refactor → Verify still pass
│
└── Tidak → TDD OPSIONAL
    ├── Config file? → Skip TDD
    ├── Boilerplate? → Skip TDD
    └── Prototype? → Skip TDD (tapi throw away setelah selesai)
```

---

## The Iron Law

```
TIDAK ADA PRODUCTION CODE TANPA FAILING TEST PERTAMA
```

**Jika kamu menulis code sebelum test:**
- Hapus code tersebut
- Mulai dari test
- Tulis ulang code berdasarkan test

**Tidak ade exception:**
- Jangan simpan sebagai "referensi"
- Jangan "adapt" saat menulis test
- Jangan liat code lama
- Delete = delete

**Implement fresh dari tests. Period.**

---

## Siklus RED-GREEN-REFACTOR

### FASE 1: RED — Tulis Test yang Gagal

Tulis SATU test minimal yang menunjukkan apa yang harus terjadi.

**Struktur test yang baik:**
```python
def test_retries_failed_operations_3_times(self):
    """Test bahwa operation di-retry tepat 3 kali sebelum success."""
    attempts = 0
    def operation():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise Exception('fail')
        return 'success'

    result = retry_operation(operation)

    self.assertEqual(result, 'success')
    self.assertEqual(attempts, 3)
```

**Struktur test yang BURUK:**
```python
def test_retry_works(self):
    """Vague, tests mock bukan real code."""
    mock = MagicMock()
    mock.side_effect = [Exception(), Exception(), 'success']
    result = retry_operation(mock)
    self.assertEqual(result, 'success')  # Mana retry count? Timing?
```

### Aturan Penulisan Test

| Aturan | Penjelasan |
|--------|------------|
| Satu behavior per test | Jangan test 3 hal sekaligus |
| Nama deskriptif | `test_<context>_<expected_behavior>` |
| Real code, bukan mock | Mock hanya jika truly unavoidable |
| Nama menjelaskan behavior | Bukan implementation |
| "and" di nama? Split! | `test_x_and_y` = dua test terpisah |

### Verifikasi RED — Wajib!

```python
# Jalankan test spesifik
python -m unittest tests/test_feature.py -v

# Konfirmasi:
# 1. Test FAIL (bukan error dari typo)
# 2. Failure message sesuai ekspektasi
# 3. Gagal karena feature belum ada (bukan karena typo)
```

**Test pass langsung?** Kamu test existing behavior. Fix test-nya.
**Test error?** Fix error, ulangi sampai fail dengan benar.

---

### FASE 2: GREEN — Kode Minimal

Tulis **kode paling sederhana** untuk membuat test pass. Tidak lebih.

**Kode GREEN yang baik:**
```python
def add(a, b):
    return a + b  # Nothing extra
```

**Kode GREEN yang BURUK:**
```python
def add(a, b):
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")  # Extra!
    return result
```

### Aturan GREEN

| Aturan | Penjelasan |
|--------|------------|
| Hardcode OK | `return 42` dulu tidak apa-apa |
| Copy-paste OK | Duplikasi akan di-refactor nanti |
| Skip edge cases OK | Edge cases akan di-test di cycle berikutnya |
| Jangan refactor | Fokus hanya membuat test pass |
| Jangan tambah feature | Hanya yang di-test yang di-implement |

### Verifikasi GREEN — Wajib!

```python
# 1. Test spesifik pass
python -m unittest tests/test_feature.py -v

# 2. Semua test pass (no regressions)
python -m unittest discover tests/ -v

# 3. Output pristine (no errors, no warnings)
```

**Test gagal?** Fix code, BUKAN test.
**Test lain fail?** Fix regressions sekarang.

---

### FASE 3: REFACTOR — Bersihkan

Setelah GREEN, baru boleh refactor:
- Hapus duplikasi
- Improve nama variable/function
- Extract helper functions
- Simplify expressions
- Tambah type hints

**Aturan REFACTOR:**
- Jangan tambah behavior
- Tests harus tetap GREEN throughout
- Jika tests fail saat refactor → UNDO immediately
- Take smaller steps

### Repeat

Cycle berikutnya untuk behavior berikutnya. Satu per satu.

```
RED → GREEN → REFACTOR → RED → GREEN → REFACTOR → ...
```

---

## Tracer Bullet vs Horizontal Slice

### Tracer Bullet (BENAR)

Satu slice end-to-end per cycle:

```
RED→GREEN: test1 → impl1
RED→GREEN: test2 → impl2
RED→GREEN: test3 → impl3
```

**Keuntungan:**
- Membuktikan path works di setiap cycle
- Mengajarkan interface yang benar
- Setiap test grounded di apa yang baru dipelajari
- Feedback loop cepat

### Horizontal Slice (SALAH)

Semua test dulu, baru semua implementasi:

```
RED:   test1, test2, test3, test4
GREEN: impl1, impl2, impl3, impl4
```

**Masalah:**
- Tests designed before implementation teaches you
- Brittle tests (designed based on imagination, not reality)
- Tidak ada feedback sampai akhir
- Sering salah paham interface

---

## Test Patterns untuk Python CLI App

### Pattern 1: JSON Persistence Test

```python
import json
import os
import tempfile
import unittest

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Create temp file for each test."""
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', suffix='.json', delete=False
        )
        self.temp_file.close()
        self.data_file = self.temp_file.name

    def tearDown(self):
        """Clean up temp file."""
        if os.path.exists(self.data_file):
            os.unlink(self.data_file)

    def test_add_task_persists_to_json(self):
        """Adding a task should write to JSON file."""
        task = {"id": 1, "title": "Test", "done": False}
        
        # Write
        with open(self.data_file, 'w') as f:
            json.dump([task], f)
        
        # Read back
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test')
```

### Pattern 2: CLI Argument Test

```python
import subprocess
import sys

class TestCLI(unittest.TestCase):
    def run_cli(self, *args):
        """Helper to run CLI and capture output."""
        result = subprocess.run(
            [sys.executable, 'app.py', *args],
            capture_output=True, text=True
        )
        return result

    def test_add_command_creates_task(self):
        """'add "Buy milk"' should create a new task."""
        result = self.run_cli('add', 'Buy milk')
        self.assertEqual(result.returncode, 0)
        self.assertIn('added', result.stdout.lower())

    def test_list_command_shows_tasks(self):
        """'list' should display all tasks."""
        self.run_cli('add', 'Task 1')
        result = self.run_cli('list')
        self.assertIn('Task 1', result.stdout)
```

### Pattern 3: Input Validation Test

```python
class TestValidation(unittest.TestCase):
    def test_rejects_empty_title(self):
        """Task with empty title should be rejected."""
        result = add_task(title="", data_file=self.data_file)
        self.assertFalse(result['success'])
        self.assertIn('title', result['error'])

    def test_rejects_duplicate_id(self):
        """Task with duplicate ID should be rejected."""
        add_task(id=1, title="First", data_file=self.data_file)
        result = add_task(id=1, title="Duplicate", data_file=self.data_file)
        self.assertFalse(result['success'])
```

### Pattern 4: Edge Case Test

```python
class TestEdgeCases(unittest.TestCase):
    def test_handles_missing_json_file(self):
        """App should handle missing data file gracefully."""
        result = list_tasks(data_file='/nonexistent/path.json')
        self.assertEqual(result, [])

    def test_handles_corrupt_json(self):
        """App should handle corrupt JSON gracefully."""
        with open(self.data_file, 'w') as f:
            f.write("{invalid json!!!")
        
        result = list_tasks(data_file=self.data_file)
        self.assertEqual(result, [])

    def test_handles_unicode_titles(self):
        """Task titles should support unicode."""
        result = add_task(title="Beli susu 🥛", data_file=self.data_file)
        self.assertTrue(result['success'])
```

---

## Common Rationalizations (dan Kenyataannya)

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 detik. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code = tech debt. |
| "Keep as reference" | You'll adapt it. That's testing after. Delete. |
| "Need to explore first" | Fine. Throw away exploration, start TDD. |
| "Test hard = design unclear" | Listen to the test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. Pragmatic = test-first. |
| "Manual test faster" | Manual doesn't prove edge cases. Re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for code you touch. |

---

## Red Flags — STOP dan Mulai Ulang

Jika kamu melakukan ini, **hapus code dan mulai ulang dengan TDD:**

- [ ] Code written before test
- [ ] Test written after implementation
- [ ] Test passes immediately on first run
- [ ] Cannot explain why test failed
- [ ] Tests added "later"
- [ ] Rationalizing "just this once"
- [ ] "I already manually tested it"
- [ ] "Keep as reference" or "adapt existing code"
- [ ] "Already spent X hours, deleting is wasteful"
- [ ] "TDD is dogmatic, I'm being pragmatic"
- [ ] "This is different because..."

**Semua ini berarti: HAPUS CODE. MULAI DENGAN TDD.**

---

## Hermes Integration

### Running Tests di Hermes

```bash
# Run specific test
python -m unittest tests/test_module.py -v

# Run all tests
python -m unittest discover tests/ -v

# Run with coverage (if coverage installed)
coverage run -m unittest discover tests/
coverage report
```

### TDD + delegate_task

```python
delegate_task(
    goal="Implement [feature] using strict TDD",
    context="""
    Follow test-driven-development skill:
    1. Write failing test FIRST
    2. Run test to verify it fails
    3. Write minimal code to pass
    4. Run test to verify it passes
    5. Refactor if needed
    6. Commit

    Project test command: python -m unittest discover tests/ -v
    Project structure: [describe relevant files]
    """,
    toolsets=['terminal', 'file']
)
```

### TDD + systematic-debugging

Bug ditemukan? Tulis failing test yang reproduce bug. Ikuti TDD cycle. Test membuktikan fix dan mencegah regression.

**Jangan fix bugs tanpa test.**

---

## Error Mapping & Troubleshooting

### Common Test Failures

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `AssertionError: X != Y` | Expected value salah | Cek expected vs actual, fix test atau code |
| `ModuleNotFoundError` | File shadowing stdlib | Rename file (jangan `json.py`, `os.py`, dll) |
| `AttributeError: has no attr` | Typo atau wrong object | Cek nama attribute, pastikan object benar |
| `FileNotFoundError` | Path salah atau file tidak ada | Cek path, pastikan setUp() buat file |
| `JSONDecodeError` | File corrupt atau kosong | Cek isi file, pastikan valid JSON |
| `TypeError: missing argument` | Function signature berubah | Cek function definition, update test call |

### Python stdlib module name collision

**Symptom:** stdlib imports fail dengan `AttributeError` atau `ImportError` di tempat yang tidak terduga.

**Contoh:** File `calendar.py` menyebabkan `datetime.strptime()` crash dengan `AttributeError: module 'calendar' has no attribute 'day_abbr'` karena `datetime.strptime` internally import stdlib `calendar`, tapi menemukan project `calendar.py` kamu.

**Rule:** Jangan pernah nama file project sama denga***@`. Gunakan prefix: `cal.py` bukan `calendar.py`, `myjson.py` bukan `json.py`.

**Quick check:** Kalau filename match dengan https://docs.python.org/3/library/ — rename it.

---

## Pola Harian—Recipes Siap Pakai

### 1. New Feature (5-15 menit)

```bash
# RED: Write failing test
cat > tests/test_new_feature.py << 'EOF'
import unittest

class TestNewFeature(unittest.TestCase):
    def test_feature_does_x(self):
        result = new_function(input)
        self.assertEqual(result, expected)
EOF

# Verify RED
python -m unittest tests/test_new_feature.py -v  # should FAIL

# GREEN: Write minimal code
# ... implement new_function ...

# Verify GREEN
python -m unittest tests/test_new_feature.py -v  # should PASS

# REFACTOR: Clean up
# ... improve names, remove duplication ...

# Verify all tests still pass
python -m unittest discover tests/ -v
```

### 2. Bug Fix (10-20 menit)

```bash
# 1. Write failing test that reproduces bug
# 2. Verify test fails (proves bug exists)
# 3. Debug root cause (use systematic-debugging skill)
# 4. Fix root cause
# 5. Verify test passes (proves bug fixed)
# 6. Verify all tests pass (no regressions)
```

### 3. Refactoring (15-30 menit)

```bash
# 1. Ensure all existing tests pass (baseline)
python -m unittest discover tests/ -v

# 2. Make small refactor change
# 3. Run all tests
# 4. If pass → next small change
# 5. If fail → UNDO immediately, take smaller steps
```

### 4. CLI App Feature (20-40 menit)

```bash
# 1. Test command parsing
# 2. Test business logic
# 3. Test JSON persistence
# 4. Test edge cases (missing file, corrupt JSON, unicode)
# 5. Test error messages
# 6. Integration test (full command flow)
```

### Completion Criterion per Recipe

- New Feature: Test exists, failed first, now passes, all green
- Bug Fix: Regression test exists, bug reproducible, fix verified
- Refactoring: All tests pass before AND after, behavior unchanged
- CLI App: All command paths tested, edge cases covered

---

## Anti-Patterns & Pitfalls

### 1. Testing Implementation, Not Behavior
**Masalah:** Test breaks saat refactor (meskipun behavior benar)
**Fix:** Test inputs→outputs, bukan internal method calls

### 2. Happy Path Only
**Masalah:** Test hanya untuk success case
**Fix:** Selalu test: empty input, null, unicode, large data, corrupt file

### 3. Brittle Tests
**Masalah:** Test terlalu spesifik ke implementasi saat ini
**Fix:** Test behavior contracts, bukan exact strings/values

### 4. Test Duplication
**Masalah:** Setup code diulang di setiap test
**Fix:** Extract ke setUp() atau helper functions

### 5. Slow Tests
**Masalah:** Test butuh 5 menit untuk run
**Fix:** Mock external services, use temp files, parallelize

### 6. Testing Framework Code
**Masalah:** Test untuk library/framework function
**Fix:** Test YOUR code, not the framework's

### 7. Ignoring Test Failures
**Masalah:** "It's probably a flaky test, skip it"
**Fix:** Investigate EVERY failure, fix root cause

### 8. Writing All Tests First
**Masalah:** Horizontal slice — semua test dulu, baru implement
**Fix:** Tracer bullet — satu test → satu implement → repeat

---

## Verification Checklist

Sebelum marking work complete:

- [ ] Setiap function/method baru punya test
- [ ] Melihat setiap test FAIL sebelum implement
- [ ] Setiap test fail karena alasan yang benar (feature missing, bukan typo)
- [ ] Menulis kode minimal untuk pass setiap test
- [ ] Semua test pass
- [ ] Output pristine (no errors, no warnings)
- [ ] Tests use real code (mocks hanya jika unavoidable)
- [ ] Edge cases dan errors tercover
- [ ] Tidak ada file shadowing stdlib modules
- [ ] setUp/tearDown clean (no leftover files)
- [ ] Test names descriptive dan specific

**Tidak bisa check semua box? Kamu skip TDD. Mulai ulang.**

---

## Quick Reference Card

```
TDD CYCLE:
  RED       → Write failing test
  Verify RED → Run test, confirm it fails correctly
  GREEN     → Write minimal code to pass
  Verify GREEN → Run test, confirm all pass
  REFACTOR  → Clean up, keep tests green
  REPEAT    → Next behavior

TEST COMMAND:
  Specific  → python -m unittest tests/test_file.py -v
  All       → python -m unittest discover tests/ -v
  Coverage  → coverage run -m unittest discover tests/

FILE NAMING:
  ✓ task_manager.py  tests/test_task_manager.py
  ✗ json.py          (shadows stdlib json)
  ✗ os.py            (shadows stdlib os)
  ✓ myjson.py        (safe)

TEST STRUCTURE:
  setUp()     → Create fixtures (temp files, test data)
  test_name   → One behavior, descriptive name
  tearDown()  → Clean up (delete temp files)
```

---

Sumber: Adapted from obra/superpowers TDD workflow
Rebuild untuk Hermes Agent + Python CLI workflow — 2026-06-28
