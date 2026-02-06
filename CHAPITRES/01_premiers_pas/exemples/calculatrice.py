#!/usr/bin/env python3
"""
EXEMPLE 1: Calculatrice Interactive Améliorée
==============================================
Cet exemple montre une calculatrice avec menu.
"""

def calculatrice():
    """Calculatrice avec menu interactif."""
    print("╔═══════════════════════════════╗")
    print("║   CALCULATRICE PYTHON        ║")
    print("╠═══════════════════════════════╣")
    print("║  1. Addition                 ║")
    print("║  2. Soustraction              ║")
    print("║  3. Multiplication           ║")
    print("║  4. Division                 ║")
    print("║  5. Quitter                  ║")
    print("╚═══════════════════════════════╝")

    while True:
        choix = input("\nVotre choix (1-5): ")

        if choix == "5":
            print("Au revoir!")
            break

        if choix not in ["1", "2", "3", "4"]:
            print("Choix invalide. Veuillez choisir 1-5.")
            continue

        # Demander les nombres
        try:
            a = float(input("Premier nombre: "))
            b = float(input("Deuxième nombre: "))

            # Effectuer l'opération
            if choix == "1":
                resultat = a + b
                operation = "+"
            elif choix == "2":
                resultat = a - b
                operation = "-"
            elif choix == "3":
                resultat = a * b
                operation = "*"
            else:  # choix == "4"
                if b == 0:
                    print("Erreur: Division par zéro impossible!")
                    continue
                resultat = a / b
                operation = "/"

            # Afficher le résultat
            print(f"  {a} {operation} {b} = {resultat}")

        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides.")

        print()


if __name__ == "__main__":
    calculatrice()
