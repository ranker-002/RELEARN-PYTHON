# Chapitre 21 : Data Science I

## Qu'est-ce que la Data Science ?

Imaginez que vous ayez accès à des millions de transactions commerciales, de messages sur les réseaux sociaux, de données météorologiques... Comment trouver des patterns intéressants ? Comment prédire ce qui va se passer demain ?

**La Data Science**, c'est exactement ça : extraire de la connaissance et des insights à partir de données. C'est un mélange de statistiques, de programmation, et de compréhension du domaine concerné.

Python est le langage roi de la Data Science grâce à des bibliothèques puissantes et simples à utiliser.

---

## NumPy : Les Calculs Numériques

NumPy est le fondement de tout l'écosystème data en Python. Il offre des tableaux (arrays) multidimensionnels et des fonctions mathématiques ultra-rapides.

```python
import numpy as np

# Créer un array depuis une liste
nombres = np.array([1, 2, 3, 4, 5])
print(nombres)

# Créer des arrays spéciaux
zeros = np.zeros(5)           # [0, 0, 0, 0, 0]
ones = np.ones(5)             # [1, 1, 1, 1, 1]
range_ = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# Opérations vectorisées (super rapides !)
print(nombres * 2)      # [2, 4, 6, 8, 10]
print(nombres + 1)      # [2, 3, 4, 5, 6]
print(nombres ** 2)     # [1, 4, 9, 16, 25]

# Tableaux 2D
matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrice.shape)     # (3, 3)

# Accéder aux éléments
print(matrice[0, 0])    # 1
print(matrice[1, :])    # [4, 5, 6]
print(matrice[:, 2])    # [3, 6, 9]

# Opérations matricielles
print(matrice.sum())        # 45
print(matrice.mean())       # 5.0
print(matrice.std())        # 2.58...
print(matrice.sum(axis=0))  # Somme par colonne: [12, 15, 18]
```

---

## Pandas : La Manipulation de Données

Pandas est construit sur NumPy et offre des structures de données comme les **DataFrames** (tableaux类似Excel) pour manipuler facilement des données tabulaires.

```python
import pandas as pd

# Créer un DataFrame depuis un dictionnaire
data = {
    "nom": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "ville": ["Paris", "Lyon", "Marseille", "Lille"],
    "salaire": [50000, 60000, 75000, 52000]
}

df = pd.DataFrame(data)
print(df)

# Afficher les premières lignes
print(df.head())      # 5 premières (par défaut)
print(df.head(2))     # 2 premières

# Informations sur le DataFrame
print(df.info())       # Types, valeurs non-null
print(df.describe())   # Stats: count, mean, std, min, max...

# Sélectionner des colonnes
print(df["nom"])           # Une colonne (Series)
print(df[["nom", "salaire"]])  # Plusieurs colonnes

# Filtrer les lignes
df_jeunes = df[df["age"] < 30]
print(df_jeunes)

# Conditions multiples
df_riches = df[(df["salaire"] > 55000) & (df["age"] > 25)]
print(df_riches)

# Trier
df_trie = df.sort_values("salaire", ascending=False)
print(df_trie)

# Ajouter une colonne
df["salaire_annuel"] = df["salaire"] * 12
print(df)

# Valeurs uniques
print(df["ville"].unique())       # ['Paris' 'Lyon' 'Marseille' 'Lille']
print(df["ville"].nunique())      # 4

# Compter les occurrences
print(df["ville"].value_counts())
```

### Travailler avec des Fichiers

```python
import pandas as pd

# Lire un fichier CSV
df = pd.read_csv("donnees.csv")

# Lire Excel
df = pd.read_excel("donnees.xlsx")

# Lire JSON
df = pd.read_json("donnees.json")

# Sauvegarder
df.to_csv("resultat.csv", index=False)     # Sans l'index
df.to_excel("resultat.xlsx", index=False)   # Sans l'index
df.to_json("resultat.json")                 # En JSON
```

### Nettoyage de Données

```python
import pandas as pd
import numpy as np

# Créer un DataFrame avec des valeurs manquantes
data = {
    "nom": ["Alice", "Bob", "Charlie", None],
    "age": [25, None, 35, 28],
    "ville": ["Paris", "Lyon", None, "Lille"],
}

df = pd.DataFrame(data)
print(df)

# Vérifier les valeurs manquantes
print(df.isnull())           # True/False
print(df.isnull().sum())     # Par colonne

# Supprimer les lignes avec des valeurs manquantes
df_clean = df.dropna()
print(df_clean)

# Remplir les valeurs manquantes
df["age"].fillna(df["age"].mean(), inplace=True)
df["ville"].fillna("Inconnue", inplace=True)
print(df)

# Supprimer les doublons
df = df.drop_duplicates()
```

### Agrégations et Group By

```python
import pandas as pd

data = {
    "produit": ["A", "A", "B", "B", "C"],
    "ventes": [100, 150, 200, 180, 90],
    "region": ["Nord", "Sud", "Nord", "Est", "Sud"]
}

df = pd.DataFrame(data)

# Grouper par produit et sommer
print(df.groupby("produit")["ventes"].sum())

# Plusieurs agrégations
print(df.groupby("produit").agg({
    "ventes": ["sum", "mean", "max"],
    "region": "count"
}))

# Grouper par plusieurs colonnes
print(df.groupby(["produit", "region"])["ventes"].sum())
```

---

## SciPy : Statistiques Avancées

```python
from scipy import stats
import numpy as np

# Créer des données
donnees = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 30])

# Statistiques descriptives
moyenne = np.mean(donnees)
mediane = np.median(donnees)
variance = np.var(donnees)
ecart_type = np.std(donnees)

print(f"Moyenne: {moyenne}")
print(f"Médiane: {mediane}")
print(f"Écart-type: {ecart_type}")

# Tests statistiques
# Test t (comparer deux échantillons)
echantillon1 = np.random.normal(100, 10, 100)
echantillon2 = np.random.normal(105, 10, 100)

t_stat, p_value = stats.ttest_ind(echantillon1, echantillon2)
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.3f}")

# Corrélation
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
correlation, p_val = stats.pearsonr(x, y)
print(f"Corrélation: {correlation:.3f}")
```

---

## Exemple Complet : Analyse de Données de Ventes

```python
import pandas as pd
import numpy as np

# Simuler des données de ventes
np.random.seed(42)
n = 1000

data = {
    "date": pd.date_range("2023-01-01", periods=n, freq="D"),
    "produit": np.random.choice(["A", "B", "C", "D"], n),
    "quantite": np.random.randint(1, 20, n),
    "prix_unitaire": np.random.uniform(10, 100, n),
    "region": np.random.choice(["Nord", "Sud", "Est", " Ouest"], n),
}

df = pd.DataFrame(data)

# Calculer le chiffre d'affaires
df["ca"] = df["quantite"] * df["prix_unitaire"]

# 1. Chiffre d'affaires total
print(f"CA Total: {df['ca'].sum():,.2f}€")

# 2. CA par produit
print("\nCA par produit:")
print(df.groupby("produit")["ca"].sum().sort_values(ascending=False))

# 3. CA par région
print("\nCA par région:")
print(df.groupby("region")["ca"].sum())

# 4. Top 10 des jours avec le plus de ventes
print("\nTop 10 jours:")
print(df.sort_values("ca", ascending=False).head(10)[["date", "produit", "ca"]])

# 5. Statistiques par produit
print("\nStats par produit:")
stats_par_produit = df.groupby("produit").agg({
    "ca": ["sum", "mean", "count"],
    "quantite": "mean",
    "prix_unitaire": "mean"
})
print(stats_par_produit)

# 6. Tendance temporelle (moyenne mobile)
df["ca_moving_avg"] = df["ca"].rolling(window=7).mean()
print("\nTendance (7 derniers jours):")
print(df[["date", "ca", "ca_moving_avg"]].tail(10))
```

---

## Résumé

| Bibliothèque | Usage Principal |
|--------------|-----------------|
| `numpy` | Calculs numériques, tableaux multidimensionnels |
| `pandas` | Manipulation de données tabulaires (DataFrames) |
| `scipy` | Statistiques avancées, tests scientifiques |

---

## Erreurs Courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| `KeyError` | Colonne inexistante | Vérifier les noms de colonnes |
| `ValueError` | Type incompatible | Convertir avec `.astype()` |
| `IndexError` | Index hors plage | Vérifier les dimensions |
| `SettingWithCopyWarning` | Modification sur une copie | Utiliser `.copy()` |

---

## Exercices Pratiques

1. **Importer et explorer** : Charger un CSV et afficher les stats de base

2. **Nettoyer un dataset** : Gérer les valeurs manquantes et doublons

3. **Analyse de ventes** : Calculer CA, moyennes, par produit/région

4. **Visualisation simple** : Créer des graphiques avec les données

5. **Test statistique** : Comparer deux échantillons avec un test t

---

## Chapitre Suivant

Vos données sont maintenant analysées ! Passons au [Chapitre 22: Visualisation](22_visualisation/README.md) pour apprendre à les représenter graphiquement.
