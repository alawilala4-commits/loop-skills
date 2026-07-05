---
name: skill_coding
description: "Menulis atau mengedit kode/script sesuai rencana dan hasil riset."
version: 1.0.0
author: user
tags: [coding, implementation, development]
prerequisites: []
---

# Skill Coding

Menulis atau mengedit kode/script sesuai rencana dan hasil riset.

## Trigger

- User minta tulis kode / buat script / implementasi
- Research selesai, lanjut implementasi
- User bilang "tulis kode", "implementasi", "buat script"

## Output Format

```
## Implementation: [Feature/Task]

### Files Changed
- `path/to/file1.py` — [deskripsi perubahan]
- `path/to/file2.js` — [deskripsi perubahan]

### Code
```python
# relevant code snippet
```

### Notes
- [Catatan tentang implementation decisions]
```

## Process

1. **Review Plan** — baca planning output dan research data
2. **Setup** — siapkan environment, dependencies, folder structure
3. **Implement** — tulis kode per module/function
4. **Self-review** — baca ulang kode, cek edge cases
5. **Commit** — git commit dengan message yang jelas

## Allowed Languages

- `javascript` — Node.js, browser scripts
- `python` — Python 3.13+ (primary)
- `bash` — shell scripts, automation

## Tools

- `terminal` untuk eksekusi
- `file` toolset untuk read/write
- `coding` toolset untuk advanced editing
- `github` skill untuk version control

## Constraints

- `allowed_languages: ["javascript", "python", "bash"]`
- Harus ada docstrings/comments
- Ikuti style guide per language (PEP8 untuk Python, ESLint untuk JS)
- Max 400 lines per file (single responsibility)

## Integration

- `depends_on: ["skill_research"]` — input dari research
- `next_on_success: ["skill_testing"]` — kode siap ditest
- `next_on_failure: []` — jika gagal, debug mandiri atau escalate

## Pitfalls

- Jangan menulis sekaligus tanpa testing per bagian
- Jangan skip error handling
- Jangan hardcode values yang seharusnya configurable

## Upgrade Notes

- v1.0.0: basic coding workflow
- Future: tambah template generator, auto-formatting, framework-specific templates
