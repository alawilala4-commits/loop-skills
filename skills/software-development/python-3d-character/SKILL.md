---
name: python-3d-character
description: "Build complete 3D game characters and game systems — ModernGL/OpenGL, Ursina, or browser-based WebGL. From procedural modeling to full game features (inventory, dialogue, save/load, AI, collision, day/night, sound, minimap). Delivers as Python or single-file offline HTML."
version: 2.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows, android-termux]
metadata:
  hermes:
    tags: [3D, GameDev, Python, Pygame, ModernGL, OpenGL, Ursina, Character, Animation, AI, Inventory, Dialogue, SaveSystem, Collision, Minimap]
    related_skills: [python-cli-app, opencode]
---

# Python 3D Game Character — Hermes Skill

Build complete 3D game characters and game systems in Python. Covers two rendering backends (ModernGL for desktop, Ursina for Termux/easy setup) and all major game subsystems: procedural modeling, animation, AI, inventory, dialogue, save/load, collision detection, weapons, and minimaps.

## When to use

- Building a 3D game character from scratch in Python
- Procedural character generation (parametric bodies, faces, accessories)
- Learning 3D graphics fundamentals
- Rapid prototyping of character designs
- Building game subsystems (inventory, dialogue, AI, save/load, collision)
- Integrating 3D characters into Pygame or Ursina-based games

## Engine Selection

| Backend | When to use | Dependencies |
|---------|-------------|--------------|
| **ModernGL** | Desktop with OpenGL 3.3+, want full shader control | `pygame moderngl numpy PyGLM` |
| **Ursina** | Termux/Android, quick prototyping, no OpenGL needed | `ursina` (bundles everything) |
| **WebGL (raw)** | Browser-based, zero install, any device | None (pure HTML/JS) |

## Web-Based Delivery (Browser, No Install)

When the user can't or won't run Python (e.g. Android without Termux, iOS, locked-down machines), deliver the game as a **single self-contained HTML file** using raw WebGL. No external dependencies, no CDN, no server needed.

### Architecture: Offline WebGL Game

```
game_offline.html      # Single file, ~30KB, zero dependencies
```

**Key techniques:**
- Inline `<script>` with WebGL 1.0 (broadest browser support)
- Manual matrix math (mat4Perspective, mat4LookAt, mat4Mul) — no libraries
- Procedural mesh generation (box, sphere) with vertex + normal data
- Uint16Array index buffers for efficient rendering
- Touch controls via `touchstart`/`touchend` events
- Keyboard support via `keydown`/`keyup`
- Save/load via `localStorage` (no server)
- Day/Night via `clearColor` + ambient light uniform
- Minimap via 2D canvas overlay

**When to use this pattern:**
- User says "jangan di termux" or "pakai browser"
- User wants to play on phone without installing anything
- File needs to be shared via WhatsApp/email (single .html file)
- Cross-platform requirement (Windows/Mac/Linux/Phone)

**Build approach:**
1. Write everything in one HTML file
2. Use `gl = canvas.getContext('webgl')` (not WebGL2 — wider support)
3. Write inline shaders (vertex + fragment as template literals)
4. Manual MVP matrix computation
5. Test by opening file directly in browser (no server needed)
6. For sharing: upload to Netlify Drop, GitHub Pages, or send file directly

**Touch controls pattern:**
```javascript
// D-pad buttons
el.addEventListener('touchstart', e => { e.preventDefault(); keys.w = true; }, {passive: false});
el.addEventListener('touchend', e => { e.preventDefault(); keys.w = false; }, {passive: false});

// Camera rotation via canvas swipe
canvas.addEventListener('touchmove', e => {
    camAngle += (e.touches[0].clientX - touchStartX) * 0.01;
    touchStartX = e.touches[0].clientX;
});
```

## Project Structure

```
3d-character/
├── main.py              # ModernGL entry point
├── main_ursina.py       # Ursina entry point
├── enemy_npc.py         # Enemy AI demo
├── customize_ui.py      # Character customization UI
├── animation_idle.py    # Idle/breathing animation
├── weapon_system.py     # Weapon switching system
├── collision_demo.py    # Collision detection demo
├── inventory_system.py  # Inventory management
├── dialogue_system.py   # NPC dialogue with choices
├── save_load.py         # Save/load game state
├── minimap.py           # Overhead minimap
├── export_obj.py        # Export to OBJ format
├── character_data.json  # Shared character data
└── character.obj        # Exported model
```

## Prerequisites

```bash
# ModernGL backend
pip install pygame moderngl numpy PyGLM pillow

# Ursina backend (Termux-friendly)
pip install ursina
```

## Core Patterns

### 1. Procedural Character Model (ModernGL)

Build character from primitive shapes (sphere head, box body/arms/legs):

```python
# model.py
import numpy as np
import moderngl as mgl

class CharacterModel:
    def __init__(self, ctx: mgl.Context):
        self.ctx = ctx
        self.vao = self._build_character()
    
    def _build_character(self):
        vertices, indices = [], []
        offset = 0
        parts = [
            ("sphere", 0.3, 16, 16, (0, 1.7, 0)),   # head
            ("box", 0.6, 0.8, 0.3, (0, 1.0, 0)),      # body
            ("box", 0.2, 0.7, 0.2, (-0.5, 1.0, 0)),   # left arm
            ("box", 0.2, 0.7, 0.2, (0.5, 1.0, 0)),    # right arm
            ("box", 0.25, 0.8, 0.25, (-0.18, 0.2, 0)), # left leg
            ("box", 0.25, 0.8, 0.25, (0.18, 0.2, 0)),  # right leg
        ]
        for shape_type, p1, p2, p3, center in parts:
            if shape_type == "sphere":
                verts, idx = self._make_sphere(p1, p2, p3, center)
            else:
                verts, idx = self._make_box(p1, p2, p3, center)
            vertices.extend(verts)
            indices.extend([i + offset for i in idx])
            offset += len(verts) // 6
        
        vbo = self.ctx.buffer(np.array(vertices, dtype='f4'))
        ibo = self.ctx.buffer(np.array(indices, dtype='i4'))
        # ... create VAO with shader program
```

### 2. Ursina Character (No OpenGL needed)

```python
from ursina import *
import math

app = Ursina()

# Build character from entities
head = Entity(model='sphere', color=color.rgb(255,220,180),
              scale=Vec3(0.6,0.6,0.6), position=Vec3(0,1.7,0))
body = Entity(model='cube', color=color.rgb(65,105,225),
              scale=Vec3(0.6,0.8,0.3), position=Vec3(0,1.0,0))
l_arm = Entity(model='cube', color=color.rgb(255,220,180),
               scale=Vec3(0.18,0.7,0.18), position=Vec3(-0.48,1.0,0))
r_arm = Entity(model='cube', color=color.rgb(255,220,180),
               scale=Vec3(0.18,0.7,0.18), position=Vec3(0.48,1.0,0))
l_leg = Entity(model='cube', color=color.rgb(50,50,80),
               scale=Vec3(0.22,0.8,0.22), position=Vec3(-0.16,0.2,0))
r_leg = Entity(model='cube', color=color.rgb(50,50,80),
               scale=Vec3(0.22,0.8,0.22), position=Vec3(0.16,0.2,0))

def update():
    if held_keys['w']:
        t = time.time() * 8
        l_arm.rotation_z = math.sin(t) * 30
        r_arm.rotation_z = -math.sin(t) * 30
        l_leg.rotation_z = -math.sin(t) * 25
        r_leg.rotation_z = math.sin(t) * 25
```

### 3. Animation System

**Idle (breathing + head look):**
```python
def animate_idle(self, t):
    breath_offset = math.sin(t * self.breath_speed) * self.breath_amount
    self.body.y = base_y + breath_offset
    self.head.y = base_y + 0.7 + breath_offset * 1.2
    self.head.rotation_y = math.sin(t * self.look_speed) * 5
    self.l_arm.rotation_z = math.sin(t * self.sway_speed) * 0.5
    self.r_arm.rotation_z = -math.sin(t * self.sway_speed) * 0.5
```

**Walk (body bob + arm/leg swing):**
```python
def animate_walk(self, t):
    speed = 8
    body_bob = abs(math.sin(t * speed)) * 0.08
    self.body.y = base_y + body_bob
    self.l_arm.rotation_z = math.sin(t * speed) * 30
    self.r_arm.rotation_z = -math.sin(t * speed) * 30
    self.l_leg.rotation_z = -math.sin(t * speed) * 25
    self.r_leg.rotation_z = math.sin(t * speed) * 25
```

### 4. Enemy AI

```python
class Enemy(Entity):
    def __init__(self, position=Vec3(5, 0, 5)):
        super().__init__()
        self.health = 50
        self.max_health = 50
        self.speed = 2
        self.attack_range = 1.5
        self.attack_damage = 10
        self.attack_cooldown = 1.0
        self.last_attack = 0
        self.alive = True
        self.position = position
        # Body parts as children...
        self.health_bar_bg = Entity(parent=self, model='cube',
                                     scale=Vec3(0.7, 0.06, 0.04), position=Vec3(0, 1.9, 0))
        self.health_bar = Entity(parent=self, model='cube',
                                 color=color.rgb(255, 50, 50),
                                 scale=Vec3(0.68, 0.05, 0.03), position=Vec3(0, 1.9, 0))
    
    def update(self, player_pos, dt):
        if not self.alive: return
        direction = player_pos - self.position
        direction.y = 0
        dist = direction.length()
        if dist > self.attack_range:
            self.position += direction.normalized() * self.speed * dt
            self.look_at(self.position + direction)
            # Walk animation
            self.l_leg.rotation_z = math.sin(time.time() * 6) * 20
            self.r_leg.rotation_z = -math.sin(time.time() * 6) * 20
        else:
            self.look_at(player_pos)
            if time.time() - self.last_attack > self.attack_cooldown:
                self.last_attack = time.time()
                self.attack(player_pos)
        # Update health bar
        ratio = self.health / self.max_health
        self.health_bar.scale_x = 0.68 * ratio
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False
            self.rotation_z = 90  # Fall over
            self.health_bar.enabled = False
```

### 5. Collision Detection

**AABB (obstacles):**
```python
def aabb_collision(pos1, half1, pos2, half2):
    return (abs(pos1.x - pos2.x) < (half1.x + half2.x) and
            abs(pos1.y - pos2.y) < (half1.y + half2.y) and
            abs(pos1.z - pos2.z) < (half1.z + half2.z))

def resolve_collision(player_pos, obstacle_pos, obstacle_half):
    diff = player_pos - obstacle_pos
    overlap_x = player_bounds.x + obstacle_half.x - abs(diff.x)
    overlap_z = player_bounds.z + obstacle_half.z - abs(diff.z)
    if overlap_x > 0 and overlap_z > 0:
        if overlap_x < overlap_z:
            player_pos.x += overlap_x if diff.x > 0 else -overlap_x
        else:
            player_pos.z += overlap_z if diff.z > 0 else -overlap_z
    return player_pos
```

**Sphere (collectibles/projectiles):**
```python
def sphere_collision(pos1, radius1, pos2, radius2):
    return (pos1 - pos2).length() < (radius1 + radius2)
```

### 6. Weapon System

```python
WEAPONS = {
    'fist': {'damage': 5, 'range': 1.5, 'speed': 1.0, 'color': color.rgb(255, 220, 180)},
    'sword': {'damage': 20, 'range': 2.0, 'speed': 0.8, 'color': color.rgb(200, 200, 220)},
    'axe': {'damage': 35, 'range': 1.8, 'speed': 0.5, 'color': color.rgb(150, 100, 60)},
    'spear': {'damage': 15, 'range': 3.0, 'speed': 1.2, 'color': color.rgb(180, 180, 180)},
}

def attack():
    w = WEAPONS[current_weapon]
    # Swing animation
    player_r_arm.rotation_z = 70
    # Check hits
    for enemy in enemies:
        if enemy.alive and (enemy.position - player_pos).length() <= w['range']:
            enemy.take_damage(w['damage'])
```

### 7. Inventory System

```python
inventory = {
    'items': [
        {'id': 'sword', 'name': 'Iron Sword', 'type': 'weapon', 'equipped': False},
        {'id': 'potion_hp', 'name': 'Health Potion', 'type': 'consumable',
         'effect': 'heal', 'value': 30, 'count': 3},
    ],
    'gold': 100,
    'capacity': 16
}

def use_item(index):
    item = inventory['items'][index]
    if item['type'] == 'consumable':
        if item['effect'] == 'heal':
            player_health = min(max_health, player_health + item['value'])
        item['count'] -= 1
    elif item['type'] == 'weapon':
        for other in inventory['items']:
            if other['type'] == 'weapon': other['equipped'] = False
        item['equipped'] = True
    save_inventory(inventory)
```

### 8. Dialogue System

```python
class DialogueNPC(Entity):
    def __init__(self, name, position, dialogue, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.dialogue = dialogue  # [{'text': ..., 'choices': [...]}]
        self.in_dialogue = False
        self.dialogue_index = 0
    
    def interact(self):
        self.in_dialogue = True
        self.dialogue_index = 0
        show_dialogue(self)
    
    def advance(self):
        self.dialogue_index += 1
        if self.dialogue_index >= len(self.dialogue):
            self.close_dialogue()
```

### 9. Save/Load System

```python
SAVE_FILE = 'savegame.json'

def save_game():
    save_data = {
        'timestamp': datetime.now().isoformat(),
        'player': {
            'position': [player.position.x, player.position.y, player.position.z],
            'health': player_state['health'],
            'level': player_state['level'],
            'exp': player_state['exp'],
            'gold': player_state['gold'],
            'inventory': player_state['inventory'],
            'stats': player_state['stats'],
        }
    }
    with open(SAVE_FILE, 'w') as f:
        json.dump(save_data, f, indent=2)

def load_game():
    with open(SAVE_FILE) as f:
        save_data = json.load(f)
    p = save_data['player']
    player.position = Vec3(*p['position'])
    player_state.update(p)
```

### 10. Minimap

```python
MINIMAP_SIZE = 200
MINIMAP_SCALE = 0.1

minimap_bg = Entity(parent=camera.ui, model='quad', color=color.rgba(10,10,20,200),
                    scale=Vec3(MINIMAP_SIZE/1000, MINIMAP_SIZE/1000, 1), position=Vec3(0.75, 0.35, 0))

def world_to_minimap(world_pos, player_pos):
    rel_x = (world_pos.x - player_pos.x) * MINIMAP_SCALE
    rel_y = (world_pos.z - player_pos.z) * MINIMAP_SCALE
    max_rel = MINIMAP_RANGE * MINIMAP_SCALE
    rel_x = max(-max_rel, min(max_rel, rel_x))
    rel_y = max(-max_rel, min(max_rel, rel_y))
    return Vec3(rel_x, rel_y, -0.1)
```

### 11. OBJ Export

```python
def make_box(w, h, d, center):
    # 6 faces, 4 vertices each, normals per face
    # Returns (vertices[list], normals[list], faces[list])

def write_obj(filepath, vertices, normals, faces, name="Character"):
    with open(filepath, 'w') as f:
        f.write(f"o {name}\n")
        for i in range(0, len(vertices), 3):
            f.write(f"v {vertices[i]:.6f} {vertices[i+1]:.6f} {vertices[i+2]:.6f}\n")
        for i in range(0, len(normals), 3):
            f.write(f"vn {normals[i]:.6f} {normals[i+1]:.6f} {normals[i+2]:.6f}\n")
        for i in range(0, len(faces), 3):
            a, b, c = faces[i]+1, faces[i+1]+1, faces[i+2]+1
            f.write(f"f {a}//{a} {b}//{b} {c}//{c}\n")
```

## Controls Reference

| Key | Action |
|-----|--------|
| W/A/S/D | Move |
| F | Attack |
| E | Talk to NPC |
| SPACE | Shoot projectile |
| TAB | Open inventory |
| 1-4 | Switch weapon |
| F5/F9 | Save/Load game |
| H | Quick heal (use potion) |
| ESC | Quit |

## Character Data Format

`character_data.json` defines body parts and animation parameters:

```json
{
  "character": {
    "name": "Hero",
    "body_parts": {
      "head": {"type": "sphere", "radius": 0.3, "color": [255, 220, 180], "position": [0, 1.7, 0]},
      "body": {"type": "box", "size": [0.6, 0.8, 0.3], "color": [65, 105, 225], "position": [0, 1.0, 0]}
    },
    "animations": {
      "walk": {"speed": 8, "arm_swing": 30, "leg_swing": 25, "body_bob": 0.05}
    }
  }
}
```

## Additional Patterns

### Quest System

```python
QUESTS = {
    'kill_slimes': {
        'name': 'Slime Hunter', 'type': 'kill', 'target': 'slime',
        'required': 3, 'reward': {'exp': 50, 'gold': 30, 'item': 'potion_hp'},
        'status': 'available', 'progress': 0,
    }
}

def update_quest_progress(quest_type, target):
    for quest_id, quest in player_state['quests'].items():
        if quest['status'] == 'active' and quest['type'] == quest_type and quest['target'] == target:
            quest['progress'] += 1
            if quest['progress'] >= quest['required']:
                quest['status'] = 'completed'
            break
```

### Day/Night Cycle

```python
def update_sky_color():
    if 6 <= time_of_day < 8:    # Dawn
        return lerp_color(sunset_color, day_color, (time_of_day - 6) / 2)
    elif 8 <= time_of_day < 18:  # Day
        return day_color
    elif 18 <= time_of_day < 20: # Sunset
        return lerp_color(day_color, sunset_color, (time_of_day - 18) / 2)
    else:                        # Night
        return night_color

def update_lighting():
    angle = ((time_of_day - 6) / 12) * math.pi
    sun.position = Vec3(math.cos(angle) * 50, math.sin(angle) * 50, -30)
    show_stars = time_of_day < 6 or time_of_day >= 20
    for star in stars: star.enabled = show_stars
```

### Procedural Sound Effects

```python
def generate_sound_waveform(freq, duration, wave_type='sine', volume=0.5, decay=True):
    samples = int(44100 * duration)
    t = np.linspace(0, duration, samples, endpoint=False)
    if wave_type == 'sine': wave = np.sin(2 * np.pi * freq * t)
    elif wave_type == 'square': wave = np.sign(np.sin(2 * np.pi * freq * t))
    elif wave_type == 'sawtooth': wave = 2 * (t * freq - np.floor(0.5 + t * freq))
    elif wave_type == 'noise': wave = np.random.uniform(-1, 1, samples)
    if decay: wave *= np.exp(-3 * t / duration)
    return (wave * 32767 * volume).astype(np.int16)

# Play via pygame.mixer
sound = pygame.mixer.Sound(buffer=wave.tobytes())
sound.play()
```

### Main Menu Pattern

```python
class MenuButton(Button):
    def __init__(self, text, y, callback):
        super().__init__(text=text, position=Vec3(0, y, 0), scale=Vec3(0.4, 0.08, 1),
                         color=color.rgb(40, 40, 60), highlight_color=color.rgb(60, 60, 90))
        self.on_click = callback

# Menu state machine
def show_main_menu():
    global menu_state
    menu_state = 'main'
    main_menu.enabled = True
    settings_menu.enabled = False
```

## User Workflow Preferences

- **Direct action over clarification**: When user says "boleh" (go ahead), proceed immediately with best judgment. Don't ask multiple-choice questions — pick the most sensible option and implement.
- **Web-first delivery**: User prefers browser-based play over Termux. Default to offline HTML/WebGL single-file delivery when targeting phone play.
- **Bahasa Indonesia**: User communicates in Indonesian. Code comments and print() messages can be in Indonesian.

## Pitfalls

1. **ModernGL needs OpenGL 3.3+** — ensure your system supports it
2. **Android/Termux**: Pygame+OpenGL won't work; use Ursina backend
3. **Matrix order**: GLM uses column-major; write to uniforms with `glm.value_ptr()`
4. **VAO recreation**: Don't recreate VAO every frame — build once, reuse
5. **Depth test**: Always enable `DEPTH_TEST` for 3D rendering
6. **Normal matrix**: Must be `transpose(inverse(model))` for correct lighting with non-uniform scale
7. **Shader compilation**: Check `program` for None on compile failure
8. **Ursina Entity args**: Use `Vec3()` for scale/position (Pyright warns about tuples but works)
9. **Termux pip timeout**: `pip install` may hang; use `--no-deps` or install one package at a time
10. **JSON key mismatch**: Export script uses `size` + `radius`; import may expect `scale` — normalize on load
11. **Lambda multi-statement**: Python lambdas can't contain `or` between function calls — use named functions for compound sound sequences
12. **Ursina rgba**: Use `color.rgba()` not `color.rgb()` for transparency; alpha is 4th arg

## Verification

```bash
# ModernGL backend
python -c "import pygame, moderngl, glm, numpy; print('ModernGL OK')"

# Ursina backend
python -c "import ursina; print('Ursina OK')"

# Run any demo
python main_ursina.py
python enemy_npc.py
python weapon_system.py
```

## References

- ModernGL docs: https://moderngl.readthedocs.io/
- PyGLM docs: https://pyglm.g-truc.net/
- Learn OpenGL: https://learnopengl.com/
- Pygame: https://www.pygame.org/docs/
- Ursina docs: https://www.ursinaengine.org/
- OBJ spec: https://en.wikipedia.org/wiki/Wavefront_.obj_file
