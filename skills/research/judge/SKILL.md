---
name: judge
description: "Evaluasi + routing keputusan untuk pipeline intel. Score candidates, decide accept/reject/defer, route to next stage. Part of multi-agent-orchestrator intel pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [judgment, scoring, triage, ranking, routing, selection]
    related_skills: [scout, research-verifier, search-engineering]
---

# Judge — Evaluation & Routing Protocol

## Purpose
Evaluasi + routing keputusan untuk pipeline intel. Score candidates, decide accept/reject/defer, route to next stage.

## When to Use
- User asks to triage findings, score options, or rank outputs
- After research-verifier returns validated evidence
- Need to decide which items proceed to production pipeline

## Do
- Score each item against explicit criteria (Relevance 35%, Quality 30%, Timeliness 20%, Actionability 15%)
- Decide: accept, reject, defer, or needs_more_info
- Explain decision in one concise line per item
- Rank strongest candidates first

## Don't
- Use intuition over explicit criteria
- Accept items with only Tier 7-9 sources
- Reject without stating reason
- Rank when accept/reject is sufficient

## Output Format
```
## JUDGMENT

### Accepted (N)
1. [Item] (Score: A, 92) → BUILD — Perfect relevance + verified

### Rejected (N)
1. [Item] (Score: F, 15) — Misaligned with goal

### Deferred (N)
1. [Item] (Score: B, 65) — Needs refinement in [area]

### Needs More Info (N)
1. [Item] (Score: C, 45) — Evidence gaps in [area]
```

## Pipeline Position
Part of multi-agent-orchestrator intel pipeline. Feed accepted items ke builder-drafter.

---

## Core Rules

1. **Score each item** against the task goal and relevance criteria.
2. **Decide: accept, reject, defer, or needs_more_info.**
3. **Prefer explicit criteria** over intuition.
4. **Explain the decision in one concise line** per item.
5. **Detect duplicates, weak evidence, and misaligned items.**
6. **When multiple candidates exist, rank the strongest first.**
7. **If the task is not ready to continue, state what is missing.**
8. **Keep decisions consistent, deterministic, and easy to audit.**

---

## Daftar Isi

1. [Evaluation Scoring](#evaluation-scoring)
2. [Decision Categories](#decision-categories)
3. [Scoring Criteria](#scoring-criteria)
4. [Duplicate & Conflict Detection](#duplicate--conflict-detection)
5. [Ranking](#ranking)
6. [Routing Format](#routing-format)
7. [Blocking Items](#blocking-items)
8. [Judge Recipes](#judge-recipes)
9. [Pitfalls](#pitfalls)

---

## Evaluation Scoring

### Score Range

| Score | Grade | Verdict |
|-------|-------|---------|
| 90-100 | A+ | ACCEPT — meets all criteria |
| 75-89 | A | ACCEPT — meets most criteria |
| 60-74 | B | DEFER — partially meets, needs refinement |
| 40-59 | C | NEEDS_MORE_INFO — gaps in evidence |
| 20-39 | D | REJECT — misaligned |
| 0-19 | F | REJECT — irrelevant or invalid |

### Scoring Formula

```
Score = Relevance × 0.35 + Quality × 0.30 + Timeliness × 0.20 + Actionability × 0.15

Where:
  Relevance    = how well it matches the goal (0-100)
  Quality      = evidence strength + source tier (0-100)
  Timeliness   = freshness and urgency (0-100)
  Actionability = can we act on it? (0-100)
```

### Score Interpretation

| Component | High Score Indicators | Low Score Indicators |
|-----------|----------------------|---------------------|
| **Relevance** | Same domain, same use case | Different domain, different use case |
| **Quality** | Tier 1 source, code evidence | Tier 8-9 source, no evidence |
| **Timeliness** | Today-this week | >1 month old |
| **Actionability** | Specific action possible | Abstract, no next step |

---

## Decision Categories

### ACCEPT — proceed

```
Decision: ACCEPT
Item: [Title]
Reason: [One line: why it passes]
Score: A (85)
Route: [Where it goes next] → Build / Deploy / Analyze / etc
```

### REJECT — discard

```
Decision: REJECT
Item: [Title]
Reason: [One line: why it fails]
Score: F (15)
Route: DISCARD
```

### DEFER — pending quality/relevance improvement

```
Decision: DEFER
Item: [Title]
Reason: [One line]
Score: B (65)
Route: PENDING — [what needs to improve]
```

### NEEDS_MORE_INFO — gaps in evidence

```
Decision: NEEDS_MORE_INFO
Item: [Title]
Reason: [One line]
Score: C (45)
Route: ESCALATE → [Researcher / Verifier / etc]
```

### WAIT — timing issue

```
Decision: WAIT
Item: [Title]
Reason: [One line]
Score: B (70)
Route: HOLD — [by when? What triggers re-evaluation?]
```

---

## Scoring Criteria

### Relevance (0-100)

| Score | Criteria |
|-------|----------|
| 90-100 | Same domain + same use case |
| 70-89 | Same domain, adjacent use case |
| 50-69 | Adjacent domain, similar use case |
| 30-49 | Tangentially related |
| 0-29 | Unrelated |

### Quality (0-100)

| Component | Weight | High Indicators | Low Indicators |
|-----------|--------|----------------|----------------|
| Source authority | 50% | Tier 1-2 | Tier 7-9 |
| Evidence strength | 30% | Code + data + verified | Opinion + speculation |
| Evidence recency | 20% | <3 months | >1 year |

### Timeliness (0-100)

| Score | Freshness |
|-------|----------|
| 90-100 | Today — this week |
| 70-89 | This month |
| 50-69 | This quarter |
| 30-49 | This year |
| 0-29 | >1 year or undated |

### Actionability (0-100)

| Score | Criteria |
|-------|----------|
| 90-100 | Specific action + clear next step |
| 70-89 | Action defined, next step implied |
| 50-69 | Vague action, needs refinement |
| 30-49 | Abstract, no clear action |
| 0-29 | Pure information, no action possible |

---

## Duplicate & Conflict Detection

### Duplicate Detection

```
For each candidate, check:
1. Same content (title + source)?
2. Same finding from different sources?
3. Same recommendation from different agents?

If duplicate → KEEP strongest, REJECT weaker
```

### Conflict Detection

```
If two candidates:
├── Contradict each other → FLAG conflict, defer both
├── Partially overlap → KEEP more complete, reject fragment
└── Address different aspects → Keep both, rank by score
```

### Merge Candidates

```
If multiple partial items address same goal:
1. Merge evidence from each
2. Keep strongest source per claim
3. Deduplicate data points
4. Score merged item
```

---

## Ranking

### Ranking Protocol

1. Score all items
2. Sort by score (highest first)
3. Apply elimination rules:
   - REJECT items below 40
   - DEFER items 40-59 with improvement path
   - ACCEPT items 60+
4. For ACCEPT items, rank by score
5. If tie, prefer higher actionability

### Rank Output Format

```
## Rankings

| Rank | Item | Score | Decision | Reason |
|------|------|-------|----------|--------|
| 1 | [A] | 92 | ACCEPT | Perfect relevance + verified |
| 2 | [B] | 85 | ACCEPT | High relevance, minor gap |
| 3 | [C] | 71 | DEFER | Good but needs refinement |
| 4 | [D] | 55 | NEEDS_MORE_INFO | Evidence gaps |
| 5 | [E] | 23 | REJECT | Misaligned |
```

### Tie-Breaker Rules

```
Same score?
1. Higher relevance wins
2. Higher actionability wins
3. Higher timeliness wins
4. Higher quality wins
5. If still tied → list alphabetically
```

---

## Routing Format

### Standard Routing Output

```
## JUDGMENT

### Accepted (N)
1. [Item] (Score: A) → [Next step]
2. [Item] (Score: A-) → [Next step]

### Rejected (N)
1. [Item] (Score: F) — [Reason]
2. [Item] (Score: D) — [Reason]

### Deferred (N)
1. [Item] (Score: B) — [What needs to improve]

### Needs More Info (N)
1. [Item] (Score: C) — [What's missing]

### Waiting (N)
1. [Item] (Score: B+) — [What event triggers re-eval]
```

### Routing Codes

| Code | Destination | Meaning |
|------|-------------|---------|
| `→ BUILD` | Builder-Drafter | Ready for implementation |
| `→ DEPLOY` | Handoff-Committer | Ready for delivery |
| `→ VERIFY` | Research-Verifier | Needs verification |
| `→ SEARCH` | Search-Engineering | Needs more data |
| `→ SCOUT` | Scout | Monitor for changes |
| `→ ANALYZE` | Analysis agent | Deep dive needed |
| `→ HOLD` | Queue | Wait for condition |
| `→ DISCARD` | Trash | Drop entirely |

---

## Blocking Items

### Blockers

```
Item: [Title]
Blocks: [What it blocks]
Reason: [Why it's blocking]
Missing: [What's needed to unblock]
```

### Dependency Chain

```
Item A → Item B → Item C
         ↑
     BLOCKER: B needs A to be resolved first
```

### Unblock Protocol

```
1. Identify blocker
2. Route blocker to appropriate agent
3. Queue dependent items
4. Set re-evaluation trigger
5. Report status to user
```

---

## Judge Recipes

### Recipe 1: Judge Research Findings

```
Goal: Decide which findings to include in report

Scoring:
- Relevance to user's question (35%)
- Evidence strength (30%)
- Date <6 months (20%)
- Can user act on it (15%)

Findings:
1. "X is faster than Y" — Tier 1, 2026, benchmark → ACEPT (A+)
2. "Might be useful" — Tier 6, speculation, no action → REJECT (F)
3. "Similar to X" — duplicate of #1 → REJECT (dup)
```

### Recipe 2: Judge Tool Selection

```
Goal: Choose best tool for task

Criteria:
- Relevance to task (35%)
- Quality/reliability (30%)
- Maintenance status (20%)
- User familiarity (15%)

Tools:
1. Tool A — same purpose, actively maintained, user knows it
2. Tool B — new but untested, user unfamiliar
3. Tool C — deprecated, security issues
```

### Recipe 3: Judge Implementation Approaches

```
Goal: Decide between approaches X, Y, Z

Scoring:
- Correctness potential (35%)
- Risk of bugs/complexity (30%)
- Implementation time (20%)
- Maintenance cost (15%)
```

### Recipe 4: Judge PR Candidates

```
Goal: Decide which PR to merge first

Scoring:
- CI status (30%)
- Review score (30%)
- Priority (25%)
- Dependencies (15%)
```

### Recipe 5: Judge Information Relevance

```
Goal: Filter N findings to top 5

Scoring:
- Directly answers question (40%)
- Source quality (30%)
- Actionable (30%)

Apply: Score → Sort → Top 5 → Reject rest
```

---

## Pitfalls

### 1. Scoring Inconsistency
**Masalah:** Same item scored differently across sessions
**Fix:** Always use the 4-component formula with same weights

### 2. Intuition Over Criteria
**Masalah:** "This feels right" decision
**Fix:** Every decision must have explicit criteria backing

### 3. Weak Evidence Acceptance
**Masalah:** Accepting items with Tier 7-9 sources
**Fix:** Cap accepted items at Tier 4+ average

### 4. Forgotten Blockers
**Masalah:** Routing items that depend on unresolved items
**Fix:** Check dependency chain before routing

### 5. Over-Ranking
**Masalah:** Trying to rank when accept/reject is sufficient
**Fix:** Only rank ACCEPTED items

### 6. Rejection Without Reason
**Masalah:** "Not sure, rejecting"
**Fix:** Every reject must have explicit score + reason

### 7. Stale Decisions
**Masalah:** Not re-evaluating deferred items
**Fix:** Set re-evaluation trigger with every defer

### 8. Biased Scoring
**Masalah:** Giving higher scores to preferred options
**Fix:** Score components independently, then calculate

---

## Quick Reference Card

```
SCORING:
  Relevance (35%)     = match to goal
  Quality (30%)       = evidence + source
  Timeliness (20%)    = freshness
  Actionability (15%) = can we act?

DECISIONS:
  ACCEPT     → Score ≥60, route to next step
  REJECT     → Score <40, discard
  DEFER      → Score 40-59, queue with improvement path
  NEEDS_INFO → Score 40-55, send to researcher
  WAIT       → Temporal blocker, hold

RANKING:
  Score → Sort → Eliminate <40 → Rank ACCEPTED
  Tie: relevance > actionability > timeliness > quality

ROUTING CODES:
  → BUILD    → Ready for implementation
  → DEPLOY   → Ready for delivery
  → VERIFY   → Needs verification
  → SEARCH   → Needs more data
  → HOLD     → Wait condition
  → DISCARD  → Drop
```

---

Sumber: Hermes Agent judgment workflow pattern
Created — 2026-06-28
