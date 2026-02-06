# =============================================================================
# CHAPITRE 22: DATA SCIENCE I - SOLUTIONS
# =============================================================================

import numpy as np
import pandas as pd
from scipy import stats


def exercice_22_1():
    """Créer et manipuler des arrays NumPy."""
    arr = np.arange(10)
    print(f"Array: {arr}")
    
    print(f"x2: {arr * 2}")
    print(f"Carré: {arr ** 2}")
    print(f"Somme: {arr.sum()}")
    print(f"Moyenne: {arr.mean()}")


def exercice_22_2():
    """Travailler avec des matrices 2D."""
    matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Matrice:\n{matrice}")
    
    print(f"Élément [1,1]: {matrice[1, 1]}")
    print(f"Deuxième ligne: {matrice[1, :]}")
    print(f"Première colonne: {matrice[:, 0]}")
    
    print(f"Somme: {matrice.sum()}")
    print(f"Somme par colonne: {matrice.sum(axis=0)}")


def exercice_22_3():
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


def exercice_22_4():
    """Sélectionner et filtrer des données."""
    df = pd.DataFrame({
        "nom": ["A", "B", "C", "D", "E"],
        "age": [20, 25, 30, 35, 40],
        "salaire": [30000, 40000, 50000, 60000, 70000]
    })
    
    print(f"Noms: {df['nom'].tolist()}")
    
    df_jeunes = df[df["age"] < 32]
    print(f"\nMoins de 32 ans:\n{df_jeunes}")


def exercice_22_5():
    """Calculer des statistiques."""
    donnees = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
    
    print(f"Moyenne: {np.mean(donnees)}")
    print(f"Médiane: {np.median(donnees)}")
    print(f"Variance: {np.var(donnees)}")
    print(f"Écart-type: {np.std(donnees)}")
    print(f"Min: {np.min(donnees)}")
    print(f"Max: {np.max(donnees)}")


def exercice_22_6():
    """Utiliser groupby pour agréger."""
    df = pd.DataFrame({
        "categorie": ["A", "A", "B", "B", "C", "C"],
        "valeur": [10, 20, 15, 25, 30, 40]
    })
    
    print("Somme par catégorie:")
    print(df.groupby("categorie")["valeur"].sum())
    
    print("\nStats par catégorie:")
    print(df.groupby("categorie").agg(["sum", "mean", "count"]))


def exercice_22_7():
    """Trier et ajouter des rangs."""
    df = pd.DataFrame({
        "nom": ["Bob", "Alice", "Charlie", "Diana"],
        "score": [85, 92, 78, 95]
    })
    
    df_trie = df.sort_values("score", ascending=False)
    print(f"Trié par score:\n{df_trie}")
    
    df["rang"] = df["score"].rank(ascending=False)
    print(f"\nAvec rang:\n{df}")


def exercice_22_8():
    """Gérer les valeurs manquantes."""
    df = pd.DataFrame({
        "A": [1, 2, None, 4],
        "B": [5, None, 7, 8],
        "C": [9, 10, 11, None]
    })
    
    print(f"Original:\n{df}")
    print(f"\nValeurs manquantes:\n{df.isnull()}")
    
    df_filled = df.fillna(df.mean())
    print(f"\nRemplacé par moyenne:\n{df_filled}")


def exercice_22_9():
    """Créer de nouvelles colonnes."""
    df = pd.DataFrame({
        "produit": ["A", "B", "C"],
        "prix": [100, 200, 150],
        "quantite": [2, 1, 3]
    })
    
    df["total"] = df["prix"] * df["quantite"]
    df["taxe"] = df["total"] * 0.2
    df["avec_taxe"] = df["total"] + df["taxe"]
    
    print(f"Avec calculs:\n{df}")


def exercice_22_10():
    """Compter et énumérer les valeurs."""
    df = pd.DataFrame({
        "categorie": ["A", "B", "A", "C", "B", "A"]
    })
    
    print("Comptage:")
    print(df["categorie"].value_counts())
    
    print("\nPourcentages:")
    print(df["categorie"].value_counts(normalize=True).round(2))


def exercice_22_11():
    """Créer des tableaux croisés dynamiques."""
    df = pd.DataFrame({
        "region": ["N", "N", "S", "S", "E", "E"],
        "produit": ["X", "Y", "X", "Y", "X", "Y"],
        "ventes": [100, 150, 200, 120, 180, 90]
    })
    
    pivot = df.pivot_table(
        values="ventes",
        index="region",
        columns="produit",
        aggfunc="sum"
    )
    print(f"Pivot table:\n{pivot}")


def exercice_22_12():
    """Concaténer des DataFrames."""
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
    
    df_concat = pd.concat([df1, df2], ignore_index=True)
    print(f"Concaténé:\n{df_concat}")


def exercice_22_13():
    """Fusionner des DataFrames."""
    df1 = pd.DataFrame({"key": ["A", "B", "C"], "val1": [10, 20, 30]})
    df2 = pd.DataFrame({"key": ["A", "B", "D"], "val2": [100, 200, 400]})
    
    merged = pd.merge(df1, df2, on="key", how="left")
    print(f"Fusion left:\n{merged}")


def exercice_22_14():
    """Faire un test statistique."""
    np.random.seed(42)
    echantillon1 = np.random.normal(100, 10, 50)
    echantillon2 = np.random.normal(105, 10, 50)
    
    t_stat, p_value = stats.ttest_ind(echantillon1, echantillon2)
    
    print(f"Échantillon 1: {np.mean(echantillon1):.2f}")
    print(f"Échantillon 2: {np.mean(echantillon2):.2f}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significatif: {'Oui' if p_value < 0.05 else 'Non'}")


def exercice_22_15():
    """Analyse complète de données de ventes."""
    np.random.seed(42)
    
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=100, freq="D"),
        "produit": np.random.choice(["P1", "P2", "P3"], 100),
        "region": np.random.choice(["N", "S", "E", "O"], 100),
        "quantite": np.random.randint(1, 50, 100),
        "prix": np.random.uniform(10, 100, 100)
    })
    
    df["ca"] = df["quantite"] * df["prix"]
    
    print(f"CA Total: {df['ca'].sum():,.2f}€")
    
    print("\nCA par produit:")
    print(df.groupby("produit")["ca"].sum().sort_values(ascending=False))
    
    print("\nCA par région:")
    print(df.groupby("region")["ca"].sum())
    
    print("\nTop 5 jours:")
    print(df.sort_values("ca", ascending=False).head()[["date", "produit", "ca"]])


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 22: DATA SCIENCE I - SOLUTIONS")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Solution 22.{i} ---")
        try:
            eval(f"exercice_22_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
