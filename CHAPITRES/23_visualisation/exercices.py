# =============================================================================
# CHAPITRE 23: VISUALISATION DE DONNÉES - EXERCICES
# =============================================================================
# Niveau: INTERMÉDIAIRE
# Concepts abordés: Matplotlib, Pandas plotting, Seaborn, personnalisation
# =============================================================================

# REMARQUE: Écrivez votre code ci-dessous pour chaque exercice

# =============================================================================
# EXERCICE 23.1 - PREMIER GRAPHIQUE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Créez un graphique linéaire affichant les nombres de 1 à 10 au carré.
#
# CONTRAINTES:
# - Axe X: 1 à 10
# - Axe Y: les carrés (1, 4, 9, ..., 100)
# - Titre: "Carrés de 1 à 10"
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_1():
    pass


# =============================================================================
# EXERCICE 23.2 - DIAGRAMME EN BÂTONS
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Affichez les ventes mensuelles d'une entreprise.
#
# DONNÉES:
# Mois: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin']
# Ventes: [12000, 15000, 11000, 18000, 20000, 17500]
#
# CONTRAINTES:
# - Diagramme en bâtons avec couleurs différentes pour chaque barre
# - Titre: "Ventes Mensuelles"
# - Rotation des labels à 45 degrés
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_2():
    pass


# =============================================================================
# EXERCICE 23.3 - HISTOGRAMME
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Générez 1000 nombres aléatoires avec une distribution normale
# et affichez l'histogramme.
#
# CONTRAINTES:
# - Utiliser np.random.normal(mu=70, sigma=10, size=1000)
# - 30 bins
# - Titre: "Distribution des Tailles"
# - Labels: "Taille (cm)", "Fréquence"
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_3():
    pass


# =============================================================================
# EXERCICE 23.4 - NUAGE DE POINTS
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Affichez la correlation entre l'âge et le revenu.
#
# DONNÉES:
# - 50 personnes avec âge entre 20 et 60 ans
# - Revenu = âge * 1000 + variable aléatoire
#
# CONTRAINTES:
# - X: âge, Y: revenu
# - Titre: "Âge vs Revenu"
# - Définir labels des axes
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_4():
    pass


# =============================================================================
# EXERCICE 23.5 - DIAGRAMME CIRCULAIRE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Affichez la répartition des utilisateurs par continent.
#
# DONNÉES:
# Continents: ['Europe', 'Amérique', 'Asie', 'Afrique', 'Océanie']
# Utilisateurs: [350, 280, 450, 180, 40]
#
# CONTRAINTES:
# - Pourcentages automatiques (autopct='%1.1f%%')
# - Titre: "Répartition des Utilisateurs"
# - Légende avec les continents
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_5():
    pass


# =============================================================================
# EXERCICE 23.6 - GRAPHIQUE AVEC SOUS-GRAPHIQUES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez une figure 2x2 avec 4 types de graphiques différents.
#
# CONTRAINTES:
# - Sous-graphique 1: Ligne (0,0) - fonction sin
# - Sous-graphique 2: Bâtons (0,1) - valeurs [3, 7, 5, 9]
# - Sous-graphique 3: Scatter (1,0) - 20 points aléatoires
# - Sous-graphique 4: Histogramme (1,1) - 100 nombres aléatoires
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_6():
    pass


# =============================================================================
# EXERCICE 23.7 - DATAFRAME PANDAS PLOT
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un DataFrame avec des données météorologiques et visualisez-le.
#
# DONNÉES:
# DataFrame avec colonnes: 'jour', 'temperature', 'humidite', 'vent'
# 7 jours de données
#
# CONTRAINTES:
# - Graphique en ligne de la température
# - Titre: "Données Météorologiques"
# - Labels corrects
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_7():
    pass


# =============================================================================
# EXERCICE 23.8 - PERSONNALISATION AVANCÉE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un graphique stylisé avec annotations.
#
# CONTRAINTES:
# - Graphique de la fonction exponentielle
# - Annotation au point (2, 7.39) avec "e² ≈ 7.39"
# - Style: fond gris clair, grille visible
# - Couleur de la ligne: rouge, epaisseur 3
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_8():
    pass


# =============================================================================
# EXERCICE 23.9 - MULTIPLES SÉRIES
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Affichez plusieurs séries sur le même graphique.
#
# DONNÉES:
# - Série 1: x = 0 à 10, y = x
# - Série 2: x = 0 à 10, y = x²
# - Série 3: x = 0 à 10, y = 2^x
#
# CONTRAINTES:
# - Légende avec les équations
# - Couleurs différentes
# - Titre: "Comparaison de Fonctions"
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_9():
    pass


# =============================================================================
# EXERCICE 23.10 - BOÎTE À MOUSTACHES
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Affichez la distribution de 3 groupes de données.
#
# DONNÉES:
# - Groupe A: 200 valeurs, moyenne 100
# - Groupe B: 200 valeurs, moyenne 80
# - Groupe C: 200 valeurs, moyenne 120
#
# CONTRAINTES:
# - Boxplot avec 3 boîte
# - Labels: 'Groupe A', 'Groupe B', 'Groupe C'
# - Titre: "Comparaison des Groupes"
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_10():
    pass


# =============================================================================
# EXERCICE 23.11 - SAUVEGARDE DE GRAPHIQUE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Créez un graphique et sauvegardez-le en PNG et PDF.
#
# CONTRAINTES:
# - Créer un graphique simple (courbe sin/cos)
# - Sauvegarder en 'sin_cos.png' (dpi=300)
# - Sauvegarder en 'sin_cos.pdf'
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_11():
    pass


# =============================================================================
# EXERCICE 23.12 - MATRICE DE CORRÉLATION (PANDAS)
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Créez un DataFrame avec des données numériques et affichez la matrice de correlation.
#
# CONTRAINTES:
# - 4 colonnes avec des données aléatoires
# - Utiliser df.corr() et sns.heatmap()
# - Annotations des valeurs
# - Titre: "Matrice de Corrélation"
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_12():
    pass


# =============================================================================
# EXERCICE 23.13 - GRAPHIQUE INTERACTIF BASIQUE
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez un graphique avec des styles différents.
#
# CONTRAINTES:
# - Utiliser style 'ggplot'
# - Afficher 3 graphiques différents avec ce style
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_13():
    pass


# =============================================================================
# EXERCICE 23.14 - COMBINAISON DE GRAPHIQUES
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez une visualisation complète d'un jeu de données.
#
# CONTRAINTES:
# - Figure avec 4 sous-graphiques
# - 1: Nuage de points (taille vs poids)
# - 2: Histogramme des âges
# - 3: Diagramme circulaire des catégories
# - 4: Évolution temporelle
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_14():
    pass


# =============================================================================
# EXERCICE 23.15 - PROJET: TABLEAU DE BORD
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez un tableau de bord complet avec des données de vente.
#
# DONNÉES:
# - 12 mois de données
# - Colonnes: 'mois', 'ventes', 'benefices', 'clients'
# - Valeurs réalistes
#
# CONTRAINTES:
# - 4 sous-graphiques arrangees intelligemment
# - Graphiques cohérents (mêmes couleurs)
# - Titre general: "Tableau de Bord - Année 2024"
# - Sauvegarder en 'tableau_de_bord.png'
#
# VOTRE CODE CI-DESSOUS:
def exercice_23_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE (Ne pas modifier)
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 23 - VISUALISATION")
    print("=" * 50)

    exercices = [
        ("23.1 - Premier graphique", exercice_23_1),
        ("23.2 - Diagramme en bâtons", exercice_23_2),
        ("23.3 - Histogramme", exercice_23_3),
        ("23.4 - Nuage de points", exercice_23_4),
        ("23.5 - Diagramme circulaire", exercice_23_5),
        ("23.6 - Sous-graphiques", exercice_23_6),
        ("23.7 - DataFrame plot", exercice_23_7),
        ("23.8 - Personnalisation", exercice_23_8),
        ("23.9 - Multiples séries", exercice_23_9),
        ("23.10 - Boîte à moustaches", exercice_23_10),
        ("23.11 - Sauvegarde", exercice_23_11),
        ("23.12 - Corrélation", exercice_23_12),
        ("23.13 - Styles", exercice_23_13),
        ("23.14 - Combinaison", exercice_23_14),
        ("23.15 - Tableau de bord", exercice_23_15),
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
    print("Pour visualiser, les exercices utilisent plt.show()")
    print("=" * 50)
