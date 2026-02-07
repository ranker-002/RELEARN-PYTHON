"""
Exercice 19.11 - GENERIC
========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser Generic pour types génériques."""
    # Crée une pile d'entiers et une pile de textes

    pile_entiers: Pile[int] = Pile()
    pile_entiers.push(1)
    pile_entiers.push(2)
    pile_entiers.push(3)

    print(f"Élément.poppé: {pile_entiers.pop()}")


# Pour tests manuels
if __name__ == "__main__":
    run()
