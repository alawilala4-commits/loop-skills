---
name: quality-linter
description: "Pemeriksaan kualitas output untuk pipeline produksi. Inspect correctness, completeness, consistency, formatting. Feed output ke handoff-committer. Part of multi-agent-orchestrator produksi pipeline."
version: 1.0.0
author: Hermes Agent (Lala Alawi)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [review, quality, linting, verification, correctness, completeness]
    related_skills: [builder-drafter, research-verifier, requesting-code-review]
---

# Quality Linter — Output Inspection Protocol

## Purpose
Pemeriksaan kualitas output untuk pipeline produksi. Inspect correctness, completeness, consistency, formatting.

## When to Use
- User asks to review any document, prompt, code summary, or draft
- After builder-drafter produces output, before handoff
- Pre-publish quality gate

## Do
- Check structure, logic, formatting, edge cases
- Catch contradictions, missing steps, weak reasoning
- Prefer deterministic checks over vague opinions
- State exact problem + minimal correction
- Keep feedback short, precise, actionable

## Don't
- Rewrite everything — minimal correction only
- Use vague feedback ("could be better")
- Skip formatting checks
- Give opinion without evidence

## Output Format
```
## Quality Lint: [OUTPUT TITLE]

**Severity:** PASS | WARN | FAIL
**Issues found:** N

### Critical (must fix)
1. Line 42: missing closing fence → Add ``` after line 45

### Warning (should fix)
1. H3 'Installation' after H2 'Usage' → Move under 'Getting Started'

### Suggestion (optional)
1. Consider adding example for edge case X
```

## Pipeline Position
Part of multi-agent-orchestrator produksi pipeline. Feed output ke handoff-committer.

---

## Core Rules

1. **Check structure, logic, formatting, and edge cases.**
2. **Catch contradictions, missing steps, weak reasoning, and broken references.**
3. **Prefer deterministic checks over vague opinions.**
4. **If the output needs fixing, state the exact problem and the minimal correction.**
5. **Do not rewrite everything unless necessary.**
6. **Keep the feedback short, precise, and easy to act on.**
7. **The goal is to improve quality before handoff.**

---

## Daftar Isi

1. [Inspection Dimensions](#inspection-dimensions)
2. [Deterministic Checks](#deterministic-checks)
3. [Edge Case Detection](#edge-case-detection)
4. [Contradiction Detection](#contradiction-detection)
5. [Reference Validation](#reference-validation)
6. [Formatting Verification](#formatting-verification)
7. [Feedback Format](#feedback-format)
8. [Severity Classification](#severity-classification)
9. [Linting Recipes](#linting-recipes)
10. [Pitfalls](#pitfalls)

---

## Inspection Dimensions

### The Five Dimensions

| Dimension | What to Check |
|-----------|---------------|
| **Correctness** | Logic, facts, code syntax, math |
| **Completeness** | Missing sections, steps, edge cases |
| **Consistency** | Internal agreement, no contradictions |
| **Formatting** | Markdown, structure, readability |
| **References** | Links, citations, attribution |

### Dimension Checklist

```
Output: [TITLE/TYPE]
Length: [N words/lines]

Correctness:
  ☐ Facts accurate (per verified sources)
  ☐ Logic sound (no leaps)
  ☐ Code syntactically valid
  ☐ Math/formulas correct

Completeness:
  ☐ All required sections present
  ☐ No TODO/placeholder left
  ☐ Edge cases addressed
  ☐ Next steps specified

Consistency:
  ☐ No internal contradictions
  ☐ Terminology consistent
  ☐ Tone consistent
  ☐ Format consistent

Formatting:
  ☐ Markdown valid
  ☐ Headings hierarchical
  ☐ Code blocks fenced
  ☐ Tables aligned
  ☐ Lists consistent style

References:
  ☐ All claims sourced
  ☐ Links valid format
  ☐ Attribution present
  ☐ No broken internal links
```

---

## Deterministic Checks

### What Can Be Checked Objectively

| Check | Method |
|-------|--------|
| Markdown syntax | Parse headings, fences, links |
| Code block validity | Check fence matching, language tag |
| Heading hierarchy | No level skipped (H1→H3 without H2) |
| List consistency | All bullets or all numbers, same style |
| Table alignment | Columns match header count |
| Link format | `[text](url)` pattern valid |
| Bracket matching | `()`, `[]`, `{}` balanced |
| Fence matching | ` ``` ` opened and closed |
| Date format | Consistent YYYY-MM-DD |
| Terminology | Same term for same concept |

### Heading Hierarchy Check

```
✅ Correct:
  # H1
  ## H2
  ### H3
  ## H2

❌ Broken:
  # H1
  ### H3 (skipped H2)
  #### H4 (skipped H3)
```

### Code Block Check

```
✅ Correct:
  ```python
  def foo():
      pass
  ```

❌ Broken:
  ```python
  def foo():
      pass
  (missing closing fence)

❌ Missing language:
  ```
  code here
  ```
```

### Table Check

```
✅ Correct:
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |

❌ Broken:
| A | B | C |
|---|---|
| 1 | 2 | 3 | 4 |  (extra column)

❌ Misaligned header:
| A | B |
|---|---|---|
| 1 | 2 | 3 |
```

---

## Edge Case Detection

### Common Edge Cases by Content Type

| Content Type | Edge Cases to Check |
|--------------|---------------------|
| **Tutorial** | Missing prerequisites, assumes prior knowledge |
| **API doc** | Missing error responses, auth requirements |
| **Config** | Missing default values, required vs optional |
| **Script** | No error handling, hardcoded paths |
| **Prompt** | Missing constraints, ambiguous instructions |
| **Report** | Missing data source, no confidence level |
| **Email** | Missing subject, no call to action |

### Edge Case Questions

```
For each output, ask:
1. "What if user has no context?" — Is it self-contained?
2. "What if input is empty/null?" — Is it handled?
3. "What if something fails?" — Is error path covered?
4. "What if scale changes?" — Does it work for 10x?
5. "What assumptions are made?" — Are they stated?
```

### Missing Step Detection

```
Process described: [X → Y → Z]
Check:
  Step X → Y: Is transition clear? Any prerequisite?
  Step Y → Z: Is transition clear? Any prerequisite?
  Missing steps between? Any hand-wave?
```

---

## Contradiction Detection

### Types of Contradictions

| Type | Example | Fix |
|------|---------|-----|
| **Direct** | "X is required" then "X is optional" | Reconcile |
| **Temporal** | "Released 2024" then "Coming 2025" | Verify date |
| **Numeric** | "100 users" then "200 users" | Verify source |
| **Logical** | "Always X" then "Except when Y" | Clarify rule |
| **Terminology** | "user" vs "account" vs "member" for same thing | Pick one |

### Contradiction Check Protocol

```
1. Extract all claims from output
2. Group by topic
3. Compare claims within each topic
4. Flag any disagreement
5. State both sides clearly
6. Suggest resolution
```

---

## Reference Validation

### Reference Check Types

| Reference Type | Check |
|----------------|-------|
| External link | Format valid, URL syntactically correct |
| Internal link | Target exists in document |
| Source citation | Claims match cited source |
| Cross-reference | Section mentioned exists |

### Link Format Validation

```
✅ Valid:
  [text](https://example.com)
  [text](#section-anchor)
  [text](relative/path.md)

❌ Invalid:
  [text]() (empty URL)
  https://example.com (no markdown link)
  [text] (missing URL)
  [text](url) (not a valid URL)
```

### Source Attribution Check

```
For each factual claim:
  Has source? → Yes / No
  Source tier? → 1-9
  Claim matches source? → Yes / Partial / No
  Accessible? → Yes / Dead / Unknown
```

---

## Formatting Verification

### Markdown Rules

| Element | Rule |
|---------|------|
| Headings | Space after `#`: `# Heading` not `#Heading` |
| Lists | Consistent marker: all `-` or all `*` |
| Code fences | Match opening and closing |
| Blank lines | Blank line before and after blocks |
| Tables | Header separator required |
| Emphasis | Consistent: `**bold**` or `*italic*` |

### Readability Checks

- **Line length**: Under 120 chars for code, wrap prose at 80
- **Paragraph length**: Max 5 sentences
- **Heading density**: Not more than 3 headings per section
- **List balance**: Items in list roughly same length
- **Code examples**: Complete (no `...` unless intentional)

### Visual Balance

```
✅ Balanced:
  - Short intro (2-3 sentences)
  - Clear sections
  - Examples where helpful
  - Short conclusion

❌ Unbalanced:
  - 500 words without heading
  - One giant code block
  - 20 sections for 3 concepts
```

---

## Feedback Format

### Lint Report Template

```
## Quality Lint: [OUTPUT TITLE]

**Severity:** PASS | WARN | FAIL
**Issues found:** N

### Critical (must fix)
1. [ISSUE]: [EXACT PROBLEM] → [MINIMAL FIX]

### Warning (should fix)
1. [ISSUE]: [PROBLEM] → [SUGGESTION]

### Suggestion (optional improvement)
1. [AREA]: [SUGGESTION]
```

### Feedback Rules

| Rule | Example |
|------|---------|
| Exact location | "Line 42: missing closing fence" |
| Exact problem | "Table has 3 headers but 4 columns" |
| Minimal fix | "Add closing ` ``` ` after line 45" |
| No vague feedback | ❌ "Could be better" → ✅ "Add heading before list" |
| No rewrite | ❌ Rewrite whole section → ❌ "Clarify X" |

### Good vs Bad Feedback

```
❌ Bad: "The structure could be improved."
✅ Good: "H3 'Installation' appears after H2 'Usage'. Move it under H2 'Getting Started'."

❌ Bad: "Reference section is weak."
✅ Good: "Source for '10M users' claim is a 2023 blog post. Add Tier 1 source or mark [ESTIMATE]."

❌ Bad: "Formatting issues in code."
✅ Good: "Code block line 23-45: missing language tag. Change ``` to ```python."
```

---

## Severity Classification

### Severity Levels

| Level | Meaning | Examples |
|-------|---------|----------|
| **FAIL** | Output is broken or misleading | Contradiction, missing section, wrong fact |
| **WARN** | Output works but has gaps | Missing edge case, weak source, unclear step |
| **INFO** | Minor improvement possible | Formatting nit, wording clarity |
| **PASS** | No issues found | — |

### Severity Decision Tree

```
Does the output:
├── Contain false facts? → FAIL
├── Have critical gaps? → FAIL
├── Contradict itself? → FAIL
├── Miss important context? → WARN
├── Have weak sources? → WARN
├── Have formatting issues? → WARN / INFO
└── Look correct and complete? → PASS
```

---

## Linting Recipes

### Recipe 1: Lint a Prompt

```
Checklist:
☐ Role defined (one sentence)
☐ Goal stated (one sentence)
☐ Rules numbered
☐ Rules testable (not vague)
☐ Context provided
☐ Expected output specified
☐ Constraints listed
☐ Example included (if helpful)
☐ No contradictions between rules
☐ No ambiguous terms
```

### Recipe 2: Lint a Technical Document

```
Checklist:
☐ Title present and specific
☐ Overview/summary at top
☐ Sections logically ordered
☐ Code blocks have language tags
☐ Code blocks are complete (no hand-waving)
☐ Parameters documented
☐ Error cases covered
☐ Examples for each major feature
☐ References section present
☐ No broken internal links
```

### Recipe 3: Lint a Report

```
Checklist:
☐ Title specific
☐ Date included
☐ Sources listed
☐ Findings separated from opinions
☐ Each finding sourced
☐ Gaps/caveats stated
☐ Confidence levels noted
☐ Next steps specified
☐ No unsupported claims
☐ Numbers have context
```

### Recipe 4: Lint an Email

```
Checklist:
☐ Subject clear and specific
☐ Opening gives context
☐ Body under 200 words
☐ One topic per paragraph
☐ Call to action clear
☐ No ambiguity about next steps
☐ Tone matches recipient
☐ No attachments mentioned but missing
```

### Recipe 5: Lint a Skill Document

```
Checklist:
☐ YAML frontmatter valid
☐ Name ≤ 64 chars, lowercase + hyphens
☐ Description ≤ 1024 chars
☐ Version present
☐ Each section has completion criteria
☐ Examples are runnable (code)
☐ No placeholder content
☐ Related skills resolve
☐ No internal contradictions
☐ Total ≤ 100,000 chars
```

---

## Pitfalls

### 1. Vague Feedback
**Masalah:** "Could be improved" tidak actionable
**Fix:** State exact problem + exact fix

### 2. Rewriting Everything
**Masalah:** "Here's how I'd rewrite it..." seluruh output
**Fix:** Minimal correction only — linter, not author

### 3. Opinion Over Evidence
**Masalah:** "I think this section is too long"
**Fix:** Gunakan deterministic rules (max 5 sentences, max 120 chars)

### 4. Missing Edge Cases
**Masalah:** Hanya check happy path
**Fix:** Always ask "what if X fails?"

### 5. Ignoring Consistency
**Masalah:** Check per-section tapi tidak cross-section
**Fix:** Compare claims across entire output

### 6. Overlooking Formatting
**Masalah:** "Content is good" tapi broken Markdown
**Fix:** Check formatting as separate dimension

### 7. Missing Severity
**Masalah:** Semua issue sama weight-nya
**Fix:** Classify: FAIL / WARN / INFO / PASS

### 8. No Location Reference
**Masalah:** "There's a code issue" tapi tidak mana
**Fix:** Always state line number or section name

---

## Quick Reference Card

```
FIVE DIMENSIONS:
  1. Correctness → facts, logic, syntax
  2. Completeness → steps, sections, edge cases
  3. Consistency → no contradictions
  4. Formatting → markdown, structure
  5. References → links, sources, attribution

DETERMINISTIC CHECKS:
  ☐ Heading hierarchy (no skip)
  ☐ Code fences (matched)
  ☐ Tables (columns = headers)
  ☐ Links (valid format)
  ☐ Brackets (balanced)
  ☐ Lists (consistent marker)

SEVERITY:
  FAIL → Misleading or broken
  WARN → Works but has gaps
  INFO → Minor improvement
  PASS → No issues

FEEDBACK FORMAT:
  [LOCATION]: [EXACT PROBLEM] → [MINIMAL FIX]

EDGE CASE QUESTIONS:
  What if no context?
  What if empty input?
  What if failure?
  What if scale?
  What assumptions?
```

---

Sumber: Hermes Agent quality assurance pattern
Created — 2026-06-28
