#!/usr/bin/env python3
"""Verify all 3D character dependencies are importable."""
import sys

def test_imports():
    errors = []
    
    # Core
    try:
        import pygame
        print(f"[OK] pygame {pygame.version.ver}")
    except ImportError as e:
        errors.append(f"[FAIL] pygame: {e}")
    
    try:
        import moderngl as mgl
        print(f"[OK] moderngl {mgl.__version__}")
    except ImportError as e:
        errors.append(f"[FAIL] moderngl: {e}")
    
    try:
        import numpy as np
        print(f"[OK] numpy {np.__version__}")
    except ImportError as e:
        errors.append(f"[FAIL] numpy: {e}")
    
    try:
        import glm
        print("[OK] PyGLM")
    except ImportError as e:
        errors.append(f"[FAIL] PyGLM: {e}")
    
    # Ursina alternative
    try:
        import ursina
        print("[OK] Ursina (alternative backend)")
    except ImportError:
        print("[--] Ursina not installed (optional, for Termux)")
    
    if errors:
        print()
        for err in errors:
            print(err)
        print("\nInstall: pip install pygame moderngl numpy PyGLM pillow")
        sys.exit(1)
    else:
        print("\nAll OK! Run: python main.py")
        print("Termux: python main_ursina.py")

if __name__ == "__main__":
    test_imports()
