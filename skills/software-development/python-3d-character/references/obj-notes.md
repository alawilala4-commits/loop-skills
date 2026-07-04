# OBJ Loader & Exporter Notes

## Key Format Differences

The `export_obj.py` script generates OBJ with this vertex format:
```
v x y z        # position
vn nx ny nz    # normal
f a//a b//b c//c  # face (position//normal)
```

## Common Key Mismatch

When loading `character_data.json`, note the field names:
- Box parts use `size` (not `scale`)
- Sphere parts use `radius` (not `scale`)
- All parts use `position` and `color`

Always normalize on load:
```python
size = part_data.get('size', part_data.get('scale', [0.5, 0.5, 0.5]))
radius = part_data.get('radius', part_data.get('scale', [0.3])[0])
```

## OBJ Import in Blender

1. File > Import > Wavefront (.obj)
2. Check "Split by Group" if you want separate objects
3. Materials are not included in basic export — add them manually

## OBJ Import in Unity

1. Drag `.obj` file into Assets folder
2. Select asset → Inspector → Scale Factor: 1
3. Drag from Assets into Scene to instantiate

## GLTF Loading (using trimesh)

```python
import trimesh

def load_gltf(path):
    scene = trimesh.load(path)
    if isinstance(scene, trimesh.Scene):
        mesh = trimesh.util.concatenate(scene.geometry.values())
    else:
        mesh = scene
    return mesh.vertices, mesh.vertex_normals, mesh.faces
```
