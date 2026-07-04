---
name: builder-drafter
description: "Penyusunan output/draf untuk pipeline produksi. Turn verified inputs → clear drafts, prompts, documents. Feed output ke quality-linter. Part of multi-agent-orchestrator produksi pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [writing, drafting, documentation, content, output, production]
    related_skills: [search-engineering, research-verifier, humanizer]
---

# Builder-Drafter — Document Production Protocol

## Purpose
Penyusunan output/draf untuk pipeline produksi. Turn verified inputs → clear drafts, prompts, documents.

## When to Use
- User asks to write, draft, create, or produce any document
- After judge accepts items, need to build output
- Producing README, prompts, reports, emails, documentation

## Do
- Use only verified or approved inputs
- Structure output for reuse/publish
- Match user's goal and format exactly
- Prefer clarity + completeness over verbosity
- Provide best default first if multiple versions useful
- Mark uncertainty clearly instead of guessing

## Don't
- Invent facts — use only verified inputs
- Over-write — match length/format requested
- Skip format matching (essay vs list vs table)
- Hide assumptions — mark with [ASSUMPTION]

## Output Format
```
## Draft: [TITLE]

**Format:** [report/email/prompt/etc]
**Target audience:** [audience]
**Sources used:** [N verified]
**Uncertainties:** [N marked]

---

[OUTPUT CONTENT]

---

**Caveats:**
- [Any uncertainty or gap]

**Next steps:**
- [What user should do with this]
```

## Pipeline Position
Part of multi-agent-orchestrator produksi pipeline. Feed output ke quality-linter.

---

## Core Rules

1. **Use only verified or approved inputs** — never invent facts.
2. **Structure the output** so it is easy to reuse or publish.
3. **Match the user's goal and format requirements exactly.**
4. **Prefer clarity, completeness, and practical usefulness** over verbosity.
5. **If multiple versions are useful**, provide the best default first.
6. **If something is uncertain**, mark it clearly instead of guessing.
7. **Keep formatting clean and production-ready.**

---

## Daftar Isi

1. [Input Verification](#input-verifikasi)
2. [Output Structure Patterns](#output-structure-patterns)
3. [Format Matching](#format-matching)
4. [Clarity Rules](#clarity-rules)
5. [Multi-Version Output](#multi-version-output)
6. [Uncertainty Marking](#uncertainty-marking)
7. [Production Readiness](#production-readiness)
8. [Draft Recipes](#draft-recipes)
9. [Pitfalls](#pitfalls)

---

## Input Verification

### Input Checklist

```
Input source: [user-provided / search-result / previous-agent-output]
├── Verified? → Yes / No / Partial
├── Authoritative? → Yes / Unknown / No
├── Current? → Yes / No / Unknown
└── Approved by user? → Yes / Pending / Not needed
```

### Handling Unverified Input

| Input Status | Action |
|--------------|--------|
| Verified + Approved | Use directly |
| Verified + Not approved | Flag before use |
| Partially verified | Mark uncertain sections |
| Unverified | Do not use — request verification |
| Contradicted | Flag contradiction, seek resolution |

### Source Attribution

```
Source: [Name/Link]
Verified: [Yes/No/Partial]
Used for: [Section/Claim]
Confidence: [High/Medium/Low]
```

---

## Output Structure Patterns

### Pattern 1: Technical Document

```markdown
# [TITLE]

> [One-line summary]

## Overview
[2-3 sentences: what and why]

## [Section 1]
[Content]

## [Section 2]
[Content]

## References
1. [Source 1](URL)
2. [Source 2](URL)
```

### Pattern 2: Prompt / Instruction

```markdown
You are the [ROLE] for [SYSTEM].

## Goal
[One sentence]

## Rules
1. [Rule 1]
2. [Rule 2]

## Context
[Background info]

## Expected Output
[Format + length + style]

## Example
[Input → Output example]
```

### Pattern 3: Report / Summary

```markdown
## [TITLE]

**Date:** YYYY-MM-DD
**Sources:** N verified

### Key Findings
1. [Finding 1]
2. [Finding 2]

### Details
[Expanded content]

### Gaps & Caveats
- [What is missing or uncertain]

### Next Steps
- [Actionable follow-up]
```

### Pattern 4: Code Documentation

```markdown
# [MODULE NAME]

[One-line description]

## Usage
```python
[Example code]
```

## Parameters
| Param | Type | Description |
|-------|------|-------------|

## Returns
[Description]

## Examples
[Code examples]
```

### Pattern 5: Email / Message

```markdown
Subject: [CLEAR SUBJECT]

Hi [Name],

[Opening — 1 sentence]

[Body — max 3 short paragraphs]

[Call to action — 1 sentence]

[Sign-off]
```

---

## Format Matching

### Format Detection

| User Request | Format |
|--------------|--------|
| "Write a README" | Markdown, technical doc format |
| "Draft an email" | Email format with subject |
| "Create a prompt" | Prompt engineering format |
| "Make a report" | Report format with sections |
| "Write documentation" | API doc format |
| "Draft a contract" | Legal format |
| "Create a plan" | Plan format with checklist |

### Length Guide

| Output Type | Target Length |
|-------------|--------------|
| Tweet/X post | 1-2 sentences |
| Slack message | 1 short paragraph |
| Email | 3-5 short paragraphs |
| Prompt | 1-2 pages |
| README | 2-5 pages |
| Report | 3-10 pages |
| Documentation | 5-20 pages |

### Tone Matching

| Audience | Tone |
|----------|------|
| Technical team | Precise, code-heavy |
| Management | High-level, outcome-focused |
| Clients | Professional, benefit-focused |
| General public | Simple, jargon-free |
| Community | Friendly, inclusive |

---

## Clarity Rules

### Sentence Construction

- **One idea per sentence** — split long sentences
- **Active voice** — "The system processes X" not "X is processed by the system"
- **Specific nouns** — "the authentication module" not "the thing"
- **Concrete verbs** — "returns", "validates", "creates" not "handles", "does"

### Paragraph Construction

- **One topic per paragraph** — no topic mixing
- **Topic sentence first** — reader knows what to expect
- **Max 5 sentences** — split long paragraphs
- **Logical flow** — each sentence connects to next

### Structure Rules

- **Headings are descriptive** — "Authentication Flow" not "Details"
- **Lists for 3+ items** — bullets or numbered
- **Tables for comparisons** — easier than prose
- **Code blocks for code** — never inline for multi-line

### Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| "In order to..." | "To..." |
| "It is important to note..." | Just state it |
| "As previously mentioned..." | Restate briefly |
| "This solution is the best" | "This solution [specific benefit]" |
| "Very unique" | "Unique" |
| "Completely finished" | "Finished" |

---

## Multi-Version Output

### When to Provide Multiple Versions

- User explicitly requests options
- Multiple valid approaches exist
- Different audiences/lengths are useful
- User wants to choose

### Version Format

```
## Recommended Version
[Best default — most useful for stated goal]

## Alternative 1: [Label]
[Different approach — label clearly]

## Alternative 2: [Label]
[Another option — label clearly]
```

### Version Labeling

| Label | When |
|-------|------|
| "Recommended" | Best default, highest utility |
| "Concise" | Shorter, less detail |
| "Detailed" | More depth, longer |
| "Technical" | Code-heavy, for developers |
| "Executive" | High-level, for management |
| "Minimal" | Bare essentials only |

---

## Uncertainty Marking

### Marking Taxonomy

| Marker | Meaning | Action Needed |
|--------|---------|---------------|
| `[VERIFY]` | Unverified claim | User should verify |
| `[ASSUMPTION]` | Stated assumption | Confirm if valid |
| `[ESTIMATE]` | Approximate value | Needs precision |
| `[OPTIONAL]` | May not apply | User discretion |
| `[TODO]` | Incomplete section | Fill in later |

### Marking Format

```markdown
- **Pricing:** $19/mo [VERIFY] — check current pricing page
- **Compatibility:** Works with Python 3.13 [ASSUMPTION] — confirmed?
- **Timeline:** ~2 weeks [ESTIMATE] — depends on scope
- **Optional:** Add logging [OPTIONAL] — only if needed
- **TODO:** Add error handling section [TODO]
```

### Confidence Statements

| Confidence | Statement |
|------------|-----------|
| High | "Based on [Tier 1 source]..." |
| Medium | "According to [Tier 3 source]..." |
| Low | "An unverified source claims..." |
| Unknown | "Not verified — confirm before use." |

---

## Production Readiness

### Final Checklist

```
☐ All inputs verified or marked
☐ Structure matches format pattern
☐ Headings descriptive
☐ Sentences clear and concise
☐ No filler or hedging language
☐ Uncertainties clearly marked
☐ Code blocks properly formatted
☐ Links valid (or marked)
☐ Length appropriate for format
☐ Tone matches audience
```

### Output Handoff Format

```
## Draft: [TITLE]

**Format:** [report/email/prompt/etc]
**Target audience:** [audience]
**Sources used:** [N verified]
**Uncertainties:** [N marked]

---

[OUTPUT CONTENT]

---

**Caveats:**
- [Any uncertainty or gap]

**Next steps:**
- [What user should do with this]
```

---

## Draft Recipes

### Recipe 1: README from Code

```
Input: Project code files
Output: README.md structure

1. Extract: project name, purpose, key features
2. Write: Overview (2-3 sentences)
3. Write: Installation (exact commands)
4. Write: Usage (code examples)
5. Write: Parameters/Options (table)
6. Write: Contributing (brief)
7. Write: License (if known)
```

### Recipe 2: Prompt from Specification

```
Input: Specification/requirement
Output: Production-ready prompt

1. Define: Role (one sentence)
2. Define: Goal (one sentence)
3. List: Rules (numbered, specific)
4. Provide: Context (background)
5. Specify: Expected output (format + length)
6. Include: Example (if helpful)
7. Add: Constraints (what NOT to do)
```

### Recipe 3: Report from Research

```
Input: Verified research findings
Output: Structured report

1. Title: Clear, specific
2. Date: Today's date
3. Sources: N verified, strongest first
4. Key findings: Bullet points, max 5
5. Details: One section per finding
6. Gaps: What is missing
7. Recommendations: Actionable next steps
```

### Recipe 4: Email from Request

```
Input: What user wants to communicate
Output: Draft email

1. Subject: Specific, actionable
2. Opening: Context in 1 sentence
3. Body: Max 3 short paragraphs
4. Ask: Clear call to action
5. Sign-off: Professional close
6. Length: Under 200 words ideal
```

### Recipe 5: Plan from Goal

```
Input: User goal/desired outcome
Output: Actionable plan

1. Goal: One sentence
2. Steps: Numbered, specific
3. Dependencies: What must come first
4. Time estimates: [ESTIMATE] markers
5. Deliverables: What each step produces
6. Checklist: Verification per step
```

---

## Pitfalls

### 1. Inventing Facts
**Masalah:** Filling gaps with assumptions presented as fact
**Fix:** Mark uncertain sections with [VERIFY] or [ASSUMPTION]

### 2. Over-Writing
**Masalah:** Long prose when bullets would do
**Fix:** "Would a list be clearer?" — if yes, use list

### 3. Mismatched Format
**Masalah:** Writing essay when user wanted list
**Fix:** Detect format from request, match exactly

### 4. Vague Headings
**Masalah:** "Details" or "More info" as headings
**Fix:** "Authentication error handling" — specific

### 5. Hidden Assumptions
**Masalah:** Assuming reader knows context
**Fix:** State assumptions explicitly, mark if unverified

### 6. Tone Mismatch
**Masalah:** Casual tone for formal document
**Fix:** Match tone to audience before writing

### 7. No Clear Ask
**Masalah:** Email/report without call to action
**Fix:** Every output should have clear next step

### 8. Skipping Verification Markers
**Masalah:** Not marking uncertain claims
**Fix:** Review output for unverified claims before delivery

---

## Quick Reference Card

```
INPUT CHECK:
  ☐ Verified?
  ☐ Approved?
  ☐ Current?
  ☐ Relevant?

OUTPUT RULES:
  - One idea per sentence
  - One topic per paragraph
  - Descriptive headings
  - Lists for 3+ items
  - Code blocks for code
  - Max 5 sentences per paragraph

MARKERS:
  [VERIFY]      → User should verify
  [ASSUMPTION]  → Stated assumption
  [ESTIMATE]    → Approximate value
  [OPTIONAL]    → May not apply
  [TODO]        → Incomplete

FORMATS:
  README     → Markdown technical doc
  Email      → Subject + 3 paragraphs
  Prompt     → Role + Goal + Rules
  Report     → Findings + Gaps + Next steps
  Plan       → Steps + Dependencies + Checklist
```

---

Sumber: Hermes Agent drafting workflow pattern
Created — 2026-06-28
