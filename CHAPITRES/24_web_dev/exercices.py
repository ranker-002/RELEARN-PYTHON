# =============================================================================
# CHAPITRE 24: WEB DEVELOPMENT - EXERCICES
# =============================================================================
# Niveau: INTERMÉDIAIRE
# Concepts abordés: Flask, FastAPI, Templates, API REST
# =============================================================================

# REMARQUE: Écrivez votre code ci-dessous pour chaque exercice

# =============================================================================
# EXERCICE 24.1 - PREMIÈRE APPLICATION FLASK
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Créez une application Flask avec une route '/' qui affiche "Bonjour Flask!".
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_1():
    pass


# =============================================================================
# EXERCICE 24.2 - ROUTES AVEC PARAMÈTRES
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Créez une route '/bonjour/<nom>' qui affiche "Bonjour {nom}!".
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_2():
    pass


# =============================================================================
# EXERCICE 24.3 - ROUTES MULTIPLES
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Créez une calculatrice avec les routes:
# - /add/<a>/<b>
# - /mul/<a>/<b>
# - /puissance/<a>/<b>
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_3():
    pass


# =============================================================================
# EXERCICE 24.4 - TEMPLATE DE BASE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Créez un template HTML base.html avec une structure HTML complète
# et un bloc 'contenu'.
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_4():
    pass


# =============================================================================
# EXERCICE 24.5 - TEMPLATE AVEC VARIABLES
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Affichez les informations d'un utilisateur dans un template.
#
# DONNÉES:
# user = {"nom": "Alice", "age": 30, "ville": "Paris"}
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_5():
    pass


# =============================================================================
# EXERCICE 24.6 - BOUCLE DANS TEMPLATE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Affichez une liste de produits dans un tableau HTML.
#
# DONNÉES:
# produits = [
#     {"nom": "Ordinateur", "prix": 999},
#     {"nom": "Souris", "prix": 29},
#     {"nom": "Clavier", "prix": 79}
# ]
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_6():
    pass


# =============================================================================
# EXERCICE 24.7 - FORMULAIRE SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un formulaire de contact avec les champs:
# - nom (text)
# - email (email)
# - message (textarea)
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_7():
    pass


# =============================================================================
# EXERCICE 24.8 - PREMIÈRE API FASTAPI
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez une API FastAPI avec:
# - GET / : "Bienvenue sur l'API"
# - GET /ping : {"message": "pong"}
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_8():
    pass


# =============================================================================
# EXERCICE 24.9 - MODÈLE PYDANTIC
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Créez un modèle Pydantic 'Personne' avec:
# - nom: str
# - age: int (minimum 0, maximum 150)
# - email: EmailStr
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_9():
    pass


# =============================================================================
# EXERCICE 24.10 - CRUD COMPLET
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Créez un CRUD pour les tâches (todos):
# - GET /todos
# - POST /todos (avec titre)
# - PUT /todos/{id} (avec statut)
# - DELETE /todos/{id}
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_10():
    pass


# =============================================================================
# EXERCICE 24.11 - API REST PRODUITS
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Créez une API pour gérer un catalogue de produits:
# - Modèle Produit (nom, prix, stock)
# - GET /produits
# - POST /produits
# - GET /produits/{id}
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_11():
    pass


# =============================================================================
# EXERCICE 24.12 - AUTHENTIFICATION SIMPLE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Ajoutez une route /protected qui requiert un token.
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_12():
    pass


# =============================================================================
# EXERCICE 24.13 - TEMPLATE HÉRITÉ
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez une structure de templates avec:
# - base.html (navigation, footer)
# - index.html (hérite de base)
# - about.html (hérite de base)
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_13():
    pass


# =============================================================================
# EXERCICE 24.14 - API AVEC BASE DE DONNÉES
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez une API avec SQLAlchemy:
# - Modèle Livre (titre, auteur, annee)
# - Endpoints CRUD complets
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_14():
    pass


# =============================================================================
# EXERCICE 24.15 - PROJET: BLOG COMPLET
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Créez un mini-blog avec:
# - Modèle Article (titre, contenu, date)
# - Routes: list, show, create
# - Templates pour chaque vue
#
# VOTRE CODE CI-DESSOUS:
def exercice_24_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE (Ne pas modifier)
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 24 - WEB DEVELOPMENT")
    print("=" * 50)

    exercices = [
        ("24.1 - Première app Flask", exercice_24_1),
        ("24.2 - Routes avec paramètres", exercice_24_2),
        ("24.3 - Routes multiples", exercice_24_3),
        ("24.4 - Template de base", exercice_24_4),
        ("24.5 - Template avec variables", exercice_24_5),
        ("24.6 - Boucle dans template", exercice_24_6),
        ("24.7 - Formulaire simple", exercice_24_7),
        ("24.8 - Première API FastAPI", exercice_24_8),
        ("24.9 - Modèle Pydantic", exercice_24_9),
        ("24.10 - CRUD complet", exercice_24_10),
        ("24.11 - API Produits", exercice_24_11),
        ("24.12 - Authentification", exercice_24_12),
        ("24.13 - Template hérité", exercice_24_13),
        ("24.14 - API avec BDD", exercice_24_14),
        ("24.15 - Projet Blog", exercice_24_15),
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
    print("Ces exercices créent des structures Flask/FastAPI")
    print("=" * 50)
