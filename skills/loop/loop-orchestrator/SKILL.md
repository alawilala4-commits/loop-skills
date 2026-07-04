---
name: loop-orchestrator
description: Mengatur alur utama agent loop, memilih skill berikutnya, dan menjaga urutan eksekusi tetap konsisten.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, orchestration, controller, routing]
---
# Loop Orchestrator

## When to Use
Gunakan saat Hermes perlu mengelola beberapa langkah kerja, memilih jalur eksekusi, atau menghubungkan beberapa skill dalam satu workflow.

## Inputs
- Tujuan utama.
- Konteks tugas.
- Constraint atau batasan.
- Status hasil dari skill lain.

## Procedure
1. Baca tujuan utama.
2. Tentukan apakah tugas perlu dipecah, dirutekan, atau dieksekusi langsung.
3. Pilih skill yang paling relevan.
4. Jalankan langkah secara berurutan atau paralel bila aman.
5. Minta verifikasi sebelum menutup tugas.
6. Replan bila hasil belum sesuai.

## Output
- Urutan langkah kerja.
- Skill yang dipanggil.
- Status eksekusi.
- Saran replan jika dibutuhkan.

## Pitfalls
- Jangan mengeksekusi tanpa tujuan yang jelas.
- Jangan lanjut jika hasil belum diverifikasi.
- Jangan memanggil skill yang tidak relevan.

## Verification
- Semua langkah utama punya alasan yang jelas.
- Output akhir sesuai tujuan awal.
- Tidak ada langkah penting yang terlewat.