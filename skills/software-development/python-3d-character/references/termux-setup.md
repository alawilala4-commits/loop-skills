# Termux Setup for 3D Python Games

## Environment Constraints

- **Python 3.13** is the default on Termux
- **Pygame+OpenGL won't work** — no SDL2 dev packages, no GPU access
- **Ursina is pre-installed** in this environment (check with `pip list | grep ursina`)
- **pip install hangs** on large packages like numpy/pygame — use `--no-deps` or install one at a time
- **Git works** — `git init`, `git add`, `git commit` all functional
- **Working directory**: `~/projects/` (not `/sdcard/`)

## Install Strategy

```bash
# If ursina is not installed:
pip install ursina

# If numpy is needed (for sound generation):
pip install --no-deps numpy

# If pygame.mixer is needed (for sound):
# WON'T WORK — no SDL2. Use ursina's built-in audio or skip sound.
```

## Running Games

```bash
cd ~/projects/3d-character
python main_ursina.py      # Works
python main.py             # FAILS (no OpenGL)
python enemy_npc.py        # Works (Ursina)
python sound_effects.py    # PARTIALLY WORKS (pygame.mixer may fail)
```

## User Preference (observed)

- User plays games on **Android phone via Termux**
- Prefers **direct action** over explanation
- Language: **Bahasa Indonesia**
- Likes **incremental feature additions** ("boleh" = OK, keep going)
- Wants to know **where to run** things
- Commits after each feature batch
