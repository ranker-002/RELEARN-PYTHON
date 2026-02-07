"""
Exercice 22.1 - NUMPY BASIQUE
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer et manipuler des arrays NumPy."""
    # Créer un array de 0 à 9
    arr = np.arange(10)
    print(f"Array: {arr}")

    # Opérations
    print(f"x2: {arr * 2}")
    print(f"Carré: {arr ** 2}")
    print(f"Somme: {arr.sum()}")
    print(f"Moyenne: {arr.mean()}")


# Pour tests manuels
if __name__ == "__main__":
    run()
