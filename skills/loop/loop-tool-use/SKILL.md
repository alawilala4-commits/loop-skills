---
name: loop-tool-use
description: Mengatur kapan dan bagaimana tool dipakai secara efisien dalam workflow Hermes.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, tools, integration, automation]

---

# Loop Tool Use

## When to Use
Gunakan saat Hermes harus memilih tool terbaik untuk menyelesaikan subtask.

## Inputs
- Subtask aktif.
- Daftar tool tersedia.
- Tujuan.
- Batasan penggunaan.

## Procedure
1. Identifikasi kebutuhan subtask.
2. Pilih tool yang paling tepat.
3. Jalankan tool hanya bila perlu.
4. Simpan hasilnya.
5. Evaluasi apakah tool tambahan diperlukan.

## Output
- Tool yang dipakai.
- Hasil tool.
- Alasan penggunaan.
- Status tindak lanjut.

## Pitfalls
- Jangan memakai tool tanpa alasan.
- Jangan pakai tool berulang jika hasil sudah cukup.
- Jangan mencampur banyak fungsi dalam satu tool call bila tidak perlu.

## Verification
- Tool dipilih secara tepat.
- Hasil tool relevan.
- Penggunaan efisien dan hemat langkah.