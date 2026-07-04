---
name: github-pr-workflow
description: "GitHub PR lifecycle end-to-end. Skill spesialis untuk coding/release pipeline — tidak bagian dari intel/produksi pipeline. Use when creating, fixing, or merging pull requests."
version: 2.0.0
author: Hermes Agent (Lala Alawi rebuild)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Pull-Requests, CI-CD, Git, Automation, Merge, Branching]
    related_skills: [github-auth, github-code-review, github-repo-management, github-issues]
---

# GitHub PR Workflow — PR/Release Flow

## Purpose
PR lifecycle end-to-end. Skill spesialis untuk coding/release pipeline — tidak bagian dari intel/produksi pipeline.

## When to Use
- Creating a new pull request
- Fixing CI failures on PR
- Reviewing and responding to feedback
- Merging and cleanup
- Hotfix releases

## Do
- Sync main before branching
- Use conventional commits (feat:, fix:, refactor:)
- Stage specific files (never `git add .` without review)
- Write descriptive PR body with Summary + Test Plan
- Monitor CI until green
- Squash merge for feature branches
- Delete branch after merge

## Don't
- Commit directly to main
- Merge with failing CI
- Use `git add .` without reviewing staged files
- Force push to main
- Leave branches after merge
- Use vague commit messages ("fix stuff")

## Output Format
```
## PR: [TITLE]

**Branch:** feat/x → main
**PR:** https://github.com/org/repo/pull/N

### Commits
1. `abc123f` feat(auth): add JWT authentication
2. `def456a` test(auth): add unit tests

### CI Status
- Tests: PASS (X/Y)
- Lint: PASS
- Build: PASS

### Merge
- Method: squash
- Status: MERGED
- Cleanup: branch deleted
```

## Pipeline Position
Skill spesialis untuk coding/release pipeline. Digunakan oleh Deployer role di multi-agent-orchestrator.

---

## Branch Naming

| Prefix | Use Case | Example |
|--------|----------|---------|
| `feat/` | New feature | `feat/add-user-auth` |
| `fix/` | Bug fix | `fix/login-redirect` |
| `refactor/` | Code restructuring | `refactor/db-layer` |
| `docs/` | Documentation | `docs/api-guide` |
| `ci/` | CI/CD changes | `ci/add-lint-job` |
| `chore/` | Maintenance | `chore/update-deps` |

### Auth Detection

```bash
# Detect auth method
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
  AUTH="gh"
else
  AUTH="git"
  # Ensure token available
  if [ -z "$GITHUB_TOKEN" ]; then
    if [ -f "${HERMES_HOME:-$HOME/.hermes}/.env" ]; then
      GITHUB_TOKEN=$(grep "^GITHUB_TOKEN=" "${HERMES_HOME:-$HOME/.hermes}/.env" | head -1 | cut -d= -f2 | tr -d '\n\r')
    elif grep -q "github.com" ~/.git-credentials 2>/dev/null; then
      GITHUB_TOKEN=$(grep "github.com" ~/.git-credentials | head -1 | sed 's|https://[^:]*:\([^@]*\)@.*|\1|')
    fi
  fi
fi
echo "Auth method: $AUTH"
```

### Extract Owner/Repo

```bash
REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\.com[:/]||; s|\.git$||')
OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO" | cut -d/ -f2)
echo "Owner: $OWNER, Repo: $REPO"
```

### Verify Access

```bash
# With gh
gh repo view $OWNER/$REPO

# With curl
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO \
  | python3 -c "import sys,json; r=json.load(sys.stdin); print(f'{r[\"full_name\"]} ★{r[\"stargazers_count\"]}')"
```

**Completion criterion:** Auth verified, owner/repo extracted, API accessible.

---

## Branch Creation Strategy

### Sync Main First

```bash
# Always start from updated main
git fetch origin
git checkout main && git pull origin main
```

### Branch Naming Convention

| Prefix | Use Case | Example |
|--------|----------|---------|
| `feat/` | New feature | `feat/add-user-auth` |
| `fix/` | Bug fix | `fix/login-redirect` |
| `refactor/` | Code restructuring | `refactor/db-layer` |
| `docs/` | Documentation | `docs/api-guide` |
| `test/` | Test additions | `test/auth-coverage` |
| `ci/` | CI/CD changes | `ci/add-lint-job` |
| `chore/` | Maintenance | `chore/update-deps` |
| `perf/` | Performance | `perf/cache-queries` |

### Create Branch

```bash
# Create and switch
git checkout -b feat/add-user-authentication

# Verify
git branch --show-current  # should output: feat/add-user-authentication
```

### Branch from Specific Point

```bash
# Branch from specific commit
git checkout -b fix/hotfix-abc abc123

# Branch from tag
git checkout -b fix/v1.x-hotfix v1.2.0
```

**Completion criterion:** On correct branch, main is up-to-date, no uncommitted changes.

---

## Commit Hygiene

### Conventional Commits Format

```
<type>(<scope>): <short description>

<body: explain WHAT and WHY, not HOW>

<footer: references>
```

### Type Reference

| Type | When to Use |
|------|-------------|
| `feat` | New feature/funtionality |
| `fix` | Bug fix |
| `refactor` | Code change (no behavior change) |
| `perf` | Performance improvement |
| `test` | Adding/fixing tests |
| `docs` | Documentation only |
| `ci` | CI/CD changes |
| `chore` | Maintenance, deps, tooling |
| `style` | Formatting (no logic change) |
| `revert` | Revert previous commit |

### Commit Best Practices

```bash
# Stage specific files (never git add . tanpa review)
git add src/auth.py src/models/user.py tests/test_auth.py

# Commit with descriptive message
git commit -m "feat(auth): add JWT-based user authentication

- Add /login and /register endpoints
- Add User model with bcrypt password hashing
- Add auth middleware for protected routes
- Add unit tests for auth flow (90% coverage)

Closes #42"
```

### Commit Rules

1. **One logical change per commit** — jangan campur feature + fix + refactor
2. **Imperative mood** — "add feature" bukan "added feature" atau "adds feature"
3. **Line length** — title ≤ 72 chars, body wrapped at 72 chars
4. **Reference issues** — selalu sertakan `Closes #N` atau `Refs #N`
5. **No WIP commits** — squash sebelum push kalau perlu

### Amend Last Commit

```bash
# Fix last commit message
git commit --amend -m "new message"

# Add forgotten files to last commit
git add forgotten_file.py
git commit --amend --no-edit
```

**Completion criterion:** Commit message follows conventional format, references issue, single logical change.

---

## Push & PR Creation

### Push Branch

```bash
# First push (set upstream)
git push -u origin HEAD

# Subsequent pushes
git push
```

### Create PR — With `gh`

```bash
gh pr create \
  --title "feat(auth): add JWT-based user authentication" \
  --body "## Summary
- Add /login and /register endpoints
- JWT token generation and validation
- Auth middleware for protected routes

## Test Plan
- [x] Unit tests pass (90% coverage)
- [x] Manual testing with curl
- [ ] Integration test with frontend

## Screenshots
N/A — API-only changes

Closes #42" \
  --reviewer "user1,user2" \
  --label "enhancement,security" \
  --base main
```

### Create PR — With `curl`

```bash
BRANCH=$(git branch --show-current)

curl -s -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/$OWNER/$REPO/pulls \
  -d "{
    \"title\": \"feat(auth): add JWT-based user authentication\",
    \"body\": \"## Summary\\n- Add login/register endpoints\\n\\nCloses #42\",
    \"head\": \"$BRANCH\",
    \"base\": \"main\"
  }"
```

### PR Options

| Flag | Effect |
|------|--------|
| `--draft` | Create as draft PR |
| `--reviewer user1,user2` | Request reviewers |
| `--label "enhancement"` | Add labels |
| `--base develop` | Target different base |
| `--project "Sprint 1"` | Add to project board |

### Draft PRs

```bash
# Create draft (not ready for review)
gh pr create --draft --title "WIP: feat: user profile"

# Mark ready when done
gh pr ready
```

**Completion criterion:** PR created, URL returned, CI triggered.

---

## CI Monitoring & Auto-Fix

### Check CI Status

```bash
# With gh
gh pr checks
gh pr checks --watch  # poll until done

# With curl
SHA=$(git rev-parse HEAD)
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/commits/$SHA/status \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(f\"Overall: {data['state']}\")
for s in data.get('statuses', []):
    print(f\"  {s['context']}: {s['state']}\")
"
```

### Poll Until Complete

```bash
SHA=$(git rev-parse HEAD)
for i in $(seq 1 20); do
  STATUS=$(curl -s \
    -H "Authorization: token $GITHUB_TOKEN" \
    https://api.github.com/repos/$OWNER/$REPO/commits/$SHA/status \
    | python3 -c "import sys,json; print(json.load(sys.stdin)['state'])")
  echo "Poll $i: $STATUS"
  if [ "$STATUS" = "success" ] || [ "$STATUS" = "failure" ] || [ "$STATUS" = "error" ]; then
    break
  fi
  sleep 30
done
```

### Get Failure Details

```bash
# With gh
gh run list --branch $(git branch --show-current) --limit 5
gh run view <RUN_ID> --log-failed

# With curl
RUN_ID=<run_id>
curl -sL -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/actions/runs/$RUN_ID/logs \
  -o /tmp/ci-logs.zip
cd /tmp && unzip -o ci-logs.zip -d ci-logs && cat ci-logs/*.txt
```

### Auto-Fix Loop

```
CI Failed
├── Test failure
│   ├── Assertion mismatch → update test or fix logic
│   └── Import/module error → add dependency
├── Lint failure → run formatter, fix style
├── Type error → fix types
├── Build failure
│   ├── Missing dep → add to requirements
│   └── Version conflict → update pins
├── Permission error → update workflow permissions (needs user)
└── Timeout → investigate perf (may need user input)
```

### Auto-Fix Pattern

```bash
# 1. Check status → identify failure
gh pr checks

# 2. Read logs → understand error
gh run view <RUN_ID> --log-failed

# 3. Fix code (use patch/write_file)
# ... fix the issue ...

# 4. Commit & push
git add <fixed_files>
git commit -m "fix: resolve CI failure in <check_name>"
git push

# 5. Re-check CI
gh pr checks --watch
```

### CI Troubleshooting Quick Reference

| Failure | Signature | Fix |
|---------|-----------|-----|
| Test assertion | `assert X == Y` | Update test or fix logic |
| Import error | `ModuleNotFoundError` | Add to requirements.txt |
| Lint | `E302, E501` | Run `ruff check --fix .` |
| Type error | `incompatible type` | Fix type hints |
| Build | `Could not find version` | Pin compatible version |
| Permission | `403 Forbidden` | Add `permissions:` to workflow |
| Timeout | `operation was canceled` | Add `timeout-minutes: N` |
| Docker | `file not found in build context` | Fix COPY path in Dockerfile |

**Completion criterion:** CI green (all checks pass), no failures remaining.

---

## Review Response & Iteration

### Read Review Comments

```bash
# With gh
gh pr view <PR_NUMBER> --comments
gh api repos/$OWNER/$REPO/pulls/<PR_NUMBER>/comments

# With curl
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/<PR_NUMBER>/comments \
  | python3 -c "
import sys, json
for c in json.load(sys.stdin):
    print(f\"{c['user']['login']}: {c['body']}\")
"
```

### Respond to Reviews

```bash
# Acknowledge comment
gh api repos/$OWNER/$REPO/pulls/<PR_NUMBER>/comments/<COMMENT_ID> \
  -f "body: 'Fixed in latest commit, thanks!'"

# Request re-review
gh pr edit <PR_NUMBER> --add-reviewer reviewer_username
```

### Push Review Fixes

```bash
# Make fixes based on review
git add <fixed_files>
git commit -m "fix: address review feedback

- Rename variable per @user1 suggestion
- Add null check per @user2 request"
git push
```

### Resolve Conversations

```bash
# Mark conversation as resolved (via GitHub UI or API)
gh api repos/$OWNER/$REPO/pulls/<PR_NUMBER>/comments/<COMMENT_ID> \
  -X DELETE  # only if you made the comment
```

**Completion criterion:** All review comments addressed, re-review requested.

---

## Merge Strategy

### Merge Methods

| Method | When to Use | Result |
|--------|-------------|--------|
| **Squash** | Feature branches (recommended) | Single clean commit on main |
| **Merge commit** | Long-running features | Preserves full history |
| **Rebase** | Clean linear history | Replays commits on main |

### Merge — With `gh`

```bash
# Squash merge + delete branch (recommended)
gh pr merge --squash --delete-branch

# Merge commit
gh pr merge --merge --delete-branch

# Rebase merge
gh pr merge --rebase --delete-branch

# Auto-merge (waits for CI + reviews)
gh pr merge --auto --squash --delete-branch
```

### Merge — With `curl`

```bash
PR_NUMBER=<number>

# Squash merge
curl -s -X PUT \
  -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/merge \
  -d "{
    \"merge_method\": \"squash\",
    \"commit_title\": \"feat: add user authentication (#$PR_NUMBER)\"
  }"
```

### Enable Auto-Merge

```bash
# Get PR node ID
PR_NODE_ID=$(curl -s \
  -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['node_id'])")

# Enable auto-merge via GraphQL
curl -s -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/graphql \
  -d "{\"query\": \"mutation { enablePullRequestAutoMerge(input: {pullRequestId: \\\"$PR_NODE_ID\\\", mergeMethod: SQUASH}) { clientMutationId } }\"}"
```

### Merge Rules

1. **CI must be green** — never merge with failing checks
2. **At least 1 approval** — unless solo project
3. **No unresolved conversations** — resolve all review threads
4. **Up-to-date with base** — rebase if main has diverged
5. **Squash for feature branches** — keep main history clean

**Completion criterion:** PR merged, branch deleted, main updated.

---

## Post-Merge Cleanup

### Local Cleanup

```bash
# Switch to main
git checkout main && git pull origin main

# Delete local branch
git branch -d feat/add-user-authentication

# Delete remote branch (if not auto-deleted)
git push origin --delete feat/add-user-authentication

# Prune stale remote-tracking branches
git fetch --prune
```

### Verify Merge

```bash
# Check commit on main
git log --oneline -5

# Verify branch deleted
git branch -a | grep feat/add-user-authentication  # should be empty
```

### Update Related Issues

```bash
# Close linked issue (auto-closes if PR body has "Closes #N")
gh issue close <ISSUE_NUMBER> --reason "completed"

# Or add comment
gh issue comment <ISSUE_NUMBER> --body "Merged in PR #<PR_NUMBER>"
```

**Completion criterion:** Main updated, local/remote branches deleted, issues closed.

---

## Error Mapping & Troubleshooting

### Common Errors

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `fatal: not a git repository` | Di luar git repo | `cd` ke repo atau `git init` |
| `Authentication failed` | Token expired/invalid | `gh auth login` atau refresh token |
| `Merge conflict` | Base branch diverged | Rebase: `git rebase main` |
| `CI timeout` | Job terlalu lama | Tambah `timeout-minutes` di workflow |
| `Permission denied` | Token scope kurang | Tambah `contents: write` permission |
| `Branch protection` | Rules tidak terpenuhi | Cek repo Settings → Branches |
| `Draft PR cannot be merged` | PR masih draft | `gh pr ready` dulu |

### Conflict Resolution

```bash
# 1. Fetch latest main
git fetch origin main

# 2. Rebase on main
git rebase origin/main

# 3. Resolve conflicts (edit files)
# ... fix conflicts ...

# 4. Continue rebase
git add <resolved_files>
git rebase --continue

# 5. Force push (only for feature branches)
git push --force-with-lease
```

### Recovery Patterns

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Recover deleted branch
git reflog
git checkout -b recovered-branch <SHA>

# Undo merge (if not pushed)
git reset --hard HEAD~1
```

**Completion criterion:** Error resolved, PR back on track.

---

## Pola Harian—Recipes Siap Pakai

### 1. Quick Fix PR (5 menit)

```bash
# Sync → Branch → Fix → Commit → Push → PR → Merge
git checkout main && git pull
git checkout -b fix/typo-in-readme
# ... fix ...
git add README.md
git commit -m "docs: fix typo in README"
git push -u origin HEAD
gh pr create --title "docs: fix typo" --body "Closes #N"
gh pr merge --squash --delete-branch
```

### 2. Feature PR dengan CI Check

```bash
git checkout main && git pull
git checkout -b feat/user-profile
# ... implement feature ...
git add .
git commit -m "feat: add user profile page"
git push -u origin HEAD
gh pr create --title "feat: user profile" --body "## Summary\n- Add profile page\n\n## Test Plan\n- [ ] Tests pass"
gh pr checks --watch
# Fix CI if needed, then:
gh pr merge --squash --delete-branch
```

### 3. Hotfix PR (urgent)

```bash
git checkout main && git pull
git checkout -b fix/critical-security-bug
# ... fix ...
git add .
git commit -m "fix: patch SQL injection vulnerability"
git push -u origin HEAD
gh pr create --title "fix: critical security patch" --body "URGENT: SQL injection fix" --label "security,hotfix"
gh pr merge --squash --delete-branch
```

### 4. Draft PR (WIP)

```bash
git checkout -b feat/large-refactor
# ... partial work ...
git add .
git commit -m "wip: start database refactor"
git push -u origin HEAD
gh pr create --draft --title "WIP: database refactor"

# Later, when ready:
gh pr ready
```

### 5. PR dengan Multiple Reviewers

```bash
gh pr create \
  --title "feat: payment integration" \
  --body "## Summary\n- Stripe integration\n\n## Test Plan\n- [ ] Unit tests\n- [ ] Integration tests" \
  --reviewer "alice,bob,charlie" \
  --label "enhancement,payments" \
  --project "Q2 Sprint"
```

### 6. Rebase Before Merge

```bash
# Update branch with latest main
git checkout feat/my-feature
git fetch origin
git rebase origin/main
# Resolve conflicts if any
git push --force-with-lease

# Then merge
gh pr merge --squash --delete-branch
```

### 7. Auto-Merge Setup

```bash
# Create PR with auto-merge
gh pr create --title "feat: X" --body "..."
gh pr merge --auto --squash --delete-branch
# PR will auto-merge when CI passes + reviews approved
```

**Completion Criterion per Recipe:**
- Quick Fix: Merged in < 5 menit
- Feature PR: CI green, reviewed, merged
- Hotfix: Merged within 1 hour
- Draft PR: Marked ready when complete
- Multi-reviewer: All reviewers approve
- Rebase: No conflicts, clean history
- Auto-merge: Merged automatically when conditions met

---

## Anti-Patterns & Pitfalls

### 1. Commit Langsung ke Main
**Masalah:** No review, no CI check, breaking changes langsung live
**Fix:** Selalu buat branch → PR → review → merge

### 2. `git add .` Tanpa Review
**Masalah:** File sensitif (.env, credentials) ikut ter-commit
**Fix:** Stage per-file, cek `git diff --cached` sebelum commit

### 3. PR Terlalu Besar (>500 lines)
**Masalah:** Review lambat, conflict sering, susah debug
**Fix:** Split jadi multiple smaller PRs

### 4. Merge Tanpa CI Green
**Masalah:** Broken code masuk main
**Fix:** Selalu tunggu CI hijau sebelum merge

### 5. Force Push ke Main
**Masalah:** Overwrite history, hilang commit orang lain
**Fix:** `--force-with-lease` hanya untuk feature branch, NEVER main

### 6. Lupa Delete Branch
**Masalah:** Branch menumpuk, repo berantakan
**Fix:** `--delete-branch` saat merge, atau periodic cleanup

### 7. Commit Message "fix stuff"
**Masalah:** Tidak jelas apa yang di-fix
**Fix:** Conventional commits format dengan deskripsi jelas

### 8. Skip Review untuk "Small Changes"
**Masalah:** Small changes bisa break everything
**Fix:** Semua changes melalui PR, minimal 1 review

---

## Verification Checklist

Sebelum menutup PR atau memulai task baru:

- [ ] Branch up-to-date dengan main
- [ ] Semua commits follow conventional format
- [ ] PR body lengkap: Summary, Test Plan, References
- [ ] CI green (all checks pass)
- [ ] Semua review comments addressed
- [ ] No unresolved conversations
- [ ] Merge method sesuai (squash/merge/rebase)
- [ ] Branch deleted setelah merge
- [ ] Local main updated (`git pull`)
- [ ] Staging branch dibersihkan
- [ ] Related issues ditutup
- [ ] No secrets terbuka di commit history

---

## Quick Reference Card

```
AUTH       → gh auth login / export GITHUB_TOKEN
BRANCH     → git checkout -b feat/description
STAGE      → git add <files> (NEVER git add .)
COMMIT     → git commit -m "type(scope): description"
PUSH       → git push -u origin HEAD
PR CREATE  → gh pr create --title "..." --body "..."
PR CHECK   → gh pr checks --watch
PR MERGE   → gh pr merge --squash --delete-branch
PR CLEANUP → git checkout main && git pull && git branch -d <branch>

CONVENTIONAL COMMITS:
  feat:     new feature
  fix:      bug fix
  refactor: code restructuring
  docs:     documentation
  test:     tests
  ci:       CI/CD changes
  chore:    maintenance
  perf:     performance

MERGE METHODS:
  --squash   → single commit (recommended)
  --merge    → merge commit
  --rebase   → linear history
  --auto     → auto-merge when ready
```

---

Sumber: https://cli.github.com/manual/gh
Rebuild untuk Hermes Agent workflow — 2026-06-28
