---
name: loop-audit
description: Audit kode, infrastruktur, konfigurasi, dan keamanan sebelum production.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, audit, quality, security, validation]
---

# Loop Audit

## When to Use
Gunakan sebelum deploy, sebelum commit PR, atau saat ada perubahan signifikan pada kode/infrastruktur.

## Inputs
- Kode yang akan diaudit.
- Tipe audit (security, performance, code-quality, config, infrastructure).
- Standar audit (OWASP, PEP8, best practice, compliance).
- Scope audit.
- Tools audit yang tersedia.

## Procedure
1. Pilih tipe audit dan scope.
2. Tentukan standar yang berlaku.
3. Jalankan tools audit (linter, SAST, dependency checker, config validator).
4. Ambil hasil dan kategorisasi.
5. Pisahkan issue kritis, mayor, minor.
6. Hasilkan laporan audit singkat.

## Output
- Laporan audit.
- Daftar issue per severity.
- Tools yang dipakai.
- Rekomendasi perbaikan.
- Status lolos/gagal audit.

## Pitfalls
- Jangan jalankan audit tanpa tujuan yang jelas.
- Jangan mengabaikan issue kritis hanya karena jumlah minority.
- Jangan memakai hanya satu tool untuk audit komprehensif.
- Jangan asumsikan kualitas tanpa diverifikasi.

## Verification
- Semua kategori issue teridentifikasi.
- Rekomendasi actionable dan spesifik.
- Kritis issue punya solusi prioritas.
- Laporan ringkas tapi lengkap.

## Tools Reference
- Security: bandit, owasp-dep-check, semgrep
- Code Quality: pylint, flake8, black, ruff
- Config: yamllint, jq (for JSON validation)
- Infra: terraform validate, dockerfile lint
- Dependencies: pip audit, npm audit, cargo audit

## Decision Tree
- Ada security issue kritis? → Blok sampai fixed
- Ada performance issue mayor? → Flag untuk optimization sprint
- Ada style violation? → Auto-fix atau reject
- Ada config typo? → Blok sampai verified

## Common Patterns
- Pre-commit hook: jalankan audit lightweight sebelum commit
- CI/CD gate: audit penuh sebelum merge
- Production pre-flight: audit final sebelum deploy