---
name: loop-budget
description: Mengontrol batas token, waktu, biaya, dan jumlah iterasi dalam proses Hermes.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, budget, limits, efficiency]

---

# Loop Budget

## When to Use
Gunakan saat workflow perlu dijaga agar tidak boros waktu, token, atau sumber daya.

## Inputs
- Budget tersedia.
- Estimasi langkah.
- Prioritas hasil.
- Batas iterasi.

## Procedure
1. Tetapkan budget awal.
2. Perkirakan biaya tiap langkah.
3. Kurangi langkah yang tidak penting.
4. Hentikan proses bila budget habis.
5. Laporkan trade-off yang terjadi.

## Output
- Batas budget.
- Sisa budget.
- Langkah yang dipotong.
- Alasan efisiensi.

## Pitfalls
- Jangan menghabiskan budget pada detail kecil.
- Jangan mengabaikan batas waktu.
- Jangan menjalankan loop tanpa batas.

## Verification
- Budget dipatuhi.
- Hasil tetap bernilai.
- Tidak ada pemborosan yang jelas.