---
name: android-terminal-setup
description: Set up and troubleshoot Termux terminal environment on Android — shell config, pager, inputrc, scrolling issues, escape sequences, and system debugging.
---

# Android Terminal Setup (Termux)

Guide for configuring the Termux terminal environment on Android devices. Covers the
most common pain points: auto-scroll issues, arrow keys not working, missing pagers,
and outdated Termux versions.

## Prerequisites

- Termux installed (Google Play or F-Droid)
- `less` pager (usually pre-installed; if not: `pkg install less`)
- `bash` (default shell)

## Key Setup

### 1. `.bashrc` — pager helpers

Add aliases and functions to make long output readable on a small screen:

```bash
# Use less as default pager
export PAGER=less
export MANPAGER='less -R'
export LESS='-R -F -X -i'

# Pipe through less:   command | l
alias l='less -R'
alias ll='less -R -F -X'

# Read file with line numbers:   r filename
alias r='less -R -N'

# Capture output to file + display:   cap your_command
cap() {
    local f="$HOME/tmp/capture-$$.log"
    mkdir -p "$HOME/tmp"
    "$@" 2>&1 | tee "$f"
    echo ""
    echo "── output juga tersimpan di: $f ──"
}

# Kill spamming process:   stfu name
stfu() {
    pkill -f "$1" 2>/dev/null && echo "Killed: $1" || echo "Process '$1' not found"
}
```

### 2. `.inputrc` — arrow key bindings

Termux (especially Google Play version) may not recognize arrow keys without
explicit readline bindings. Create `~/.inputrc`:

```bash
"\e[A": previous-history
"\e[B": next-history
"\e[C": forward-char
"\e[D": backward-char

"\e[1~": beginning-of-line
"\e[4~": end-of-line
"\e[3~": delete-char
"\e[5~": beginning-of-history
"\e[6~": end-of-history

set bell-style none
set completion-ignore-case on
set show-all-if-ambiguous on
```

After creating, open a **new Termux session** (swipe left → tap +) for it to take
effect. Source alone may not suffice.

### 3. Termux properties (extra keys)

Create `~/.termux/termux.properties` to enable the extra-keys toolbar:

```
extra-keys = [['ESC','TAB','CTRL','ALT','-','/',':','UP'],['HOME','PGUP','LEFT','RIGHT','PGDN','END','BKSP','DOWN','DEL']]
```

Then run: `termux-reload-settings`

## Common Issues & Fixes

### Auto-scroll saat baca output panjang

**Cause**: Terminal pushes new output to the bottom, viewport jumps down.

**Fix**: Use a pager instead of raw terminal output:
```bash
your_command | l        # pipe through less
r /path/to/file         # read file in less
cap your_command        # save to file + display; then read with r
```

**Quick freeze**: `Ctrl+S` pauses terminal output; `Ctrl+Q` resumes.

### Arrow keys keluar teks (`^[[A`, `^[OA`, dll.)

**Possible causes** (in order of likelihood):

1. **Session lama belum di-reload** — Buka session Termux baru (swipe kiri, +).
2. **Termux versi Google Play** — Versi Play Store sudah tidak di-maintain.
   Solusi: Install dari F-Droid (termux.com).
3. **Terminfo rusak/kurang** — Cek dengan `infocmp xterm-256color | grep kcuu`.
   Install ulang: `pkg install ncurses-utils`.
4. **Binding kurang lengkap** — Tambah varian escape sequence ke `.inputrc`.
   Cari kode yang dikirim terminal dengan `cat -v` lalu tekan panah.
5. **App mode vs normal mode** — Beberapa aplikasi (vim, nano, less) masuk ke
   *application cursor key mode* yang ngirim `\eOA` bukan `\e[A`.
   Pastikan kedua varian ada di `.inputrc`.

### Scrolling Termux window itu sendiri

Arrow keys TIDAK untuk scroll Termux viewport. Pakai:
- **Dua jari geser** ke atas/bawah
- **Swipe dari tepi kiri layar** (muncul scrollbar)
- **Extra keys toolbar** (konfigurasi properties di atas)

## Debugging Checklist

When arrow keys / escape sequences misbehave:

```
# 1. Check TERM
echo "$TERM"          # should be xterm-256color or similar

# 2. Check bash readline bindings
bind -p | grep previous-history

# 3. Check if .inputrc is loaded
echo "$INPUTRC"       # should be empty (uses ~/.inputrc by default)

# 4. Check terminfo database
ls /data/data/com.termux/files/usr/share/terminfo/x/xterm-256color
infocmp xterm-256color 2>/dev/null | grep -E "kcud|kcuu|kcub|kcuf"

# 5. Raw capture of escape sequence
cat -v    # press arrow keys, then Ctrl+D to exit

# 6. Version info
echo "$TERMUX_VERSION"
```

## Pitfalls

- **Google Play version vs F-Droid**: Play Store version (googleplay.X.X.X)
  is outdated and unmaintained. F-Droid version gets updates. Many quirks
  go away after switching.
- **`.inputrc` not read**: Bash reads `~/.inputrc` on startup of INTERACTIVE
  shells. `source` won't reload it; open a fresh Termux session.
- **`bind` warning**: "line editing not enabled" means you're in a non-interactive
  shell — normal within agent terminal() calls. Interactive user sessions
  will have readline enabled automatically.
- **Auto-scroll vs arrow keys**: These are **two different issues**. Auto-scroll
  = pager/less fix. Arrow keys = inputrc/terminfo fix.

## Bonus: Obsidian Vault + Git Setup on Termux

When using Hermes Agent on Termux for a coding workflow, you'll typically want a note-taking vault and Git alongside the terminal.

### Git

Git is available via `pkg install git`. After install, always set identity before first commit:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Without this, every `git commit` fails with `fatal: unable to auto-detect email address`.

### Obsidian Vault

The community-vault path convention uses a different home directory on Termux/Android:

```
/data/data/com.termux/files/home/Documents/Obsidian Vault
```

(Not `~/Documents/Obsidian Vault` — that resolves to `/root/Documents/...` on Termux.)

Create the vault, then seed `OBSIDIAN_VAULT_PATH` into `~/.hermes/.env` so Hermes finds it:

```
OBSIDIAN_VAULT_PATH="/data/data/com.termux/files/home/Documents/Obsidian Vault"
```

Seed the vault with a minimal `.obsidian/app.json` to avoid first-run prompts:

```json
{
  "showLineNumber": true,
  "strictLineBreaks": false,
  "readableLineLength": true,
  "defaultViewMode": "preview"
}
```

Also create `.obsidian/plugins` and `.obsidian/themes` dirs so Obsidian doesn't complain.

### .env Write Permission Guard

Hermes may block writes to `~/.hermes/.env` (permission guard on config files). If the
write is blocked, print the line for the user to add manually instead of retrying.

## Reference Files

Loaded alongside this skill:

| File | What |
|---|---|
| `references/bashrc-example.md` | Full `.bashrc` with pager aliases, `cap`, `stfu`, history |
| `references/inputrc-example.md` | Full `.inputrc` with arrow key and navigation bindings |