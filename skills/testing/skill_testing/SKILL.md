---
name: skill_testing
description: Menjalankan tes otomatis untuk kode yang baru diubah.
version: 1.0.0
author: OWL Agent
tags: [testing, ci, automation]
triggers:
  - "uji kode"
  - "jalankan unit test"
  - "cek apakah kode sudah aman untuk deploy"
prerequisites:
  - Perubahan kode sudah dibuat oleh Skill_Coding
  - Lingkungan eksekusi (local/VPS) tersedia
---

# Skill Testing

Menjalankan tes otomatis untuk kode yang baru diubah.

## Tujuan
Memastikan perubahan kode tidak mengintroduksi regresi dan memenuhi standar kualitas sebelum melanjutkan ke tahap review atau deploy.

## Trigger / Pemicu
- Pengguna berkata: "uji kode", "jalankan unit test", "cek apakah kode sudah aman untuk deploy"
- Setelah fase coding selesai (Skill_Coding selesai)
- Pengguna mengetik: "test", "run test", "cek error"

## Prasyarat
1. Perubahan kode sudah dibuat oleh Skill_Coding (file-file baru atau sudah diedit tersedia di repo).
2. Lingkungan eksekusi (local machine, VPS, atau container) tersedia dan dapat menjalankan perintah test yang sesuai dengan bahasa/proyek.
3. Dependencies terinstall (misalnya `npm install`, `pip install -r requirements.txt` sudah dilakukan).

## Output Format
Berikut format laporan tes yang akan dihasilkan:

```
## Test Results: [Nama Modul/Fitur]

### Summary
- Total: X tests
- Passed: Y
- Failed: Z
- Skipped: W

### Failures
| Test | Error | File |
|------|-------|------|
| test_X | AssertionError: expected 5 but got 6 | file.py:42 |
| test_Y | TypeError: unsupported operand type(s) for +: 'int' and 'str' | utils.js:13 |

### Coverage
- Overall: X%
- Missed lines: [12, 34, 56]

### Recommendations
- [Perbaiki fungsi X agar menangani kasus edge]
- [Tambahkan tes untuk kondisi Y]
```

## Langkah-langkah
1. **Identifikasi project dan bahasa**  
   - Deteksi apakah proyek berbasis Python (`requirements.txt`, `setup.py`, `pyproject.toml`), JavaScript/Node (`package.json`), Bash, atau lain-lain.
2. **Temukan atau buat perintah test**  
   - Cari script test dalam `package.json` (`"test"`), file `Makefile`, atau instruksi dalam `README.md`.  
   - Jika tidak ada, buat perintah default sesuai bahasa (lihat bagian Test Commands).
3. **Jalankan tes**  
   - Jalankan perintah dan tangkap output (stdout + stderr).  
   - Simpan hasil ke file sementara untuk analisis.
4. **Analisis hasil**  
   - Hitung total, passed, failed, skipped.  
   - Ekstrak pesan error dan file yang gagal.  
   - Jika ada coverage tool (mis. `coverage`, `jest --coverage`), ambil laporan coverage.
5. **Jika ada kegagalan**  
   - Ringkas error utama (maksimal 3 failure teratas).  
   - Rekomendasikan pemanggilan `skill_debugging` untuk analisis lebih dalam.
6. **Jika semua lulus**  
   - Beri sinyal ke orchestrator untuk melanjutkan ke `skill_review`.
7. **Bersihkan artefak sementara** (opsional) – hapus file log atau coverage yang tidak diperlukan.

## Test Commands per Bahasa
```bash
# Python (unittest)
python -m unittest discover -s tests -v

# Python (pytest)
pytest -v --tb=short

# JavaScript / Node (npm)
npm test

# JavaScript / Node (yarn)
yarn test

# Bash syntax check
bash -n script.sh

# Linting Python
python -m pylint src/
python -m flake8 src#

# Linting JavaScript/JSX
npx eslint src/
npx eslint --fix src#

# Coverage (opsional)
# Python
coverage run -m pytest && coverage report
# JavaScript
jest --coverage
```

## Constraints dan Asumsi
- `requires_execution_environment: true` – butuh runtime untuk menjalankan test.
- Target: semua critical path (fungsi publik, API endpoint, alur utama) harus mendapat coverage minimal 80% untuk kode baru.
- Tidak menjalankan test yang bersifat integrasi atau end-to-end kecuali sudah dijalankan oleh CI terpisah (skill ini fokus pada unit test).
- Timeout default: 120 detik per jalankan test (bisa diubah via konfigurasi jika diperlukan).

## Integrasi dengan Skill Lain
- `depends_on: ["skill_coding"]` – kode harus sudah ada dari tahap coding.
- `next_on_success: ["skill_review"]` – jika semua test lolos, lanjut ke tahap review.
- `next_on_failure: ["skill_debugging"]` – jika ada failure, alihkan ke debugging untuk inspeksi lebih lanjut.

## Checklist Verifikasi
Sebelum mengakhiri skill ini, pastikan:
- [ ] Perintah test berhasil dijalankan tanpa error timeout.
- [ ] Output test telah ditangkap dan diformat sesuai template di atas.
- [ ] Jika ada failure, daftar error dan file telah disajikan secara jelas.
- [ ] Jika coverage dijalankan, persentase coverage termasuk dalam laporan.
- [ ] Rekomendasi tindak lanjut (debugging/review) telah diberikan sesuai hasil.
- [ ] Tidak ada file sementara yang tersisa di working directory (opsional).

## Anti-Pattern dan Perbaikan
| Anti-Pattern | Dampak | Perbaikan |
|--------------|--------|-----------|
| Hanya menjalankan *happy path* test | Bug di edge case tidak terdeteksi | Tambahkan tes untuk input tidak valid, kondisi batas, dan exception. |
| Mengabaikan output stderr | Kesalahan penting terlewat | Selalu tampilkan dan analisis stderr bersama stdout. |
| Menggunakan test yang flaky (intermittent fail) | Mengurangi kepercayaan hasil tes | Identifikasi source of flakiness (race condition, external service) dan fix atau mock. |
| Menguji implementasi bukan perilaku | Tes mudah rusak saat refactor | Fokus pada apa yang dilakukan fungsi, bukan bagaimana ia dilakukan intern. |
| Tidak membersihkan artefak test (mis. file sementara, database test) | Lingkungan terpolusi, tes berikutnya gagal | Gunakan fixture atau teardown untuk membersihkan setelah setiap test. |
| Menjalankan test suite lengkap untuk perubahan kecil | Memboroskan waktu | Jalankan hanya test terkait file yang diubah (gunakan pytest -k atau jest --testNamePattern) bila memungkinkan. |

## Recipe / Contoh Penggunaan
**Scenario**: Pengguna baru saja menyelesaikan fitur penambahan fitur "tambah item ke keranjang" dalam aplikasi Python Flask.

1. **Trigger**: Pengguna mengetik `"uji kode"`.
2. **Deteksi**: Skill mendeteksi proyek Python karena ada `requirements.txt` dan folder `tests/`.
3. **Perintah Test**: `pytest -v --tb=short`.
4. **Eksekusi**: Output menunjukkan 12 test lulus, 2 gagal karena validasi input tidak memenuhi ketentuan.
5. **Analisis**:  
   - Total: 14  
   - Passed: 12  
   - Failed: 2  
   - Skipped: 0  
   - Failures:  
     | Test | Error | File |
     |------|-------|------|
     | test_add_item_negative_quantity | AssertionError: Expected status 400 but got 200 | tests/test_cart.py:57 |
     | test_add_item_non_numeric | TypeError: unsupported operand type(s) for +: 'int' and 'str' | tests/test_cart.py:73 |
6. **Rekomendasi**: Panggil `skill_debugging` untuk meneliti fungsi `add_item` di `cart.py`.
7. **Hasil**: Skill mengembalikan laporan di atas dan menunggu tindak lanjut.

**Scenario 2**: Semua test lulus (misalnya 20 passed, 0 failed).  
- Skill mengeluarkan ringkasan dengan 0 failures dan memberikan sinjal ke orchestrator untuk melanjutkan ke `skill_review`.

## Decision Tree (ASCII Diagram)
```
Mulai
 |
 |-- Deteksi bahasa/proyek?
 |        |
 |        Ya --> Tentukan perintah test (npm test / pytest / bash -n)
 |        |
 |        Tidak --> Gunakan perintah default sesuai ekstensi file
 |
 |-- Jalankan perintah test
 |
 |-- Apakah ada output error / non-zero exit?
 |        |
 |        Ya --> Kumpulkan failures, buat tabel, beri rekomendasi debug
 |        |
 |        Tidak --> Hitung coverage (jika dijalankan), buat ringkasan sukses
 |
 |-- Apakah ada coverage target < 80% (jika diukur)?
 |        |
 |        Ya --> Tambahkan nota coverage dalam rekomendasi
 |        |
 |        Tidak --> Lanjut
 |
 |-- Output laporan sesuai format di atas
 |
 |-- Apakah ada failure?
 |        |
 |        Ya --> Trigger skill_debugging
 |        |
 |        Tidak --> Trigger skill_review
 |
 Selesai
```

## FAQ
**Q: Apa yang harus dilakukan jika proyek tidak memiliki script test?**  
A: Buat perintah test dasar sesuai bahasa (mis. `python -m unittest discover` untuk Python atau `bash -n *.sh` untuk Bash). Jika tidak ada kode uji sama sekali, beri tahu pengguna untuk menuliskan tes terlebih dahulu melalui `skill_coding`.

**Q: Bisakah saya menyertakan coverage report ke output?**  
A: Ya. Jalankan alat coverage (mis. `coverage run -m pytest && coverage report` atau `jest --coverage`) dan sisipkan sekusi "Coverage" dalam laporan.

**Q: Apakah skill ini bisa dijalankan di CI/CD (GitHub Actions, GitLab CI)?**  
A: Skill ini dirancang untuk dijalankan dalam sesi Hermes, tetapi nilai yang sama dapat dijalin ke CI dengan menyalin perintah test yang sama.

**Q: Bagaimana jika tes memakan waktu lama (> 2 menit)?**  
A: Pertimbangkan untuk menjalankan hanya test yang terkait file yang berubah (mis. `pytest -k "nama_file"`). Atau atur timeout yang lebih besar dalam konfigurasi skill.

## Referensi dan Template
- **Template Laporan**: Lihat bagian *Output Format* di atas.
- **Contoh perintah test**: Lihat bagian *Test Commands*.
- **Panduan kirjoitus unit test baik**: lihat skill `test-driven-development` untuk prinsip RED-GREEN-REFACTOR.
- **Panduan coverage**: lihat dokumentasi alat coverage resmi (Coverage.py, Istanbul/Jest).

## Catatan Penggunaan
- Skill ini bersifat *read-only* untuk source code; tidak akan mengubah file kecuali secara tidak sengaja melalui perintah test yang menulis file (mis. coverage menghasilkan file `.coverage`). Pastikan `.gitignore` mencakup artefak tersebut bila tidak ingin dimasukkan ke repo.
- Jika proyek menggunakan virtual environment atau lingkungan terisolasi, pastikan aktifkan sebelum menjalankan test (mis. `source venv/bin/activate` atau `pipenv shell`). Anda dapat menambahkan langkah aktivasi ke bagian "Langkah-langkah" bila diperlukan.

## Versi dan Changelog
- **v1.0.0** – Rilis awal dengan struktur lengkap, checklist, anti-pattern, decision tree, dan contoh penggunaan.
- **v0.1.0** – Versi awal hanya berisi trigger, prerequisites, steps dasar, dan perintah test.

## Lisensi
MIT – Bebas digunakan dan dimodifikasi dengan mencantumkan atribusi.