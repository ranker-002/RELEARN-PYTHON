#!/usr/bin/env python3
"""Test simple du serveur de vérification."""
import sys
from pathlib import Path

# Setup path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

print("Importing modules...")
from relearn_python.verify_server.verifier import get_chapter_info, run_verification

chapter_path = Path(__file__).parent
print(f"Chapter path: {chapter_path}")

print("\nGetting chapter info...")
try:
    info = get_chapter_info(chapter_path)
    print(f"Info: {info}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

print("\nRunning verification...")
try:
    results = run_verification(chapter_path)
    print(f"Results keys: {results.keys()}")
    print(f"Total: {results['total']}, Passed: {results['passed']}, Failed: {results['failed']}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
