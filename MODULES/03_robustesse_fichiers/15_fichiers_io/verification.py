#!/usr/bin/env python3
"""
CHAPITRE 15 - Verification
"""

import sys


def verifier_tous():
    print("=" * 60)
    print("VERIFICATION - CHAPITRE 15: FICHIERS I/O")
    print("=" * 60)
    
    for i in range(1, 16):
        try:
            exec(f"from exercices import exercice_15_{i}")
            eval(f"exercice_15_{i}()")
            print(f"✓ Exercice 15.{i}: CORRECT")
        except Exception as e:
            print(f"✗ Exercice 15.{i}: ERREUR - {e}")
    
    print("=" * 60)


if __name__ == "__main__":
    verifier_tous()
