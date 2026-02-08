"""
Exercice 22.15 - ANALYSE COMPLETE
=================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Analyse complète de données de ventes."""
    np.random.seed(42)

    # Créer des données
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=100, freq="D"),
        "produit": np.random.choice(["P1", "P2", "P3"], 100),
        "region": np.random.choice(["N", "S", "E", "O"], 100),
        "quantite": np.random.randint(1, 50, 100),
        "prix": np.random.uniform(10, 100, 100)
    })

    # CA
    df["ca"] = df["quantite"] * df["prix"]

    # CA total
    print(f"CA Total: {df['ca'].sum():,.2f}€")

    # CA par produit
    print("\nCA par produit:")
    print(df.groupby("produit")["ca"].sum().sort_values(ascending=False))

    # CA par région
    print("\nCA par région:")
    print(df.groupby("region")["ca"].sum())

    # Top 5 jours
    print("\nTop 5 jours:")
    print(df.sort_values("ca", ascending=False).head()[["date", "produit", "ca"]])


# Pour tests manuels
if __name__ == "__main__":
    run()
