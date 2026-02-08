"""
Exercice 22.12 - CONCATÉNATION
==============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Concaténer des DataFrames."""
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

    # Concaténer
    df_concat = pd.concat([df1, df2], ignore_index=True)
    print(f"Concaténé:\n{df_concat}")


# Pour tests manuels
if __name__ == "__main__":
    run()
