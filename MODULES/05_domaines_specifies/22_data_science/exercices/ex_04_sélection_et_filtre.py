"""
Exercice 22.4 - SÉLECTION ET FILTRE
===================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Sélectionner et filtrer des données."""
    df = pd.DataFrame({
        "nom": ["A", "B", "C", "D", "E"],
        "age": [20, 25, 30, 35, 40],
        "salaire": [30000, 40000, 50000, 60000, 70000]
    })

    # Colonnes
    print(f"Noms: {df['nom'].tolist()}")

    # Filtre
    df_jeunes = df[df["age"] < 32]
    print(f"\nMoins de 32 ans:\n{df_jeunes}")


# Pour tests manuels
if __name__ == "__main__":
    run()
