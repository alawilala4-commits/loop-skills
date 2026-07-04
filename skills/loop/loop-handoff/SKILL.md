---
name: loop-handoff
description: Menyerahkan pekerjaan ke skill lain, sub-agent, atau human review bila diperlukan.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, handoff, delegation, escalation]

---

# Loop Handoff

## When to Use
Gunakan saat tugas lebih cocok dikerjakan oleh skill lain atau perlu keputusan manusia.

## Inputs
- Tugas aktif.
- Alasan handoff.
- Pihak tujuan.
- Konteks yang harus dibawa.

## Procedure
1. Identifikasi alasan handoff.
2. Pilih penerima yang tepat.
3. Ringkas konteks penting.
4. Kirim tugas dengan instruksi jelas.
5. Catat status handoff.

## Output
- Pihak penerima.
- Ringkasan konteks.
- Alasan handoff.
- Status tindak lanjut.

## Pitfalls
- Jangan handoff terlalu cepat.
- Jangan kirim konteks terlalu panjang.
- Jangan kehilangan tujuan utama.

## Verification
- Penerima tepat.
- Konteks cukup untuk lanjut.
- Tugas berpindah tanpa kehilangan arah.