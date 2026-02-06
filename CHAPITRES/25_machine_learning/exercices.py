# =============================================================================
# CHAPITRE 25: MACHINE LEARNING - EXERCICES
# =============================================================================
# Niveau: AVANCÉ
# Concepts: Scikit-learn, Régression, Classification, Clustering
# =============================================================================

# =============================================================================
# EXERCICE 25.1 - RÉGRESSION LINÉAIRE SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Créez un modèle de régression linéaire pour prédire le prix d'une maison
# selon sa surface.
#
# DONNÉES:
# X = [[50], [60], [70], [80], [90], [100]]  # surface en m²
# y = [100000, 120000, 140000, 160000, 180000, 200000]  # prix en €
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_1():
    pass


# =============================================================================
# EXERCICE 25.2 - ÉVALUATION R² SCORE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Calculez le R² Score de votre modèle de régression.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_2():
    pass


# =============================================================================
# EXERCICE 25.3 - RÉGRESSION MULTIPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Prédisez le prix d'une maison avec: surface=75, chambres=3, age=5
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_3():
    pass


# =============================================================================
# EXERCICE 25.4 - RÉGRESSION LOGISTIQUE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un modèle de classification pour prédire si un email est spam.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_4():
    pass


# =============================================================================
# EXERCICE 25.5 - KNN CLASSIFICATION
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Utilisez KNN pour classifier des fleurs Iris.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_5():
    pass


# =============================================================================
# EXERCICE 25.6 - ARBRE DE DÉCISION
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un arbre de décision et affichez l'importance des features.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_6():
    pass


# =============================================================================
# EXERCICE 25.7 - RANDOM FOREST
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Comparez Random Forest avec Decision Tree sur le même dataset.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_7():
    pass


# =============================================================================
# EXERCICE 25.8 - K-MEANS CLUSTERING
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Regroupez des données en 3 clusters avec K-Means.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_8():
    pass


# =============================================================================
# EXERCICE 25.9 - VALIDATION CROISÉE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Évaluez un modèle avec une validation croisée 5-fold.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_9():
    pass


# =============================================================================
# EXERCICE 25.10 - PRÉTRAITEMENT
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Standardisez et normalisez un jeu de données.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_10():
    pass


# =============================================================================
# EXERCICE 25.11 - PIPELINE
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez un pipeline: StandardScaler + LogisticRegression.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_11():
    pass


# =============================================================================
# EXERCICE 25.12 - MATRICE DE CONFUSION
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez et affichez la matrice de confusion d'un modèle.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_12():
    pass


# =============================================================================
# EXERCICE 25.13 - ROC AUC
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Calculez le score ROC-AUC d'un modèle de classification binaire.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_13():
    pass


# =============================================================================
# EXERCICE 25.14 - FEATURE SELECTION
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Sélectionnez les features les plus importantes.
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_14():
    pass


# =============================================================================
# EXERCICE 25.15 - PROJET: PRÉDICTION DE PRIX IMMOBILIER
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez un modèle complet de prédiction de prix:
# - Charger des données (ou en générer)
# - Prétraitement
# - Comparer plusieurs modèles
# - Évaluer avec validation croisée
# - Afficher les résultats
#
# VOTRE CODE CI-DESSOUS:
def exercice_25_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 25 - MACHINE LEARNING")
    print("=" * 50)

    exercices = [
        ("25.1 - Régression linéaire", exercice_25_1),
        ("25.2 - Évaluation R²", exercice_25_2),
        ("25.3 - Régression multiple", exercice_25_3),
        ("25.4 - Régression logistique", exercice_25_4),
        ("25.5 - KNN", exercice_25_5),
        ("25.6 - Arbre de décision", exercice_25_6),
        ("25.7 - Random Forest", exercice_25_7),
        ("25.8 - K-Means", exercice_25_8),
        ("25.9 - Validation croisée", exercice_25_9),
        ("25.10 - Prétraitement", exercice_25_10),
        ("25.11 - Pipeline", exercice_25_11),
        ("25.12 - Matrice de confusion", exercice_25_12),
        ("25.13 - ROC AUC", exercice_25_13),
        ("25.14 - Feature selection", exercice_25_14),
        ("25.15 - Projet complet", exercice_25_15),
    ]

    for nom, fonction in exercices:
        print(f"\n{nom}")
        print("-" * 30)
        try:
            fonction()
            print("✓ Exécuté avec succès")
        except Exception as e:
            print(f"✗ Erreur: {e}")

    print("\n" + "=" * 50)
    print("Installez les dépendances: uv sync --extra data")
    print("=" * 50)
