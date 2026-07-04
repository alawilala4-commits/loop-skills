---
name: loop-planning
description: Menyusun rencana langkah demi langkah untuk tugas Hermes sebelum eksekusi dimulai.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, planning, decomposition, strategy]

---

# Loop Planning

## When to Use
Gunakan ketika tujuan masih umum dan perlu diubah menjadi langkah kerja yang terstruktur.

## Inputs
- Tujuan akhir.
- Prioritas.
- Constraint.
- Risiko.
- Sumber daya yang tersedia.

## Procedure
1. Identifikasi tujuan akhir.
2. Tentukan batasan dan risiko.
3. Pecah tugas menjadi langkah kecil.
4. Urutkan berdasarkan prioritas dan dependensi.
5. Hasilkan rencana singkat dan bisa dieksekusi.

## Output
- Daftar langkah kerja.
- Urutan prioritas.
- Dependensi antar langkah.
- Titik verifikasi.

## Pitfalls
- Jangan membuat rencana terlalu panjang.
- Jangan melewatkan constraint penting.
- Jangan mengasumsikan data yang belum ada.

## Verification
- Setiap langkah bisa dilakukan.
- Rencana menuju hasil yang jelas.
- Tidak ada langkah yang ambigu.