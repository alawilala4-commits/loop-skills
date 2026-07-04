---
name: skill_research
description: "Mengumpulkan referensi, data, atau requirement dari web/API."
version: 1.0.0
author: user
tags: [research, data-gathering, web]
prerequisites: []
---

# Skill Research

Mengumpulkan referensi, data, atau requirement dari web atau API.

## Trigger

- User minta riset / cari data / "carikan info tentang X"
- Planning output butuh data gathering
- User bilang "riset", "cari referensi", "butuh data tentang"

## Output Format

```
## Research Report: [Topic]

### Summary
[2-3 kalimat temuan utama]

### Findings
1. [Finding 1](URL)
2. [Finding 2](URL)
3. ...

### Data
| Key | Value | Source |
|-----|-------|--------|
| ... | ... | ... |

### Open Questions
- [Yang belum terjawab]

### Recommendations
- [Action items dari hasil riset]
```

## Process

1. **Query Formulation** — convert topic menjadi search queries (gunakan search-engineering skill jika tersedia)
2. **Source Discovery** — cari dari web, API, dokumentasi
3. **Extraction** — extract relevant data points
4. **Cross-reference** — bandingkan antar sumber untuk validitas
5. **Synthesis** — ringkas menjadi findings yang actionable

## Tools

- `web` toolset untuk search dan web_fetch
- `browser` toolset untuk interactive web
- `terminal` untuk curl/API calls
- `research-verifier` skill untuk validasi (jika tersedia)

## Constraints

- `requires_network_access: true` — butuh koneksi internet
- Selalu cantumkan sumber URL
- Max 10 sources per research
- Prioritize primary sources over secondary

## Integration

- `depends_on: ["skill_planning"]` — input datang dari planning
- `next_on_success: ["skill_coding"]` — data diteruskan ke coding
- `next_on_failure: []` — jika gagal, coba query ulang atau escalate

## Pitfalls

- Jangan ambil data dari satu sumber saja
- Cek tanggal publikasi (outdated info berbahaya)
- Jangan mix fakta dengan opini tanpa labeling

## Upgrade Notes

- v1.0.0: basic web/API research
- Future: tambah API key management, structured data extraction, citation format
