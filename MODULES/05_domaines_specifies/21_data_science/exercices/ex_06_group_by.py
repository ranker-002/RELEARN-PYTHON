"""
Exercice 22.6 - GROUP BY
========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Utiliser groupby pour agréger."""
    df = pd.DataFrame({
        "categorie": ["A", "A", "B", "B", "C", "C"],
        "valeur": [10, 20, 15, 25, 30, 40]
    })

    # Grouper et sommer
    print("Somme par catégorie:")
    print(df.groupby("categorie")["valeur"].sum())

    # Plusieurs agrégations
    print("\nStats par catégorie:")
    print(df.groupby("categorie").agg(["sum", "mean", "count"]))


# Pour tests manuels
if __name__ == "__main__":
    run()
