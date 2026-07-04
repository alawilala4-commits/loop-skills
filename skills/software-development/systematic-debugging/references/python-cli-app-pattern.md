# Python CLI App Pattern — Session Reference

## Pattern Summary

User repeatedly requests CLI apps with this exact structure:
1. CRUD operations (add/delete/list)
2. Search/filter capability
3. JSON file persistence (save/load)
4. unittest-based tests — user specifies minimum count (15/20/25/30)
5. All tests must pass green before marking complete
6. Git commit after tests pass
7. Obsidian vault update after commit

## Naming Convention

**CRITICAL:** Never name project files after Python stdlib modules.
- `calendar.py` → use `cal.py` (shadows stdlib `calendar`, breaks `datetime.strptime`)
- `json.py` → use `data.py` or `store.py`
- `os.py`, `sys.py`, `math.py`, `random.py`, `email.py`, `http.py` — same rule

## Test Structure Template

```python
#!/usr/bin/env python3
"""test_<app>.py — N tests for <app>.py CLI app."""

import json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from <app> import (
    load_<items>,
    save_<items>,
    add_<item>,
    delete_<item>,
    list_<items>,
    search_<items>,
    get_<item>,
    update_<item>,
    count_<items>,
)

class Test<App>(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        self.tmp.write("[]")
        self.tmp.close()
        self.path = self.tmp.name

    def tearDown(self):
        if os.path.exists(self.path):
            os.unlink(self.path)

    # Tests grouped by operation: load/save, add, delete, list, search, get/update, count
    # Each test uses self.path for file isolation
    # Search tests cover: by field, case-insensitive, no-match, multiple matches

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## Common Test Failures & Fixes

1. **stdlib shadow** — file named `calendar.py` → rename to `cal.py`, update imports
2. **search test count mismatch** — keyword matches more fields than expected (e.g. "python" matches title AND content in same note). Fix: use non-overlapping test data
3. **list sort order assertion** — output format has date in middle of line, not at end. Fix: use `assertIn` for date substring, not `endswith`
4. **LSP false positives** — Pyright reports `Object of type "None" is not subscriptable` on `add_note([], ...)` return. These are false positives (function always returns list). Ignore and run tests directly.

## User Preferences

- Respond in Bahasa Indonesia
- Direct action, no verbose explanations
- Tests written together with app (not after)
- Commit message format: "Project N: <app>.py — <description>"
- Obsidian path: `/data/data/com.termux/files/home/Documents/Obsidian Vault/My Project.md`
- Git repo: `~/projects/`
