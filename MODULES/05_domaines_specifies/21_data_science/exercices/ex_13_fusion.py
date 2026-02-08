"""
Exercice 22.13 - FUSION
=======================


"""


def run():
    """Fonction principale de l'exercice."""
    """Fusionner des DataFrames."""
    df1 = pd.DataFrame({"key": ["A", "B", "C"], "val1": [10, 20, 30]})
    df2 = pd.DataFrame({"key": ["A", "B", "D"], "val2": [100, 200, 400]})

    # Fusion
    merged = pd.merge(df1, df2, on="key", how="left")
    print(f"Fusion left:\n{merged}")


# Pour tests manuels
if __name__ == "__main__":
    run()
