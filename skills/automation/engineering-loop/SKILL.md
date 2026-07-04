---
name: engineering-loop
description: "Loop rekursif untuk mengerjakan task engineering (coding, automation, integrasi) dengan siklus plan → execute → verify → fix → repeat atau selesai."
version: "1.0.0"
author: OWL Agent
tags:
  - loop
  - engineering
  - orchestrator
  - automation
triggers:
  - "jalankan loop"
  - "kerjakan tugas besar"
  - "otomatisin workflow"
  - "selesaikan issue ini"
---

# Engineering Loop

Loop rekursif untuk mengerjakan task engineering (coding, automation, integrasi) dengan siklus plan → execute → verify → fix → repeat atau selesai.

## Tujuan
Skill ini mengelola satu tugas engineering dari awal sampai selesai menggunakan siklus berulang:
1. Memahami dan memecah task.
2. Menjalankan langkah-langkah kecil.
3. Mengecek hasil dan mencatat state.
4. Memperbaiki jika ada masalah.
5. Mengulang sampai kriteria selesai tercapai atau perlu handoff ke manusia.

## Fase loop
Gunakan fase-fase ini setiap iterasi:

1. **Plan**
   - Baca konteks, issue, atau permintaan user.
   - Pecah menjadi sub-tugas kecil yang bisa selesai dalam 1–2 langkah konkret.
   - Tuliskan rencana singkat untuk iterasi ini saja (bukan seluruh proyek).

2. **Execute**
   - Jalankan sub-tugas sesuai plan: coding, konfigurasi, menulis dokumen, atau menyiapkan automation.
   - Jangan mengubah banyak hal sekaligus; fokus pada satu perubahan yang bisa diuji dengan jelas.

3. **Verify**
   - Cek hasil dengan cara paling langsung yang memungkinkan: tes otomatis, linting, inspeksi manual, atau review struktur.
   - Catat apakah langkah berhasil, sebagian berhasil, atau gagal total.

4. **Adjust**
   - Kalau gagal, analisis penyebabnya dan usulkan perbaikan eksplisit untuk iterasi berikutnya.
   - Kalau berhasil tapi belum memenuhi tujuan akhir, rencanakan langkah lanjut yang paling penting.
   - Kalau sudah memenuhi tujuan dan aman, siapkan ringkasan final.

5. **Record & Decide**
   - Perbarui state loop: apa yang baru saja dilakukan, hasilnya, dan apa berikutnya.
   - Putuskan: lanjut iterasi berikut, atau akhiri loop dan handoff ke manusia.

## Batasan tool

### Boleh
- Menggunakan editor/kode untuk perubahan kecil yang bisa diuji.
- Menjalankan tes otomatis, linting, dan static analysis.
- Menggunakan web search untuk dokumentasi dan referensi teknis.
- Membaca/menulis berkas konfigurasi non-kritis (mis. lokal, staging, file contoh).

### Tidak boleh
- Jangan deploy ke production tanpa instruksi eksplisit.
- Jangan menghapus berkas penting atau data user.
- Jangan menjalankan perintah destruktif (mis. `rm -rf`, `DROP TABLE`) tanpa konfirmasi manusia.
- Jangan mengubah lebih dari satu area besar sekaligus dalam satu iterasi; jika perlu, pecah tugas jadi beberapa iterasi.

## Kriteria selesai
Loop boleh dihentikan jika:
- Tujuan utama (issue/task) sudah tercapai dan terverifikasi.
- Tidak ada lagi perbaikan penting yang dapat dilakukan otomatis dengan aman.
- Diperlukan keputusan atau penilaian manusia untuk melanjutkan.

## Handoff ke manusia
Saat loop memutuskan berhenti:
- Buat ringkasan singkat: apa yang sudah dilakukan, apa yang belum, dan risiko yang tersisa.
- Sertakan rekomendasi langkah berikut untuk manusia.
- Pastikan semua perubahan tercatat dengan jelas (commit, file changelog, atau catatan sistem).

## State & Rekam Jejak
- Gunakan file atau struktur state (mis. JSON / STATE.md) untuk mencatat:
  - fase saat ini,
  - sub-tugas yang dilakukan,
  - hasil verifikasi,
  - rencana iterasi berikutnya.
- Setiap iterasi harus mengacu ke state sebelumnya sehingga loop tetap tahu “di mana posisi sekarang”.

## Verification Checklist
- [ ] Rencana iterasi jelas dan terukur (sub‑tugas spesifik, kriteria sukses terdefinisi).
- [ ] Setiap sub‑tugas dieksekusi menggunakan skill yang sesuai (coding, testing, debugging, dsb.).
- [ ] Hasil verifikasi tercatat (pass/fail, log, screenshot jika relevan).
- [ ] Jika gagal, analisis penyebab ditulis dan perbaikan untuk iterasi berikutnya direncanakan.
- [ ] State iterasi (JSON/FILE) diperbarui setelah setiap siklus.
- [ ] Batas iterasi maksimal tidak terlampaui; jika tercapai, loop berhenti dengan penjelasan.
- [ ] Semua perubahan bersifat reversible (commit, backup, atau file temporary) sebelum diterapkan ke produksi.
- [ ] Akhir loop menghasilkan ringkasan yang mencapai tujuan awal atau memberikan alasan berhenti.
- [ ] Tidak ada perintah destruktif yang dijalankan tanpa konfirmasi atau validasi.
- [ ] Output akhir (laporan, file perubahan) tersedia untuk ditinjau oleh pengguna atau skill selanjutnya.

## Anti‑Pattern & Fixes
| Anti‑Pattern | Dampak | Perbaikan |
|--------------|--------|-----------|
| Loop tanpa batas iterasi maksimal | Risiko infinite loop, konsumsi resource tak terbatas | Tetapkan `max_iterations` (mis. 5) dan hentikan dengan laporan jika tercapai. |
| Mengubah banyak file sekaligus dalam satu iterasi | Sulit menyalurkan penyebab kegagalan, meningkatkan risiko regresi | Fokus pada satu file atau satu perubahan kecil per iterasi; gunakan commit terpisah bila memungkinkan. |
| Melewati langkah verifikasi | Masalah tidak terdeteksi hingga akhir, memperbaiki lebih mahal | Selalu jalankan verifikasi (tes, lint, inspeksi) setelah setiap eksekusi. |
| Tidak mencatat state iterasi | Hilang konteks, ulang usaha yang sama | Simpan state (JSON/file) setelah setiap iterasi dan bacanya sebelum memulai siklus berikutnya. |
| Menganggap “selesai” hanya karena satu sub‑tugas berhasil | Tujuan utama mungkin belum terpenuhi | Evaluasi keseluruhan kriteria selesai, bukan hanya sub‑tugas terakhir. |
| Mengabaikan pesan error atau warning | Masalah kecil bisa mengakumulasi menjadi besar | Catat dan analisis semua output error/warning; jika signifikan, perbaiki sebelum lanjut. |
| Menggunakan perintah destruktif tanpa konfirmasi | Hilang data atau konfigurasi penting | Tambahkan konfirmasi pengguna atau backup sebelum menjalankan perintah berpotensi merusak. |
| Tidak memberi ruang untuk intervensi manusia ketika diperlukan | Loop mungkin terus berjalan meskipun keputusan subjektif diperlukan | Tambahkan titik decision di mana loop meminta klarifikasi atau handoff ke manusia jika ambigu atau butuh penilaian subjektif. |
| Mengulang identical action tanpa perubahan | Loop stagnasi, tidak ada progres | Setelah kegagalan, ubah parametre atau metode (mis. ganti approach, tambahkan debugging) sebelum mencoba lagi. |

## Recipes / Contoh Penggunaan

### Contoh 1: Perbaikan bug dalam fungsi Python
1. **Trigger**: Pengguna berkata “selesaikan issue ini: fungsi hitung_total salah ketika input negatif”.
2. **Plan**:
   - Sub‑tugas 1: Buat unit test yang meniru kasus negatif.
   - Sub‑tugas 2: Lihat kode fungsi, temukan logika yang salah.
   - Sub‑tugas 3: Perbaiki fungsi.
   - Sub‑tugas 4: Jalankan seluruh test suite.
3. **Execute**:
   - Jalankan `skill_coding` untuk menulis test, lalu `skill_coding` lagi untuk perbaikan kode.
4. **Verify**:
   - Jalankan `skill_testing` (pytest) dan periksa lulus.
5. **Adjust**:
   - Jika test masih gagal, analisis traceback dan perbaiki lagi.
6. **Record & Decide**:
   - Simpan hasil setiap iterasi, update state, jika semua test lulus → selesai.

### Contoh 2: Menyiapkan skrip otomatisasi backup harian
1. **Trigger**: “otomatisin backup folder konfigurasi setiap malam”.
2. **Plan**:
   - Sub‑tugas 1: Tuliskan script bash yang melakukan rsync ke lokasi backup.
   - Sub‑tugas 2: Tambahkan entri crontab untuk menjalankannya setiap jam 02:00.
   - Sub‑tugas 3: Uji script secara manual.
   - Sub‑tugas 4: Verifikasi crontab terpasang dan menjalankan.
3. **Execute**:
   - Gunakan `skill_coding` untuk menulis script, lalu terminal untuk menambahkan crontab.
4. **Verify**:
   - Jalankan script secara manual dan periksa hasil backup.
   - Periksa syslog/cron untuk konfirmasi terjadwal.
5. **Adjust**:
   - Jika script gagal karena path salah, perbaiki path dan ulangi.
6. **Record & Decide**:
   - Setelah verifikasi sukses, catat bahwa tugas selesai dan beri laporan akhir.

### Contoh 3: Integrasi API eksternal ke dalam layanan existentes
1. **Trigger**: “integrasikan layanan pembayaran X ke API kami”.
2. **Plan**:
   - Sub‑tugas 1: Baca dokumentasi API X, buat spesifikasi request/response.
   - Sub‑tugas 2: Tambahkan fungsi wrapper di kode.
   - Sub‑tugas 3: Tulis unit test untuk menangani sukses dan kegagalan.
   - Sub‑tugas 4: Jalankan integrasi test di staging.
3. **Execute**:
   - `skill_coding` untuk menulis wrapper dan test.
4. **Verify**:
   - Jalankan test, lakukan manual check dengan sandbox API.
5. **Adjust**:
   - Jika gagal karena autentikasi, perbaiki header dan ulangi.
6. **Record & Decide**:
   - Setelah semua test lulus di staging, tandai selesai dan siapkan pull‑request.

## Decision Tree (ASCII Diagram)

```
Mulai
 |
 |-- Definisikan tujuan akhir & kriteria selesai?
 |        |
 |        Ya --> Buat rencana iterasi pertama (sub‑tugas + kriteria sukses)
 |        |
 |        Tidak --> Minta klarifikasi minimal dari user
 |
 |-- Untuk setiap iterasi:
 |        |
 |        --> Eksekusi sub‑tugas sesuai rencana
 |        |
 |        --> Verifikasi hasil (tes/lint/inspeksi)
 |        |
 |        --> Apakah semua kriteria sukses terpenuhi?
 |                 |
 |                 Ya --> Buat laporan akhir, kirim sinyal selesai
 |                 |
 |                 Tidak --> Analisis kegagalan, perbaiki rencana untuk iterasi berikutnya
 |                 |
 |        --> Update state iterasi, increment counter
 |        |
 |        --> Apakah iterasi >= max_iterations?
 |                 |
 |                 Ya --> Buat laporan gagal (batas iterasi tercapai), berhenti
 |                 |
 |                 Tidak --> Kembali ke awal loop (rencana iterasi berikutnya)
 |
 Selesai
```

## FAQ
**Q: Bagaimana menentukan nilai maksimal iterasi yang tepat?**  
A: Bergantung pada kompleksitas tugas. Untuk bug sederhana, 3‑5 iterasi biasanya cukup. Untuk fitur besar yang perlu banyak sub‑tugas, bisa naik ke 8‑10. Selalu beri ruang untuk evaluasi awal; jika setelah 2 iterasi belum ada progres, pertimbangkan untuk menambah waktu atau mendapatkan bantuan manusia.

**Q: Apakah saya boleh mengulang sub‑tugas yang sama dalam iterasi berbeda?**  
A: Ya, jika sub‑tugas perlu refinemen (mis. memperbaiki bug yang masih muncul). Namun pastikan setiap ulangan membawa perubahan (mis. perbaikan yang berbeda) dan dicatat dalam supaya tidak terjadi loop tak berguna.

**Q: Bagaimana jika verifikasi membutuhkan manual review yang memakan waktu?**  
A: Anda masih dapat memasukkan langkah manual sebagai bagian dari verifikasi, tetapi catat hasilnya (mis. screenshot atau catatan) dan lanjutkan ke adjust. Jika memang butuh keahlian spesialis, lakukan handoff ke manusia setelah mencatat temuan.

**Q: Bisakah saya menggunakan skill ini untuk tugas non‑technical (mis. menulis dokumen)?**  
A: Ya, selama Anda dapat men‑define sub‑tugas (mis. outline, tulis bagian, review) dan memiliki cara verifikasi (melihat apakah bagian tersebut sesuai outline, mendapat masukan reviewer), loop akan bekerja.

**Q: Apa yang harus saya lakukan jika loop terus mengembalikan ke 똑같은 kegagalan?**  
A: Lihat kolom “Analisis kegagalan” – mungkin Anda perlu mengganti strategi sepenuhnya (mis. pendekatan algoritmik, menggunakan library lain, atau mendefinisikan ulang sub‑tugas). Jika masih tidak berubah setelah 2‑3 kali percobaan berbeda, eskalasi ke umano atau cari referensi tambahan.

## Referensi & Template
- **Template State JSON** (simpan di `~/.hermes/tmp/engineering-loop-state.json`):
  ```json
  {
    "iteration": 3,
    "goal": "Perbaiki bug hitung_total",
    "plan": [
      {"subtask": "Buat test case negatif", "criteria": "Test passes"},
      {"subtask": "Perbaiki fungsi", "criteria": "Semua test lulus"}
    ],
    "results": [
      {"subtask": "Buat test case negatif", "status": "pass", "notes": ""},
      {"subtask": "Perbaiki fungsi", "status": "fail", "notes": "AssertionError: expected 0 got -5"}
    ],
    "next_plan": [
      {"subtask": "Investigasi logika kondisi", "criteria": "Menemukan penyebab"}
    ]
  }
  ```
- **Template Laporan Iterasi** (markdown):
  ```
  ## Iterasi #<n>
  - **Rencana**: <deskripsi singkat>
  - **Eksekusi**: <perintah/skill yang dipakai>
  - **Verifikasi**: <hasil tes/lint, pass/fail>
  - **Catatan**: <apa yang terjadi, error, wawasan>
  - **Keputusan**: lanjut/ulang/revisi/selesai
  ```
- **Template Laporan Akhir**:
  ```
  # Laporan Akhir Engineering Loop
  **Tujuan**: <tujuan awal>
  **Iterasi total**: <n>
  **Hasil**: <selesai/gagal karena batas iterasi>
  **Ringkasan per iterasi**:
  - Iter 1: …
  - Iter 2: …
  …
  **Rekomendasi**: <langkah selanjutnya untuk pengguna atau handoff>
  ```

## Integrasi dengan Skill Lain
- `depends_on: []` – dapat berdiri sendiri, tetapi biasanya dipicu setelah pengguna menentukan tujuan teknik.
- `next_on_success: [\"skill_builder-drafter\", \"skill_handoff-committer\"]` – bila loop selesai dengan sukses, hasil dapat disusun menjadi dokumen lebih formal atau diserah‑terima ke pipeline produksi.
- `next_on_failure: [\"skill_clarify\"]` – jika loop berhenti karena ambiguitas atau kebutuhan keputusan manusia, alihkan ke skill klarifikasi untuk mendapatkan informasi lebih lanjut dari pengguna.
- Bisa juga memanggil `skill_coding`, `skill_testing`, `skill_debugging`, `skill_review` sebagai sub‑tugas dalam fase Execute/Verify.

## Versi dan Changelog
- **v1.0.0** – Rilis awal dengan struktur lengkap, verification checklist, anti‑pattern & fixes, recipes, decision tree, FAQ, referensi, integrasi, dan contoh penggunaan.
- **v0.1.0** – Versi awal hanya berisi dasar alur kerja, trigger, prerequisites, dan langkah‑langkah umum.

## Lisensi
MIT – Bebas digunakan dan dimodifikasi dengan mencantumkan atribusi.