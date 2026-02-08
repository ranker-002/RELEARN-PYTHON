"""
Exercice 22.3 - PANDAS DATAFRAME
================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer et explorer un DataFrame."""
    data = {
        "nom": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, 30, 35, 28],
        "ville": ["Paris", "Lyon", "Marseille", "Lille"],
    }

    df = pd.DataFrame(data)
    print(f"DataFrame:\n{df}")
    print(f"\nShape: {df.shape}")
    print(f"\nColonnes: {list(df.columns)}")


# Pour tests manuels
if __name__ == "__main__":
    run()
