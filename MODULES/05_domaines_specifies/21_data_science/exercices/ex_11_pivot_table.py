"""
Exercice 22.11 - PIVOT TABLE
============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer des tableaux croisés dynamiques."""
    df = pd.DataFrame({
        "region": ["N", "N", "S", "S", "E", "E"],
        "produit": ["X", "Y", "X", "Y", "X", "Y"],
        "ventes": [100, 150, 200, 120, 180, 90]
    })

    # Pivot
    pivot = df.pivot_table(
        values="ventes",
        index="region",
        columns="produit",
        aggfunc="sum"
    )
    print(f"Pivot table:\n{pivot}")


# Pour tests manuels
if __name__ == "__main__":
    run()
