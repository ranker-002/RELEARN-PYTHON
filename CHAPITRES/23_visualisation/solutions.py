# =============================================================================
# CHAPITRE 23: VISUALISATION DE DONNÉES - SOLUTIONS
# =============================================================================
# Niveau: INTERMÉDIAIRE
# Corrections commentées pour chaque exercice
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# =============================================================================
# EXERCICE 23.1 - PREMIER GRAPHIQUE
# =============================================================================
def exercice_23_1():
    """
    Solution de l'exercice 23.1
    Affiche les carrés de 1 à 10.
    """
    x = list(range(1, 11))
    y = [i**2 for i in x]

    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', color='blue', linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('X²')
    ax.set_title('Carrés de 1 à 10')
    ax.grid(True, alpha=0.3)
    plt.show()


# =============================================================================
# EXERCICE 23.2 - DIAGRAMME EN BÂTONS
# =============================================================================
def exercice_23_2():
    """
    Solution de l'exercice 23.2
    Affiche les ventes mensuelles.
    """
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin']
    ventes = [12000, 15000, 11000, 18000, 20000, 17500]
    couleurs = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(mois, ventes, color=couleurs)
    ax.set_xlabel('Mois')
    ax.set_ylabel('Ventes (€)')
    ax.set_title('Ventes Mensuelles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# =============================================================================
# EXERCICE 23.3 - HISTOGRAMME
# =============================================================================
def exercice_23_3():
    """
    Solution de l'exercice 23.3
    Affiche la distribution des tailles.
    """
    donnees = np.random.normal(70, 10, 1000)

    fig, ax = plt.subplots()
    ax.hist(donnees, bins=30, color='steelblue', edgecolor='white')
    ax.set_xlabel('Taille (cm)')
    ax.set_ylabel('Fréquence')
    ax.set_title('Distribution des Tailles')
    ax.grid(True, alpha=0.3)
    plt.show()


# =============================================================================
# EXERCICE 23.4 - NUAGE DE POINTS
# =============================================================================
def exercice_23_4():
    """
    Solution de l'exercice 23.4
    Affiche la correlation âge-revenu.
    """
    np.random.seed(42)
    ages = np.random.randint(20, 60, 50)
    revenus = ages * 1000 + np.random.randint(-5000, 5000, 50)

    fig, ax = plt.subplots()
    ax.scatter(ages, revenus, alpha=0.6, c='crimson', s=60)
    ax.set_xlabel('Âge')
    ax.set_ylabel('Revenu (€)')
    ax.set_title('Âge vs Revenu')
    ax.grid(True, alpha=0.3)
    plt.show()


# =============================================================================
# EXERCICE 23.5 - DIAGRAMME CIRCULAIRE
# =============================================================================
def exercice_23_5():
    """
    Solution de l'exercice 23.5
    Affiche la répartition des utilisateurs.
    """
    continents = ['Europe', 'Amérique', 'Asie', 'Afrique', 'Océanie']
    utilisateurs = [350, 280, 450, 180, 40]
    couleurs = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']

    fig, ax = plt.subplots()
    ax.pie(utilisateurs, labels=continents, colors=couleurs,
           autopct='%1.1f%%', startangle=90, explode=[0.02]*5)
    ax.set_title('Répartition des Utilisateurs')
    plt.tight_layout()
    plt.show()


# =============================================================================
# EXERCICE 23.6 - GRAPHIQUE AVEC SOUS-GRAPHIQUES
# =============================================================================
def exercice_23_6():
    """
    Solution de l'exercice 23.6
    Affiche 4 sous-graphiques.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Graphique 1: Sinus
    x = np.linspace(0, 2*np.pi, 100)
    axes[0, 0].plot(x, np.sin(x), color='red')
    axes[0, 0].set_title('Sinus')

    # Graphique 2: Bâtons
    axes[0, 1].bar(['A', 'B', 'C', 'D'], [3, 7, 5, 9], color='green')
    axes[0, 1].set_title('Bâtons')

    # Graphique 3: Scatter
    axes[1, 0].scatter(np.random.rand(20), np.random.rand(20), color='purple')
    axes[1, 0].set_title('Scatter')

    # Graphique 4: Histogramme
    axes[1, 1].hist(np.random.randn(100), bins=20, color='orange')
    axes[1, 1].set_title('Histogramme')

    plt.tight_layout()
    plt.show()


# =============================================================================
# EXERCICE 23.7 - DATAFRAME PANDAS PLOT
# =============================================================================
def exercice_23_7():
    """
    Solution de l'exercice 23.7
    Affiche des données météorologiques.
    """
    df = pd.DataFrame({
        'jour': [f'Jour {i}' for i in range(1, 8)],
        'temperature': [18, 20, 22, 19, 24, 25, 23],
        'humidite': [65, 60, 55, 70, 50, 45, 52],
        'vent': [15, 12, 18, 10, 8, 5, 11]
    })

    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(x='jour', y='temperature', kind='line', marker='o', ax=ax,
            color='red', linewidth=2, label='Température (°C)')
    ax.set_title('Données Météorologiques')
    ax.set_ylabel('Température (°C)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()


# =============================================================================
# EXERCICE 23.8 - PERSONNALISATION AVANCÉE
# =============================================================================
def exercice_23_8():
    """
    Solution de l'exercice 23.8
    Graphique stylisé avec annotations.
    """
    x = np.linspace(0, 5, 100)
    y = np.exp(x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.style.use('grayscale')
    ax.plot(x, y, color='red', linewidth=3, label='eˣ')
    ax.annotate('e² ≈ 7.39', xy=(2, 7.39), xytext=(2.5, 20),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=12, color='black')
    ax.set_xlabel('x')
    ax.set_ylabel('eˣ')
    ax.set_title('Fonction Exponentielle')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f0f0f0')
    plt.show()


# =============================================================================
# EXERCICE 23.9 - MULTIPLES SÉRIES
# =============================================================================
def exercice_23_9():
    """
    Solution de l'exercice 23.9
    Compare plusieurs fonctions.
    """
    x = np.linspace(0, 10, 100)

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(x, x, label='y = x', color='blue', linewidth=2)
    ax.plot(x, x**2, label='y = x²', color='red', linewidth=2)
    ax.plot(x, 2**x, label='y = 2ˣ', color='green', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Comparaison de Fonctions')
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.show()


# =============================================================================
# EXERCICE 23.10 - BOÎTE À MOUSTACHES
# =============================================================================
def exercice_23_10():
    """
    Solution de l'exercice 23.10
    Compare 3 groupes de données.
    """
    np.random.seed(42)
    groupe_a = np.random.normal(100, 15, 200)
    groupe_b = np.random.normal(80, 20, 200)
    groupe_c = np.random.normal(120, 10, 200)

    donnees = [groupe_a, groupe_b, groupe_c]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(donnees, labels=['Groupe A', 'Groupe B', 'Groupe C'],
               patch_artist=True,
               boxprops=dict(facecolor='lightblue'),
               medianprops=dict(color='red'))
    ax.set_ylabel('Valeurs')
    ax.set_title('Comparaison des Groupes')
    ax.grid(True, alpha=0.3, axis='y')
    plt.show()


# =============================================================================
# EXERCICE 23.11 - SAUVEGARDE DE GRAPHIQUE
# =============================================================================
def exercice_23_11():
    """
    Solution de l'exercice 23.11
    Sauvegarde un graphique en PNG et PDF.
    """
    x = np.linspace(0, 4*np.pi, 100)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, np.sin(x), label='sin(x)', color='blue')
    ax.plot(x, np.cos(x), label='cos(x)', color='red')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Sinus et Cosinus')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Sauvegarder
    fig.savefig('sin_cos.png', dpi=300, bbox_inches='tight')
    fig.savefig('sin_cos.pdf', bbox_inches='tight')
    print("Graphiques sauvegardés: sin_cos.png et sin_cos.pdf")
    plt.close()


# =============================================================================
# EXERCICE 23.12 - MATRICE DE CORRÉLATION
# =============================================================================
def exercice_23_12():
    """
    Solution de l'exercice 23.12
    Affiche la matrice de corrélation.
    """
    import seaborn as sns

    np.random.seed(42)
    df = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100) * 2,
        'C': np.random.rand(100) + np.random.rand(100),
        'D': np.random.randn(100)
    })

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0,
                fmt='.2f', ax=ax)
    ax.set_title('Matrice de Corrélation')
    plt.tight_layout()
    plt.show()


# =============================================================================
# EXERCICE 23.13 - GRAPHIQUES AVEC STYLES
# =============================================================================
def exercice_23_13():
    """
    Solution de l'exercice 23.13
    Utilise différents styles.
    """
    styles = ['ggplot', 'seaborn', 'bmh']
    x = np.linspace(0, 10, 100)

    for i, style in enumerate(styles):
        plt.style.use(style)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, np.sin(x) + i, label=f'Style: {style}')
        ax.legend()
        ax.set_title(f'Graphique avec {style}')
        plt.show()


# =============================================================================
# EXERCICE 23.14 - COMBINAISON DE GRAPHIQUES
# =============================================================================
def exercice_23_14():
    """
    Solution de l'exercice 23.14
    Visualisation complète d'un jeu de données.
    """
    np.random.seed(42)

    fig = plt.figure(figsize=(14, 10))

    # 1: Nuage de points
    ax1 = fig.add_subplot(2, 2, 1)
    taille = np.random.randint(150, 190, 100)
    poids = taille * 0.5 + np.random.randn(100) * 5
    ax1.scatter(taille, poids, alpha=0.6, c='blue')
    ax1.set_xlabel('Taille (cm)')
    ax1.set_ylabel('Poids (kg)')
    ax1.set_title('Taille vs Poids')

    # 2: Histogramme des âges
    ax2 = fig.add_subplot(2, 2, 2)
    ages = np.random.randint(18, 65, 100)
    ax2.hist(ages, bins=15, color='green', edgecolor='white')
    ax2.set_xlabel('Âge')
    ax2.set_ylabel('Effectif')
    ax2.set_title('Distribution des Âges')

    # 3: Diagramme circulaire
    ax3 = fig.add_subplot(2, 2, 3)
    categories = ['A', 'B', 'C', 'D']
    valeurs = [25, 35, 20, 20]
    ax3.pie(valeurs, labels=categories, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    ax3.set_title('Répartition par Catégorie')

    # 4: Évolution temporelle
    ax4 = fig.add_subplot(2, 2, 4)
    mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin']
    valeurs_temps = [100, 120, 110, 140, 130, 150]
    ax4.plot(mois, valeurs_temps, marker='o', color='purple', linewidth=2)
    ax4.set_xlabel('Mois')
    ax4.set_ylabel('Valeur')
    ax4.set_title('Évolution Temporelle')

    plt.tight_layout()
    plt.show()


# =============================================================================
# EXERCICE 23.15 - TABLEAU DE BORD
# =============================================================================
def exercice_23_15():
    """
    Solution de l'exercice 23.15
    Tableau de bord complet des ventes.
    """
    mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin',
            'Juil', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
    ventes = [15000, 18000, 16000, 22000, 25000, 28000,
              30000, 29000, 32000, 35000, 38000, 42000]
    profits = [3000, 4000, 3500, 5500, 6500, 7500,
               8000, 7500, 9000, 10000, 11000, 13000]
    clients = [150, 180, 165, 220, 250, 280,
               300, 290, 320, 350, 380, 420]

    df = pd.DataFrame({
        'mois': mois,
        'ventes': ventes,
        'profits': profits,
        'clients': clients
    })

    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Tableau de Bord - Année 2024', fontsize=16, fontweight='bold')

    # 1: Ventes mensuelles
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.bar(mois, ventes, color='steelblue')
    ax1.set_title('Ventes Mensuelles')
    ax1.set_ylabel('Ventes (€)')
    ax1.tick_params(axis='x', rotation=45)

    # 2: Profits
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(mois, profits, marker='o', color='green', linewidth=2)
    ax2.set_title('Evolution des Profits')
    ax2.set_ylabel('Profits (€)')
    ax2.grid(True, alpha=0.3)

    # 3: Clients
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.fill_between(mois, clients, alpha=0.3, color='orange')
    ax3.plot(mois, clients, marker='s', color='orange', linewidth=2)
    ax3.set_title('Nombre de Clients')
    ax3.set_ylabel('Clients')
    ax3.tick_params(axis='x', rotation=45)

    # 4: Ventes vs Profits scatter
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.scatter(ventes, profits, c='red', s=100, alpha=0.7)
    ax4.set_xlabel('Ventes (€)')
    ax4.set_ylabel('Profits (€)')
    ax4.set_title('Ventes vs Profits')

    # Ajouter regression line
    z = np.polyfit(ventes, profits, 1)
    p = np.poly1d(z)
    ax4.plot(ventes, p(ventes), "b--", alpha=0.8, label='Tendance')
    ax4.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig('tableau_de_bord.png', dpi=300, bbox_inches='tight')
    print("Tableau de bord sauvegardé: tableau_de_bord.png")
    plt.close()


# =============================================================================
# BONUS: EXEMPLES COMPLÉMENTAIRES
# =============================================================================

def exemple_styles_matplotlib():
    """Affiche les différents styles disponibles."""
    styles_disponibles = plt.style.available
    print(f"Styles disponibles ({len(styles_disponibles)}):")
    for style in styles_disponibles:
        print(f"  - {style}")


def exemple_visualisation_3d():
    """Exemple de graphique 3D."""
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Surface 3D')
    fig.colorbar(surf)
    plt.show()
