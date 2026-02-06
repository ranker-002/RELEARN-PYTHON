#!/usr/bin/env python3
"""
CHAPITRE 16: SERIALISATION
"""

import sys


def verifier_tous():
    print("=" * 60)
    print("CHAPITRE 16: SERIALISATION")
    print("=" * 60)
    
    for i in range(1, 11):
        try:
            exec(f"from exercices import exercice_16_{i}")
            eval(f"exercice_16_{i}()")
            print(f"✓ 16.{i}")
        except Exception as e:
            print(f"✗ 16.{i}: {e}")


if __name__ == "__main__":
    verifier_tous()
