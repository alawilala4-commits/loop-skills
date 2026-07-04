# OBJ/GLTF Model Loading Reference

## OBJ Loader

```python
import numpy as np
import moderngl as mgl

def load_obj(ctx, path, prog):
    """Load OBJ file into ModernGL VAO."""
    vertices = []
    normals = []
    texcoords = []
    faces = []
    
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('v '):
                parts = line.split()
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('vn '):
                parts = line.split()
                normals.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('vt '):
                parts = line.split()
                texcoords.append([float(parts[1]), float(parts[2])])
            elif line.startswith('f '):
                parts = line.split()[1:]
                face = []
                for p in parts:
                    indices = p.split('/')
                    v_idx = int(indices[0]) - 1
                    t_idx = int(indices[1]) - 1 if len(indices) > 1 and indices[1] else 0
                    n_idx = int(indices[2]) - 1 if len(indices) > 2 and indices[2] else 0
                    face.append((v_idx, t_idx, n_idx))
                if len(face) >= 3:
                    faces.extend(face[:3])
                    if len(face) == 4:
                        faces.extend([face[0], face[2], face[3]])
    
    data = []
    for v_idx, t_idx, n_idx in faces:
        if v_idx < len(vertices):
            data.extend(vertices[v_idx])
        else:
            data.extend([0, 0, 0])
        if n_idx < len(normals):
            data.extend(normals[n_idx])
        else:
            data.extend([0, 1, 0])
    
    vbo = ctx.buffer(np.array(data, dtype='f4'))
    vao = ctx.vertex_array(
        prog,
        [(vbo, '3f 3f', 'in_position', 'in_normal')]
    )
    return vao
```

## GLTF Loading (using trimesh)

```python
import trimesh
import numpy as np

def load_gltf(path):
    """Load GLTF/GLB using trimesh."""
    scene = trimesh.load(path)
    
    if isinstance(scene, trimesh.Scene):
        geometries = list(scene.geometry.values())
        mesh = trimesh.util.concatenate(geometries)
    else:
        mesh = scene
    
    vertices = mesh.vertices.astype(np.float32)
    normals = mesh.vertex_normals.astype(np.float32) if hasattr(mesh, 'vertex_normals') else np.zeros_like(vertices)
    faces = mesh.faces.astype(np.uint32)
    
    return vertices, normals, faces
```

## Procedural Character Variations

```python
import random

def random_character_params():
    """Generate random character parameters for variety."""
    return {
        'height': random.uniform(0.8, 1.2),
        'build': random.choice(['slim', 'normal', 'heavy']),
        'head_size': random.uniform(0.8, 1.2),
        'arm_length': random.uniform(0.85, 1.15),
        'leg_length': random.uniform(0.85, 1.15),
        'color_skin': (
            random.uniform(0.6, 0.9),
            random.uniform(0.4, 0.7),
            random.uniform(0.3, 0.6)
        ),
        'color_shirt': (
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1)
        ),
    }
```
