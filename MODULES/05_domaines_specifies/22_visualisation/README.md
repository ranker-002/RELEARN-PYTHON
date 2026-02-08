# Chapitre 22 : Visualisation de Données avec Matplotlib

## Introduction : Pourquoi Visualiser les Données ?

Imagine que tu aies un fichier Excel avec 10 000 lignes de données de ventes. Comment trouver rapidement les tendances ? Les pics de vente ? Les correlations entre variables ?

La **visualisation de données** transforme les nombres en graphiques comprhensibles en un coup d'œil. C'est comme passer d'une page de texte稠密 à une photo - l'information devient immédiatement accessible.

Les data scientists passent 80% de leur temps à nettoyer et visualiser les données. Matplotlib est la bibliothèque de visualisation la plus utilisée en Python.

---

## 1. Introduction à Matplotlib

### Installation

```bash
uv sync --extra core
```

### Import standard

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

### Figure et Axes

Matplotlib fonctionne avec deux concepts clés :
- **Figure** : le conteneur principal (la fenêtre ou l'image)
- **Axes** : la zone où on dessine le graphique

```python
# Créer une figure et des axes
fig, ax = plt.subplots()

# Dessiner quelque chose
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Afficher
plt.show()
```

---

## 2. Les Types de Graphiques

### Graphique Linéaire (`plot`)

Parfait pour montrer l'évolution d'une valeur dans le temps.

```python
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x, y, label='y = x²', color='blue', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Graphique Linéaire')
ax.legend()
plt.show()
```

### Diagramme en Bâtons (`bar`)

Parfait pour comparer des catégories.

```python
langues = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
popularite = [30, 20, 15, 10, 8]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(langues, popularite, color=['blue', 'yellow', 'red', 'green', 'cyan'])
ax.set_xlabel('Langages')
ax.set_ylabel('Popularité (%)')
ax.set_title('Popularité des Langages de Programmation')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Histogramme (`hist`)

Parfait pour voir la distribution des valeurs.

```python
# Générer des données aléatoires
donnees = np.random.normal(170, 10, 1000)  # Moyenne 170, std 10

fig, ax = plt.subplots()
ax.hist(donnees, bins=30, color='steelblue', edgecolor='white')
ax.set_xlabel('Taille (cm)')
ax.set_ylabel('Fréquence')
ax.set_title('Distribution des Tailles')
plt.show()
```

### Nuage de Points (`scatter`)

Parfait pour voir les correlations entre deux variables.

```python
x = np.random.rand(100) * 100
y = x * 1.5 + np.random.rand(100) * 20  # Corrélation positive

fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5, c='red', s=50)
ax.set_xlabel('Variable X')
ax.set_ylabel('Variable Y')
ax.set_title('Nuage de Points - Corrélation Positive')
plt.show()
```

### Diagramme Circulaire (`pie`)

Parfait pour montrer des proportions.

```python
tailles = [30, 25, 20, 15, 10]
labels = ['Groupe A', 'Groupe B', 'Groupe C', 'Groupe D', 'Groupe E']
couleurs = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

fig, ax = plt.subplots()
ax.pie(tailles, labels=labels, colors=couleurs, autopct='%1.1f%%',
       startangle=90, explode=[0.05]*5)
ax.set_title('Répartition des Groupes')
plt.show()
```

### Graphique en Boîte (`boxplot`)

Parfait pour voir la distribution et les outliers.

```python
donnees = [np.random.normal(100, 10, 200),  # Groupe 1
           np.random.normal(90, 20, 200),     # Groupe 2
           np.random.normal(80, 30, 200)]     # Groupe 3

fig, ax = plt.subplots()
ax.boxplot(donnees, labels=['Groupe A', 'Groupe B', 'Groupe C'])
ax.set_ylabel('Valeurs')
ax.set_title('Distribution par Groupe')
plt.show()
```

---

## 3. Personnalisation Avancée

### Styles et Couleurs

```python
# Différentes styles de ligne
styles = ['-', '--', '-.', ':']
labels = ['Solide', 'Traitillé', 'Point-Tiret', 'Pointillé']

fig, ax = plt.subplots()
for i, (style, label) in enumerate(zip(styles, labels)):
    ax.plot([1, 2, 3, 4], [i+1, i+2, i+3, i+4], linestyle=style, label=label, linewidth=2)
ax.legend()
plt.show()

# Couleurs par nom ou code hexadécimal
ax.plot(x, y, color='#FF5733')  # Orange rouge
ax.plot(x, y, color='rgb(255, 87, 51)')  # RGB
```

### Annotations et Texte

```python
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3], [0, 1, 4, 9])

# Annotation avec flèche
ax.annotate('Maximum', xy=(2, 4), xytext=(1, 6),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=12, color='red')

# Ajouter du texte
ax.text(0.5, 8, 'Croissance exponentielle', fontsize=14, style='italic')
plt.show()
```

### Sous-graphiques (`subplots`)

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Graphique 1
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title('Graphique 1')

# Graphique 2
axes[0, 1].bar(['A', 'B', 'C'], [3, 7, 5])
axes[0, 1].set_title('Graphique 2')

# Graphique 3
axes[1, 0].scatter([1, 2, 3, 4], [4, 1, 9, 16])
axes[1, 0].set_title('Graphique 3')

# Graphique 4
axes[1, 1].hist(np.random.randn(100), bins=20)
axes[1, 1].set_title('Graphique 4')

plt.tight_layout()
plt.show()
```

---

## 4. Visualisation avec Pandas

### Méthodes directes sur DataFrame

```python
# Créer un DataFrame
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=100),
    'ventes': np.random.randint(100, 500, 100),
    'profits': np.random.randint(20, 100, 100)
})

# Graphique rapide
df.plot(x='date', y='ventes', kind='line', title='Ventes Journalières')
plt.show()

# Plusieurs colonnes
df.plot(x='date', y=['ventes', 'profits'], subplots=True)
plt.show()
```

### Utilisation de Seaborn

Seaborn est construit sur Matplotlib et offre des graphiques plus beaux par défaut.

```python
import seaborn as sns

# Réglage du style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Graphique de correlation
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Matrice de Corrélation')
plt.show()

# Pairplot pour explorer les relations
sns.pairplot(df)
plt.show()
```

---

## 5. Export et Sauvegarde

```python
# Sauvegarder en différents formats
fig.savefig('mon_graphique.png', dpi=300, bbox_inches='tight')
fig.savefig('mon_graphique.pdf', bbox_inches='tight')
fig.savefig('mon_graphique.svg', bbox_inches='tight')

# Sauvegarder avec transparence
fig.savefig('avec_transparence.png', transparent=True)
```

---

## 6. Erreurs Courantes à Éviter

### 1. Oublier `plt.show()`

```python
# MAUVAIS
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
# Rien ne s'affiche !

# CORRECT
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### 2. Surcharger le graphique

```python
# MAUVAIS - Trop d'informations
ax.plot(x1, y1, color='red', linestyle='-', linewidth=2, marker='o', markersize=10)
ax.plot(x2, y2, color='blue', linestyle='--', linewidth=2, marker='s', markersize=10)

# CORRECT - Un graphique clair
ax.plot(x1, y1, label='Série 1', color='red')
ax.plot(x2, y2, label='Série 2', color='blue')
ax.legend()
ax.set_xlabel('Temps')
ax.set_ylabel('Valeur')
```

### 3. Mauvaise utilisation des subplots

```python
# MAUVAIS - Axes non référencés correctement
fig, axs = plt.subplots(2, 2)
axs[0].plot([1, 2, 3], [1, 4, 9])  # Erreur possible

# CORRECT
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
```

---

## 7. Résumé et Tableau de Référence

| Fonction | Type de Graphique | Cas d'Usage |
|----------|-------------------|-------------|
| `plt.plot(x, y)` | Ligne | Séries temporelles, tendances |
| `plt.bar(x, y)` | Bâtons | Comparaisons catégorielles |
| `plt.hist(x)` | Histogramme | Distribution des valeurs |
| `plt.scatter(x, y)` | Nuage de points | Corrélations |
| `plt.pie(x)` | Circulaire | Proportions |
| `plt.boxplot(x)` | Boîte | Distribution avec outliers |
| `df.plot()` | Multiples | Graphiques rapides sur DataFrame |

---

## 8. Ressources Complémentaires

- [Documentation Matplotlib](https://matplotlib.org/stable/gallery.html)
- [Galerie de exemplos](https://matplotlib.org/stable/plot_types/index.html)
- [Tutoriel Seaborn](https://seaborn.pydata.org/tutorial.html)

---

## Prochain Chapitre

Tu as maintenant les bases de la visualisation ! Passons au **chapitre 24 : Web Development** où tu apprendras à créer des applications web avec Flask et FastAPI.

---

*Félicitations ! Tu peux maintenant créer des visualisations professionnelles ! 📊*
