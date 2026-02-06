"""
Calculatrice CLI - Starter Code

Commencez ici et complétez les fonctions manquantes.
"""


def addition(a: float, b: float) -> float:
    """Additionne deux nombres."""
    pass


def soustraction(a: float, b: float) -> float:
    """Soustrait b de a."""
    pass


def multiplication(a: float, b: float) -> float:
    """Multiplie deux nombres."""
    pass


def division(a: float, b: float) -> float:
    """Divise a par b. Gère la division par zéro."""
    pass


def afficher_menu() -> None:
    """Affiche le menu des opérations."""
    print("\n=== CALCULATRICE CLI ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter\n")


def obtenir_nombre(invite: str) -> float:
    """
    Demande un nombre à l'utilisateur.
    Réessaie jusqu'à ce qu'un nombre valide soit entré.
    """
    while True:
        try:
            return float(input(invite))
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide.")


def main() -> None:
    """Point d'entrée de l'application."""
    while True:
        afficher_menu()
        choix = input("Votre choix: ")

        if choix == "5":
            print("Au revoir!")
            break

        if choix not in ["1", "2", "3", "4"]:
            print("Choix invalide. Veuillez réessayer.")
            continue

        a = obtenir_nombre("Entrez le premier nombre: ")
        b = obtenir_nombre("Entrez le deuxième nombre: ")

        if choix == "1":
            resultat = addition(a, b)
            print(f"Résultat: {a} + {b} = {resultat}")
        elif choix == "2":
            resultat = soustraction(a, b)
            print(f"Résultat: {a} - {b} = {resultat}")
        elif choix == "3":
            resultat = multiplication(a, b)
            print(f"Résultat: {a} * {b} = {resultat}")
        elif choix == "4":
            try:
                resultat = division(a, b)
                print(f"Résultat: {a} / {b} = {resultat}")
            except ZeroDivisionError:
                print("Erreur: Division par zéro impossible!")


if __name__ == "__main__":
    main()
