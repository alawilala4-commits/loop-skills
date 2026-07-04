---
name: research-verifier
description: "Validasi evidence + deteksi konflik untuk pipeline intel. Verify sources, compare claims, flag contradictions. Feed output ke judge. Part of multi-agent-orchestrator intel pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [verification, fact-checking, sources, evidence, validation, research]
    related_skills: [search-engineering, web]
---

# Research Verifier — Evidence Validation Protocol

## Purpose
Validasi evidence + deteksi konflik untuk pipeline intel. Verify sources, compare claims, flag contradictions.

## When to Use
- User asks to verify claims, check sources, or validate research findings
- After search-engineering returns sources, need validation
- Before judge makes decision, evidence must be verified

## Do
- Check authority, currentness, relevance of each source
- Compare multiple sources (min 2-3 for facts)
- Separate confirmed facts from weak claims
- Flag contradictions and missing evidence clearly

## Don't
- Invent confidence — base it on sources reviewed
- Accept single source as proof
- Ignore date staleness
- Hedge — say "weak" not "might be weak"

## Output Format
```
## Verification: <CLAIM/TOPIC>

### Verdict: STRONG | MODERATE | WEAK | INSUFFICIENT

### Evidence Summary
- Sources reviewed: N
- Authoritative sources: N of N
- Consensus level: Full | Majority | Split | None

### Confirmed Facts
1. [FACT] — Confirmed by [Tier 1, Tier 2]

### Weak Claims
1. [CLAIM] — Only [Tier 6] confirms

### Contradictions
- Source A claims X, Source B claims Y → Resolution: [higher tier wins]

### Missing Evidence
- 🔴 No authoritative source found for [claim]

### Recommendation
[Actionable verdict]
```

## Pipeline Position
Part of multi-agent-orchestrator intel pipeline. Feed output ke judge.

---

## Core Rules

1. **Check whether sources are authoritative, current, and relevant.**
2. **Compare multiple sources** when possible.
3. **Separate confirmed facts from weak claims or speculation.**
4. **Flag contradictions, missing evidence, and low-confidence statements.**
5. **Prefer direct evidence over summaries of summaries.**
6. **If the evidence is weak, say so clearly and explain what is missing.**
7. **Keep the verification concise and actionable.**
8. **Do not invent confidence** — base it on the sources you reviewed.

---

## Daftar Isi

1. [Source Authority Check](#source-authority-check)
2. [Currentness Validation](#currentness-validation)
3. [Relevance Assessment](#relevance-assessment)
4. [Cross-Source Comparison](#cross-source-comparison)
5. [Fact vs Claim Classification](#fact-vs-claim-classification)
6. [Contradiction Detection](#contradiction-detection)
7. [Evidence Strength Scoring](#evidence-strength-scoring)
8. [Verification Output Format](#verification-output-format)
9. [Verification Recipes](#verification-recipes)
10. [Pitfalls](#pitfalls)

---

## Source Authority Check

### Authority Tiers

| Tier | Source Type | Trust Weight |
|------|-------------|--------------|
| **1** | Official docs, specifications, primary sources | 100% |
| **2** | Academic papers, peer-reviewed journals | 95% |
| **3** | Established tech blogs (with named authors) | 80% |
| **4** | Stack Overflow (high-voted answers) | 75% |
| **5** | Community wikis (Wikipedia, Fandom) | 70% |
| **6** | Medium/Dev.to (verified authors) | 60% |
| **7** | Reddit/Twitter (karma-weighted) | 50% |
| **8** | Random blogs, SEO-spam | 30% |
| **9** | Anonymous/unverifiable | 10% |

### Authority Checklist

```
Source: [URL/Author]
├── Named author? → Yes (+10) / No (-10)
├── Author expert in field? → Yes (+15) / Unknown (0) / No (-15)
├── Cites primary sources? → Yes (+20) / No (-10)
├── Editorial oversight? → Yes (+10) / No (0)
├── Published by known org? → Yes (+15) / No (0)
└── Peer-reviewed? → Yes (+20) / No (0)

Score: __/100
Verdict: STRONG (>80) | MODERATE (50-80) | WEAK (<50)
```

### Red Flags for Authority

- Anonymous author with no credentials
- No publication date
- No references or citations
- Aggressive monetization (pop-ups, affiliate links throughout)
- AI-generated content markers
- Domain mimics official site (e.g., `python-docs-website.com`)

---

## Currentness Validation

### Date Check Protocol

```
Claim: "X is the latest version"
├── Source date: 2024-06-01
├── Today: 2026-06-28
├── Age: 2 years
├── Topic: Software versions (fast-moving)
└── Verdict: STALE — likely outdated
```

### Freshness by Topic

| Topic | Max Age for "Current" | Staleness Risk |
|-------|----------------------|----------------|
| Software versions | 3 months | High |
| API documentation | 6 months | High |
| Security vulnerabilities | 1 month | Critical |
| Best practices | 1 year | Medium |
| Foundational theory | 5 years | Low |
| Historical facts | Indefinite | None |

### Staleness Indicators

- References versions no longer maintained
- Links return 404
- Mentions "upcoming" features that likely shipped
- Comments section notes "this is outdated"
- Dates from COVID era (2020-2022) without update

---

## Relevance Assessment

### Relevance Criteria

| Criterion | High Relevance | Low Relevance |
|-----------|---------------|---------------|
| Topic match | Exact topic | Adjacent topic |
| Depth | In-depth analysis | Surface mention |
| Context | Same use case | Different context |
| Audience | Target audience | Wrong audience |
| Scope | Matches query scope | Too broad or narrow |

### Relevance Score

```
Relevance to query: [QUERY]
Source: [URL]

Directly answers? → Yes (+30) / Partially (+15) / No (0)
Same context? → Yes (+20) / Somewhat (+10) / No (0)
Appropriate depth? → Yes (+20) / Too shallow (+5) / Too deep (+10)
Same audience? → Yes (+15) / Mixed (+5) / No (0)
Actionable? → Yes (+15) / No (0)

Score: __/100
Verdict: HIGH (>75) | MODERATE (50-75) | LOW (<50)
```

---

## Cross-Source Comparison

### Minimum Source Count

| Claim Type | Minimum Sources |
|------------|-----------------|
| Hard fact (dates, versions) | 2 sources |
| Tutorial/guide | 2-3 sources |
| Opinion/best practice | 3-5 sources |
| Controversial topic | 5+ sources |

### Comparison Matrix

| Source | Claim A | Claim B | Claim C | Tier |
|--------|---------|---------|---------|------|
| Source 1 (Official) | ✅ Confirms | ❌ Disputes | — | 1 |
| Source 2 (Blog) | ✅ Confirms | — | ✅ Confirms | 3 |
| Source 3 (SO) | ✅ Confirms | — | ⚠️ Partial | 4 |

**Consensus:** Claim A strongly confirmed. Claim B disputed. Claim C moderate support.

### Agreement Patterns

| Pattern | Verdict |
|---------|---------|
| All sources agree | HIGH confidence |
| Majority agree, minority silent | MODERATE-HIGH confidence |
| Majority agree, minority disagree | MODERATE confidence |
| Equal split | LOW confidence — needs more sources |
| Single source only | LOW confidence — unverified |
| Sources all cite same primary source | Treat as single source |

---

## Fact vs Claim Classification

### Classification Taxonomy

| Type | Definition |Confidence |
|------|-----------|-----------|
| **Verified Fact** | Multiple authoritative sources confirm | 95-100% |
| **Likely Fact** | Authoritative source confirms, no disputes | 80-95% |
| **Probable** | Multiple non-authoritative sources agree | 60-80% |
| **Claim** | Single source or weak evidence | 40-60% |
| **Speculation** | Marked as unconfirmed/rumor | 20-40% |
| **Disputed** | Sources contradict | <20% |
| **Debunked** | Authoritative source explicitly denies | <5% |

### Signal Words

| Confidence | Marker Words |
|------------|-------------|
| **High** | "confirmed", "announced", "released", "documentation states", "according to official" |
| **Medium** | "reportedly", "appears to", "sources say", "community reports" |
| **Low** | "might", "could", "rumored", "speculated", "unconfirmed", "allegedly" |

---

## Contradiction Detection

### Contradiction Types

| Type | Example | Resolution |
|------|---------|------------|
| **Date mismatch** | Source A: released Jan 2025, Source B: released Mar 2025 | Check primary source |
| **Version conflict** | Source A: v2.1 latest, Source B: v2.2 latest | Check official changelog |
| **Feature claim** | Source A: feature exists, Source B: feature removed | Check official docs |
| **Performance** | Source A: 2x faster, Source B: no improvement | Check methodology |
| **Compatibility** | Source A: works on X, Source B: doesn't work on X | Check version numbers |

### Contradiction Resolution Protocol

```
Contradiction detected: [DESCRIPTION]

Step 1: Check source authority
  → Higher tier source wins

Step 2: Check date
  → More recent source wins (for time-sensitive topics)

Step 3: Check primary vs secondary
  → Primary source wins

Step 4: Check consensus
  → Majority position wins

Step 5: If still tied
  → Flag as disputed, present both sides
```

### Missing Evidence Flags

- 🔴 **Critical gap**: No authoritative source found
- 🟡 **Moderate gap**: Only one source confirms
- 🟢 **Minor gap**: Sources agree but lack primary source
- ⚪ **No gap**: Multiple authoritative sources confirm

---

## Evidence Strength Scoring

### Composite Score Formula

```
Evidence Score = (Authority × 0.35) + (Currentness × 0.25) + (Relevance × 0.25) + (Consensus × 0.15)

Where:
  Authority    = average source tier score (0-100)
  Currentness  = freshness score (0-100)
  Relevance    = relevance to query (0-100)
  Consensus    = agreement level (0-100)
```

### Score Interpretation

| Score | Verdict | Action |
|-------|---------|--------|
| **90-100** | STRONG | Use with high confidence |
| **70-89** | GOOD | Use with minor caveats |
| **50-69** | MODERATE | Use with clear caveats |
| **30-49** | WEAK | Flag as uncertain, seek more sources |
| **0-29** | INSUFFICIENT | Do not use, find better evidence |

### Confidence Statement Templates

| Score | Statement |
|-------|-----------|
| 90-100 | "This is confirmed by multiple authoritative sources." |
| 70-89 | "This is well-supported, with minor gaps noted." |
| 50-69 | "This is partially supported; see caveats below." |
| 30-49 | "Evidence is weak; this should be verified before use." |
| 0-29 | "Insufficient evidence; do not rely on this claim." |

---

## Verification Output Format

### Verification Report Template

```
## Verification: <CLAIM/TOPIC>

### Verdict: STRONG | MODERATE | WEAK | INSUFFICIENT

### Evidence Summary
- Sources reviewed: N
- Authoritative sources: N of N
- Date range: YYYY-MM-DD to YYYY-MM-DD
- Consensus level: Full | Majority | Split | None

### Confirmed Facts
1. [FACT] — Confirmed by [Source Tier 1, Source Tier 2]
2. [FACT] — Confirmed by [Source Tier 1]

### Weak Claims (use with caution)
1. [CLAIM] — Only [Source Tier 6] confirms; no authoritative source
2. [SPECULATION] — Marked as "rumored" in [Source Tier 3]

### Contradictions
- Source A claims X, Source B claims Y
- Resolution: [Higher tier source wins / Date wins / Still disputed]

### Missing Evidence
- 🔴 No authoritative source found for [specific claim]
- 🟡 Only one source confirms [specific claim]

### Recommendation
[Actionable verdict based on evidence strength]
```

### Conciseness Rules

1. **Max 5 findings** — prioritize strongest evidence
2. **One sentence per finding** — no elaboration
3. **Tier every source** — always note authority level
4. **Flag every gap** — never hide missing evidence
5. **No hedging** — say "weak" not "might be weak"

---

## Verification Recipes

### Recipe 1: Verify a Statistic

```
Claim: "X has 10 million users"

Verification:
1. Find primary source (official announcement, press release)
2. Check date of statistic
3. Compare with independent sources
4. Note methodology (active users vs registered users)
5. Flag if self-reported vs independently verified
```

### Recipe 2: Verify a Tutorial

```
Claim: "Tutorial X covers topic Y"

Verification:
1. Check author credentials
2. Check publication date
3. Verify code examples run (if applicable)
4. Check comments for corrections
5. Compare with official docs
```

### Recipe 3: Verify a Comparison

```
Claim: "Tool A is faster than Tool B"

Verification:
1. Find benchmark methodology
2. Check if independent or vendor-sponsored
3. Verify test conditions match your use case
4. Look for counter-benchmarks
5. Note sample size and significance
```

### Recipe 4: Verify a Breaking Change

```
Claim: "API X is being deprecated"

Verification:
1. Check official changelog/docs
2. Look for official announcement
3. Check effective date
4. Look for migration guide
5. Verify with community reports
```

### Recipe 5: Verify a Security Claim

```
Claim: "Library X has vulnerability Y"

Verification:
1. Check CVE database (nvd.nist.gov)
2. Check official security advisory
3. Verify affected versions
4. Check for patches/mitigations
5. Look for active exploitation reports
```

---

## Pitfalls

### 1. Single Source Bias
**Masalah:** Accepting claim based on one source
**Fix:** Always seek minimum 2-3 sources

### 2. Authority Blindness
**Masalah:** Trusting high-tier source without checking date/relevance
**Fix:** Tier is not everything — check all criteria

### 3. Recency Illusion
**Masalah:** Assuming newer = more accurate
**Fix:** For foundational topics, older authoritative sources may be better

### 4. Confirmation Bias
**Masalah:** Only seeking sources that confirm existing belief
**Fix:** Actively search for counter-evidence

### 5. False Balance
**Masalah:** Treating fringe view same as consensus
**Fix:** Weight by authority and consensus, not just count

### 6. Over-Confidence
**Masalah:** Claiming certainty when evidence is weak
**Fix:** Use confidence templates, match language to score

### 7. Ignoring Context
**Masalah:** Accepting evidence from different context
**Fix:** Check relevance score before using

### 8. Summary Chain
**Masalah:** Citing a summary of a summary
**Fix:** Always trace to primary source

---

## Quick Reference Card

```
VERIFICATION CHECKLIST:
  ☐ Source authority checked (tier 1-9)
  ☐ Date checked (current for topic)
  ☐ Relevance confirmed (matches query)
  ☐ Multiple sources compared (min 2-3)
  ☐ Facts separated from claims
  ☐ Contradictions flagged
  ☐ Missing evidence noted
  ☐ Confidence matches evidence

SCORING:
  90-100 = STRONG      → Use with confidence
  70-89  = GOOD         → Use with minor caveats
  50-69  = MODERATE     → Use with clear caveats
  30-49  = WEAK         → Flag as uncertain
  0-29   = INSUFFICIENT → Do not use

CONTRADICTION RESOLUTION:
  1. Higher authority wins
  2. More recent wins (time-sensitive)
  3. Primary source wins
  4. Majority wins
  5. If tied → flag as disputed
```

---

Sumber: Hermes Agent verification workflow pattern
Created — 2026-06-28
