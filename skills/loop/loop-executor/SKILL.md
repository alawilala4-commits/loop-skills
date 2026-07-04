---
name: loop-executor
description: Menjalankan langkah kerja yang sudah direncanakan dengan fokus pada eksekusi.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, execution, action]

---

# Loop Executor

## When to Use
Gunakan setelah rencana siap dan eksekusi perlu dilakukan secara konkret.

## Inputs
- Rencana kerja.
- Langkah aktif.
- Tools yang dibutuhkan.
- Constraint eksekusi.

## Procedure
1. Ambil langkah aktif.
2. Jalankan instruksi satu per satu.
3. Simpan hasil tiap langkah.
4. Laporkan error bila ada.
5. Berhenti jika perlu verifikasi.

## Output
- Hasil eksekusi.
- Status langkah.
- Error atau hambatan.
- Artefak yang dihasilkan.

## Pitfalls
- Jangan lompat langkah.
- Jangan mengubah tujuan tanpa alasan.
- Jangan diam saat eksekusi gagal.

## Verification
- Langkah selesai sesuai instruksi.
- Output dapat diperiksa.
- Tidak ada error tak tertangani.