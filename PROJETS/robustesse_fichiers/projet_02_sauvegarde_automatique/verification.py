#!/usr/bin/env python3
"""
Verification Automatique
========================
Usage: python verification.py
"""

import sys
import subprocess
import os
from pathlib import Path


def verifier(msg, test_func):
    try:
        result = test_func()
        print(f"OK: {msg}")
        return result if result is not None else True
    except Exception as e:
        print(f"ECHEC: {msg} - {e}")
        return False


def test_structure():
    required = ["src", "tests", "data"]
    return all((Path(__file__).parent / d).exists() for d in required)


def test_import():
    from src.main import Colors
    return True


def test_execution():
    env = {"PYTHONPATH": str(Path(__file__).parent / "src")}
    result = subprocess.run(
        ["python", "-c", "from main import Colors; print('OK')"],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent),
        timeout=10,
        env={**os.environ, **env}
    )
    return result.returncode == 0 and "OK" in result.stdout


def run():
    print(f"\n=== Verification ===\n")
    
    tests = [
        ("Structure", test_structure),
        ("Import", test_import),
        ("Execution", test_execution),
    ]
    
    passed = sum(1 for name, t in tests if verifier(name, t))
    
    print(f"\n=== Resultat: {passed}/{len(tests)} ===\n")
    if passed == len(tests):
        print("Projet valide!\n")
    else:
        print(f"{len(tests) - passed} test(s) en echec.\n")


if __name__ == "__main__":
    run()
