# =============================================================================
# CHAPITRE 26: DEEP LEARNING - EXERCICES
# =============================================================================
# Niveau: EXPERT
# Concepts: PyTorch, Tenseurs, Réseaux de Neurones, CNN, LSTM
# =============================================================================

# Prérequis: uv sync --extra ai

# =============================================================================
# EXERCICE 26.1 - PREMIERS TENSEURS
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Créez différents types de tenseurs.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_1():
    pass


# =============================================================================
# EXERCICE 26.2 - OPÉRATIONS SUR TENSEURS
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Effectuez des opérations mathématiques sur des tenseurs.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_2():
    pass


# =============================================================================
# EXERCICE 26.3 - AUTOGRAD
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Calculez des gradients avec autograd.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_3():
    pass


# =============================================================================
# EXERCICE 26.4 - RÉGRESSION LINÉAIRE PYTORCH
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Implémentez une régression linéaire avec PyTorch.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_4():
    pass


# =============================================================================
# EXERCICE 26.5 - RÉSEAU DE NEURONES SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un réseau avec 2 couches cachées.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_5():
    pass


# =============================================================================
# EXERCICE 26.6 - FONCTIONS D'ACTIVATION
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Testez différentes fonctions d'activation.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_6():
    pass


# =============================================================================
# EXERCICE 26.7 - CNN SIMPLE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Créez un réseau convolutif pour CIFAR-10.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_7():
    pass


# =============================================================================
# EXERCICE 26.8 - DATA LOADING
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Utilisez DataLoader avec un dataset personnalisé.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_8():
    pass


# =============================================================================
# EXERCICE 26.9 - TRANSFER LEARNING
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Utilisez un modèle pré-entraîné (ResNet18).
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_9():
    pass


# =============================================================================
# EXERCICE 26.10 - LSTM
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Implémentez un LSTM pour des données séquentielles.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_10():
    pass


# =============================================================================
# EXERCICE 26.11 - SAVE/LOAD MODEL
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Sauvegardez et chargez un modèle.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_11():
    pass


# =============================================================================
# EXERCICE 26.12 - GPU UTILISATION
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Entraînez un modèle sur GPU.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_12():
    pass


# =============================================================================
# EXERCICE 26.13 - DROPOUT ET BATCHNORM
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Ajoutez dropout et batchnorm à un réseau.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_13():
    pass


# =============================================================================
# EXERCICE 26.14 - CUSTOM LOSS
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez une fonction de perte personnalisée.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_14():
    pass


# =============================================================================
# EXERCICE 26.15 - PROJET: CLASSIFICATION D'IMAGES
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez un pipeline complet de classification d'images
# avec data augmentation, validation, et évaluation.
#
# VOTRE CODE CI-DESSOUS:
def exercice_26_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 26 - DEEP LEARNING")
    print("=" * 50)
    print()
    print("Installez les dépendances: uv sync --extra ai")
    print()
    
    exercices = [
        ("26.1 - Premiers tenseurs", exercice_26_1),
        ("26.2 - Opérations", exercice_26_2),
        ("26.3 - Autograd", exercice_26_3),
        ("26.4 - Régression linéaire", exercice_26_4),
        ("26.5 - Réseau simple", exercice_26_5),
        ("26.6 - Fonctions d'activation", exercice_26_6),
        ("26.7 - CNN", exercice_26_7),
        ("26.8 - Data Loading", exercice_26_8),
        ("26.9 - Transfer Learning", exercice_26_9),
        ("26.10 - LSTM", exercice_26_10),
        ("26.11 - Save/Load", exercice_26_11),
        ("26.12 - GPU", exercice_26_12),
        ("26.13 - Dropout/Batchnorm", exercice_26_13),
        ("26.14 - Custom Loss", exercice_26_14),
        ("26.15 - Projet complet", exercice_26_15),
    ]
    
    for nom, fonction in exercices:
        print(f"✓ {nom}")
    
    print()
    print("=" * 50)
