#!/usr/bin/env python3
"""Visualisasi Generator CLI - Quick generator untuk semua mode visualisasi."""

import sys
import os
import json

HERMES_HOME = os.path.expanduser("~/.hermes")
PROJECTS_DIR = os.path.expanduser("~/projects/visualisasi-test")


def ensure_dirs():
    os.makedirs(PROJECTS_DIR, exist_ok=True)


def gen_wolfram(query, output):
    """Generate Wolfram Alpha query HTML."""
    encoded = query.replace(' ', '+')
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wolfram Alpha: {query}</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'JetBrains Mono', monospace; background: #020617; color: white; min-height: 100vh; padding: 2rem; }}
    .container {{ max-width: 1000px; margin: 0 auto; }}
    h1 {{ font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem; }}
    .query {{ color: #22d3ee; font-size: 0.9rem; background: rgba(8, 51, 68, 0.3); padding: 0.5rem 1rem; border-radius: 0.5rem; display: inline-block; }}
    .result-box {{ background: rgba(15, 23, 42, 0.5); border: 1px solid #1e293b; border-radius: 1rem; padding: 1.5rem; margin-top: 1.5rem; overflow: hidden; }}
    .link {{ color: #22d3ee; font-size: 0.8rem; margin-top: 1rem; display: inline-block; text-decoration: none; border: 1px solid #1e293b; padding: 0.4rem 0.8rem; border-radius: 0.4rem; }}
    iframe {{ width: 100%; height: 600px; border: none; border-radius: 0.5rem; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Wolfram Alpha Result</h1>
    <span class="query">{query}</span>
    <div class="result-box">
      <iframe src="https://www.wolframalpha.com/input?i={encoded}" frameborder="0"></iframe>
    </div>
    <a class="link" href="https://www.wolframalpha.com/input?i={encoded}" target="_blank">Open in Wolfram Alpha</a>
  </div>
</body>
</html>'''
    output = os.path.join(PROJECTS_DIR, output) if not os.path.isabs(output) else output
    with open(output, 'w') as f:
        f.write(html)
    print(f"OK Wolfram Alpha HTML: {output}")


def gen_flowchart(title, steps, output):
    """Generate Excalidraw flowchart."""
    elements = []
    y = 100
    node_ids = []

    for i, step in enumerate(steps):
        nid = f"node_{i}"
        node_ids.append(nid)
        elements.append({
            "type": "rectangle", "id": nid, "x": 300, "y": y, "width": 200, "height": 60,
            "strokeColor": "#22d3ee", "backgroundColor": "rgba(8, 51, 68, 0.4)",
            "fillStyle": "solid", "strokeWidth": 2, "roughness": 0,
            "opacity": 100, "roundness": {"type": 3},
            "boundElements": [{"id": f"text_{i}", "type": "text"}]
        })
        elements.append({
            "type": "text", "id": f"text_{i}", "x": 310, "y": y + 10, "width": 180, "height": 40,
            "text": step, "fontSize": 16, "fontFamily": 1, "strokeColor": "#ffffff",
            "textAlign": "center", "verticalAlign": "middle",
            "containerId": nid, "originalText": step, "autoResize": True
        })

        if i > 0:
            elements.append({
                "type": "arrow", "id": f"arrow_{i}", "x": 400, "y": y - 60, "width": 0, "height": 60,
                "points": [[0, 0], [0, 60]], "endArrowhead": "arrow",
                "strokeColor": "#64748b", "strokeWidth": 2,
                "startBinding": {"elementId": node_ids[i-1], "fixedPoint": [0.5, 1]},
                "endBinding": {"elementId": nid, "fixedPoint": [0.5, 0]}
            })
        y += 120

    data = {
        "type": "excalidraw", "version": 2, "source": "hermes-visualisasi",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff"}
    }

    output = os.path.join(PROJECTS_DIR, output) if not os.path.isabs(output) else output
    with open(output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"OK Flowchart: {output}")
    print(f"   Open at: https://excalidraw.com")


def gen_architecture(title, components, connections, output):
    """Generate dark-themed architecture diagram."""
    svg_elements = []
    for comp in components:
        svg_elements.append(
            f'<rect x="{comp["x"]}" y="{comp["y"]}" width="{comp["w"]}" height="{comp["h"]}" '
            f'rx="6" fill="{comp["fill"]}" stroke="{comp["stroke"]}" stroke-width="1.5"/>'
            f'<text x="{comp["x"] + comp["w"]//2}" y="{comp["y"] + comp["h"]//2 - 8}" fill="white" '
            f'font-size="11" font-weight="600" text-anchor="middle">{comp["label"]}</text>'
            f'<text x="{comp["x"] + comp["w"]//2}" y="{comp["y"] + comp["h"]//2 + 10}" fill="#94a3b8" '
            f'font-size="9" text-anchor="middle">{comp.get("sub", "")}</text>'
        )

    arrows = []
    for conn in connections:
        arrows.append(
            f'<line x1="{conn["x1"]}" y1="{conn["y1"]}" x2="{conn["x2"]}" y2="{conn["y2"]}" '
            f'stroke="{conn.get("color", "#64748b")}" stroke-width="1.5" marker-end="url(#arrowhead)"/>'
        )

    svg_content = "\n".join(svg_elements + arrows)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} Architecture</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'JetBrains Mono', monospace; background: #020617; min-height: 100vh; padding: 2rem; color: white; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    h1 {{ font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; }}
    .subtitle {{ color: #94a3b8; font-size: 0.875rem; margin-bottom: 2rem; }}
    .diagram-container {{ background: rgba(15, 23, 42, 0.5); border-radius: 1rem; border: 1px solid #1e293b; padding: 1.5rem; overflow-x: auto; }}
    svg {{ width: 100%; min-width: 900px; display: block; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>{title} Architecture</h1>
    <p class="subtitle">System architecture diagram</p>
    <div class="diagram-container">
      <svg viewBox="0 0 1000 500">
        <defs>
          <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#64748b"/>
          </marker>
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.5"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)"/>
        {svg_content}
      </svg>
    </div>
  </div>
</body>
</html>'''
    output = os.path.join(PROJECTS_DIR, output) if not os.path.isabs(output) else output
    with open(output, 'w') as f:
        f.write(html)
    print(f"OK Architecture: {output}")


if __name__ == '__main__':
    ensure_dirs()

    if len(sys.argv) < 2:
        print("Usage: python3 visualize.py <mode> [options]")
        print("Modes: wolfram, flowchart, architecture")
        print("")
        print("Examples:")
        print('  python3 visualize.py wolfram "plot sin(x)" output.html')
        print('  python3 visualize.py flowchart "My Process" "Step 1,Step 2,Step 3" output.excalidraw')
        sys.exit(1)

    mode = sys.argv[1]

    if mode == 'wolfram':
        if len(sys.argv) < 4:
            print("Usage: python3 visualize.py wolfram <query> <output.html>")
            sys.exit(1)
        gen_wolfram(sys.argv[2], sys.argv[3])

    elif mode == 'flowchart':
        if len(sys.argv) < 5:
            print("Usage: python3 visualize.py flowchart <title> <step1,step2,...> <output.excalidraw>")
            sys.exit(1)
        steps = sys.argv[3].split(',')
        gen_flowchart(sys.argv[2], steps, sys.argv[4])

    elif mode == 'architecture':
        print("Architecture mode: use as library")
        print("  from visualize import gen_architecture")
        print("  gen_architecture(title, components, connections, output)")

    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)
