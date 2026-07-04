---
name: python-cli-builder
description: Build Python CLI apps as learning projects on Android/Termux — CRUD + search/filter + JSON persistence + unittest suite + Git commit + Obsidian update. Trigger when user says "buat project", "lanjutkan project", "project berikutnya", or asks for a new CLI app.
---

# Python CLI Builder

Build a complete Python CLI app in a single session following a fixed pattern.

## Workflow

### Option A: Single-Agent (default)
Execute in order:
1. **Pick a topic** — suggest options or use the user's idea. Avoid stdlib name clashes (e.g. `calendar` → `cal.py`).
2. **Create project directory** under `~/projects/<name>/`
3. **Write `<name>.py`** — full implementation with all features
4. **Write `test_<name>.py`** — comprehensive unittest suite (user specifies count: 15/20/25/30/40/50/60+)
5. **Run tests** — all must pass green. Fix any failures immediately.
6. **Git commit** — `git init` if needed, `git add`, `git commit -m "..."`
7. **Update Obsidian** — append to `~/Documents/Obsidian Vault/My Project.md`

### Option B: Multi-Agent Orchestration (when user requests it)
When the user explicitly asks for multi-agent workflow, orchestrator pattern, or "Orchestrator → Coder → Tester  Reviewer → Logger" flow, switch to the `multi-agent-orchestrator` skill. That skill handles the full delegation workflow via `delegate_task`. The multi-agent pattern has been validated on 2026-06-24 with project task-manager (60 tests, all green, review PASS, commit b980aaa). Full template: `~/Documents/Obsidian Vault/Hermes Multi-Agent Memory.md`.

## App Architecture

Every app follows this structure:

```
~/projects/<name>/
├── <name>.py          # Main CLI app
├── test_<name>.py     # Unittest suite
└── <name>_data.json   # Auto-generated JSON data file
```

### Core Pattern

Each `<name>.py` includes:

- **Data layer**: `load_data()` / `save_data()` using JSON file in project directory
- **CRUD functions**: add, delete, get, list, search, filter
- **Domain-specific functions**: stats, summaries, aggregations
- **CLI interface**: `run_cli(args)` with subcommands, `if __name__ == "__main__"` entry point
- **Validation**: raise `ValueError` on bad input (invalid type, negative amount, bad date)

### Function Signature Convention

```python
def load_data(path=DATA_FILE) -> list:
def save_data(records, path=DATA_FILE) -> None:
def add_X(records, field1, field2, ...) -> dict:
def delete_X(records, id) -> dict | None:
def list_X(records) -> list:
def search_X(records, keyword) -> list:
def filter_X(records, criteria) -> list:
```

### CLI Command Convention

```
python <name>.py <command> [args...]
python <name>.py help
```

## Test Structure

Use `unittest.TestCase` with `setUp` that initializes empty data. Organize into classes:

- `TestHelpers` — load/save, parse, ID generation
- `TestAddX` — basic add, with description, with date, default date, sequential IDs, rounding
- `TestAddXValidation` — invalid input, zero/negative, bad date
- `TestListX` — empty, sorted, does not mutate
- `TestFilterX` — by various criteria, no match, empty
- `TestDeleteX` — existing, not found, first/last
- `TestSummary/Stats` — correct calculations, empty case
- `TestSearch` — category, description, case-insensitive, no match
- `TestTotals` — income/expense/balance or domain equivalent
- `TestIntegration` — full workflow, multi-month, aggregation, save/load roundtrip

### Test Count Targets

Match the user's specified count. Typical distribution:
- 15 tests: basic CRUD only
- 25 tests: + filter, search
- 40 tests: + stats, edge cases
- 60 tests: + integration, full validation

## Git Setup

```bash
cd ~/projects/<name>
git init  # only if .git doesn't exist
git add <name>.py test_<name>.py
git commit -m "add <name>.py — <description> + N tests green"
```

Git identity (already configured):
- Name: `OWL User`
- Email: `owl@localhost`

## Obsidian Update

**File**: `~/Documents/Obsidian Vault/My Project.md`

### Entry format (one line per project, under `## Progress`)

```
- [x] Project ke-N: <name>.py — <fitur> + JSON persistence + test_<name>.py (N tests green), commit <hash>
```

**Rules**:
- Group by date heading (`### 2026-06-22`, `### 2026-06-23`, etc.)
- Within each date, order by project number (sequential)
- Fitur list: comma-separated, no "and" or "—" before the last item, use `+` before "JSON persistence" and "test_..."
- Always include `+ JSON persistence +` before the test mention
- Test count: exact number, format `(N tests green)`
- Commit: short 7-char hash

### Ringkasan (summary table)

Maintain a markdown table at the bottom of the file:

```
## Ringkasan

| # | Project | File | Tests | Commit |
|---|---------|------|-------|--------|
| 1 | Hello World | hello.py | - | 6474aae |
| 2 | Todo | todo.py | 26 | 4be2d84 |
...

**Total: N project, N+ tests, semua green**
```

Update the table AND the total line every time a project is added.

## Pitfalls

- **Stdlib name clash**: Don't name files `calendar.py`, `email.py`, `test.py`, `code.py`, `json.py`. Use alternatives like `cal.py`.
- **LSP false positives on Termux**: Pyright may show "unknown import symbol" for local imports. Ignore — tests will still run correctly.
- **Test count mismatch**: If tests don't match the requested count, add integration/edge-case tests to hit the target.
- **Mutable default arguments**: Never use `def f(x=[])` — use `None` + initialization inside function.
- **JSON file path**: Use `os.path.dirname(os.path.abspath(__file__))` to anchor DATA_FILE to the project directory, not CWD.
- **Floating point in tests**: Use `round(..., 2)` for monetary values. Compare with `assertEqual` on rounded values.
- **setUp vs setUpClass**: Use `setUp` (per-test fresh data) so tests don't share state.
- **Walrus operator in setUp**: Avoid `self.items = [add_item(self.items := [], ...)]` pattern — it causes `SyntaxError` in some Python/Termux contexts. Use plain dict literals or sequential calls instead.
- **Banker's rounding in test assertions**: Python uses banker's rounding (`round(0.005, 2)` = `0.0`, not `0.01`). When testing rounding behavior, use values that round predictably (e.g. `0.006` → `0.01`). Don't assert on exact halfway cases.
- **Integration test math**: Double-check expected values in integration tests. Deleting an expense of 500 from balance 4300 should give 4800 (not 4500). Write out the arithmetic explicitly when writing assertions.
- **Integration test variable scoping**: When patching integration tests mid-stream, ensure all referenced variables are defined in the right order. If you replace a block that defines a variable (e.g. `py_entries = filter_by_tag(...)`) with a different assertion, the variable may become undefined for later assertions. Always check the full test function after patching.
- **Tag normalization pattern**: For apps with tags, use a `_validate_tags()` helper that lowercases, strips whitespace, removes empties, and deduplicates. Store tags as sorted lists. Filter by tag should be case-insensitive.
- **Test count precision**: When the user specifies "exactly N tests", hit that exact count. If you overshoot, remove redundant tests (e.g. duplicate validation tests, overlapping integration tests). If you undershoot, add edge-case or integration tests. Count with `python -m unittest` (not `-v`) to verify the exact `Ran N` number before committing. The `-v` flag only lists test names; the non-verbose output shows the total clearly.
- **`@patch` decorator ordering**: When stacking multiple `@patch` decorators, mock parameters are passed in reverse order (bottom decorator = first parameter). This is error-prone. **Prefer `with patch(...) as mock:` context managers** inside the test body — they're clearer and avoid parameter ordering bugs entirely.
- **Testing functions with `random.shuffle`**: Patch `random.shuffle` with `lambda x: None` to make order deterministic. Use `with` context managers, not stacked `@patch` decorators. Remember to also patch `builtins.input` for interactive functions. See `references/unittest-patch-ordering.md` for details. Remember to also patch `builtins.input` for interactive functions.
- **Dependency injection for testability**: For functions that depend on the current time, extract the time source into a module-level helper (e.g., `def _now(): return time.time()`). Tests can then patch `module._now` with `unittest.mock.patch` to control time deterministically. This avoids `time.sleep()` in tests and makes countdown/timer behavior fully deterministic. Example: `with patch("timer._now", side_effect=[1000.0, 1010.0, 1020.0]):`
- **Search matching both title AND content**: When a `search_notes`/`search_entries` function searches both title and content fields, a keyword may match BOTH the title of one entry AND the content of another. Test assertions must account for this — e.g., searching "python" may return 2 results if one entry has "Python" in the title and another has "python" in the content. Always verify which entries actually match before asserting counts.
- **Integration test variable replacement**: When replacing a block in an integration test that defines a variable used later (e.g., `py_entries = filter_by_tag(...)`), the replacement must either re-define the variable or remove all references to it. A partial replacement that leaves dangling references causes `NameError` that looks like a logic error but is actually a scoping issue from the edit.
- **Email/phone validation**: For CRM-type apps, accept email and phone as plain strings. Validate non-empty only — don't enforce format. The user's data is for their own use.
- **Optional CLI flags pattern**: For commands with optional args (`--notes X`, `--date YYYY-MM-DD`, `--sets N`), use a `while i < len(args)` loop with `if args[i] == "--flag" and i + 1 < len(args): ... i += 2`. Build a `_parse_add_args(args)` helper for complex commands. Always validate date format with `datetime.strptime` inside the core function, not the CLI parser.
- **Borrow/return lifecycle**: For library/rental apps, track `available` boolean on the item. `borrow_book()` sets `available = False` and computes `due_date = borrow_date + timedelta(days=N)`. `return_book()` sets `return_date` and `available = True`. Always find the active loan by `book_id` AND `return_date is None` — not just book_id — to handle re-borrowing after return.
- **Personal records / leaderboard**: For fitness/stats apps, compute records as `max(workouts, key=lambda w: w["duration"])`. Handle `None` values in optional fields (e.g., `sets=None`) by filtering with `if w["sets"] is not None` before aggregating.
- **Stage-based workflows**: For pipeline/CRM apps, define VALID_STAGES as a module-level set. Default new entries to "lead". Use `move_stage()` with validation against the set.
- **Notes as subdocuments**: For apps that support notes on entities (like CRM contacts), store notes as a list of dicts inside the parent entity. Provide `add_note()` and `list_notes()` functions.
- **Test count precision**: When the user specifies "exactly N tests", hit that exact count. Count with `python -m unittest` (not `-v`) to verify the exact `Ran N` number before committing. If you overshoot, remove redundant tests. If you undershoot, add edge-case or integration tests.
- **Search matching both title AND content**: When a search function searches multiple fields (title + content), a keyword may match BOTH fields across different entries. Always verify which entries actually match before asserting counts. See `references/search-field-matching.md` for the pattern and a list of projects where this bit.
- **Integration test variable scoping after patch**: When replacing a block in an integration test that defines a variable used later, the replacement must either re-define the variable or remove all references to it. Partial replacements that leave dangling references cause `NameError`.
- **Banker's rounding in test assertions**: Python uses banker's rounding (`round(0.005, 2)` = `0.0`). When testing rounding, use values that round predictably (e.g., `0.006` -> `0.01`).
- **Multi-entity apps**: For apps managing multiple entity types (e.g., school: students + teachers + enrollments, clinic: patients + doctors + appointments + prescriptions), use a single JSON file with top-level keys per entity (`{"students": [], "teachers": [], "appointments": []}`). Each entity has its own add/delete/list/search functions. Cross-entity operations (enroll, book, prescribe) reference entities by ID. See `references/multi-entity-pattern.md` for the full pattern including test setUp pitfalls.
- **Nested data structures**: For sub-entities (enrollments, prescriptions, notes), store as dicts/lists inside the parent entity. Example: `student["enrollments"]["Math"] = {"grade": None, "attendance": []}`. Provide dedicated functions (`enroll_student`, `add_prescription`) rather than raw dict manipulation.
- **Datetime validation**: For appointment-style apps, validate `YYYY-MM-DD HH:MM` format with `datetime.strptime(date_time, "%Y-%m-%d %H:MM")`. Strip whitespace before validation. Use `timedelta(days=N)` for computing due dates.
- **Attendance tracking**: Store as list of `{"date": "YYYY-MM-DD", "status": "present|absent"}` dicts. Validate status against allowed values. Use `datetime.now().strftime("%Y-%m-%d")` for today's date, extracted into a `_today_str()` helper for testability.
- **Grade/score storage**: Store grades as strings (allows "A+", "B-", "95", etc.) rather than enforcing numeric. Default to `None` (ungraded). Provide `set_grade()` function that validates enrollment before setting.
- **Multi-agent validation**: The `multi-agent-orchestrator` skill (autonomous-ai-agents:multi-agent-orchestrator) has been validated on 2026-06-24. It works. Use it when the user asks for multi-agent/delegation/orchestrator workflow. The 4-agent pattern (Coder → Tester  Reviewer → Logger) with sequential delegation via `delegate_task` produces clean results with clear separation of concerns. Full session log: `~/Documents/Obsidian Vault/Hermes Multi-Agent Memory.md` and `autonomous-ai-agents:multi-agent-orchestrator/references/session-2026-06-24.md`
- **No printing from core functions**: Core domain functions (add, delete, compute, search) should NOT print. Reserve `print()` for CLI interface only ("Added: #...", "Error: ..."). Lets tests assert on return values without capturing stdout.
- **`_fresh_data()` factory in tests**: For multi-entity apps (school, clinic), define a `_fresh()` or `_fresh_data()` factory function at module level that returns a fresh data dict. Use it in setUp. When you need pre-populated entities (e.g., add a student before enrolling), add them at the start of each test, NOT in setUp — setUp should create the blank slate.
- **`_today_str()` helper**: Extract `datetime.now().strftime("%Y-%m-%d")` into a module-level `_today_str()` function. In tests, override behavior by passing explicit date strings to functions rather than mocking the clock. Only mock `_now()` when testing elapsed-time logic.
