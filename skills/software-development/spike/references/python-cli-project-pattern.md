# Python CLI Project Pattern

Session-derived pattern from building todo.py, cal.py in ~/projects/.

## Structure

Each CLI app follows this layout:

```
~/projects/
├── appname.py          # Main CLI app
├── test_appname.py     # Tests (unittest, no pytest needed)
├── data.json           # JSON persistence file (auto-created)
└── .git                # Single repo for all projects
```

## Workflow

1. Write main app with manual `sys.argv` dispatch (no argparse dependency)
2. Write tests using stdlib `unittest` (no pytest dependency)
3. Run: `python test_appname.py` — all green
4. Commit: `git add appname.py test_appname.py && git commit -m "..."`
5. Update Obsidian progress tracker

## Conventions

- JSON persistence: `load_*()` / `save_*()` functions with `DEFAULT_FILE` path
- CLI dispatch: manual `sys.argv` parsing with `if/elif` on `args[0]`
- IDs: sequential via `_next_id()` helper
- Tests use `tempfile.NamedTemporaryFile` for isolation — never write to real data file in tests
- No external dependencies — stdlib only

## Naming warning

NEVER name files after Python stdlib modules. Use prefixed names:
- `cal.py` not `calendar.py`
- `myjson.py` not `json.py`
- `myos.py` not `os.py`

See the "Python stdlib module name collision" pitfall in the systematic-debugging skill.
