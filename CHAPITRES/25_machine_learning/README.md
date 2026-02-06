# Chapitre 25 : Machine Learning avec Scikit-learn

## Introduction : Qu'est-ce que le Machine Learning ?

Le **Machine Learning** (apprentissage automatique) permet aux ordinateurs d'apprendre à partir de données sans être explicitement programmés. Au lieu d'écrire des règles manuelles, nous donnons des exemples au modèle et il découvre les patterns.

Applications concrètes :
- Prédire le prix d'une maison
- Détecter des spams
- Recommander des produits
- Reconnaître des images

---

## 1. Installation

```bash
uv sync --extra data
```

```python
import sklearn
print(sklearn.__version__)
```

---

## 2. Les Types d'Apprentissage

### Apprentissage Supervisé

Données étiquetées → Le modèle apprend la relation entre entrées et sorties.

```python
# Classification: prédire une catégorie
# Exemple: spam ou non-spam ?

# Régression: prédire une valeur continue
# Exemple: prix d'une maison
```

### Apprentissage Non Supervisé

Données non étiquetées → Le modèle trouve des structures cachées.

```python
# Clustering: grouper des similaires
# Exemple: segmentation de clients
```

---

## 3. Régression Linéaire

### Concept

Trouver la droite qui minimise l'erreur entre prédictions et valeurs réelles.

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Données d'entraînement
X = np.array([[1], [2], [3], [4], [5]])  # Surface (m²)
y = np.array([150000, 180000, 210000, 240000, 270000])  # Prix (€)

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# Prédire
surface = np.array([[6]])  # Maison de 6 m²
prix = model.predict(surface)
print(f"Prix prédit: {prix[0]:,.0f} €")

# Coefficients
print(f"Prix au m²: {model.coef_[0]:,.0f} €")
print(f"Prix de base: {model.intercept_:,.0f} €")
```

### Évaluation du Modèle

```python
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f"RMSE: {rmse:,.0f} €")
print(f"R² Score: {r2:.3f}")
```

---

## 4. Régression Multiple

Plusieurs variables prédictives.

```python
from sklearn.linear_model import LinearRegression
import pandas as pd

# Données avec plusieurs features
df = pd.DataFrame({
    'surface': [50, 60, 70, 80, 90, 100],
    'chambres': [2, 2, 3, 3, 4, 4],
    'age': [10, 5, 15, 8, 2, 1],
    'prix': [150000, 180000, 200000, 240000, 280000, 310000]
})

X = df[['surface', 'chambres', 'age']]
y = df['prix']

model = LinearRegression()
model.fit(X, y)

print("Impact des features:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: {coef:,.0f} €")
```

---

## 5. Classification

### Régression Logistique

Pour prédire des catégories (2 classes).

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Générer des données
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0,
                           n_informative=2, random_state=42)

# Diviser en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Créer et entraîner
model = LogisticRegression()
model.fit(X_train, y_train)

# Évaluer
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision: {accuracy:.2%}")
print(classification_report(y_test, y_pred))
```

---

## 6. K-Nearest Neighbors (KNN)

Classifier selon les voisins les plus proches.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Dataset Iris (fleurs)
iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# KNN avec k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Prédire une nouvelle fleur
nouvelle_fleur = [[5.1, 3.5, 1.4, 0.2]]  # Longueur/largeur sépales et pétales
espece = knn.predict(nouvelle_fleur)
print(f"Espèce prédite: {iris.target_names[espece[0]]}")
```

---

## 7. Arbres de Décision

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Créer l'arbre
arbre = DecisionTreeClassifier(max_depth=3)  # Limiter la profondeur
arbre.fit(X_train, y_train)

# Évaluer
print(f"Précision: {arbre.score(X_test, y_test):.2%}")

# Visualiser l'importance des features
for feature, importance in zip(iris.feature_names, arbre.feature_importances_):
    if importance > 0:
        print(f"{feature}: {importance:.3f}")
```

---

## 8. Random Forest

Ensemble d'arbres pour de meilleures performances.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

print(f"Précision: {rf.score(X_test, y_test):.2%}")

# Feature importance
importances = dict(zip(cancer.feature_names, rf.feature_importances_))
top_5 = sorted(importances.items(), key=lambda x: x[1], reverse=True)[:5]
print("\nTop 5 features:")
for feature, importance in top_5:
    print(f"  {feature}: {importance:.3f}")
```

---

## 9. K-Means Clustering

Regrouper des données sans labels.

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Générer des données
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

# K-Means avec 4 clusters
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Prédire les clusters
labels = kmeans.predict(X)
centers = kmeans.cluster_centers_

# Visualiser
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X')
plt.title('K-Means Clustering')
plt.show()
```

---

## 10. Validation Croisée

Évaluer la robustesse du modèle.

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

rf = RandomForestClassifier(n_estimators=100)

# Validation croisée 5-fold
scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')

print(f"Précisions par fold: {scores}")
print(f"Précision moyenne: {scores.mean():.2%} ± {scores.std():.2%}")
```

---

## 11. Prétraitement des Données

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

# Standardisation (moyenne=0, std=1)
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Normalisation (0-1)
normalizer = MinMaxScaler()
X_normalized = normalizer.fit_transform(X)

print("Données originales - Moyenne:", X.mean(axis=0))
print("Données standardisées - Moyenne:", X_standardized.mean(axis=0))
```

---

## 12. Pipeline

Enchaîner les opérations.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, (iris.target != 0).astype(int)  # Binaire: 0 ou 1

# Pipeline: Standardisation + Classification
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X, y)
print(f"Précision: {pipeline.score(X, y):.2%}")
```

---

## 13. Métriques d'Évaluation

| Métrique | Usage |
|----------|-------|
| Accuracy | Classification équilibrée |
| Precision | Éviter les faux positifs |
| Recall | Éviter les faux négatifs |
| F1-Score | Balance Precision/Recall |
| MSE/RMSE | Régression |
| R² Score | Variance expliquée |

```python
from sklearn.metrics import confusion_matrix, roc_auc_score

# Matrice de confusion
cm = confusion_matrix(y_test, y_pred)
print("Matrice de confusion:")
print(cm)

# ROC-AUC (classification binaire)
y_proba = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_proba)
print(f"ROC-AUC: {roc_auc:.3f}")
```

---

## 14. Erreurs Courantes

### 1. Surapprentissage (Overfitting)

```python
# MAUVAIS - Arbre trop profond
arbre = DecisionTreeClassifier(depth=None)  # Pas de limite

# CORRECT - Limiter la profondeur
arbre = DecisionTreeClassifier(max_depth=5)
```

### 2. Données non divisées

```python
# MAUVAIS - Évaluer sur les mêmes données d'entraînement
model.fit(X, y)
print(model.score(X, y))  # Trop optimiste!

# CORRECT - Diviser en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
```

---

## 15. Projet Complet: Prédiction de Diabète

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_diabetes

# Charger les données (classification binaire simplifiée)
diabetes = load_diabetes()
X, y = diabetes.data, (diabetes.target > 140).astype(int)  # Diabète ou non

# Diviser
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluer
y_pred = model.predict(X_test)
print(f"Précision: {accuracy_score(y_test, y_pred):.2%}")
print("\nRapport:")
print(classification_report(y_test, y_pred, target_names=['Non diabétique', 'Diabétique']))

# Importance des features
print("\nFacteurs de risque principaux:")
for feature, importance in sorted(zip(diabetes.feature_names, model.feature_importances_),
                                  key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {feature}: {importance:.3f}")
```

---

## Résumé

| Algorithme | Type | Usage |
|------------|------|-------|
| LinearRegression | Régression | Prédire des valeurs continues |
| LogisticRegression | Classification | 2 classes |
| KNN | Classification/Régression | Petit dataset |
| DecisionTree | Classification/Régression | Interprétable |
| RandomForest | Classification/Régression | Robuste, performant |
| K-Means | Clustering | Segmentation |

---

## Prochain Chapitre

Tu as maintenant les bases du Machine Learning ! Passons au **chapitre 26 : Deep Learning** avec PyTorch pour créer des réseaux de neurones.

---

*Félicitations ! Tu peux maintenant créer des modèles prédictifs! 🤖*
