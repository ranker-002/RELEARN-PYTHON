#!/usr/bin/env python3
"""
EXEMPLE 3: Convertisseur d'Unit�s
=================================
Cet exemple montre plusieurs conversions de units.
"""

def convertir_longueur():
    """Convertit entre différentes unités de longueur."""
    print("\n╔════════════════════════════════╗")
    print("║   CONVERTISSEUR DE LONGUEUR   ║")
    print("╠════════════════════════════════╣")
    print("║  1. Mètres → Kilomètres        ║")
    print("║  2. Kilomètres → Mètres        ║")
    print("║  3. Centimètres → Pouces      ║")
    print("║  4. Miles → Kilomètres        ║")
    print("║  0. Retour                     ║")
    print("╚════════════════════════════════╝")

    choix = input("\nVotre choix: ")

    if choix == "1":
        metres = float(input("Mètres: "))
        km = metres / 1000
        print(f"{metres} m = {km} km")
    elif choix == "2":
        km = float(input("Kilomètres: "))
        metres = km * 1000
        print(f"{km} km = {metres} m")
    elif choix == "3":
        cm = float(input("Centimètres: "))
        pouces = cm / 2.54
        print(f"{cm} cm = {pouces:.2f} pouces")
    elif choix == "4":
        miles = float(input("Miles: "))
        km = miles * 1.60934
        print(f"{miles} miles = {km:.2f} km")


def convertir_poids():
    """Convertit entre différentes unités de poids."""
    print("\n╔════════════════════════════════╗")
    print("║    CONVERTISSEUR DE POIDS     ║")
    print("╠════════════════════════════════╣")
    print("║  1. Kg → Livres               ║")
    print("║  2. Livres → Kg               ║")
    print("║  3. Kg → Onces                ║")
    print("║  0. Retour                    ║")
    print("╚════════════════════════════════╝")

    choix = input("\nVotre choix: ")

    if choix == "1":
        kg = float(input("Kilogrammes: "))
        livres = kg * 2.20462
        print(f"{kg} kg = {livres:.2f} livres")
    elif choix == "2":
        livres = float(input("Livres: "))
        kg = livres / 2.20462
        print(f"{livres} livres = {kg:.2f} kg")
    elif choix == "3":
        kg = float(input("Kilogrammes: "))
        onces = kg * 35.274
        print(f"{kg} kg = {onces:.2f} onces")


def menu_principal():
    """Menu principal du convertisseur."""
    while True:
        print("\n╔════════════════════════════════════╗")
        print("║      CONVERTISSEUR MULTI-USAGE    ║")
        print("╠════════════════════════════════════╣")
        print("║  1. Longueur                       ║")
        print("║  2. Poids                           ║")
        print("║  3. Température                    ║")
        print("║  4. Devises (EUR → USD)             ║")
        print("║  0. Quitter                         ║")
        print("╚════════════════════════════════════╝")

        choix = input("\nVotre choix: ")

        if choix == "0":
            print("Au revoir!")
            break
        elif choix == "1":
            convertir_longueur()
        elif choix == "2":
            convertir_poids()
        elif choix == "3":
            # Température (réutilise l'exercice du chapitre)
            celsius = float(input("Température en Celsius: "))
            fahrenheit = celsius * 9/5 + 32
            print(f"{celsius}°C = {fahrenheit:.1f}°F")
        elif choix == "4":
            euros = float(input("Montant en euros: "))
            dollars = euros * 1.10
            print(f"{euros:.2f} EUR = {dollars:.2f} USD")
        else:
            print("Choix invalide!")


if __name__ == "__main__":
    menu_principal()
