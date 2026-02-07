"""
Exercice 22.8 - VALEURS MANQUANTES
==================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Gérer les valeurs manquantes."""
    df = pd.DataFrame({
        "A": [1, 2, None, 4],
        "B": [5, None, 7, 8],
        "C": [9, 10, 11, None]
    })

    print(f"Original:\n{df}")
    print(f"\nValeurs manquantes:\n{df.isnull()}")

    # Remplir avec la moyenne
    df_filled = df.fillna(df.mean())
    print(f"\nRemplacé par moyenne:\n{df_filled}")


# Pour tests manuels
if __name__ == "__main__":
    run()
