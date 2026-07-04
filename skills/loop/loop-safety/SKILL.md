---
name: loop-safety
description: Menjaga aksi agent tetap aman, valid, dan tidak keluar dari batas.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, safety, guardrails, policy]

---

# Loop Safety

## When to Use
Gunakan sebelum aksi berisiko, sebelum tool berbahaya, atau saat output sensitif.

## Inputs
- Aksi yang akan dilakukan.
- Risiko.
- Batas kebijakan.
- Konteks sensitif.

## Procedure
1. Identifikasi risiko.
2. Cek apakah aksi boleh dilakukan.
3. Kurangi scope bila perlu.
4. Minta verifikasi jika tidak aman.
5. Blokir tindakan yang melanggar batas.

## Output
- Status aman/tidak aman.
- Risiko utama.
- Aksi yang diizinkan.
- Aksi yang ditolak.

## Pitfalls
- Jangan mengabaikan risiko kecil yang berdampak besar.
- Jangan teruskan aksi tanpa cek safety.
- Jangan menyamakan "bisa dilakukan" dengan "aman dilakukan".

## Verification
- Aksi sesuai batas.
- Risiko sudah dipertimbangkan.
- Keputusan aman terdokumentasi.