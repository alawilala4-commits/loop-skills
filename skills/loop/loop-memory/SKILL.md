---
name: loop-memory
description: Menyimpan konteks, keputusan, dan hasil kerja agar disimpan untuk iterasi berikutnya.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, memory, state, persistence]

---

# Loop Memory

## When to Use
Gunakan saat hasil, keputusan, atau konteks perlu disimpan untuk loop berikutnya.

## Inputs
- Konteks penting.
- Keputusan.
- Hasil kerja.
- Temuan berulang.
- Preferensi yang relevan.

## Procedure
1. Pilih informasi penting.
2. Buang detail yang tidak berguna.
3. Simpan dengan label jelas.
4. Kaitkan dengan tugas aktif.
5. Sediakan data untuk dipanggil ulang.

## Output
- State ringkas.
- Riwayat keputusan.
- Catatan temuan.
- Referensi konteks.

## Pitfalls
- Jangan menyimpan semuanya tanpa filter.
- Jangan menyimpan data yang tidak relevan.
- Jangan kehilangan konteks inti.

## Verification
- Informasi penting mudah dipakai ulang.
- State ringkas tapi lengkap.
- Tidak ada duplikasi berlebihan.