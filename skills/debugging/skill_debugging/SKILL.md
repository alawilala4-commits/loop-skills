---
name: skill_debugging
description: "Menganalisis error dari Testing dan memperbaiki masalah."
version: 1.0.0
author: user
tags: [debugging, error-analysis, fix]
prerequisites: []
---

# Skill Debugging

Menganalisis error dari Testing dan memperbaiki masalah.

## Trigger

- Test failure dari skill_testing
- User laporkan bug / error
- User bilang "debug", "error", "fix", "perbaiki"

## Output Format

```
## Debug Report: [Issue]

### Error
```
[error message dan traceback]
```

### Root Cause
[Penyebab masalah]

### Fix Applied
- File: `path/to/file.py`
- Change: [deskripsi fix]

### Verification
- [ ] Test passes after fix
- [ ] No regression
```

## Process

1. **Reproduce** — jalankan ulang test untuk confirm error
2. **Analyze** — baca traceback, identify root cause
3. **Hypothesize** — buat hipotesis penyebab
4. **Fix** — apply minimal fix
5. **Verify** — jalankan test lagi
6. **Document** — catat fix untuk referensi future

## Debugging Techniques

- **Print debugging** — tambah print/log di titik kritis
- **Binary search** — comment setengah kode untuk isolate
- **Rubber duck** — jelaskan masalah ke user/rubber duck
- **Stack trace analysis** — baca dari bawah (error) ke atas (origin)

## Constraints

- `max_retry: 3` — max 3 kali retry sebelum escalate
- Minimal fix: jangan rewrite seluruh module
- Selalu cek regression setelah fix

## Integration

- `depends_on: ["skill_testing"]` — input dari test failures
- `next_on_success: ["skill_coding"]` — fix diteruskan ke coding untuk apply
- `next_on_failure: []` — jika gagal setelah 3 retry, escalate ke user

## Pitfalls

- Jangan fix symptom — cari root cause
- Jangan fix tanpa verify
- Jangan lupa cek side effects dari fix

## Upgrade Notes

- v1.0.0: basic debug flow
- Future: tambah error pattern database, auto-fix suggestions, log analysis tools
