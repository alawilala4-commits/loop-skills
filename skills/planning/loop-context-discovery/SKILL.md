---
name: loop-context-discovery
description: "Menemukan file, fungsi, konfigurasi, dan log yang relevan sebelum melakukan perubahan."
version: "1.0.0"
author: OWL Agent
tags:
  - context
  - discovery
  - repo
triggers:
  - "cari file relevan"
  - "temukan konteks"
  - "scan kode sebelum edit"
---

# Loop Context Discovery

Menemukan file, fungsi, konfigurasi, dan log yang relevan sebelum melakukan perubahan.

## Tujuan
Menghindari perubahan buta dengan terlebih dahulu menemukan bagian kode/konfigurasi yang benar-benar relevan dengan tugas, sehingga setiap iterasi loop dapat fokus pada area yang tepat dan terukur.

## Kapan dipakai
Gunakan skill ini setelah Anda memiliki rencana singkat dari loop-planning dan ingin memastikan Anda mengetahui lokasi spesifik file, fungsi, konfigurasi, atau log yang perlu diedit atau diperiksa sebelum melakukan perubahan.

## Input yang dibutuhkan
- Rencana singkat dari loop-planning (mis. daftar langkah kecil yang akan dilakukan).
- Nama modul, service, atau fitur yang terdampak (jika diketahui).
- Opsional: batasan environment (lokal, VPS, Android/Termux) untuk menyesuaikan pencarian.

## Langkah kerja
1. **Ambil rencana singkat** – ekstrak kata kunci, nama fungsi, nama file yang disebutkan.
2. **Gunakan pencarian teks dan struktur directory** untuk menemukan:
   - file utama yang berkaitan dengan fitur atau modul yang disebutkan.
   - file konfigurasi (`.env`, `.yaml`, `.yml`, `.json`, `.toml`, `config.js`, `settings.py`, dsb.).
   - file test yang sudah ada untuk fitur tersebut (mis. `tests/`, `__tests__`, `spec/`).
3. **Identifikasi titik masuk (entry points)** dan dependensi penting:
   - file yang dieksekusi pertama kali (mis. `main.py`, `index.js`, `server.ts`).
   - file yang di‑import atau required oleh file target.
4. **Catat file/fungsi yang**:
   - akan diedit dalam iterasi ini.
   - perlu dicek ulang setelah perubahan (mis. test terkait, konfigurasi yang mungkin terpengaruh).
5. **Pilih subset kecil file** yang benar‑benar akan disentuh di iterasi ini (biasanya 1‑3 file) agar loop tetap fokus dan verifikasi cepat.
6. **Catat hubungan antar file** jika penting (mis. fungsi A memanggil fungsi B, konfigurasi C digunakan oleh modul D).
7. **Berikan saran area yang paling aman untuk perubahan pertama** (mis. file dengan test terisolasi, atau fungsi helper yang tidak berpengaruh ke core).

## Output yang diharapkan
- Daftar file/fungsi relevan dengan lokasi lengkap (path relatif dari repo root).
- Catatan singkat hubungan antar file (jika adaDependencies kritis).
- Saran area yang paling aman untuk perubahan pertama (mis. “Edit `utils/helpers.js` karena memiliki unit test terpisah dan tidak memengaruhi API publik”).

## Batasan tool
- **Hanya operasi baca (read‑only)** terhadap file dan struktur directory.
- **Jangan melakukan perubahan file atau konfigurasi** di skill ini – semua perubahan akan dilakukan oleh skill lain (coding, testing, dsb.) di iterasi selanjutnya.

## Verification Checklist
- [ ] Output berisi daftar file dengan path lengkap dan jelas.
- [ ] Setiap item dalam daftar memiliki alasan mengapa relevan (mis. “mengandungi fungsi X yang disebutkan dalam rencana”).
- [ ] File konfigurasi yang relevan (jika ada) terdaftar.
- [ ] File test yang terkait dengan fungsi/file yang akan diedit teridentifikasi.
- [ ] Titik masuk dan dependensi penting telah diidentifikasi (jika berlaku).
- [ ] Subset file yang dipilih untuk iterasi pertama adalah minimal dan terfokus (biasanya ≤ 3 file).
- [ ] Tidak ada file yang tidak terkait dengan rencana yang disertakan secara tidak perlu.
- [ ] Jika ada log atau file catatan yang relevan (mis. log aplikasi, file migration), mereka juga tercantum.
- [ ] Output dapat dengan mudah dibaca oleh manusia dan dapat dimasukkan ke state loop (mis. JSON atau catatan teks).

## Anti‑Pattern & Fixes
| Anti‑Pattern | Dampak | Perbaikan |
|--------------|--------|-----------|
| Mengembalikan ratusan file tanpa filter | Informasi berlebih, menyulitkan pemilihan area fokus | Batasi hasil pencarian dengan konteks (nama modul, ekstensi file, directory yang relevan). |
| Melewati file konfigurasi yang penting | Perubahan kode bisa gagal karena konfigurasi tidak sesuai | Selalu sertakan pencarian untuk ekstensi konfigurasi umum (`.env`, `.yaml`, `.yml`, `.json`, `.toml`, `config.*`, `settings.*`). |
| Menganggap file dengan nama cocok adalah yang benar tanpa memeriksa isi | Bisa menunjuk ke file dummy atau contoh yang tidak digunakan | Setelah menemukan kandidat, lihat isi singkat (mis. baris pertama) untuk memastikan relevansi. |
| Tidak mengidentifikasi test terkait | Risiko perubahan tidak teruji sampai tidak terdeteksi tidak terjangkau oleh test | Setelah menemukan fungsi/file target, cari file test yang mengimpor atau menyebutkannya. |
| Memilih file yang terlalu banyak untuk iterasi pertama | Melanggar prinsip loop kecil, memperlambat verifikasi | Pilih subset terkecil yang masih dapat memberikan nilai (biasanya satu file utama + satu test terkait). |
| Mengabaikan hubungan antar file (mis. fungsi yang dipanggil dari banyak tempat) | Perubahan bisa menimbulkan efek samping yang tidak terduga | Catat dependensi dan jika ada banyak pemanggil, pertimbangkan untuk membuat perubahan yang backward compatible atau menambahkan test regresi. |
| Mengandalkan pencarian nama saja tanpa melihat struktur directory | Puede melewatkan file yang ada di subfolder dengan nama berbeda namun fungsi serupa | Gunakan pencarian rekursif dengan pola yang fleksibel dan perhatikan struktur folder (mis. `src/`, `lib/`, `pkg/`). |
| Menyertakan file binary atau besar (mis. gambar, database) dalam daftar | Memboroskan output dan tidak relevan untuk perubahan kode | Filter hasil berdasarkan ekstensi kode dan konfigurasi; abaikan file binary atau ukuran > 100KB kecuali spesifik yang diperlukan. |
| Tidak mencatat asumsi atau batasan pencarian | Pengguna mungkin tidak tahu batasan hasil | Tambahkan catatan singkat di output tentang bagaimana pencarian dilakukan (mis. “Diketahui hasil pencarian terbatas pada folder `src/` dan ekstensi `.py`, `.js`, `.ts`”). |
| Memberi saran area yang tidak aman (mis. file core tanpa test) | Risiko regresi tinggi | Prioritaskan file yang memiliki test terpisah atau adalah utility/helper sebelum menyentuh core API atau konfigurasi produksi. |

## Recipes / Contoh Penggunaan

### Contoh 1: Menemukan file yang relevan sebelum memperbaiki bug login
**Rencana dari loop-planning**: “Iterasi 1: Tambah unit test login dengan password khusus”.
**Input**:
- Rencana: tambah unit test login dengan password khusus.
- Nama modul: `auth`.
**Langkah kerja**:
1. Ekstrak kata kunci: `login`, `password`, `auth`.
2. Pencarian teks:
   - Cari file yang mengandungi kata “login” dan “auth”: hasil `src/auth.py`, `routes/auth.js`, `tests/auth_test.py`.
   - Cari konfigurasi terkait auth: `.env` (lihat baris `JWT_SECRET`), `config/auth.yaml`.
   - Cari test login: `tests/auth/test_login.py`, `__tests__/auth.test.js`.
3. Identifikasi titik masuk: `src/auth.py` berisi fungsi `login_user` yang dipanggil oleh `routes/auth.js`.
4. Catat file/fungsi yang akan diedit: `tests/auth/test_login.py` (karena rencana ingin menambah test).
   - Perlu dicek ulang setelah perubahan: `src/auth.py` (pastikan fungsi login masih bekerja) dan `config/auth.yaml` (pastikan tidak ada konfigurasi yang membatasi karakter khusus).
5. Pilih subset kecil untuk iterasi pertama: `tests/auth/test_login.py` saja (karena menambah test tidak mengubah kode produksi).
6. Hubungan antar file: `tests/auth/test_login.py` mengimpor `login_user` dari `src/auth.py`.
7. Saran area aman untuk perubahan pertama: Edit `tests/auth/test_login.py` karena hanya menambah test, tidak berisiko mengubah perilaku esistensi.
**Output**:
- File yang akan diedit: `tests/auth/test_login.py` (tambah test case untuk password khusus).
- File yang perlu dicek setelah perubahan: `src/auth.py`, `config/auth.yaml`.
- Hubungan: test mengimpor fungsi login_user dari src/auth.py.
- Saran aman: mulai dengan menambah test karena isolasi dan dapat diverifikasi dengan langsung menjalankan test suite.

### Contoh 2: Menemukan konfigurasi sebelum menambahkan fitur ekspor CSV
**Rencana**: “Iterasi 1: Tambah argumen `--export-csv` ke parser CLI”.
**Input**:
- Rencana: tambah argumen ekspor CSV.
- Nama fitur: `export`.
**Langkah kerja**:
1. Kata kunci: `export`, `csv`, `cli`.
2. Pencarian:
   - File CLI utama: `src/main.py`, `cli/index.js`.
   - File konfigurasi yang mungkin terkait: `config.csv.yaml`, `.env` (variabel `EXPORT_PATH`).
   - Test terkait CLI: `tests/cli/test_main.py`, `spec/cli_spec.js`.
3. Titik masuk: `src/main.py` berisi fungsi `parse_args` dan `main`.
4. Akan diedit: `src/main.py` (menambahkan argumen baru).
   - Perlu dicek: `tests/cli/test_main.py` (untuk memastikan argumen baru terdeteksi), `docs/usage.md` (opsional).
5. Subset kecil: `src/main.py` dan `tests/cli/test_main.py`.
6. Hubungan: test mengimpor fungsi `parse_args` dari main untuk memeriksa argumen.
7. Saran aman: mulai dengan `src/main.py` karena perubahan kecil dan dapat langsung diverifikasi dengan menjalankan test CLI.
**Output**:
- Akan diedit: `src/main.py` (tambah pilihan `--export-csv`).
- Perlu dicek setelah: `tests/cli/test_main.py`, `docs/usage.md`.
- Hubungan: test memanggil CLI dengan arg baru dan memeriksa kode kembali.
- Saran aman: edit file utama karena perubahan argumen bersifat deklaratif dan tidak mengubah logika inti.

### Contoh 3: Menemukan log sebelum menyesuaikan level logging
**Rencana**: “Iterasi 1: Ubah level logging dari INFO ke DEBUG pada modul pembayaran”.
**Input**:
- Rencana: ubah level logging.
- Nama modul: `payment`.
**Langkah kerja**:
1. Kata kunci: `payment`, `logging`, `level`.
2. Pencarian:
   - File modul pembayaran: `src/payment/processor.py`, `services/payment.js`.
   - File konfigurasi logging: `logging.yaml`, `log_config.json`, atau bagian di `config/app.yaml` terkait logging.
   - File yang menangkap log: `logs/payment.log` (jika ada), atau handler logging di kode.
3. Titik masuk: `src/payment/processor.py` (diinisialisasi logger).
4. Akan diedit: `src/payment/processor.py` (mengubah `logger.setLevel(logging.DEBUG)` atau set konfigurasi).
   - Perlu dicek: file log output (`logs/payment.log`) setelah perubahan, serta test yang memastikan logging tidak mengganggu alur.
5. Subset kecil: `src/payment/processor.py` dan `logs/payment.log` (atau konfigurasi logging jika ada di file terpisah).
6. Hubungan: logger di processor digunakan seluruh modul pembayaran; perubahan level akan memengaruhi semua output log modul tersebut.
7. Saran aman: ubah level di `src/payment/processor.py` karena mudah diobservasi melalui file log atau output konsol, dan dapat dibalik bila terlalu verbose.
**Output**:
- Akan diedit: `src/payment/processor.py` (set level logger ke DEBUG).
- Perlu dicek setelah: `logs/payment.log` (verifikasi bahwa pesan DEBUG muncul) dan `tests/payment/test_logger.py` jika ada.
- Hubungan: logger ini digunakan oleh semua fungsi di processor.py.
- Saran aman: perubahan level logging dapat dilakukan dan diobservasi dengan cepat tanpa merusak fungsionalitas.

## Decision Tree (ASCII Diagram)

```
Mulai
 |
 |-- Dapatkan rencana singkat dari loop-planning?
 |        |
 |        Ya --> Ekstrak kata kunci, nama fungsi/file yang disebutkan
 |        |
 |        Tidak --> Minta klarifikasi minimal (apa yang ingin Anda cari?)
 |
 |-- Lakukan pencarian teks dan struktur direktori berdasarkan kata kunci
 |        |
 |        --> Hasil: file kandidat (kod, konfigurasi, test, log)
 |
 |-- Filter hasil berdasarkan relevansi:
 |        |
 |        --> Cocokkan dengan nama modul/fitur dari rencana
 |        --> Prioritaskan file dengan ekstensi kode (.py, .js, .ts, .java, .go, .rb)
 |        --> Sertakan konfigurasi umum (.env, .yaml, .yml, .json, .toml, config.*, settings.*)
 |        --> Sertakan file test (tests/*, __tests__/*, spec/*, *_test.*, *Spec.*)
 |        --> Jika rencana menyebut log, sertakan file log atau konfigurasi logging
 |
 |-- Identifikasi titik masuk dan dependensi
 |        |
 |        --> Untuk setiap file kandidat, telusuri import/require untuk mencari dependensi
 |        --> Catat file yang dieksekusi pertama (main, index, server) sebagai entry point
 |
 |-- Tentukan file yang akan diedit dalam iterasi ini
 |        |
 |        --> Pilih file yang sesuai langsung dengan tugas (mis. menambah test → edit file test)
 |        --> Jika belum jelas, pilih file dengan kemungkinan najmengganggu (utility, helper, test terisolasi)
 |
 |-- Identifikasi file yang perlu dicek setelah perubahan
 |        |
 |        --> File yang diimpor atau yang bergantung pada file yang akan diedit
 |        --> Konfigurasi yang digunakan oleh file tersebut
 |        --> Log yang relevan (jika perubahan memengaruhi output log)
 |
 |-- Pilih subset kecil untuk iterasi pertama (biasanya 1‑3 file)
 |        |
 |        --> Pastikan subset mencakup file yang akan diedit dan minimal file pemeriksaan |
 |
 |-- Catat hubungan antar file bila penting
 |        |
 |        --> Mis. fungsi A memanggil fungsi B, konfigurasi C digunakan oleh modul D |
 |
 |-- Beri saran area yang paling aman untuk perubahan pertama
 |        |
 |        --> Prioritaskan file yang memiliki test terpisah atau tidak memengaruhi API publik |
 |
 |-- Output daftar file, catatan hubungan, dan saran area aman
 |
 Selesai
```

## FAQ
**Q: Saya tidak tahu nama modul atau fitur yang tepat, hanya ada deskripsi vague seperti “perbaiki sesuatu di bagian frontend”. Apa yang harus saya lakukan?**  
A: Minta klarifikasi minimal: nama file atau folder yang diduga terkait (mis. “Apakah maksud Anda folder `src/components/` atau file `App.js`?”). Jika tidak ada informasi, gunakan struktur repo umum: cari file yang mengandungi kata kunci dari deskripsi (mis. “frontend”, “UI”, “button”) dan batasi pada direktori yang tampak terkait UI (mis. `src/`, `client/`, `web/`).

**Q: Hasil pencarian saya menghasilkan banyak file konfigurasi (puluhan .env, .yaml). Bagaimana memfilter mereka?**  
A: Fokus pada file konfigurasi yang berada di direktori yang sama atau induk dengan file kode target. Jika tidak jelas, pilih satu file konfigurasi yang paling umum digunakan oleh proyek (mis. file `.env` di root, `config/app.yaml`) dan catat bahwa Anda membuat asumsi; nanti jika ternyata tidak relevan, Anda dapat mengulang pencarian dengan konteks yang lebih spesifik setelah iterasi pertama.

**Q: Apakah saya harus menyertakan file dokumentasi (mis. README, docstrings) dalam daftar relevan?**  
A: Biasanya tidak diperlukan untuk perubahan kode kecuali rencana spesifik menyebutkan pembaruan dokumentasi. Jika diperlukan, teruskan sebagai bagian dari file yang perlu dicek setelah perubahan (mis. update docstring atau README) tetapi tetap tetap baca‑saja di skill ini.

**Q: Bagaimana jika saya tidak menemukan test yang terkait dengan fungsi yang akan saya edit?**  
A: Catat bahwa tidak ada test otomatis yang ditemukan. Saran untuk iterasi pertama adalah membuat unit test baru (jika rencana belum mencakupnya) atau melakukan verifikasi manual yang cepat (mis. menjalankan fungsi dengan input contoh dan memeriksa output). Ini juga menjadi titik baik untuk menambahkan langkah membuat test di iterasi berikutnya.

**Q: Saya menemukan bahwa file yang akan saya edit memiliki banyak dependensi (di‑import oleh banyak modul lain). Apakah masih aman untukDiedit dalam satu iterasi kecil?**  
A: Jika perubahan bersifat backward compatible (mis. menambah parameter opsional, memperbaiki bug tanpa mengubah tipe), maka masih dapat dilakukan. Jika perubahan berpotensi mengakibatkan perubahan perilaku yang luas, pertimbangkan untuk:
   - Membuat perubahan yang backward compatible terlebih dahulu.
   - Menambahkan test regresi yang memanggil fungsi dari berbagai pemanggil.
   - Jika tidak yakin, batasi iterasi pertama ke penulisan test yang memanggil fungsi dalam konteks yang terisolasi (mis. via mock) sebelum menyentuh implementasi asli.

**Q: Bagaimana saya bisa memastikan bahwa output dari skill ini dapat langsung digunakan oleh engineering-loop atau skill lain?**  
A: Biasanya output berupa teks yang dapat Anda salin ke file state (mis. `~/hermes/tmp/loop-context-discovery.json`) atau gunakan sebagai konteks dalam pemanggilan skill berikutnya. Jika Anda ingin format terstruktur, beri tahu saya dan saya dapat menambahkan langkah yang menulis ke file JSON dalam output skill ini.

## Referensi & Template
- **Template Output Daftar File** (markdown):
  ```
  ## File yang relevan
  - **Akan diedit**: `tests/auth/test_login.py` (menambah test case password khusus)
  - **Perlu dicek setelah perubahan**: `src/auth.py`, `config/auth.yaml`
  - **Titik masuk / dependensi**: `src/auth.py` (dieksport oleh `routes/auth.js`)
  - **Hubungan antar file**: test mengimpor `login_user` dari `src/auth.py`
  - **Saran area pertama yang aman**: `tests/auth/test_login.py` (isolasi, dapat langsung diverifikasi dengan menjalankan test)
  ```
- **Template Output JSON** (jika ingin format terstruktur untuk state loop):
  ```json
  {
    "to_edit": ["tests/auth/test_login.py"],
    "to_verify": ["src/auth.py", "config/auth.yaml"],
    "entry_point": ["src/auth.py"],
    "dependencies": {
      "tests/auth/test_login.py": ["src/auth.py"]
    },
    "notes": "Test mengimpor fungsi login_user dari src/auth.py",
    "recommended_first": "tests/auth/test_login.py"
  }
  ```
- **Template Ringkasan untuk Pengguna** (teks singkat):
  ```
  File yang akan diedit: <path>
  File yang perlu dicek: <path1>, <path2>
  Hubungan: <deskripsi singkat>
  Saran awal: <path>
  ```

## Integrasi dengan Skill Lain
- `depends_on: []` – skill ini berdiri sendiri untuk menemukan konteks sebelum perubahan.
- `next_on_success: [\"skill_engineering-loop\"]` – biasanya setelah mengetahui konteks, lanjut ke loop eksekusi (engineering-loop) untuk melakukan iterasi perubahan.
- Bisa juga dipakai sebelum memanggil `skill_coding`, `skill_testing`, `skill_debugging`, atau `skill_deploy` sebagai langkah pertama dalam iterasi (mengetahui mana yang harus diedit atau diverifikasi).

## Versi dan Changelog
- **v1.0.0** – Rilis awal dengan struktur lengkap, verification checklist, anti‑pattern & fixes, recipes, decision tree, FAQ, referensi, integrasi, dan contoh penggunaan.
- **v0.1.0** – Versi awal hanya berisi dasar alur kerja, trigger, prerequisites, dan langkah‑langkah umum.

## Lisensi
MIT – Bebas digunakan dan dimodifikasi dengan mencantumkan atribusi.