---
name: loop-verifier
description: Memeriksa hasil kerja Hermes agar sesuai tujuan, valid, dan siap dipakai.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, verification, validation, QA]

---

# Loop Verifier

## When to Use
Gunakan setelah eksekusi, sebelum final output, atau saat hasil perlu dicek ulang.

## Inputs
- Output terbaru.
- Tujuan awal.
- Checklist validasi.
- Constraint kualitas.

## Procedure
1. Bandingkan output dengan tujuan.
2. Cari error, kekurangan, dan inkonsistensi.
3. Cek format, isi, dan kelengkapan.
4. Tandai bagian yang perlu diperbaiki.
5. Kirim hasil evaluasi ke replanner atau finalizer.

## Output
- Status validasi.
- Daftar masalah.
- Saran perbaikan.
- Keputusan lanjut atau berhenti.

## Pitfalls
- Jangan hanya memeriksa format.
- Jangan menganggap sukses tanpa bukti.
- Jangan melewati kesalahan kecil yang berdampak besar.

## Verification
- Output lolos checklist.
- Semua error kritis tertangani.
- Hasil siap untuk tahap berikutnya.