# Large Repo Extraction Pattern

When auditing large repos (agent harnesses, monorepos, frameworks >50MB / >1000 files):

## Pattern: Clone → Inspect → Extract Essentials → Cleanup

```bash
# 1. Shallow clone to portable storage (not /tmp — NOT writable on Android)
git clone --depth 1 https://github.com/owner/repo.git /storage/emulated/0/TermuxFiles/repo-audit
cd /storage/emulated/0/TermuxFiles/repo-audit

# 2. Identify structure & scale
find . -not -path './.git/*' -type f | wc -l
du -sh .
du -sh */ 2>/dev/null | sort -rh | head -10

# 3. Identify key files
find . -not -path './.git/*' -maxdepth 2 -name "*.md" -o -name "*.toml" -o -name "*.json" -o -name "*.yaml" -o -name "Makefile" -o -name "Dockerfile" | head -40

# 4. Read README
head -150 README.md 2>/dev/null || head -150 README.zh-CN.md 2>/dev/null

# 5. Language breakdown (fast, no tokens)
find . -not -path './.git/*' -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -20

# 6. Extract essentials to a targeted subset (example: ECC → personal subset)
mkdir -p ~/projects/my-extract/{agents,skills,rules,commands}
cp agents/planner.md agents/tdd-guide.md agents/python-reviewer.md ~/projects/my-extract/agents/
cp -r skills/tdd-workflow skills/python-patterns skills/python-testing ~/projects/my-extract/skills/
cp rules/python/coding-style.md rules/python/testing.md rules/python/security.md ~/projects/my-extract/rules/
```

## Use Case: ECC → ECC Essential

Applied to `affaan-m/ECC` (79MB, 3263 files):
- Extracted 67 agents → 10 essential agents
- Extracted 271 skills → 11 focused skills
- Extracted 22 rules → 16 common + python rules
- Extracted 92 commands → 9 useful commands
- Result: 530K subset (99% smaller) at `~/projects/ecc-important/`

## Decision Framework

When to extract vs. use full repo:
- **Solo dev / Android / CLI apps** → extract essentials (smaller, faster)
- **Team / production / full harness** → install full repo
- **Just reviewing** → clone → inspect → no extraction needed
