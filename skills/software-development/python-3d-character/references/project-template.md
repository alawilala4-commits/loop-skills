# 3D Character Project Template

Copy this template to start a new 3D character project:

```
my-3d-game/
├── main.py              # Entry point
├── character_data.json  # Character definition
├── requirements.txt     # Dependencies
├── test_imports.py      # Verify setup
├── enemy_npc.py         # Enemy AI
├── customize_ui.py      # Character customization
├── animation_idle.py    # Idle animation
├── weapon_system.py     # Weapons
├── collision_demo.py    # Collision detection
├── inventory_system.py  # Inventory
├── dialogue_system.py   # NPC dialogue
├── save_load.py         # Save/load
├── minimap.py           # Minimap
└── export_obj.py        # OBJ export
```

## Quick Start

```bash
mkdir my-3d-game && cd my-3d-game
git init

# Copy files from ~/projects/3d-character/ as starting point
cp ~/projects/3d-character/*.py .
cp ~/projects/3d-character/character_data.json .

# Test
python main_ursina.py
```

## Termux Notes

On Android/Termux:
- Pygame + ModernGL won't work (no SDL dev packages in Termux repos)
- Use Ursina backend instead (`pip install ursina`)
- `pip install` may timeout on Termux — try `pip install --no-deps <pkg>` one at a time
- OpenGL context requires VNC or software rendering for ModernGL

## Feature Checklist

- [ ] Basic character model (head, body, arms, legs)
- [ ] Walk animation
- [ ] Idle/breathing animation
- [ ] Camera controller
- [ ] Ground plane + sky
- [ ] Enemy NPC with AI
- [ ] Health bars
- [ ] Weapon system (4 weapons)
- [ ] Collision detection (AABB + sphere)
- [ ] Projectile shooting
- [ ] Inventory system
- [ ] Character customization UI
- [ ] Dialogue system
- [ ] Save/load game
- [ ] Minimap
- [ ] OBJ export
