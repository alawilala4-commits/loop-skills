---
name: loop-context-management
description: "Kelola context: gather, organize, pass antar step & skill."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, context, state, handoff, knowledge-transfer]
---

# Loop Context Management

## Purpose
Kelola context: gather, organize, pass antar step & skill.

## Use When
- Mulai task baru & perlu background.
- Handoff ke skill atau sub-agent.
- Iterasi berlanjut & perlu recall state.
- Kolaborasi multi-agent.

## Steps
1. Collect: gather relevant context (requirement, code, logs, decision).
2. Organize: structure context hierarchically (what, why, current state).
3. Prioritize: highlight critical info, deprioritize noise.
4. Pass: format untuk skill/agent berikutnya.
5. Tag: label context untuk future retrieval.

## Output
- Context package well-organized.
- Key decision & assumption documented.
- Current state & blockers clear.
- Ready for handoff atau continuation.

## Pitfalls
- Jangan context dump semuanya — filter noise.
- Jangan kehilangan critical decision trail.
- Jangan format context tidak readable.
- Jangan assume receiver understand implicitly.

## Verification
- Context clear & actionable.
- No ambiguity.
- Receiver dapat lanjut without re-asking.
- All assumption explicit.