# Termux Environment Notes for Python 3D Games

## What's Pre-Installed
- Python 3.13
- `ursina` (3D engine, bundles pyglet + OpenGL emulation)
- `pyglet` (windowing/OpenGL)
- `numpy`

## What Does NOT Work
- `pygame` — needs `sdl-config` / SDL2 dev packages which are not in Termux repos
- `pip install pygame` — fails with `RuntimeError: Unable to run "sdl-config"`
- `pip install moderngl` — may timeout or fail (slow/no PyPI mirror)
- `pip install` in general — frequently times out on Termux

## What Works
- `ursina` — already installed, works out of the box
- `pyglet` — already installed
- Raw WebGL via HTML — bypasses Python entirely
- `python -m http.server` — works for local serving

## Workarounds
1. **Use Ursina instead of Pygame+ModernGL** — Ursina bundles everything
2. **Use offline HTML/WebGL** — no Python needed on target device
3. **Pre-install deps in a clean Termux** before the user session:
   ```bash
   pkg update && pkg install python
   pip install ursina numpy
   ```
4. **For pygame on Termux** (advanced):
   ```bash
   pkg install sdl2 sdl2-dev  # may not exist in default repos
   # This usually doesn't work — use Ursina instead
   ```

## User Preference Signal
User explicitly said: "kalau bisa jangan di termux" (if possible, not Termux).
They wanted browser-based delivery. The offline HTML approach is the answer.
