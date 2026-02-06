#!/usr/bin/env python3
"""
CHAPITRE 17: DECORATEURS ET GENERATEURS
"""

import sys


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 17: DECORATEURS ET GENERATEURS")
    print("=" * 60)
    
    for i in range(1, 11):
        try:
            exec(f"from exercices import exercice_17_{i}")
            eval(f"exercice_17_{i}()")
            print(f"✓ 17.{i}")
        except Exception as e:
            print(f"✗ 17.{i}: {e}")


if __name__ == "__main__":
    verifier_tous()
