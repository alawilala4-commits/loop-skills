---
name: android-termux
description: Termux setup, troubleshooting, and maintenance on Android — installation, terminal scroll issues, package management, backup/restore, and common terminal emulation bugs.
---

# Android Termux

Setup, maintenance, and troubleshooting guide for Termux on Android devices.

## Installation

**CRITICAL: Use F-Droid, NOT Google Play.**
- Google Play version (terminated ~2022) is outdated and has terminal emulation bugs (arrow keys, less, vim, etc. don't work properly).
- F-Droid version is actively maintained: [f-droid.org/packages/com.termux](https://f-droid.org/packages/com.termux/)
- After install, run: `termux-setup-storage` to access shared storage.

## Common Terminal Scroll Issue

**Symptom:** When scrolling up in Termux, the viewport auto-scrolls back down. Or arrow keys / less / vim show literal text (`^[[A`, etc.) instead of navigating.

**Root cause (Google Play version):** Old terminal emulator in the Play Store build has broken terminfo handling and does not properly process cursor-key escape sequences inside interactive programs (`less`, `vim`, `nano`).

**Fix:** Uninstall Termux from Google Play, install from F-Droid.

**Workarounds (if stuck on Play version):**
- `your_command | cat > ~/output.txt` — save output to file, read with `head`/`tail`/`cat`
- `your_command | more` — `more` is simpler than `less` and may work
- Inside `less`: use `j`/`k` (not arrow keys) for scroll up/down

### LESS pitfalls

- `export LESS='-R -F -X -i'` — the `-F` flag causes `less` to **exit immediately** if the content fits on one screen. Remove `-F` if you want less to always take over the terminal.
- Safe defaults: `export LESS='-R -X -i'`

## Scripts and Configuration

### Common files to backup before reinstalling Termux

| Path | Purpose |
|---|---|
| `~/.bashrc` | Shell config |
| `~/.ssh/` | SSH keys |
| `~/bin/` | Custom scripts |
| `~/.hermes/config.yaml` | Hermes agent config |
| `~/.hermes/profiles/` | Hermes profiles |
| `~/.hermes/skills/` | Hermes skills |

Do NOT backup `~/.hermes/venv/` (large, can be reinstalled with `hermes setup`)

### Post-install setup

```bash
pkg update && pkg upgrade -y
pkg install python git openssh ncurses-utils
pip install hermes-agent  # if using Hermes
```

## Package Management

- `pkg search <name>` — search packages
- `pkg install <name>` — install
- `pkg list-installed` — list installed
- `pkg upgrade` — upgrade all

## User Preferences (this user)

- Prefers communication in **Bahasa Indonesia**.