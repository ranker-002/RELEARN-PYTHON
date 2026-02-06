# =============================================================================
# CHAPITRE 22: DATA SCIENCE I - EXERCICES
# =============================================================================

import numpy as np
import pandas as pd
from scipy import stats


# =============================================================================
# EXERCICE 22.1 - NUMPY BASIQUE
# =============================================================================
def exercice_22_1():
    """Créer et manipuler des arrays NumPy."""
    # Créer un array de 0 à 9
    arr = np.arange(10)
    print(f"Array: {arr}")
    
    # Opérations
    print(f"x2: {arr * 2}")
    print(f"Carré: {arr ** 2}")
    print(f"Somme: {arr.sum()}")
    print(f"Moyenne: {arr.mean()}")


# =============================================================================
# EXERCICE 22.2 - TABLEAUX 2D
# =============================================================================
def exercice_22_2():
    """Travailler avec des matrices 2D."""
    # Créer une matrice 3x3
    matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Matrice:\n{matrice}")
    
    # Accès aux éléments
    print(f"Élément [1,1]: {matrice[1, 1]}")
    print(f"Deuxième ligne: {matrice[1, :]}")
    print(f"Première colonne: {matrice[:, 0]}")
    
    # Opérations
    print(f"Somme: {matrice.sum()}")
    print(f" Somme par colonne: {matrice.sum(axis=0)}")


# =============================================================================
# EXERCICE 22.3 - PANDAS DATAFRAME
# =============================================================================
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


# =============================================================================
# EXERCICE 22.4 - SÉLECTION ET FILTRE
# =============================================================================
def exercice_22_4():
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


# =============================================================================
# EXERCICE 22.5 - STATISTIQUES
# =============================================================================
def exercice_22_5():
    """Calculer des statistiques."""
    donnees = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
    
    print(f"Moyenne: {np.mean(donnees)}")
    print(f"Médiane: {np.median(donnees)}")
    print(f"Variance: {np.var(donnees)}")
    print(f"Écart-type: {np.std(donnees)}")
    print(f"Min: {np.min(donnees)}")
    print(f"Max: {np.max(donnees)}")


# =============================================================================
# EXERCICE 22.6 - GROUP BY
# =============================================================================
def exercice_22_6():
    """Utiliser groupby pour agréger."""
    df = pd.DataFrame({
        "categorie": ["A", "A", "B", "B", "C", "C"],
        "valeur": [10, 20, 15, 25, 30, 40]
    })
    
    # Grouper et sommer
    print("Somme par catégorie:")
    print(df.groupby("categorie")["valeur"].sum())
    
    # Plusieurs agrégations
    print("\nStats par catégorie:")
    print(df.groupby("categorie").agg(["sum", "mean", "count"]))


# =============================================================================
# EXERCICE 22.7 - TRI ET RANG
# =============================================================================
def exercice_22_7():
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


# =============================================================================
# EXERCICE 22.8 - VALEURS MANQUANTES
# =============================================================================
def exercice_22_8():
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


# =============================================================================
# EXERCICE 22.9 - CRÉER COLONNE
# =============================================================================
def exercice_22_9():
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


# =============================================================================
# EXERCICE 22.10 - ENUMÉRER
# =============================================================================
def exercice_22_10():
    """Compter et énumérer les valeurs."""
    df = pd.DataFrame({
        "categorie": ["A", "B", "A", "C", "B", "A"]
    })
    
    # Compter
    print("Comptage:")
    print(df["categorie"].value_counts())
    
    # Pourcentages
    print("\nPourcentages:")
    print(df["categorie"].value_counts(normalize=True).round(2))


# =============================================================================
# EXERCICE 22.11 - PIVOT TABLE
# =============================================================================
def exercice_22_11():
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


# =============================================================================
# EXERCICE 22.12 - CONCATÉNATION
# =============================================================================
def exercice_22_12():
    """Concaténer des DataFrames."""
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
    
    # Concaténer
    df_concat = pd.concat([df1, df2], ignore_index=True)
    print(f"Concaténé:\n{df_concat}")


# =============================================================================
# EXERCICE 22.13 - FUSION
# =============================================================================
def exercice_22_13():
    """Fusionner des DataFrames."""
    df1 = pd.DataFrame({"key": ["A", "B", "C"], "val1": [10, 20, 30]})
    df2 = pd.DataFrame({"key": ["A", "B", "D"], "val2": [100, 200, 400]})
    
    # Fusion
    merged = pd.merge(df1, df2, on="key", how="left")
    print(f"Fusion left:\n{merged}")


# =============================================================================
# EXERCICE 22.14 - TEST STATISTIQUE
# =============================================================================
def exercice_22_14():
    """Faire un test statistique."""
    np.random.seed(42)
    echantillon1 = np.random.normal(100, 10, 50)
    echantillon2 = np.random.normal(105, 10, 50)
    
    # Test t
    t_stat, p_value = stats.ttest_ind(echantillon1, echantillon2)
    
    print(f"Échantillon 1: {np.mean(echantillon1):.2f}")
    print(f"Échantillon 2: {np.mean(echantillon2):.2f}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significatif: {'Oui' if p_value < 0.05 else 'Non'}")


# =============================================================================
# EXERCICE 22.15 - ANALYSE COMPLETE
# =============================================================================
def exercice_22_15():
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


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 22: DATA SCIENCE I")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Exercice 22.{i} ---")
        try:
            eval(f"exercice_22_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
