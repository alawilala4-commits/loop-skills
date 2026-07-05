#!/usr/bin/env python3
import re, sys, pathlib
FAIL = 0
ROOT = pathlib.Path('skills')
for p in sorted(ROOT.rglob('SKILL.md')):
    root = p.parent
    rel = str(p)
    data = p.read_text()
    if not data.startswith('---'):
        print(f'missing-frontmatter: {rel}')
        FAIL = 1
        continue
    body = data[3:]
    end = body.find('---')
    fm = body[:end]
    for key in ['name','description']:
        if not re.search(rf'^{key}\s*:', fm, re.M):
            print(f'frontmatter-missing:{key}: {rel}')
            FAIL = 1
    doc = body[end+3:].strip()
    if not doc:
        print(f'empty-body: {rel}')
        FAIL = 1
sys.exit(FAIL)
