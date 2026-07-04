---
name: scout
description: "Discovery awal untuk pipeline intel. Cari sinyal baru, opportunities, changes. Feed output ke search-engineering. Part of multi-agent-orchestrator intel pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [scout, discovery, monitoring, signals, opportunities, research]
    related_skills: [search-engineering, blogwatcher, session-search]
---

# Scout — Signal Discovery Protocol

## Purpose
Discovery awal untuk pipeline intel. Cari sinyal baru, opportunities, changes.

## When to Use
- User asks to scout, monitor, atau discover new opportunities
- Need broad scan before focused search
- Monitoring domain for changes

## Do
- Cast wide net first (5-8 queries)
- Filter noise and duplicates aggressively
- Summarize findings compact: what/why/action
- Feed output ke search-engineering

## Don't
- Fully analyze or solve — that's verifier/judge's job
- Return more than 5 high-signal findings
- Include outdated items (>1 week)
- Accept unverified claims

## Output Format
```
� [CATEGORY]: [Title](URL) — What: [sentence]. Why: [sentence]. Action: [step].
```

## Pipeline Position
Part of multi-agent-orchestrator intel pipeline. Feed output ke search-engineering.

---

## Core Rules

1. **Look for fresh, high-signal opportunities, changes, issues, or sources.**
2. **Prefer breadth first**, then surface the most relevant items.
3. **Capture only the minimum useful evidence** needed for triage.
4. **Filter out obvious noise, duplicates, and low-value findings.**
5. **Summarize each finding in a compact, structured way.**
6. **Include why it matters and why it should be escalated.**
7. **Do not fully analyze or solve** — your job is discovery and triage.
8. **Keep output short, sharp, and action-oriented.**

---

## Daftar Isi

1. [Scout Dimensions](#scout-dimensions)
2. [Breadth-First Search Strategy](#breadth-first-search-strategy)
3. [Signal Filtering](#signal-filtering)
4. [Noise Rejection](#noise-rejection)
5. [Finding Format](#finding-format)
6. [Triage Classification](#triage-classification)
7. [Escalation Criteria](#escalation-criteria)
8. [Scout Recipes](#scout-recipes)
9. [Pitfalls](#pitfalls)

---

## Scout Dimensions

### What to Look For

| Dimension | Examples |
|-----------|----------|
| **New releases** | Library versions, tool updates, API changes |
| **Trending repos** | GitHub stars surging, new GitHub trending |
| **Security alerts** | CVEs, exploit reports, dependency vulnerabilities |
| **Community signals** | Reddit threads, HN posts, Twitter discussions |
| **Breaking changes** | Deprecation notices, migration warnings |
| **Opportunities** | Free tiers, new APIs, open source projects |
| **Competitive shifts** | New tools, pricing changes, acquisitions |
| **Technical breakthroughs** | New papers, benchmarks, architecture patterns |

### What NOT to Scout

- Already-known items (check session history first)
- Items older than 1 week (unless specifically requested)
- Content already in user's workflow (existing skills, current projects)
- Minor patch releases (bug fixes without new features)
- Opinion pieces without actionable content

---

## Breadth-First Search Strategy

### Search Layers

```
Layer 1: Broad scan (multiple queries, multiple sources)
  → Goal: Cast wide net, 30-60 seconds

Layer 2: Signal triage (filter & rank)
  → Goal: Separate signal from noise, 10-20 seconds

Layer 3: Deep scan on top signals (2-3 per scout)
  → Goal: Verify quality before escalate, 10-15 seconds
```

### Source Coverage

| Source | URL Pattern | What to Find |
|--------|-------------|--------------|
| GitHub Trending | github.com/trending | New repos gaining stars |
| Hacker News | news.ycombinator.com | Tech discussions |
| Reddit (r/programming, etc.) | reddit.com/r/... | Community discussions |
| Twitter/X | Search API | Announcements, hot takes |
| Blog feeds | RSS feeds | Release posts, tutorials |
| CVE Database | nvd.nist.gov | Security vulnerabilities |
| Package registries | pypi.org, npmjs.com | New package releases |

### Query Strategy

```
Goal: "Find new AI coding tools"

Broad queries (5-8):
1. "AI coding assistant" stars:>100 site:github.com
2. "code generation" release 2025 2026
3. "best AI tools for developers" this week
4. r/programming AI coding
5. hn "show" AI coding CLI

Then narrow: which 2-3 have highest signal?
```

---

## Signal Filtering

### Signal Quality Matrix

| Quality | Characteristic | Action |
|---------|---------------|--------|
| **High** | Authoritative source, recent, directly relevant | Escalate immediately |
| **Medium** | Good source, somewhat relevant | Escalate with caveat |
| **Low** | Weak source, tangentially relevant | Skip unless pattern emerges |
| **Noise** | Unverified, duplicate, outdated | Skip |

### Signal Indicators

| Indicator | Weight |
|-----------|--------|
| Timestamped within 7 days | +20 |
| From primary source (GitHub, official) | +20 |
| Has code/data/evidence | +15 |
| Multiple sources confirm | +15 |
| Directly relevant to user's domain | +10 |
| Actionable (can do something with it) | +10 |
| Novel (not seen before) | +10 |

### Triage Decision Tree

```
Finding:
├── High signal + recent + relevant → ESCALATE
├── Medium signal + potentially useful → QUEUE for next scout
├── Low signal → SKIP
├── Duplicate of known item ├── SKIP
└── Outdated (>1 week) → SKIP
```

---

## Noise Rejection

### Noise Patterns

| Pattern | Why It's Noise | Action |
|---------|---------------|--------|
| Duplicate content | Same story, different aggregator | Skip |
| Clickbait headline | No substance behind headline | Skip |
| AI-generated spam | Low-value, auto-generated | Skip |
| Minor patch release | v1.2.3 → v1.2.4, no new features | Skip |
| Stale news | >1 week, no ongoing relevance | Skip |
| Pure opinion | No data, no evidence, no actionable | Skip |
| Marketing content | Company blog, promotional | Skip unless substantive |
| Framework war | "X vs Y" with no new information | Skip |

### Duplicate Detection

Before escalating, check:
1. Is this the same as a previous scout result?
2. Was this already discussed in a session?
3. Is this already in the user's workflow?

If yes to any → skip or note as "relevant: [previous date]"

---

## Finding Format

### Finding Template

```
### FINDING: [TITLE]

**Source:** [Tier] [Source Name](URL)
**Date:** [YYYY-MM-DD]
**Category:** [release/opportunity/security/community]

**What:** [One sentence: what happened or exists]

**Why it matters:** [One sentence: why user should care]

**Action:** [Specific action to take or investigate further]

**Confidence:** HIGH | MEDIUM | LOW
```

### Minimal Finding (for quick scanning)

```
� [CATEGORY]: [Title](URL) — What [one sentence]. Why: [one sentence].
� [CATEGORY]: [Title](URL) — What: [one sentence]. Why: [one sentence].
```

### Category Tags

| Tag | Color | Meaning |
|-----|-------|---------|
| `RELEASE` | � | New version, launch |
| `SECURITY` | 🔴 | Vulnerability, exploit |
| `TREND` | � | Growing project/trend |
| `OPPORTUNITY` | 💰 | Free tier, new API, tool |
| `COMMUNITY` | 💬 | Discussion, debate |
| `CHANGE` | ⚠️ | Breaking change, deprecation |
| `KNOWLEDGE` | 📚 | Tutorial, paper, insight |

---

## Triage Classification

### Triage Buckets

| Bucket | Definition | Next Action |
|--------|-----------|-------------|
| **ESCALATE** | High signal, high relevance | Feed into workflow immediately |
| **QUEUE** | Medium signal, monitor | Check again in next scout |
| **SKIP** | Low signal or noise | Drop |
| **WATCH** | Early signal, not mature yet | Monitor without action |

### Escalation Priority

```
Priority 1: Security issues → ESCALATE NOW
Priority 2: Breaking changes in tools user uses → ESCALATE TODAY
Priority 3: New features in domain of interest → ESCALATE THIS WEEK
Priority 4: Opportunities (free tools, APIs) → QUEUE
Priority 5: Interesting but not urgent → QUEUE
```

---

## Escalation Criteria

### Must Escalate

- Security vulnerability in dependency user uses
- Breaking change in tool/library user depends on
- New release of tool user actively uses
- Major opportunity (free API, open source replacement)
- New GitHub project with rapid star growth in user's domain

### Should Escalate (with context new library in adjacent domain
- New API that could simplify existing workflow
- Community discussion about tool user uses
- Trend in technology user is interested in

### Should NOT Escalate

- Items already known to user
- Items outside user's domain
- Unverified claims
- Marketing content
- Stale news (>1 week)

---

## Scout Recipes

### Recipe 1: New Tool Discovery

```
Goal: Find new AI coding tools

Queries:
1. "AI coding assistant" stars:>50 site:github.com since:>2026-06-01
2. "CLI code generation" new release
3. r/LocalLLaMA new tools
4. hn "show" code assistant
5. Twitter/X AI coding new

Filter: Remove tools already known
Output: Top 3 new tools with evidence
```

### Recipe 2: Security Monitoring

```
Goal: Scout for security issues in dependencies

Queries:
1. CVE user's dependencies (check pyproject.toml / package.json)
2. "python security vulnerability" this week
3. npm audit / pip audit results
4. New CVE entries for packages used
5. Security advisories on GitHub

Filter: Only HIGH/CRITICAL severity
Output: Actionable vulnerabilities with fix versions
```

### Recipe 3: Technology Trend

```
Goal: Scout trends in domain X

Queries:
1. Domain keywords site:news.ycombinator.com
2. Domain stars:>1000 site:github.com weekly trending
3. Domain keywords reddit:this week
4. Domain keywords twitter:this week
5. Conference talks, new books, courses
```

### Recipe 4: Opportunity Discovery

```
Goal: Find free tools, APIs, or opportunities

Queries:
1. "free API" [domain] no auth required
2. "open source alternative" to [paid tool] site:github.com
3. "free tier" [category] API 2025 2026
4. GitHub trending CLI tools
5. New developer tools with free plan
```

### Recipe 5: Competitive Monitoring

```
Goal: Monitor changes in tools X, Y, Z

Queries:
1. Tool X changelog release
2. Tool Y new features
3. Tool Z pricing change
4. Community discussions about X, Y, Z
5. Alternatives to X, Y, Z gaining traction
```

---

## Pitfalls

### 1. Analysis Paralysis
**Masalah:** Trying to fully analyze each finding
**Fix:** Discovery only — leave analysis to verifier

### 2. Over-Scanning
**Masalah:** 50 findings, none useful
**Fix:** Stop at 5 high-signal findings

### 3. Noise Blindness
**Masalah:** Missing real signal because of noise
**Fix:** Use noise rejection patterns strictly

### 4. Recency Bias
**Masalah:** Only looking at today's content
**Fix:** Some valuable signals are 1-2 weeks old

### 5. Domain Drift
**Masalah:** Finding interesting but irrelevant content
**Fix:** Always filter against user's domain/workflow

### 6. Duplicate Flood
**Masalah:** Same story from 5 sources
**Fix:** Deduplicate before reporting

### 7. Action Without Triage
**Masalah:** Escalating everything
**Fix:** Use triage buckets strictly

### 8. Vague Findings
**Masalah:** "Found something interesting"
**Fix:** What, why, action — mandatory fields

---

## Quick Reference Card

```
 SCOUT FLOW:
  Broad Scan → Triage → Top Signals → Report

SOURCES:
  GitHub Trending, HN, Reddit, Twitter/X, CVE DB, Package Registries

SIGNAL vs NOISE:
  High: Authoritative + recent + relevant + novel
  Noise: Duplicate + stale + unverified + irrelevant

FINDING FORMAT:
  [CATEGORY]: [Title] — What: [sentence]. Why: [sentence]. Action: [step].

TRIAGE:
  P1 (SECURITY) → Escalate NOW
  P2 (BREAKING) → Escalate TODAY
  P3 (FEATURE)  → Escalate THIS WEEK
  P4 (OPPORTUNITY) → Queue
  P5 (INTERESTING) → Queue
  NOISE → Skip

RULES:
  ✅ Do: Discover + triage
  ❌ Don't: Analyze + solve
  ✅ Do: Short, sharp, actionable
  ❌ Don't: Long analysis
```

---

Sumber: Hermes Agent discovery workflow pattern
Created — 2026-06-28
