#!/usr/bin/env python3
"""<name>.py — CLI <Description>

Commands:
  <command>    <description>
  help
"""

import json
import os
import sys
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "<name>_data.json")


# ── storage helpers ──────────────────────────────────────────────────────────

def load_data(path=DATA_FILE):
    """Load items from JSON file. Return list of dicts."""
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_data(items, path=DATA_FILE):
    """Save list of item dicts to JSON file."""
    with open(path, "w") as f:
        json.dump(items, f, indent=2)


def _next_id(items):
    """Return next sequential integer ID (1-based)."""
    if not items:
        return 1
    return max(i["id"] for i in items) + 1


# ── core functions ────────────────────────────────────────────────────────────

def add_item(items, name, ...):
    """Add a new item. Returns the new item dict."""
    if not name or not name.strip():
        raise ValueError("name must not be empty")
    item = {
        "id": _next_id(items),
        "name": name.strip(),
        "created_at": datetime.now().isoformat(),
    }
    items.append(item)
    return item


def delete_item(items, item_id):
    """Delete item by ID. Returns removed dict or None."""
    for i, it in enumerate(items):
        if it["id"] == item_id:
            return items.pop(i)
    return None


def list_items(items):
    """Return items sorted by id."""
    return sorted(items, key=lambda x: x["id"])


def get_item(items, item_id):
    """Get item by ID. Returns dict or None."""
    for it in items:
        if it["id"] == item_id:
            return it
    return None


def search_items(items, keyword):
    """Search by keyword in name/description (case-insensitive)."""
    kw = keyword.lower()
    return [it for it in items if kw in it["name"].lower()]


# ── CLI interface ─────────────────────────────────────────────────────────────

USAGE = """Usage: python <name>.py <command> [options]

Commands:
  add         ...
  delete      <id>
  list
  search      <keyword>
  help
"""


def run_cli(args):
    """Run CLI command. Returns exit code."""
    if not args or args[0] in ("help", "--help", "-h"):
        print(USAGE)
        return 0

    cmd = args[0]
    items = load_data()

    if cmd == "add":
        # parse args, call add_item, save_data
        pass
    elif cmd == "delete":
        # parse id, call delete_item, save_data
        pass
    # ... etc
    else:
        print(f"Unknown command: {cmd}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(run_cli(sys.argv[1:]))
