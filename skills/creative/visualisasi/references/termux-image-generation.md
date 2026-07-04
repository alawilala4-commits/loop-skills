# Termux Image Generation Constraints & Solutions

## Problem: Generate images on Termux (Android, no GPU, no display)

### Available Tools

| Tool | Status | Quality | Use Case |
|------|--------|---------|----------|
| Pillow (PIL) | ✅ pip install Pillow | ⭐ Low | Simple shapes only — jelek untuk karakter/figur |
| cairosvg | ✅ pip install cairosvg | ⭐⭐⭐ High | SVG → PNG, best untuk karakter/illustration |
| p5.js HTML | ✅ write HTML file | N/A | Interactive web view, TIDAK bisa kirim ke Telegram |
| Node canvas | ❌ npm install fails (needs native compile) | - | Tidak usable di Termux |
| Chromium/Playwright | ❌ Not available | - | Tidak ada headless browser di Termux |
| ImageMagick | ❌ pkg install fails | - | Tidak tersedia |

### The Winning Pipeline: Python SVG → cairosvg → PNG

```python
import cairosvg
svg_content = '<svg>...</svg>'  # Your SVG string
png_path = 'output.png'
cairosvg.svg2png(bytestring=svg_content.encode(), write_to=png_path, output_width=512, output_height=512)
```

### Why Pillow Fails for Characters

Pillow only supports:
- Basic shapes (ellipse, rectangle, line, polygon)
- No radial gradients (must fake with manual pixel loops)
- No filters (drop shadow, blur require manual implementation)
- Poor anti-aliasing on diagonal curves
- Result: characters look flat, creepy, or amateur

### Why SVG + cairosvg Wins

SVG supports:
- Linear & radial gradients
- Filters (drop shadow, blur)
- Transforms (rotate, scale)
- Filter effects (feGaussianBlur, feDropShadow)
- Unicode characters (sparkles ✦, stars ★)
- CairoSVG renders at high quality with proper anti-aliasing

### Sending to Telegram

```python
# Wrong — HTML/JSON not supported as image
# send_file('output.html')  # Telegram shows as document, not image

# Right — PNG always works
# MEDIA:/path/to/output.png  # Sends as photo
```

Telegram supports: JPG, PNG, GIF (no HTML, no SVG directly)

### RNG Pattern for Procedural Generation

```python
# WRONG — generator object is not callable
def rng(s):
    while True:
        s = (s * 16807) % 2147483647
        yield s / 2147483647
r = rng(seed)
r()  # TypeError: 'generator' object is not callable

# CORRECT — callable class
class RNG:
    def __init__(self, s):
        self.s = s
    def __call__(self):
        self.s = (self.s * 16807) % 2147483647
        return self.s / 2147483647
r = RNG(seed)
r()  # Returns float 0..1
```

### Pitfall: Ellipse x0 <= x1

```python
# WRONG — produces x0 > x1 for negative side
draw.ellipse([x - 5, y, x - 18, y + 8])  # x-5 > x-18 when side=-1

# CORRECT — use min/max or abs
draw.ellipse([min(x-5, x-18), y, max(x-5, x-18), y+8])
```

### File Size Reference

- Simple character (512x512): ~30-60 KB
- Medium complexity: ~60-120 KB  
- Heavy gradients/filters: ~100-200 KB
- Telegram max: 10 MB (plenty of headroom)

### Installation

```bash
pip3 install cairosvg
# Dependencies auto-installed: cairocffi, cssselect2, tinycss2, defusedxml
```
