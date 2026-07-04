---
name: skill_planning
description: "Memecah task besar menjadi langkah-langkah kecil yang terstruktur."
version: 1.0.0
author: user
tags: [planning, decomposition, workflow]
prerequisites: []
---

# Skill Planning

Memecah task besar menjadi langkah-langkah kecil yang terstruktur dan executable.

## Trigger

- User minta rencana / breakdown / "bagaimana mengerjakan X"
- Task besar yang butuh multi-step execution
- User bilang "plan", "rencanakan", "pecah task ini"

## Output Format

Setiap plan menghasilkan:

```
## Plan: [Nama Task]

### Goal
[Satu kalimat tujuan]

### Steps
1. [Step 1] — estimated time: Xm
2. [Step 2] — estimated time: Xm
3. ...

### Dependencies
- Step 2 depends on Step 1
- ...

### Risks & Mitigations
- Risk: X → Mitigation: Y

### Success Criteria
- [ ] Criteria 1
- [ ] Criteria 2
```

## Process

1. **Understand** — klarifikasi scope dan constraint (bisa pakai clarify tool)
2. **Decompose** — pecah menjadi step 2-5 langkah executable
3. **Order** — tentukan dependency dan urutan
4. **Estimate** — kasih estimasi waktu per step
5. **Validate** — konfirmasi ke user sebelum eksekusi

## Constraints

- `requires_human_confirmation: false` — bisa langsung jalankan tanpa konfirmasi user
- Max 10 steps per plan
- Setiap step harus actionable (bukan vague)

## Integration

- `next_on_success: ["skill_research"]` — setelah plan selesai, lanjut ke research
- `next_on_failure: []` — jika gagal, ulangi planning atau escalate

## Pitfalls

- Jangan terlalu granular (step < 5 menit tidak perlu)
- Jangan terlalu besar (step > 60 menit harus dipecah lagi)
- Selalu cek dependency antar step

## Upgrade Notes

- v1.0.0: basic planning
- Future: tambah Gantt chart export, integration dengan kanban, parallel step detection
