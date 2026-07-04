---
name: ai-research-workflow
description: "Alur kerja penelitian menggunakan AI: mengumpulkan referensi, menyintesis informasi, dan menyusun output akhir."
version: 1.0.0
author: OWL Agent
tags: [research, workflow, ai, intel]
triggers:
  - "riset topik"
  - "kumpulkan referensi"
  - "buat ringkasan literatur"
prerequisites:
  - Akses internet untuk pencarian web
  - Lingkungan eksekusi tersedia (local/VPS)
---

# AI Research Workflow

Alur kerja penelitian menggunakan AI: mengumpulkan referensi, menyintesis informasi, dan menyusun output akhir.

## Tujuan
Membantu pengguna dalam melakukan riset terkait topik tertentu, mengumpulkan sumber terpercaya, menyintesis fakta, dan menghasilkan ringkasan atau laporan yang dapat langsung digunakan.

## Trigger / Pemicu
- Pengguna berkata: "riset topik", "kumpulkan referensi", "buat ringkasan literatur"
- Permintaan untuk mencari informasi terbaru, perbandingan produk, atau summary dari dokumentasi teknis.

## Prasyarat
1. Akses internet untuk melakukan pencarian web atau mengakses dokumentasi publik.
2. Lingkungan eksekusi (local machine, VPS, atau container) tersedia dan dapat menjalankan perintah pencarian serta membuka halaman web.

## Input yang Dibutuhkan
- Topik atau pertanyaan utama.
- Batasan waktu jika ada (misalnya: terbaru, tahun tertentu, versi tertentu).
- Format output yang diinginkan (misalnya: bullet points, tabel, langkah-langkah-langkah).

## Output yang Diharapkan
- Ringkasan singkat dari topik.
- Poin-poin penting yang relevan.
- Referensi sumber dengan tautan atau kutipan.
- Rekomendasi tindak lanjut jika relevan (misalnya: area yang perlu riset lebih lanjut, tool yang direkomendasikan).

## Alur Kerja
1. Pahami intent user dan pecah menjadi sub-tugas.
2. Cari sumber yang relevan dan prioritaskan yang paling kredibel (dokumentasi resmi, jurnal terkemuka, situs berita terpercaya).
3. Ambil fakta yang langsung menjawab pertanyaan.
4. Jika ada beberapa opsi atau definisi, lakukan perbandingan.
5. Susun jawaban akhir secara ringkas dan jelas.
6. Jika informasi belum cukup, minta klarifikasi minimum yang diperlukan.

## Batasan Tool
### Boleh
- Pencarian web untuk fakta umum, dokumentasi, dan update terbaru.
- Membaca halaman dokumentasi publik.
- Mengambil kutipan singkat untuk verifikasi fakta.
- Menggunakan browser otomatis jika diperlukan untuk halaman interaktif.

### Tidak boleh
- Jangan melakukan aksi destruktif, seperti hapus data, deploy ke production, atau submit form sensitif tanpa instruksi eksplisit.
- Jangan login ke akun pengguna tanpa persetujuan jelas.
- Jangan mengeksekusi kode yang mengubah file penting tanpa konfirmasi.
- Jangan memakai tool browser untuk membuka situs berisiko tinggi jika tugas tidak membutuhkannya.
- Jangan mengarang sumber jika sumber belum ditemukan.

## Aturan Keselamatan
- Jika ada ambiguitas, pilih interpretasi paling masuk akal lalu sebutkan asumsi singkat.
- Jika sumber saling bertentangan, prioritaskan dokumentasi resmi atau sumber primer.
- Jika tugas menyentuh data pribadi, minta konfirmasi sebelum melanjutkan.

## Kriteria Selesai
Skill dianggap selesai jika:
- Pertanyaan user terjawab langsung.
- Sumber utama sudah cukup.
- Jawaban akhir bisa dipakai tanpa revisi besar.

## Catatan Implementasi
- Simpan instruksi panjang di file pendukung jika perlu.
- Gunakan subfolder `references/` untuk detail teknis.
- Gunakan `scripts/` hanya jika ada langkah yang perlu diotomatisasi.

## Verification Checklist
- [ ] Output berisi ringkasan yang jelas dan relevan dengan topik.
- [ ] Setiap fakta didukung oleh kutipan atau tautan ke sumber.
- [ ] Sumber yang digunakan terpercaya (dokumentasi resmi, jurnal terakreditasi, berita terpercaya).
- [ ] Tidak ada plagiarisme: konten ditulis ulang dengan kata sendiri, kutipan diberi tanda kutip dan atribusi.
- [ ] Format output sesuai permintaan user (bullet, tabel, langkah-langkah).
- [ ] Jika ada perbandingan, tabel atau poin-poin jelas menunjukkan perbedaan dan kesamaan.
- [ ] Tidak ada informasi yangarang atau spekulasi tanpa basis sumber.
- [ ] Link sumber aktif dan dapat diakses (jika mungkin).
- [ ] Output bebas dari kalimat yang ambigu atau berlebihan.
- [ ] Jika user meminta batasan waktu (mis. terbaru), semua sumber menggunakan data dalam rentang yang diminta.

## Anti-Pattern & Fixes
| Anti-Pattern | Dampak | Perbaikan |
|--------------|--------|-----------|
| Mengandalkan satu sumber saja | Bias, kurang verifikasi | Gunankan minimal 2-3 sumber independen untuk setiap klaim penting. |
| Meng kutip sumber tanpa verifikasi | Risiko informasi salah atau hoax | Buka sumber, pastikan relevansi, dan ambil kutipan langsung yang mendukung klaim. |
| Menyalin teks utuh dari sumber | Plagiarisme | Parafrasa dengan kata sendiri, beri kutipan hanya untuk fakta spesifik atau statistik. |
| Mengabaikan tanggal publikasi | Menggunakan data usang | Filter hasil pencarian oleh tanggal, prioritaskan sumber terbaru sesuai batasan user. |
| Menggunakan situs berita kabur atau blog tidak terverifikasi | Informasi kurang akurat | Prioritaskan situs resmi (.gov, .edu), jurnal peer-reviewed, atau media terkemuka dengan fakt-checking. |
| Tidak menyertakan referensi | Pengguna tidak bisa memverifikasi | Sertakan daftar referensi berformat mudah (URL, judul, tanggal akses). |
| Overload informasi tanpa struktur | Output sulit dibaca | Gunakan bullet, subheading, atau tabel untuk mengorganisir poin-poin. |
| Mengabaikan konteks lokal/topik spesifik | Informasi tidak relevan | Selalu hubungkan fakta kembali ke pertanyaan atau konteks user. |
| Mengandalkan pencarian web saja tanpa membaca konten keseluruhan | Kutipan diambil dari konteks salah | Baca sekilas abstract atau pengantar untuk memastikan konteks sesuai. |
| Memakai bahasa terlalu formal atau kasual tidak sesuai audiens | Output kurang tepat | Sesuaikan gaya bahasa dengan permintaan user (mis. teknis untuk profesional, santai untuk umum). |

## Recipes / Contoh Penggunaan
**Contoh 1: Riset tentang perbandingan framework CSS Tailwind vs Bootstrap**
1. Trigger: User berkata "bandingkan Tailwind CSS dan Bootstrap".
2. Deteksi kata kunci: perbandingan, framework CSS.
3. Alur:
   - Cari dokumentasi resmi Tailwind CSS dan Bootstrap.
   - Ambil poin-poin utama: ukuran file, kemudahan penggunaan, komponen UI, customisasi, komunitas.
   - Buat tabel perbandingan dengan kolom: Fitur, Tailwind, Bootstrap, Keterangan.
   - Sertakan kutipan singkat dari dokumentasi untuk setiap poin.
   - Ringkas keputusan: Tailwind lebih utility-first dan customizable; Bootstrap lebih siap pakai dengan komponen bawaan.
4. Output akhir berupa tabel + ringkasan + referensi.

**Contoh 2: Ringkasan literatur tentang dampak kerja jarak jauh pada produktivitas programmer**
1. Trigger: User berkata "riset topik produktivitas kerja remote programmer".
2. Alur:
   - Cari jurnal terkemuka (IEEE, ACM) dan studi tahun 2022-2024 menggunakan Google Scholar.
   - Ambil abstrak dan temuan utama: produktivitas meningkat/stabil, faktor yang mempengaruhi (komunikasi, workspace, work-life balance).
   - Sintesis dalam bullet points: faktor positif, faktor tantangan, rekomendasi manajer.
   - Sertakan referensi dengan link ke DOI atau URL.
3. Output: bullet points + referensi.

**Contoh 3: Membuat ringkasan fitur baru dari dokumentasi resmi library Python (mis. pandas 2.2)**
1. Trigger: User berkata "ringkasan fitur baru pandas 2.2".
2. Alur:
   - Buka halaman release notes pandas 2.2 di pandas.pydata.org.
   - Ekstrak setiap fitur baru: kolom nama nullable, peningkatan performa groupby, dukungan PyArrow backend.
   - Untuk setiap fitur, tuliskan deskripsi singkat dan contoh kode singkat jika relevan.
   - Format output sebagai daftar bernomor dengan sub-bullet.
3. Output: daftar fitur + contoh kode + referensi ke release notes.

## Decision Tree (ASCII Diagram)
```
Mulai
 |
 |-- Pahami pertanyaan user?
 |        |
 |        Ya --> Pecah menjadi sub-tugas (apa yang perlu dicari?)
 |        |
 |        Tidak --> Minta klarifikasi (minimal satu kata kunci)
 |
 |-- Untuk setiap sub-tugas:
 |        |
 |        --> Cari web dengan kata kunci relevan
 |        |
 |        --> Filter hasil: prioritaskan .gov, .edu, dokumentasi resmi, jurnal terkemuka
 |        |
 |        --> Buka 2-3 sumber teratas, ambil kutipan yang langsung menjawab
 |        |
 |        --> Jika ada beberapa opsi/definisi, buat perbandingan (tabel atau poin-poin)
 |        |
 |        --> Susun jawaban: ringkasan + poin penting + referensi
 |        |
 |        --> Jika informasi kurang, ulangi pencarian dengan kata kunci lain atau minta klarifikasi
 |
 |-- Apakah semua sub-tugas terpenuhi?
 |        |
 |        Ya --> Buat output akhir sesuai format yang diminta (bullet, tabel, langkah)
 |        |
 |        Tidak --> Kembali ke langkah pencarian untuk sub-tugas yang kurang
 |
 |-- Verifikasi checklist (lihat di atas)
 |
 |-- Selesai
```

## FAQ
**Q: Saya tidak yakin sumber mana yang terpercaya.**  
A: Prioritaskan: (1) dokumentasi resmi produk/proyek, (2) jurnal peer-reviewed (IEEE, ACM, Springer), (3) laporan pemerintah atau lembaga riconosciuto, (4) media terkemuka yang memiliki fakta-checking (BBC, Reuters, Kompas). Hindari blog pribadi tanpa kredibilitas atau forum tanpa verifikasi.

**Q: Bagaimana jika saya menemukan informasi yang bertentangan antar sumber?**  
A: Periksa tanggal dan otoritas sumber. Pilih informasi dari sumber yang lebih baru dan lebih otoritatif (mis. dokumentasi resmi > blog). Sebutkan dalam output bahwa ada perbedaan dan berikan masing-masing sumber beserta versi/tanggalnya.

**Q: Apakah saya bisa menggunakan kutipan langsung lebih dari 90 karakter?**  
A: Disarankan tidak melebihi 2 kalimat atau sekitar 120 kutipan untuk menghindari plagiarisme. Jika diperlukan kutipan lebih panjang, gunakan blok kutipan dan sertakan atribusi lengkap.

**Q: Saya perlu output dalam format tertentu (mis. slide PowerPoint atau markdown).**  
A: Skill ini menghasilkan konten teks yang dapat dengan mudah dikonversi. Anda dapat menyalin hasil ke dalam template markdown atau slide dan menambahkan formatting sesuai kebutuhan. Jika ingin format file langsung, beri tahu saya dan saya dapat menambahkan langkah konversi (mis. pandoc) ke dalam skill.

**Q: Bagaimana jika topik sangat spesifik dan hasil pencarian sedikit?**  
A: Luaskan kata kunci dengan sinonim atau istilah yang lebih luas, lalu filter hasil lagi untuk relevansi. Jika masih sedikit, berikan informasi yang ada bersama catatan bahwa data terbatas dan mungkin perlu riset lapangan atau sumber primer (wawancara, data internal).

## Referensi & Template
- **Template Ringkasan Bullet**:  
  ```
  - **Poin utama**: penjelasan singkat.  
    Sumber: [Judul](URL) (tanggal akses)
  ```
- **Template Tabel Perbandingan**:  
  | Fitur | Opsi A | Opsi B | Keterangan |
  |-------|--------|--------|------------|
  | Fitur 1 | nilai | nilai | keterangan |
  | Sumber: [Judul A](URL_A), [Judul B](URL_B) |
- **Template Referensi**:  
  1. Judul dokumen. Nama Situs, tahun. URL (diakses: DD Bulan YYYY).  
  2. Nama Penulis. “Judul Artikel.” Jurnal, vol(no), halaman, tahun. DOI.

## Integrasi dengan Skill Lain
- `depends_on: []` – skill ini dapat berdiri sendiri, tetapi biasanya dijalankan setelah pengguna menyampaikan topik riset.
- `next_on_success: [\"skill_builder-drafter\"]` – bila output perlu disusun menjadi draft dokumen lebih formal (mis. laporan, proposal), alihkan ke skill yang menyusun draft.
- `next_on_failure: [\"skill_clarify\"]` – jika informasi tidak cukup atau ambigu, alihkan ke skill klarifikasi untuk menanyakan detail lebih lanjut dari pengguna.

## Versi dan Changelog
- **v1.0.0** – Rilis awal dengan struktur lengkap, verification checklist, anti-patterns, recipes, decision tree, FAQ, dan integrasi.
- **v0.1.0** – Versi awal hanya berisi dasar alur kerja, trigger, prerequisites, dan langkah-langkah umum.

## Lisensi
MIT – Bebas digunakan dan dimodifikasi dengan mencantumkan atribusi.