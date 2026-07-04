---
name: loop-retry
description: Mengulang langkah yang gagal dengan strategi, parameter, atau pendekatan berbeda.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, retry, recovery]

---

# Loop Retry

## When to Use
Gunakan ketika eksekusi gagal tetapi masih layak dicoba lagi.

## Inputs
- Langkah gagal.
- Penyebab kegagalan.
- Parameter sebelumnya.
- Strategi alternatif.

## Procedure
1. Identifikasi titik gagal.
2. Tentukan apakah layak diulang.
3. Ubah parameter atau pendekatan.
4. Jalankan ulang satu langkah.
5. Catat hasil retry.

## Output
- Status retry.
- Perubahan strategi.
- Hasil ulang.
- Keputusan lanjut atau stop.

## Pitfalls
- Jangan retry tanpa mengubah apa pun.
- Jangan retry terus-menerus tanpa batas.
- Jangan mengabaikan akar masalah.

## Verification
- Retry punya alasan yang jelas.
- Hasil baru lebih baik atau lebih informatif.
- Proses tidak berputar sia-sia.