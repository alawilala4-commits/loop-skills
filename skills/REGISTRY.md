# REGISTRY.md
Daftar skill Hermes, hierarchy, fungsi, dan aturan pakai.

## Hierarchy

**Root**
- `multi-agent-orchestrator`

**Research / Evaluation pipeline**
- `scout`
- `search-engineering`
- `research-verifier`
- `judge`
- `builder-drafter`
- `quality-linter`
- `handoff-committer`

**Engineering pipeline**
- `test-driven-development`
- `systematic-debugging`
- `github-pr-workflow`

**Execution agents**
- `claude-code`
- `codex`

---

## 1) multi-agent-orchestrator
**Pipeline role:** Orchestrate  
**Tugas utama:** Mengatur alur kerja multi-agent dari awal sampai akhir.  
**Fungsi inti:** Memecah tugas besar menjadi langkah kecil, memilih skill yang tepat, memutuskan paralel vs berurutan, mengelola dependency, dan menjaga handoff tetap bersih.  
**Dipakai saat:** Tugas kompleks, banyak subtask, atau saat perlu koordinasi lintas skill.  
**Batasan:** Jangan menjadi penulis akhir atau evaluator konten utama; fokus pada routing dan kontrol alur.  
**Output yang diharapkan:** Rencana kerja, routing per skill, status blokir, dan handoff decision.  
**Relasi:** Mengawasi pipeline riset, engineering, dan execution agent.

---

## 2) scout
**Pipeline role:** Discovery  
**Tugas utama:** Menemukan sinyal awal yang layak diproses lebih lanjut.  
**Fungsi inti:** Mencari peluang, perubahan, isu, atau sumber baru dengan cakupan luas namun ringkas.  
**Dipakai saat:** Saat input masih kasar, banyak noise, atau perlu triage awal.  
**Batasan:** Jangan menganalisis terlalu dalam; cukup temukan kandidat paling menjanjikan.  
**Output yang diharapkan:** Daftar item singkat dengan alasan kenapa item itu penting.  
**Relasi:** Memberi input ke `search-engineering` atau langsung ke `judge`.

---

## 3) search-engineering
**Pipeline role:** Search  
**Tugas utama:** Mengubah kebutuhan menjadi pencarian yang tajam dan efektif.  
**Fungsi inti:** Menyusun query pendek, mencari sumber relevan, mengumpulkan bukti awal, dan mengurangi noise.  
**Dipakai saat:** Butuh data, referensi, fakta, atau bahan riset.  
**Batasan:** Jangan memutuskan final; fokus pada discovery berbasis pencarian.  
**Output yang diharapkan:** Query, sumber, ringkasan temuan, dan catatan gap.  
**Relasi:** Biasanya diikuti `research-verifier`.

---

## 4) research-verifier
**Pipeline role:** Verify  
**Tugas utama:** Memastikan bukti yang ditemukan benar, relevan, dan konsisten.  
**Fungsi inti:** Mengecek kredibilitas sumber, membandingkan referensi, mendeteksi kontradiksi, dan menilai kualitas evidence.  
**Dipakai saat:** Hasil riset perlu divalidasi sebelum dipakai.  
**Batasan:** Jangan menulis ulang hasil riset secara penuh; fokus pada validasi.  
**Output yang diharapkan:** Status valid/meragukan, konflik, gap, dan confidence note.  
**Relasi:** Menyuplai `judge` dan `builder-drafter`.

---

## 5) judge
**Pipeline role:** Evaluate  
**Tugas utama:** Menilai kandidat item dan menentukan langkah lanjut.  
**Fungsi inti:** Memberi keputusan `accept`, `reject`, `defer`, atau `needs_more_info` berdasarkan kriteria yang jelas.  
**Dipakai saat:** Ada beberapa kandidat atau perlu triage keputusan.  
**Batasan:** Jangan melakukan riset mendalam; fokus pada evaluasi dan routing.  
**Output yang diharapkan:** Keputusan singkat, alasan ringkas, dan prioritas tindak lanjut.  
**Relasi:** Mengarahkan item ke draft, verify ulang, atau stop.

---

## 6) builder-drafter
**Pipeline role:** Draft  
**Tugas utama:** Mengubah hasil tervalidasi menjadi output yang bisa dipakai.  
**Fungsi inti:** Menyusun draft, prompt, dokumen, atau struktur kerja yang jelas dan rapi.  
**Dipakai saat:** Hasil sudah cukup yakin dan perlu dikemas jadi deliverable.  
**Batasan:** Jangan menambahkan asumsi liar; gunakan hanya input yang sudah tervalidasi.  
**Output yang diharapkan:** Draft final atau hampir final dengan format bersih.  
**Relasi:** Biasanya setelah `research-verifier` dan sebelum `quality-linter`.

---

## 7) quality-linter
**Pipeline role:** Lint  
**Tugas utama:** Memeriksa kualitas akhir sebelum hasil dikirim.  
**Fungsi inti:** Mengecek struktur, konsistensi, kelengkapan, kejelasan, dan kesalahan nyata.  
**Dipakai saat:** Draft sudah jadi dan perlu quality gate.  
**Batasan:** Jangan mengubah arah isi secara besar; cukup koreksi yang perlu.  
**Output yang diharapkan:** Daftar issue, saran minimal, dan status siap kirim.  
**Relasi:** Menjaga agar `handoff-committer` menerima hasil yang bersih.

---

## 8) handoff-committer
**Pipeline role:** Deliver  
**Tugas utama:** Menyiapkan serah-terima akhir yang bersih dan ringkas.  
**Fungsi inti:** Mengemas hasil akhir, menyebutkan risiko tersisa, dan menandai apa yang sudah selesai.  
**Dipakai saat:** Semua pekerjaan inti selesai dan hasil siap disampaikan.  
**Batasan:** Jangan membuka analisis baru; fokus pada final packaging.  
**Output yang diharapkan:** Final handoff, ringkasan hasil, dan next action bila ada.  
**Relasi:** Titik akhir pipeline riset/delivery.

---

## 9) test-driven-development
**Pipeline role:** Code  
**Tugas utama:** Menjalankan pengembangan berbasis test dulu.  
**Fungsi inti:** Mendefinisikan perilaku lewat test, baru implementasi, lalu memastikan suite hijau.  
**Dipakai saat:** Bangun fitur baru, refactor, atau perbaikan yang butuh jaminan perilaku.  
**Batasan:** Jangan lompat ke implementasi sebelum kontrak perilaku jelas.  
**Output yang diharapkan:** Test cases, implementasi minimal, dan status lulus test.  
**Relasi:** Sering dipakai bersama `systematic-debugging` dan `github-pr-workflow`.

---

## 10) systematic-debugging
**Pipeline role:** Debug  
**Tugas utama:** Menemukan akar masalah sebelum memperbaiki.  
**Fungsi inti:** Reproduksi masalah, kumpulkan evidence, bentuk hipotesis, dan uji perbaikan secara bertahap.  
**Dipakai saat:** Bug, error, regresi, atau perilaku yang tidak konsisten.  
**Batasan:** Jangan menempel patch cepat tanpa root cause.  
**Output yang diharapkan:** Root cause, evidence, langkah perbaikan, dan verifikasi.  
**Relasi:** Menyokong `test-driven-development` dan `github-pr-workflow`.

---

## 11) github-pr-workflow
**Pipeline role:** PR/Release  
**Tugas utama:** Mengalirkan perubahan dari branch ke PR, review, merge, dan release.  
**Fungsi inti:** Membuat PR yang jelas, menjaga scope kecil, menindaklanjuti review, dan memastikan jalur rilis bersih.  
**Dipakai saat:** Perubahan sudah siap dibagikan ke repo atau masuk release flow.  
**Batasan:** Jangan merge tanpa validasi dan review yang memadai.  
**Output yang diharapkan:** PR description, checklist, review status, dan release readiness.  
**Relasi:** Biasanya diakhiri setelah `test-driven-development` atau `systematic-debugging`.

---

## 12) claude-code
**Pipeline role:** Agent  
**Tugas utama:** Menjalankan tugas agent umum secara fleksibel.  
**Fungsi inti:** Eksekusi interaktif, kerja multi-step, dan respons cepat untuk berbagai kebutuhan.  
**Dipakai saat:** Perlu agent general-purpose yang bisa bergerak cepat.  
**Batasan:** Tetap patuhi routing orchestrator dan jangan ambil alih peran spesialis tanpa alasan.  
**Output yang diharapkan:** Hasil kerja ringkas, jelas, dan siap dipakai.  
**Relasi:** Bisa bekerja di berbagai titik pipeline.

---

## 13) codex
**Pipeline role:** Agent  
**Tugas utama:** Menjalankan tugas coding dan automation dengan fokus eksekusi.  
**Fungsi inti:** Mengubah instruksi jadi implementasi yang minimal, benar, dan maintainable.  
**Dipakai saat:** Tugas dominan kode, scripting, atau otomasi.  
**Batasan:** Jangan terlalu banyak berbicara; fokus pada hasil konkret.  
**Output yang diharapkan:** Kode atau aksi yang siap pakai, plus ringkasan singkat.  
**Relasi:** Kuat untuk integrasi dengan `test-driven-development` dan `github-pr-workflow`.

---

## Urutan kerja utama

### Research path
`multi-agent-orchestrator` → `scout` → `search-engineering` → `research-verifier` → `judge` → `builder-drafter` → `quality-linter` → `handoff-committer`

### Engineering path
`multi-agent-orchestrator` → `test-driven-development` / `systematic-debugging` → `github-pr-workflow`

### Execution path
`multi-agent-orchestrator` → `claude-code` / `codex`

---

## Aturan desain
- Satu skill = satu tanggung jawab utama.
- Hindari overlap antar skill.
- Orchestrator mengatur, skill spesialis mengeksekusi.
- Judge hanya evaluasi, bukan riset.
- Linter hanya quality gate, bukan penulis utama.
- Handoff hanya finalisasi, bukan eksplorasi.
- Execution agents dipakai jika perlu kerja cepat dan interaktif.

---

## Catatan implementasi
- Gunakan nama skill yang stabil dan konsisten.
- Simpan detail panjang di dokumen terpisah bila perlu.
- Jaga agar deskripsi tetap ringkas supaya mudah dikenali sistem.
- Hierarchy ini dibuat untuk memudahkan routing, review, dan scaling.

---
Last updated: 2026-06-28
