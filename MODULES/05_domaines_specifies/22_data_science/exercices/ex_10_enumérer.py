"""
Exercice 22.10 - ENUMÉRER
=========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Compter et énumérer les valeurs."""
    df = pd.DataFrame({
        "categorie": ["A", "B", "A", "C", "B", "A"]
    })

    # Compter
    print("Comptage:")
    print(df["categorie"].value_counts())

    # Pourcentages
    print("\nPourcentages:")
    print(df["categorie"].value_counts(normalize=True).round(2))


# Pour tests manuels
if __name__ == "__main__":
    run()
