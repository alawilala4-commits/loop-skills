---
name: search-engineering
description: "Pencarian sumber terfokus untuk pipeline intel. Convert vague requests → strong queries. Feed output ke research-verifier. Part of multi-agent-orchestrator intel pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [search, research, web, queries, evidence, analysis]
    related_skills: [web, session-search, blogwatcher]
---

# Search Engineering — Query Construction & Source Discovery

## Purpose
Pencarian sumber terfokus untuk pipeline intel. Convert vague requests → strong queries.

## When to Use
- User asks to search, research, or find information online
- After scout returns findings, need focused source discovery
- Need authoritative sources for verification

## Do
- Convert vague goals into keyword-based queries
- Use multiple short queries (3-5) for coverage
- Prefer authoritative + recent sources
- Separate facts, opinions, speculation

## Don't
- Use single long query instead of multiple short ones
- Return summaries of summaries
- Over-explain — focus on high-signal results

## Output Format
```
## Research: <TOPIC>

### Key Findings
1. [FACT] — Strong evidence (Tier 1 source)
2. [FACT] — Moderate evidence (Tier 2 source)
3. [OPINION] — Multiple sources agree

### Strongest Sources
1. [Title](URL) (Tier 1) — Key takeaway
2. [Title](URL) (Tier 2) — Key takeaway

### Gaps & Contradictions
- [What is missing or disputed]

### Recommendation
[Actionable takeaway]
```

## Pipeline Position
Part of multi-agent-orchestrator intel pipeline. Feed output ke research-verifier.

---

## Core Rules

1. **Convert the user goal into focused, keyword-based search queries.**
2. **Use multiple short queries** when that improves coverage.
3. **Prefer authoritative and recent sources** when the topic is time-sensitive.
4. **Separate facts, opinions, and speculation.**
5. **Return a concise summary of what was found**, with the strongest sources first.
6. **Note gaps, contradictions, or weak evidence clearly.**
7. **Do not over-explain** — focus on high-signal results.
8. **If the query is ambiguous**, propose the most likely interpretation and search that first.

---

## Daftar Isi

1. [Query Construction](#query-construction)
2. [Multi-Query Strategy](#multi-query-strategy)
3. [Source Evaluation](#source-evaluation)
4. [Output Format](#output-format)
5. [Ambiguity Resolution](#ambiguity-resolution)
6. [Time-Sensitive Research](#time-sensitive-research)
7. [Research Recipes](#research-recipes)
8. [Pitfalls](#pitfalls)

---

## Query Construction

### Vague → Focused Transformation

| Vague Request | Focused Query |
|---------------|---------------|
| "AI tools for coding" | `best AI coding assistants 2025 site:github.com OR site:medium.com` |
| "learn Python" | `Python 3.13 tutorial beginner project-based 2025` |
| "what is MCP" | "Model Context Protocol"Anthropic MCP specification` |
| "termux problems" | `Termux Android 16 fix errors 2025 site:wiki.termux.com OR site:reddit.com` |
| "free API for text" | `free text generation API no auth 2025 site:github.com` |

### Query Construction Formula

```
[TOPIC] + [VERSION/CONTEXT] + [QUALIFIER] + [SOURCE_FILTER]

Examples:
  "claude code CLI" + "v2" + "install Termux" + "site:docs.anthropic.com"
  "python CLI app" + "3.13" + "JSON persistence tutorial" + "site:real-python.com"
  "github actions" + "" + "python unittest CI" + "site:docs.github.com"
```

### Query Modifiers

| Modifier | Effect | Example |
|----------|--------|---------|
| `"exact phrase"` | Match exact phrase | `"Model Context Protocol"` |
| `site:` | Filter by domain | `site:docs.python.org` |
| `-exclude` | Exclude term | `tutorial -beginner -basic` |
| `filetype:` | Filter by file | `filetype:pdf` |
| `after:` | Date filter | `after:2025-01-01` |
| `OR` | Alternative terms | `site:github.com OR site:medium.com` |

### Query Length Sweet Spot

- **3-6 keywords** — sweet spot untuk specificity + coverage
- **< 3 keywords** — too broad, noise tinggi
- **> 8 keywords** — too narrow, miss relevant results
- **Multiple short queries** — better than one long query

---

## Multi-Query Strategy

### When to Use Multiple Queries

- Topic has multiple aspects (e.g., "AI tools" → coding + writing + search)
- Single query returns poor results
- Need comparative data (e.g., Tool A vs Tool B)
- Time-sensitive topic need recent sources

### Query Fan Pattern

```
Goal: "Find best free AI coding tools"

Query 1: "best free AI coding assistant 2025"             (umbrella)
Query 2: "cursor IDE free tier features"                    (specific tool)
Query 3: "github copilot free alternative teachers"         (specific tool)
Query 4: "windsurf codeium free AI code generation"         (specific tool)
Query 5: "site:github.com free AI coding agent"             (open source)
```

### Coverage Matrix

| Aspect | Query | Status |
|--------|-------|--------|
| Best overall | "best free AI coding tools 2025" | ⏳ Searching |
| Cursor | "cursor free tier 2025" | ⏳ Not searched |
| Open source | "site:github.com free AI coding agent stars:>1000" | ⏳ Not searched |

---

## Source Evaluation

### Source Tier

| Tier | Sources | Trust Level |
|------|---------|-------------|
| **1 — Official** | docs site, official blog, specification | Highest |
| **2 — Authoritative** | Stack Overflow, Wikipedia, established tech blogs | High |
| **3 — Community** | Reddit, Medium, Dev.to, Hacker News | Medium |
| **4 — Social** | Twitter/X, Facebook, TikTok | Low-Medium |
| **5 — Unknown** | Random blogs, forums, SEO-spam | Lowest |

### Evaluation Criteria

| Criterion | ✅ Strong | ❌ Weak |
|-----------|----------|---------|
| **Author** | Named expert | Anonymous |
| **Date** | Recent (<1 year) | Outdated (>2 years) |
| **Sources** | Cites primary sources | No references |
| **Consensus** | Multiple sources agree | Single outlier claim |
| **Evidence** | Code, data, benchmarks | Fioles only |
| **Purpose** | Inform or document | Sell or promote |

### Fact vs Opinion vs Speculation

| Type | Marker | Weight |
|------|--------|--------|
| **Fact** | Dates, versions, code, data | High |
| **Opinion** | "I think", "best", "worst" | Medium |
| **Speculation** | "might", "could", "rumored" | Low |
| **Confidence** | "confirmed", "announced", "released" | Highest |

---

## Output Format

### Research Summary Template

```
## Research: <TOPIC>

### Key Findings
1. [FACT] — Strong evidence (Tier 1 source)
2. [FACT] — Strong evidence (Tier 2 source)
3. [OPINION] — Multiple sources confirm pattern
4. [SPECULATION] — Weak evidence, note gap

### Strongest Sources
1. [Title](URL) (Tier 1) — Key takeaway
2. [Title](URL) (Tier 2) — Key takeaway
3. [Title](URL) (Tier 3) — Key takeaway

### Gaps & Contradictions
- Source A claims X, Source B claims Y
- No authoritative source found for Z
- Topic evolving rapidly — data may be outdated

### Recommendation
[Actionable takeaway based on evidence]
```

### Conciseness Rules

1. **Max 3 sentences per finding** — no fluff
2. **Max 5 sources** — prioritize quality over quantity
3. **One-line summary per source** — key takeaway only
4. **Bullet points, not paragraphs** — scannable
5. **No introduction, no conclusion** — results only

---

## Ambiguity Resolution

| Ambiguity | Proposed Interpretation | Action |
|-----------|------------------------|--------|
| "What's the best X?" | User wants comparison + recommendation | Search for comparisons, rank by criteria |
| "How do I fix Y?" | User has specific error, need solution | Search for exact error message |
| "What is Z?" | User wants concise explanation + use cases | Search for official docs first |
| "Latest news on W?" | User wants recent developments | Search with date filter, prefer 2025+ |
| No domain specified | User wants general overview | Search broad, narrow if needed |

---

## Time-Sensitive Research

### When Time-Sensitive

- Software versions and releases
- API changes and deprecations
- Security vulnerabilities
- Pricing changes
- Breaking news in tech

### Tactics

1. **Add year**: `"claude code 2025"` not `"claude code"`
2. **Use `after:` filter**: `after:2025-06-01`
3. **Prefer changelogs**: `site:docs.anthropic.com changelog`
4. **Check dates**: Verify source date before citing
5. **Note staleness**: Flag if newest source is >6 months old

---

## Research Recipes

### Recipe 1: Tool Comparison

```
Goal: Compare Tool A vs Tool B

Queries:
1. "Tool A vs Tool B 2025 comparison"
2. "Tool A features pricing 2025"
3. "Tool B features pricing 2025"
4. "site:reddit.com Tool A Tool B which is better"

Output: Comparison table + recommendation
```

### Recipe 2: Error Resolution

```
Goal: Fix specific error message

Queries:
1. "exact error message" site:stackoverflow.com
2. "error keyword" fix site:github.com
3. "error keyword" troubleshooting guide

Output: Root cause + fix steps + prevention
```

### Recipe 3: Learning Path

```
Goal: Learn X from scratch

Queries:
1. "X tutorial beginner 2025"
2. "X best practices guide"
3. "X project ideas practice"
4. "site:realpython.com X" OR "site:docs.python.org X"

Output: Curated learning path + resources
```

### Recipe 4: API/Library Research

```
Goal: Find best library for X

Queries:
1. "best X library 2025 site:github.com"
2. "X library comparison benchmarks"
3. "site:github.com X library stars:>500"

Output: Top 3 libraries + comparison + recommendation
```

### Recipe 5: News & Trends

```
Goal: Latest developments in X

Queries:
1. "X news 2025"
2. "X announcement site:blog.google OR site:openai.com"
3. "site:news.ycombinator.com X"

Output: Timeline of developments + impact analysis
```

---

## Pitfalls

### 1. Single Query Bias
**Masalah:** One query misses important perspectives
**Fix:** Always use 3-5 queries for coverage

### 2. Recency Blindness
**Masalah:** Citing outdated sources for time-sensitive topics
**Fix:** Check dates, prefer 2025+ for tech topics

### 3. Source Tier Confusion
**Masalah:** Treating random blog same as official docs
**Fix:** Tier your sources, weight accordingly

### 4. Confirmation Bias
**Masalah:** Only searching for evidence that confirms existing belief
**Fix:** Search for counter-arguments too

### 5. Over-Explaining
**Masalah:** Long prose when bullets would do
**Fix:** Max 3 sentences per finding, bullet points

### 6. Ignoring Gaps
**Masalah:** Not noting when evidence is weak or missing
**Fix:** Always note gaps, contradictions, weak evidence

### 7. Query Too Broad
**Masalah:** "AI tools" returns 1000 irrelevant results
**Fix:** Add qualifiers: year, language, use case, domain

### 8. Query Too Narrow
**Masalah:** Zero results for overly specific query
**Fix:** Remove qualifiers one at a time until results appear

---

## Quick Reference Card

```
QUERY FORMULA:
  [TOPIC] + [VERSION] + [QUALIFIER] + [SOURCE_FILTER]

QUERY COUNT:
  3-5 queries per research goal

SOURCE TIERS:
  1 = Official docs (highest trust)
  2 = Authoritative (Stack Overflow, Wikipedia)
  3 = Community (Reddit, Medium)
  4 = Social (Twitter/X)
  5 = Unknown (lowest trust)

OUTPUT:
  Key findings (max 5)
  Strongest sources (max 5)
  Gaps & contradictions
  Recommendation (1 sentence)

CONCISENESS:
  Max 3 sentences per finding
  Bullet points, not paragraphs
  No intro, no conclusion
```

---

Sumber: Hermes Agent search workflow pattern
Created — 2026-06-28
