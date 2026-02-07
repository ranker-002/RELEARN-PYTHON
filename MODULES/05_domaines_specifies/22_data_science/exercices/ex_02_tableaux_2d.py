"""
Exercice 22.2 - TABLEAUX 2D
===========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Travailler avec des matrices 2D."""
    # Créer une matrice 3x3
    matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Matrice:\n{matrice}")

    # Accès aux éléments
    print(f"Élément [1,1]: {matrice[1, 1]}")
    print(f"Deuxième ligne: {matrice[1, :]}")
    print(f"Première colonne: {matrice[:, 0]}")

    # Opérations
    print(f"Somme: {matrice.sum()}")
    print(f" Somme par colonne: {matrice.sum(axis=0)}")


# Pour tests manuels
if __name__ == "__main__":
    run()
