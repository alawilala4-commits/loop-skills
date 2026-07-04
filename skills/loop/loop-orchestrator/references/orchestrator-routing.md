# Orchestrator Decision Tree

## Start: Task Received

### Assess Scope
- Single step or multi-step?
- Clear or ambiguous requirement?
- New task or continuation?

### Route to Next Skill

**IF single-step, clear:**
→ EXECUTOR (just do it)

**IF multi-step, complex:**
→ PLANNING (break into plan)

**IF ambiguous, unclear:**
→ RESEARCH (gather info first)

**IF continuation from prior work:**
→ MEMORY (recall context first)

## During Execution

### Monitor Progress
- Each step completed?
- Output matches expected?
- No blockers?

**IF blocked:**
→ FALLBACK (try alternative) OR RETRY (try again)

**IF output poor quality:**
→ CRITIC (review & flag issues)

**IF need more context:**
→ CONTEXT-MANAGEMENT (organize & clarify)

## After Execution

### Verify Results

**IF results OK:**
→ QUALITY check, then REFLECTION

**IF results bad:**
→ REPLANNER (revise plan) OR INCIDENT-RESPONSE (if production issue)

**IF multiple results:**
→ SYNTHESIS (combine into final output)

## Final Steps

### Save Learnings
→ MEMORY (for future similar tasks)

### Escalate if Needed
→ HANDOFF (to human, another skill, or sub-agent)

## Routing Cheatsheet

| Situation | Next Skill |
|-----------|-----------|
| Know exactly what to do | executor |
| Task is complex, need plan | planning |
| Don't have enough info | research |
| Need to remember prior context | memory |
| Hit an obstacle | fallback, retry |
| Quality check needed | quality, critic |
| Combine multiple outputs | synthesis |
| Escalate or delegate | handoff |
| Done, save learning | reflection, memory |
