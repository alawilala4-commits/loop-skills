---
name: loop-router
description: Memilih skill, tool, atau jalur kerja yang paling tepat untuk setiap subtask.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [loop, routing, selection, dispatch]

---

# Loop Router

## When to Use
Gunakan saat Hermes harus memutuskan skill mana yang paling cocok untuk satu subtask.

## Inputs
- Daftar subtask.
- Daftar skill tersedia.
- Tujuan subtask.
- Constraint teknis.

## Procedure
1. Identifikasi kebutuhan subtask.
2. Cocokkan dengan kemampuan skill yang tersedia.
3. Pilih skill paling relevan.
4. Catat alasan pemilihan.
5. Kirim subtask ke skill tujuan.

## Output
- Skill tujuan.
- Alasan pemilihan.
- Status routing.
- Alternatif jika skill utama gagal.

## Pitfalls
- Jangan memilih skill hanya karena nama mirip.
- Jangan kirim subtask tanpa alasan yang jelas.
- Jangan abaikan constraint.

## Verification
- Skill yang dipilih memang relevan.
- Routing efisien.
- Jalur cadangan tersedia bila perlu.