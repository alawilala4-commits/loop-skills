---
name: loop-replanner
description: Menyusun ulang rencana kerja bila hasil gagal, tidak lengkap, atau konteks berubah.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, replanning, recovery, adaptation]

---

# Loop Replanner

## When to Use
Gunakan saat rencana awal tidak berhasil, hasil berubah, atau constraint baru muncul.

## Inputs
- Rencana lama.
- Hasil verifikasi.
- Error yang ditemukan.
- Constraint baru.
- Tujuan yang masih berlaku.

## Procedure
1. Identifikasi penyebab kegagalan.
2. Pisahkan masalah utama dan masalah sampingan.
3. Susun rencana revisi.
4. Kurangi langkah yang tidak perlu.
5. Serahkan rencana baru ke orchestrator atau executor.

## Output
- Rencana revisi.
- Alasan perubahan.
- Langkah yang dihapus atau ditambah.
- Prioritas baru.

## Pitfalls
- Jangan mengulang rencana lama tanpa perubahan.
- Jangan memperbesar scope tanpa alasan.
- Jangan mengabaikan akar masalah.

## Verification
- Rencana baru menutup kelemahan lama.
- Langkah baru realistis.
- Tujuan tetap tercapai.