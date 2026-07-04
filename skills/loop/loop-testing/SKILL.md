---
name: loop-testing
description: "Menjalankan validasi hasil kerja sebelum dianggap selesai."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, testing, validation, quality]
---

# Loop Testing

## Purpose
Menjalankan validasi hasil kerja sebelum dianggap selesai.

## Use When
- Setelah implementasi fitur.
- Setelah perbaikan bug.
- Sebelum deploy.
- Saat perubahan signifikan pada codebase.

## Steps
1. Identifikasi jenis test yang relevan (unit, integration, e2e, performance).
2. Jalankan test suite.
3. Catat hasil: test passed, failed, skipped.
4. Analisis failure: root cause & fix.
5. Re-run test sampai green.
6. Laporkan coverage & risiko residual.

## Output
- Test status (passed/failed/skipped).
- Coverage percentage.
- Failure details & fixes applied.
- Rekomendasi test tambahan.

## Pitfalls
- Jangan skip test hanya karena lambat.
- Jangan commit kode dengan test kegagalan.
- Jangan trust hanya unit test tanpa integration.
- Jangan abaikan flaky test.

## Verification
- Semua test green.
- Coverage ≥ 80% untuk critical path.
- No regresi di existing test.
- Pesan error jelas & actionable.