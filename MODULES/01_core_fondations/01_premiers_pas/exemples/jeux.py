#!/usr/bin/env python3
"""
EXEMPLE 2: Jeu de Devinettes
============================
Cet exemple montre un jeu où l'utilisateur doit deviner un nombre.
"""

import random


def jeu_devinettes():
    """Jeu de devinettes de nombre."""
    print("╔════════════════════════════════════╗")
    print("║     JEU DE DEVINETTES             ║")
    print("║  Devinez le nombre entre 1 et 100 ║")
    print("╚════════════════════════════════════╝")

    # Choisir un nombre aléatoire
    secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 10

    while tentatives < max_tentatives:
        tentatives += 1

        # Demander une proposition
        try:
            proposition = int(input(f"\nTentative {tentatives}/{max_tentatives}: "))
        except ValueError:
            print("Veuillez entrer un nombre valide!")
            tentatives -= 1  # Ne pas compter cette tentative
            continue

        # Vérifier la proposition
        if proposition == secret:
            print(f"\n🎉 Félicitations! Vous avez trouvé en {tentatives} tentatives!")
            return
        elif proposition < secret:
            print("  ➕ Plus grand!")
        else:
            print("  ➖ Plus petit!")

    # Joueur perd
    print(f"\n😢 Perdu! Le nombre était {secret}")


if __name__ == "__main__":
    jeu_devinettes()
