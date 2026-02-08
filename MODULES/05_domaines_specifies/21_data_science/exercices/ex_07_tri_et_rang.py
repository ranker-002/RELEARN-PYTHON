"""
Exercice 22.7 - TRI ET RANG
===========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Trier et ajouter des rangs."""
    df = pd.DataFrame({
        "nom": ["Bob", "Alice", "Charlie", "Diana"],
        "score": [85, 92, 78, 95]
    })

    df_trie = df.sort_values("score", ascending=False)
    print("Trié par score:")
    print(df_trie)

    df["rang"] = df["score"].rank(ascending=False)
    print("\nAvec rang:")
    print(df)


# Pour tests manuels
if __name__ == "__main__":
    run()
