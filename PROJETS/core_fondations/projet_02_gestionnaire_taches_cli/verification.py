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
    import sys
    import py_compile
    from pathlib import Path
    src_path = Path(__file__).parent / "src"
    modules = ["main", "models/tache", "models/projet", "models/tag",
               "services/gestionnaire", "services/filtre", "services/exporteur",
               "utils/config", "utils/date_utils"]
    for module in modules:
        file_path = src_path / f"{module}.py"
        if file_path.exists():
            py_compile.compile(str(file_path), doraise=True)
    return True


def test_execution():
    import subprocess
    import sys
    from pathlib import Path
    src_path = Path(__file__).parent / "src"
    result = subprocess.run(
        [sys.executable, "src/main.py", "--help"],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent),
        timeout=10
    )
    return result.returncode == 0 and "help" in result.stdout.lower()


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
