"""
Exercice 19.15 - MODULE COMPLET
===============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Système d'inventaire avec types complets."""
    inv = Inventaire()

    inv.ajouter_produit("Ordinateur", 1000, 5)
    inv.ajouter_produit("Souris", 25, 10)
    inv.ajouter_produit("Clavier", 50, 8)

    print(f"Valeur totale: {inv.valeur_inventaire()}€")

    resultat = inv.rechercher("Souris")
    if resultat:
        print(f"Souris: {resultat.quantite} en stock")


# Pour tests manuels
if __name__ == "__main__":
    run()
