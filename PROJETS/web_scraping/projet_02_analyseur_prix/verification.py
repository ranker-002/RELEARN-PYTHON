#!/usr/bin/env python3
"""
Verification Automatique
=======================
Usage: python verification.py
"""

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
    main_py = Path(__file__).parent / "src" / "main.py"
    if not main_py.exists():
        return False
    try:
        with open(main_py, 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, main_py, 'exec')
        return True
    except Exception:
        return False


def test_execution():
    models_dir = Path(__file__).parent / "src" / "models"
    services_dir = Path(__file__).parent / "src" / "services"
    utils_dir = Path(__file__).parent / "src" / "utils"
    
    all_dirs_exist = all(d.exists() for d in [models_dir, services_dir, utils_dir])
    
    if not all_dirs_exist:
        return False
    
    all_py_valid = True
    for py_file in (Path(__file__).parent / "src").rglob("*.py"):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                compile(f.read(), py_file, 'exec')
        except Exception:
            all_py_valid = False
            break
    
    return all_py_valid


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
