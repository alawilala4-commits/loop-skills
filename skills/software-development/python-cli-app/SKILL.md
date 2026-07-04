---
name: python-cli-app
description: Build a Python CLI app with JSON persistence, unittest, Git commit, and Obsidian update — the user's recurring learning project pattern. For the full workflow with all pitfalls, see python-cli-builder.
---

# Python CLI App (Learning Project Pattern)

The user builds Python CLI apps as Termux/Android learning exercises. Each session defines a new app with specific features. This skill encodes the fixed parts of the workflow so each session can focus on the app logic.

> **Full workflow with all pitfalls**: see `python-cli-builder` skill (loaded automatically when relevant).

## Fixed Structure

```
~/projects/<app-name>/
├── <app-name>.py      # CLI entry point (__main__ guard)
├── test_<app-name>.py # unittest tests
└── <app-name>_data.json # Auto-generated JSON persistence
```

## Workflow (per session)

1. **Generate the CLI app** with the requested commands/features
2. **Generate the test file** with the user-specified test count (common counts: 50, 60, 70, 75)
3. **Run tests**: `cd ~/projects/<app-name> && python -m unittest test_<app-name> -v`
4. **Iterate** until ALL tests pass green — fix logic bugs AND bugs in tests
5. **Git commit**: `cd ~/projects/<app-name> && git init && git add <app-name>.py test_<app-name>.py && git commit -m "add <app-name>.py — <description>"`
6. **Update Obsidian**: Append checklist item + log entry to `/data/data/com.termux/files/home/Documents/Obsidian Vault/My Project.md`

## Environment Constraints

- Python 3.13 on Termux (Android)
- No pytest — use stdlib `unittest` only
- Git identity: `OWL User / owl@localhost`
- Working directory: `~/projects/<app-name>/`
- LSP diagnostics from Pyright are false positives for local file imports — ignore them

## Test Patterns That Matter

### Mocking `input()` for interactive CLI commands
```python
@patch("builtins.input", side_effect=["a", "b"])
def test_interactive_command(self, mock_input):
    result = some_function(...)
    self.assertEqual(result["total"], 2)
```

### Mocking `random.shuffle` for deterministic order
```python
@patch("module.random.shuffle", lambda x: None)
def test_shuffled_thing(self):
    # items stay in original order
    ...
```

### Mocking `time.time()` for clock-based logic
```python
@patch("module._now", return_value=1010.0)
def test_timer(self, mock_now):
    ...
```

### JSON persistence roundtrip
```python
with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
    path = f.name
try:
    save_data(self.items, path)
    loaded = load_data(path)
    self.assertEqual(len(loaded), expected)
finally:
    os.unlink(path)
```

## Test Count Targeting

- User specifies exact count: "write 60 tests", "write 70 tests", etc.
- If initial count is short, add integration/edge-case tests to reach the target
- If initial count exceeds, remove redundant tests
- `python -m unittest test_<file>` prints `Ran N tests` — use this to verify exact count

## Obsidian Update Template

**Checklist** (append to Progress section, grouped by date):
```
### 2026-06-23
- [x] Project ke-N: <app-name>.py — <fitur> + JSON persistence + test_<app-name>.py (N tests green), commit <hash>
```

**Format rules**:
- Group by date heading (`### YYYY-MM-DD`)
- Within each date, order by project number
- Fitur: comma-separated, use `+` before "JSON persistence" and "test_..."
- Test count: exact, format `(N tests green)`
- Commit: short 7-char hash

**Ringkasan** (update table + total line every time):
```
## Ringkasan

| # | Project | File | Tests | Commit |
|---|---------|------|-------|--------|
| N | Name | file.py | N | hash |

**Total: N project, N+ tests, semua green**
```

## Pitfalls (learned from 29+ projects)

| Pitfall | Fix |
|---|---|
| `round()` uses banker's rounding (0.5 → nearest even) | Use 0.006 not 0.005 when testing rounding to 0.01 |
| `@patch` decorator order: bottom-up, params reverse | Use `with patch(...):` context manager for multiple patches — NOT stacked `@patch` decorators |
| interactive `input()` validation loops with `@patch` | Include invalid input in side_effect before valid: `["invalid", "a"]` |
| Test for "exactly N" — off-by-one common | Run tests, check `Ran N` output, add/remove before committing |
| JSON persistence: relative vs absolute paths | Use `os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")` |
| Commands with optional args parsing | Build `_parse_args(args)` helper using while-loop over flags |
| Duplicate `old_string` in patch | Add more surrounding context to make unique |
| Walrus operator in `setUp` causes SyntaxError | Use plain dict/list literals, never `self.items = [f(self.items := [])]` |
| Search tests: keyword matches across multiple fields | If entry A has keyword in title AND entry B in content, both match — count carefully |
| `setUp` with mutable module-level globals | Always create fresh lists/dicts in `setUp`, never module-level |
| Test class `setUp` not available in new test class | Tests added to wrong class (e.g. `TestOverdue` instead of `TestIntegration`) — verify class context |
| `test_search_partial_match` on fresh data | Fresh `setUp` has no data — must `add_book()` first before searching |

## Session Start Checklist

1. Check `~/projects/` for highest-numbered project to determine next project number
2. Read Obsidian `My Project.md` to see completed projects
3. Confirm with user: "Mau lanjut project ke-N?" or accept their goal message
4. Build app → tests → green → commit → Obsidian → confirm done
