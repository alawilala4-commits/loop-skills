---
name: skill_review
description: "Review hasil akhir (kode, dokumen, konfigurasi) sebelum deploy."
version: 1.0.0
author: user
tags: [review, quality-assurance, final-check]
prerequisites: []
---

# Skill Review

Review hasil akhir (kode, dokumen, konfigurasi) sebelum deploy.

## Trigger

- Testing phase selesai, semua test pass
- User minta review / "review dulu sebelum deploy"
- User bilang "review", "cek lagi", "quality check"

## Output Format

```
## Review: [Feature/Project]

### Overall Score: [A/B/C/D]

### Checklist
- [ ] Code follows style guide
- [ ] No hardcoded secrets/credentials
- [ ] Error handling is adequate
- [ ] Tests cover critical paths
- [ ] Documentation is up to date
- [ ] No unnecessary complexity
- [ ] Performance is acceptable
- [ ] Security considerations addressed

### Issues Found
| Severity | Issue | Recommendation |
|----------|-------|----------------|
| High | ... | ... |
| Medium | ... | ... |
| Low | ... | ... |

### Verdict
[APPROVE / REQUEST_CHANGES / REJECT]
```

## Process

1. **Code Review** — cek kualitas, readability, structure
2. **Security Review** — cek vulnerability, exposed secrets
3. **Performance Review** — cek bottlenecks, unnecessary operations
4. **Test Coverage Review** — cek apakah tests adequate
5. **Final Verdict** — approve, request changes, atau reject

## Review Criteria

- **Correctness** — apakah kode melakukan apa yang dimaksud
- **Maintainability** — apakah kode mudah dibaca dan di-maintain
- **Security** — tidak ada injection, exposed creds, atau unsafe practices
- **Performance** — tidak ada N+1 queries, memory leaks, atau O(n²) yang tidak perlu

## Constraints

- `requires_human_confirmation: true` — review result harus dikonfirmasi user sebelum deploy
- Tidak boleh skip review sebelum deploy

## Integration

- `depends_on: ["skill_testing"]` — setelah testing pass
- `next_on_success: ["skill_deploy"]` — jika review approve
- `next_on_failure: []` — jika request changes, kembali ke coding

## Pitfalls

- Jangan review terlalu lama — max 30 menit per session
- Jangan nitpick — fokus pada substantive issues
- Jangan skip review karena "cuma perubahan kecil"

## Upgrade Notes

- v1.0.0: basic review checklist
- Future: tambah automated review tools, security scanning, performance benchmarking
