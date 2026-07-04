1|---
2|name: visualisasi
3|description: "Semua kebutuhan visualisasi: Wolfram Alpha query, architecture diagram, flowchart, concept map, data viz, infographic, sketch, generative art. Satu skill untuk semua."
4|version: 1.0.0
5|author: OWL Agent
6|license: MIT
7|dependencies: []
8|platforms: [linux, macos, windows]
9|metadata:
10|  hermes:
11|    tags: [visualization, diagram, chart, graph, architecture, flowchart, infographic, wolfram, data-viz, sketch, generative-art]
12|    related_skills: [architecture-diagram, excalidraw, baoyu-infographic, p5js, manim-video, sketch]
13|---
14|
15|# Visualisasi — Semua Visualisasi dalam Satu Skill
16|
17|Satu skill untuk semua kebutuhan visualisasi. Pilih mode sesuai kebutuhan:
18|
19|**User preference (Indonesia):** User komunikasi Bahasa Indonesia, suka langsung action (explain minimal).
20|
21|| Mode | Input | Output | Use Case |
22||------|-------|--------|----------|
23|| **wolfram** | Pertanyaan matematika/sains/data | Grafik/interaktif HTML dari Wolfram Alpha | Hitung, analisis data, plot fungsi |
24|| **architecture** | Deskripsi sistem/infra | Dark-themed SVG architecture diagram | Sistem, cloud, microservices |
25|| **flowchart** | Deskripsi proses/alur | Excalidraw .excalidraw file | Alur kerja, sequence, proses |
26|| **concept-map** | Konsep + relasi | SVG/HTML mind map | Peta konsep, hubungan ide |
27|| **data-viz** | Dataset (angka/CSV) | Interaktif HTML chart | Grafik batang, garis, pie, scatter |
28|| **infographic** | Konten/teks | HTML/PNG infographic | Ringkasan visual, presentasi |
29|| **sketch** | Deskripsi UI/screen | 2-3 HTML mockup variants | Eksplorasi UI, wireframe |
30|| **generative** | Konsep visual | p5.js HTML sketch | Seni generatif, animasi |
31|| **character** | Deskripsi karakter | SVG → PNG via cairosvg | Karakter game, mascot, portrait |
32|
33|---
34|
35|## Quick Test (Setelah membuat visualisasi)
36|
37|Setelah generate file HTML, cara test:
38|
39|```bash
40|# Linux/Termux
41|xdg-open ~/projects/visualisasi-test/contoh.html
42|
43|# macOS
44|open ~/projects/visualisasi-test/contoh.html
45|```
46|
47|Kalau terminal command blocked by approval (User denied), fallback:
48|- File tetap valid, user buka manual dari file manager
49|- Atau gunakan `skill_view` untuk review skill dan generate ulang
50|
51|**Note:** Kalau user minta "testing langsung" atau "cek langsung", JANGAN explain panjang — langsung buat file + informasikan path-nya.
52|
53|---
54|
55|## Mode 1: Wolfram Alpha Query
56|
57|**Gunakan saat:** User minta perhitungan, plot fungsi, data analysis, konversi, atau pertanyaan sains/matematika.
58|
59|### Workflow
60|1. Terima pertanyaan (bahasa apapun, translate ke English untuk query)
61|2. Fetch via web atau generate Wolfram Alpha URL
62|3. Hasilkan HTML interaktif dengan embedded Wolfram Alpha result
63|
64|### URL Format
65|```
66|https://www.wolframalpha.com/input?i={encoded_query}
67|```
68|
69|### Contoh Query
70|- `integrate x^2 sin(x) dx`
71|- `plot sin(x) from 0 to 2pi`
72|- `GDP of Indonesia 2024`
73|- `distance from Jakarta to Surabaya`
74|- `weather in Bandung`
75|- `population of Southeast Asia`
76|- `derivative of e^x * cos(x)`
77|
78|### Iframe Embedding Pattern
79|Gunakan iframe untuk menampilkan Wolfram Alpha result langsung (tidak perlu screenshot):
80|```html
81|<iframe src="https://www.wolframalpha.com/input?i={encoded_query}"
82|        frameborder="0" width="100%" height="600px"></iframe>
83|```
84|Output: standalone HTML yang bisa dibuka di browser atau dikirim via Telegram (view-only, interactive di link).
85|
86|### Output
87|Generate standalone HTML file yang:
88|- Menampilkan Wolfram Alpha result via iframe atau screenshot
89|- Menampilkan query asli dan hasil terjemahan
90|- Styling dark-themed konsisten dengan architecture diagram
91|- Include link ke Wolfram Alpha untuk interaksi lebih
92|
93|### Template
94|```html
95|<!DOCTYPE html>
96|<html lang="en">
97|<head>
98|  <meta charset="UTF-8">
99|  <meta name="viewport" content="width=device-width, initial-scale=1.0">
100|  <title>Wolfram Alpha: {query}</title>
101|  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
102|  <style>
103|    * { margin: 0; padding: 0; box-sizing: border-box; }
104|    body { font-family: 'JetBrains Mono', monospace; background: #020617; color: white; min-height: 100vh; padding: 2rem; }
105|    .container { max-width: 1000px; margin: 0 auto; }
106|    .header { margin-bottom: 2rem; }
107|    h1 { font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem; }
108|    .query { color: #22d3ee; font-size: 0.9rem; word-break: break-all; }
109|    .result-box { background: rgba(15, 23, 42, 0.5); border: 1px solid #1e293b; border-radius: 1rem; padding: 1.5rem; margin-top: 1rem; }
110|    .link { color: #22d3ee; font-size: 0.8rem; margin-top: 1rem; display: inline-block; }
111|    iframe { width: 100%; height: 600px; border: none; border-radius: 0.5rem; }
112|  </style>
113|</head>
114|<body>
115|  <div class="container">
116|    <div class="header">
117|      <h1>Wolfram Alpha Result</h1>
118|      <p class="query">{query}</p>
119|    </div>
120|    <div class="result-box">
121|      <iframe src="https://www.wolframalpha.com/input?i={encoded_query}" frameborder="0"></iframe>
122|    </div>
123|    <a class="link" href="https://www.wolframalpha.com/input?i={encoded_query}" target="_blank">Open in Wolfram Alpha →</a>
124|  </div>
125|</body>
126|</html>
127|```
128|
129|---
130|
131|## Mode 2: Architecture Diagram
132|
133|**Gunakan saat:** User minta diagram arsitektur sistem, cloud infrastructure, microservices, database map.
134|
135|Lihat skill `architecture-diagram` untuk full reference (template, color palette, component types).
136|
137|### Quick Workflow
138|1. Identifikasi komponen (frontend, backend, database, cloud, security, message bus)
139|2. Tentukan koneksi antar komponen
140|3. Generate HTML dengan SVG inline
141|4. Save sebagai `.html` file
142|
143|### Color Palette (WAJIB)
144|| Component | Fill | Stroke |
145||-----------|------|------|
146|| Frontend | `rgba(8, 51, 68, 0.4)` | `#22d3ee` |
147|| Backend | `rgba(6, 78, 59, 0.4)` | `#34d399` |
148|| Database | `rgba(76, 29, 149, 0.4)` | `#a78bfa` |
149|| Cloud/AWS | `rgba(120, 53, 15, 0.3)` | `#fbbf24` |
150|| Security | `rgba(136, 19, 55, 0.4)` | `#fb7185` |
151|| Message Bus | `rgba(251, 146, 60, 0.3)` | `#fb923c` |
152|| External | `rgba(30, 41, 59, 0.5)` | `#94a3b8` |
153|
154|---
155|
156|## Mode 3: Flowchart
157|
158|**Gunakan saat:** User minta flowchart, sequence diagram, process flow, decision tree.
159|
160|Lihat skill `excalidraw` untuk format element JSON.
161|
162|### Quick Workflow
163|1. Identifikasi steps, decisions, dan flow
164|2. Generate Excalidraw JSON elements
165|3. Save sebagai `.excalidraw` file
166|4. User buka di excalidraw.com
167|
168|### Alternative: HTML Flowchart
169|Untuk simplicity, generate HTML+SVG flowchart langsung:
170|```html
171|<!-- Gunakan SVG rectangles + arrows + text -->
172|<!-- Styling sama dengan architecture diagram (dark theme) -->
173|```
174|
175|---
176|
177|## Mode 4: Concept Map / Mind Map
178|
179|**Gunakan saat:** User minta peta konsep, mind map, hubungan antar ide.
180|
181|### Output
182|SVG-based mind map dengan:
183|- Central node (konsep utama) — larger, bold
184|- Branch nodes (sub-konsep) — connected with lines
185|- Color-coded by depth/category
186|- Dark theme, JetBrains Mono font
187|
188|### Layout Algorithm
189|1. Center = main concept
190|2. Level 1 = circular distribution (radius 200px)
191|3. Level 2 = further out (radius 350px)
192|4. Lines: curved bezier between nodes
193|5. Colors: rotate hue per branch
194|
195|---
196|
197|## Mode 5: Data Visualization
198|
199|**Gunakan saat:** User minta grafik dari data (bar chart, line chart, pie chart, scatter plot).
200|
201|### Output
202|Standalone HTML file dengan:
203|- Chart rendering via inline SVG atau lightweight JS (Chart.js CDN)
204|- Dark theme konsisten
205|- Interactive tooltips
206|- Legend
207|
208|### Supported Chart Types
209|- **Bar chart** — perbandingan kategori
210|- **Line chart** — tren waktu
211|- **Pie/Donut** — proporsi
212|- **Scatter plot** — korelasi
213|- **Area chart** — kumulatif
214|- **Radar/Spider** — multi-variabel
215|
216|### Template Structure
217|```html
218|<!DOCTYPE html>
219|<html lang="en">
220|<head>
221|  <meta charset="UTF-8">
222|  <title>Data Visualization</title>
223|  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
224|  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
225|  <style>
226|    body { font-family: 'JetBrains Mono', monospace; background: #020617; color: white; padding: 2rem; }
227|    .chart-container { background: rgba(15, 23, 42, 0.5); border: 1px solid #1e293b; border-radius: 1rem; padding: 1.5rem; max-width: 900px; margin: 0 auto; }
228|  </style>
229|</head>
230|<body>
231|  <div class="chart-container">
232|    <canvas id="chart"></canvas>
233|  </div>
234|  <script>
235|    // Chart.js config with dark theme
236|  </script>
237|</body>
238|</html>
239|```
240|
241|---
242|
243|## Mode 6: Infographic
244|
245|**Gunakan saat:** User minta ringkasan visual, info besar, educational graphic.
246|
247|Lihat skill `baoyu-infographic` untuk 21 layouts × 21 styles.
248|
249|### Quick Workflow
250|1. Analisis konten (data, pesan, audience)
251|2. Pilih layout yang cocok
252|3. Generate HTML infographic
253|4. Export ke PNG jika perlu
254|
255|---
256|
257|## Mode 7: UI Sketch / Mockup
258|
259|**Gunakan saat:** User minta wireframe, UI mockup, screen design exploration.
260|
261|Lihat skill `sketch` untuk workflow lengkap (2-3 variants, comparison).
262|
263|### Quick Workflow
264|1. Tentukan feel/references/core action
265|2. Generate 2-3 HTML variants
266|3. Save ke `sketches/{topic}-{stance}/index.html`
267|
268|---
269|
270|## Mode 8: Generative Art
271|
272|**Gunakan saat:** User minta seni generatif, visualisasi animasi, creative coding.
273|
274|Lihat skill `p5js` untuk full pipeline.
275|
276|### Quick Workflow
277|1. Tentukan mood, color world, motion vocabulary
278|2. Pilih: animated atau static
279|3. Generate single HTML file dengan p5.js
280|4. Export ke PNG/GIF/MP4 sesuai kebutuhan
281|
282|---
283|
284|## Mode 9: Character / Illustration (SVG + CairoSVG)
285|
286|**Gunakan saat:** User minta generate gambar karakter, mascot, portrait, atau figur spesifik.
287|
288|**KENAPA SVG, bukan Pillow?** Pillow hasilnya jelek + serem untuk karakter (cuma bentuk dasar: lingkaran, elips). SVG via `cairosvg` menghasilkan gambar berkualitas tinggi di Termux — gradients, gradients, filter, transform semua didukung.
289|
290|### Pipeline
291|
292|```
293|Python SVG string → cairosvg.svg2png() → PNG file → kirim via MEDIA:
294|```
295|
296|### Dependencies
297|
298|```bash
299|pip3 install cairosvg
300|# (otomatis install cairocffi, cssselect2, tinycss2, defusedxml)
301|```
302|
303|### RNG Pattern (WAJAI BUG INI!)
304|
305|```python
306|# SALAH — generator object bukan callable
307|def rng(s):
308|    while True:
309|        s = (s * 16807) % 2147483647
310|        yield s / 2147483647
311|r = rng(seed)
312|r()  # TypeError: 'generator' object is not callable
313|
314|# BENAR — callable class
315|class RNG:
316|    def __init__(self, s):
317|        self.s = s
318|    def __call__(self):
319|        self.s = (self * 16807) % 2147483647
320|        return self.s / 2147483647
321|r = RNG(seed)
322|r()  # OK!
323|```
324|
325|### SVG Structure untuk Karakter
326|
327|Gunakan pattern ini untuk karakter yang bagus:
328|
329|1. **`<defs>` section** — gradients, filters (shadow, blur), define once
330|2. **Background** — rect with gradient (sky/ground split)
331|3. **Environment elements** — clouds, trees, flowers, grass (back to front)
332|4. **Character** — shadow ellipse → feet → body → arms → head → face details → accessories
333|5. **Decorations** — sparkles, butterfly, particles
334|6. **Render** — `cairosvg.svg2png(bytestring=svg.encode(), write_to=path, output_width=512, output_height=512)`
335|
336|### Wajib di SVG Character
337|
338|- **Radial gradient untuk kulit/head** — biar ada volume
339|- **Filter drop shadow** — biar karakter nggak "mengambang"
340|- **Cheek blush** (radial pink dengan opacity fade) — biar cute
341|- **Eye highlights** (putih kecil) — biar mata "hidup"
342|- **Sparkle Unicode characters** (`✦`, `*`) — dekorasi universal yang render rapi
343|- **Wing/ellipse pakai min/max** — hindari `x1 > x0` error saat direction negatif
344|
345|### Pitfall Khusus Character
346|
347|1. **Jangan buat karakter horror tanpa sengaja** — dark palette + mata tajam + tanpa pipi = creepy. Pakai palette bright/warm + blush + mata bulat = cute
348|2. **Ellipse coordinates HARUS x0 <= x1** — saat pakai left-side + negative width, selalu `min()` / `max()` atau `abs()`
349|3. **cairosvg butuh Ruang disk** — pastikan ada space untuk PNG output (~40-80KB per gambar)
350|4. **Telegram PNG max 10MB** — karakter SVG→PNG biasanya ~50-200KB, aman
351|5. **Font availability di Cairo** — beberapa font nggak ada di Termux. Pakai `font-family="sans-serif"` atau generic
352|
353|### Template Lengkap
354|
355|Lihat `templates/character-template.svg` untuk template copy-paste yang sudah teruji menghasilkan karakter cute nature. 
356|
357|---
358|
359|## Decision Tree
360|
361|Ketika user minta visualisasi, tanyakan:
362|
363|1. **"Apa yang mau divisualisasikan?"**
364|   - Data/angka → Mode 5 (Data Viz)
365|   - Sistem/arsitektur → Mode 2 (Architecture)
366|   - Proses/alur → Mode 3 (Flowchart)
367|   - Konsep/hubungan → Mode 4 (Concept Map)
368|   - Perhitungan/sains → Mode 1 (Wolfram)
369|   - Ringkasan info → Mode 6 (Infographic)
370|   - UI/screen → Mode 7 (Sketch)
371|   - Seni/animasi → Mode 8 (Generative)
372|
373|2. **"Outputnya apa?"**
374|   - HTML file (interactive, buka di browser)
375|   - PNG image
376|   - Excalidraw file (untuk edit lebih)
377|   - MP4 video (untuk animasi)
378|
379|3. **"Berapa banyak variasi?"**
380|   - 1 final → langsung generate
381|   - 2-3 variants → sketch mode
382|
383|---
384|
385|## Pitfalls
386|
387|1. **Jangan campur warna tanpa sistem** — selalu pakai palette yang didefinisikan
388|2. **Jangan lupa font** — JetBrains Mono untuk tech, sesekali Inter untuk UI
389|3. **Jangan over-generate SVG** — kompleksitas tinggi = render lambat
390|4. **Selalu save sebagai file** — jangan output inline, user harus bisa buka
391|5. **Jangan lupa link/reference** — untuk Wolfram, Excalidraw, selalu kasih link
392|6. **Data integrity** — jangan ubah angka/data asli, tampilkan apa adanya
393|7. **Mobile responsive** — diagram harus readable di layar kecil
394|8. **Accessibility** — selalu ada text label, jangan hanya warna
395|9. **PILLOW TIDAK COCOK UNTUK GAMBAR KARAKTER** — hasilnya jelek/serem. Gunakan SVG + `cairosvg` untuk karakter/figur (lihat Mode 9)
396|10. **RNG harus callable, bukan generator** — `def rng(s): yield...` produces generator object that errors when called as `r()`. Pakai class pattern: `class RNG: def __call__(self): self.s = (self.s*16807)%2147483647; return self.s/2147483647`
397|11. **Termux punya batasan tool** — nggak ada Chromium/Playwright untuk render HTML→PNG. `cairosvg` (pip install cairosvg) adalah jalur terbaik SVG→PNG di Termux.
398|12. **Telegram cuma terima file gambar** — HTML/JSON/excalidraw TIDAK bisa dikirim langsung ke Telegram. Harus dikonversi ke PNG/JPG dulu.
399|
400|---
401|
402|## References & Templates
403|
404|| File | Purpose |
405||------|---------|
406|| `references/wolfram-alpha.md` | Wolfram Alpha query patterns, embedding options, common queries |
407|| `references/termux-image-generation.md` | Termux constraints, SVG→cairosvg pipeline, RNG pattern, pitfalls |
408|| `templates/data-viz.html` | Starter HTML for Chart.js data visualization (copy & modify) |
409|| `templates/character-template.svg` | Copy-paste SVG template for cute character generation (tested, working) |
410|| `scripts/visualize.py` | CLI generator: `python3 visualize.py wolfram|flowchart|architecture` |
411|
412|---
413|
414|

## Verification Checklist

- [ ] Output file exists and is not empty
- [ ] File format matches mode (HTML, SVG, PNG, etc.)
- [ ] Dark theme colors applied (if applicable)
- [ ] Fonts embedded or web-safe
- [ ] Interactive elements functional (if HTML)
- [ ] No broken links or missing resources
- [ ] File size within limits (e.g., PNG < 10MB for Telegram)
- [ ] Tested opening in target environment (browser, Telegram, etc.)
- [ ] Includes source query or description as comment/metadata
- [ ] No offensive or unintended content

## Anti-Patterns & Fixes

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Using Pillow for character images | Low quality, jagged edges | Use SVG + cairosvg |
| Hardcoding colors without palette | Inconsistent look, poor accessibility | Use defined color palette |
| Forgetting to set viewport | Poor mobile responsiveness | Add `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| Overly complex SVG with thousands of elements | Slow render, timeout | Simplify shapes, use groups, limit detail |
| Missing fallback text for icons | Accessibility issues | Add `aria-label` or text alternatives |
| Using external CDNs that may be blocked | Broken diagrams in restricted networks | Bundle critical assets inline or use data URIs |
| Generating massive raster images | File too large to send | Resize dimensions, compress, or use SVG |
| Not validating user input before Wolfram query | Potential injection or invalid queries | Sanitize input, escape special chars |
| Assuming fixed screen size | Layout breaks on different devices | Use relative units (%, vw, vh) or viewBox |
| Forgetting to close tags in SVG | XML parsing error | Validate XML structure |

## Recipes (Contoh Perintah)

### Membuat Diagram Arsitektur dari Deskripsi Teks

```bash
hermes run visualisasi architecture "Sistem microservices dengan frontend React, backend Node.js, database PostgreLD, cache Redis, message broker RabbitMQ, dan layanan email"
```

### Membuat Grafik Line dari CSV

```bash
hermes run visualisasi data-variasi "sales.csv" --type line --title "Penjualan Bulanan"
```

### Membuat Karakter SVG dari Deskripsi

```bash
hermes run visualisasi character "Karutan kucing anggrek dengan topi kuning, senyum lebar, dan bulu fluffi" --output kucing.png
```

### Membuat Infographic Ringkas

```bash
hermes run visualisasi infographic "Manfaat olahraga rutin: meningkatkan imunitas, mengurangi stres, meningkatkan konsentrasi" --style minimal
```

### Menghitung Integral dengan Wolfram Alpha

```bash
hermes run visualisasi wolfram "integral dari 0 hingga pi dari sin(x) dx"
```

## Diagram ASCII Contoh

Berikut contoh diagram alur sederhana dalam format ASCII yang dapat dihasilkan oleh mode flowchart:

```
+-----------+    ---+    +----------+
|  Mulai    | ---> |  Proses A  | ---> | Keputusan |
+-----------+      +----------+       +----------+
                                   | Ya
                                   v
                           +----------+
                           |  Proses B|
                           +----------+
                                   |
                                   v
                           +----------+
                           |   Selesai|
                           +----------+
```

## FAQ

**Q: Mengapa karakter saya terlihat buruk saat menggunakan Pillow?**  
A: Pillow mengalikasi bentuk dasar; untuk detail halus seperti gradien, bayangan, dan tekstur, gunakan SVG yang dirender via cairosvg.

**Q: Bagaimana cara mengubah ukuran output PNG tanpa kehilangan kualitas?**  
A: Hasilkan SVG vektor terlebih dahulu, lalu konversi ke PNG dengan dimensi yang diinginkan menggunakan `cairosvg.svg2png(..., output_width=W, output_height=H)`.

**Q: Apakah saya bisa mengirim langsung file HTML ke Telegram?**  
A: Tidak, Telegram hanya menampilkan file gambar/video/audio. Konversi HTML ke screenshot atau gunakan iframe ke layanan eksternal (seperti Wolfram) yang bisa dibuka di browser.

## Referensi Tambahan

- https://developer.mozilla.org/en-US/docs/Web/SVG
- https://www.chartjs.org/docs/latest/
- https://excalidraw.com/
- https://www.wolframalpha.com/


## Integration dengan Skill Lain
415|
416|| Skill | Kapan pakai |
417||-------|------------|
418|| `architecture-diagram` | Detail arsitektur sistem, full template |
419|| `excalidraw` | Flowchart yang mau diedit user |
420|| `baoyu-infographic` | Infographic dengan 21 layout |
421|| `p5js` | Generative art, interactive viz |
422|| `manim-video` | Animasi edukasi, math explanation |
423|| `sketch` | UI mockup variants |
424|