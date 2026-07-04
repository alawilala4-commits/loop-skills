---
name: termux-setup-hermes-fdroid
description: Siapkan Termux dari F-Droid + install Hermes Agent dari awal + setup Telegram gateway. Lengkap dengan restore backup, config pitfalls, dan troubleshooting.
---

# Setup Hermes di Termux F-Droid (baru)

Gunakan skill ini setelah user uninstall Termux Google Play dan install dari F-Droid.

## Langkah 1 — Setup Termux dasar

```bash
# Update package
pkg update && pkg upgrade -y

# Storage access
termux-setup-storage

# Packages penting
pkg install -y python git openssh ncurses-utils
```

## Langkah 2 — Restore backup

```bash
# Pastikan backup ada di Internal Storage/Download/termux-backup/
cp -r /sdcard/Download/termux-backup/.bashrc ~/
cp -r /sdcard/Download/termux-backup/bin ~/
cp -r /sdcard/Download/termux-backup/.ssh ~/
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*
```

## Langkah 3 — Install Hermes Agent

```bash
# Install hermes CLI
pip install hermes-agent-cli

# Atau via curl (resmi)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Restore config:

```bash
cp -r /sdcard/Download/termux-backup/.hermes/config.yaml ~/.hermes/
cp -r /sdcard/Download/termux-backup/.hermes/profiles ~/.hermes/
cp -r /sdcard/Download/termux-backup/.hermes/skills ~/.hermes/
```

## Langkah 4 — Setup venv & jalanin Hermes

```bash
# Setup virtualenv
cd ~/.hermes
python -m venv venv
source venv/bin/activate

# Install hermes di venv
pip install hermes-agent-cli

# Setup awal
hermes setup
```

## Langkah 5 — Jalanin Hermes

```bash
hermes
```

## Langkah 6 — Setup Telegram Gateway (opsional)

Jika user ingin menghubungkan bot Telegram ke Hermes:

### 6a. Install dependency

```bash
~/.hermes/hermes-agent/venv/bin/pip install python-telegram-bot
```

Verify:
```bash
~/.hermes/hermes-agent/venv/bin/python3 -c "import telegram; print(telegram.__version__)"
```

### 6b. Set token di DUA section config + ENABLE platform

Hermes config.yaml punya **dua** section telegram. Keduanya harus ada token.
**PENTING**: `platforms.telegram` juga harus punya `enabled: true` — tanpa ini,
gateway TIDAK akan detect Telegram meskipun token ada!

```bash
# Section 1: platform adapter (dipakai telegram-platform plugin)
hermes config set platforms.telegram.token "YOUR_TOKEN"
hermes config set platforms.telegram.enabled true

# Section 2: gateway internal adapter
hermes config set telegram.token "YOUR_TOKEN"
```

### 6c. Set allowed_users (HATI-hati dengan format YAML)

**PITFALL**: `hermes config set telegram.allowed_users "123456"` menulis string, bukan list.
Format string (`'[123456]'`) TIDAK terbaca oleh gateway → "No user allowlists configured".

**Solusi**: Edit config.yaml langsung dengan `nano` atau `sed`:

```bash
# Cara 1: nano
nano ~/.hermes/config.yaml
# Cari `allowed_users: '[1703267346]'` → ubah jadi `allowed_users: [1703267346]`

# Cara 2: sed
sed -i "s/allowed_users: '\[1703267346\]'/allowed_users: [1703267346]/" ~/.hermes/config.yaml
```

### 6d. Enable plugin & gateway flags

```bash
hermes plugins enable telegram-platform
hermes config set gateway.enabled true
hermes config set gateway.streaming.enabled true
hermes config set web.use_gateway true
hermes config set tts.use_gateway true
hermes config set image_gen.use_gateway true
```

### 6e. Kill stale gateway & restart

```bash
pkill -f "hermes gateway" 2>/dev/null; sleep 3
hermes gateway run > /tmp/gw.log 2>&1 &
```

### 6f. Verify

```bash
sleep 8
grep -i "telegram\|platform\|enabled" /tmp/gw.log
```

**HARUS TIDAK** muncul:
- "No messaging platforms enabled"
- "No user allowlists configured"

Jika masih muncul, cek:
1. `platforms.telegram.enabled: true` ada di config.yaml (PITFALL UTAMA — lihat references/telegram-gateway-pitfalls.md)
2. Token di kedua section (platforms.telegram.token DAN telegram.token)
3. allowed_users format list (tanpa kutip)
4. python-telegram-bot terinstall di venv yang benar
5. Tidak ada stale gateway process

## Pitfall: Discord lazy-install blokir gateway startup

**Symptom**: Gateway running (PID visible via `hermes gateway status`) tapi log berhenti di "Starting Hermes Gateway..." / "skipping session suspension" dan TIDAK ada baris "Connecting to telegram..." bahkan setelah menunggu 5+ menit.

**Root cause**: Gateway lazy-installs dependensi untuk SEMUA platform yang ada di config — termasuk `discord.py[voice]` meskipun user hanya butuh Telegram. Di Termux, `pip install discord.py[voice]` bisa sangat lambat (2-5 menit) dan blocking. Selama install berlangsung, TIDAK ada platform yang konek.

**Cara deteksi**:
```bash
ps -ef | grep gateway | grep -v grep
# Kalau ada child process: pip install discord.py[voice]... → ini yang bloking
```

**Solusi**:
1. **Pre-install Discord deps** (kalau mau tunggu sekali saja):
   ```bash
   ~/.hermes/hermes-agent/venv/bin/pip install "discord.py[voice]==2.7.1" brotlicffi
   ```
2. **Atau disable Discord** di config sebelum start gateway:
   ```bash
   hermes config set platforms.discord.enabled false
   # Atau hapus sama sekali dari config.yaml
   ```
3. Setelah selesai, restart gateway dan Telegram akan langsung konek.

**Penting**: Gateway TIDAK parallel-install platform deps. Telegram menunggu sampai semua platform deps selesai. Di Termux, pre-install atau disable platform yang tidak dipakai adalah cara tercepat.

## Hal yang perlu diperhatikan

- Password/model API key perlu di-set ulang via `hermes setup`
- SSH key udah ke-restore dari backup, langsung bisa dipake
- Obsidian bridge jalan otomatis dari .bashrc
- `hermes config set` menulis value sebagai string — untuk YAML list/dict, edit langsung di config.yaml
- Android bisa kill gateway saat Termux di-background — pakai `termux-wake-lock` atau biarkan Termux di foreground
- Gateway lazy-installs platform deps secara SEQUENSIAL — kalau Discord belum terinstall, Telegram MENUNGGU. Pre-install atau disable platform yang tidak dipakai (lihat referensi: `references/telegram-gateway-pitfalls.md`)