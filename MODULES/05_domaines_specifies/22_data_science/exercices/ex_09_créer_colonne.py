"""
Exercice 22.9 - CRÉER COLONNE
=============================


"""


def run():
    """Fonction principale de l'exercice."""
    """Créer de nouvelles colonnes."""
    df = pd.DataFrame({
        "produit": ["A", "B", "C"],
        "prix": [100, 200, 150],
        "quantite": [2, 1, 3]
    })

    # Nouvelle colonne
    df["total"] = df["prix"] * df["quantite"]
    df["taxe"] = df["total"] * 0.2
    df["avec_taxe"] = df["total"] + df["taxe"]

    print(f"Avec calculs:\n{df}")


# Pour tests manuels
if __name__ == "__main__":
    run()
