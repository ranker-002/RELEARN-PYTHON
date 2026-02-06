# =============================================================================
# CHAPITRE 9: ARGUMENTS AVANCÉS - EXERCICES
# =============================================================================
# Niveau: INTERMEDIAIRE
# Concepts abordes: *args, **kwargs, positional-only, keyword-only, decorateurs
# =============================================================================

# =============================================================================
# EXERCICE 9.1 - *ARGS SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction moyenne(*notes) qui calcule la moyenne de
# tous les nombres passes en argument.
#
# EXEMPLE:
# moyenne(10, 20, 30) -> 20.0
# moyenne(15, 25) -> 20.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_1():
    pass


# =============================================================================
# EXERCICE 9.2 - **KWARGS SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction creer_profil(**info) qui cree un dictionnaire
# avec les informations fournies.
#
# EXEMPLE:
# creer_profil(nom="Alice", age=25, ville="Paris")
# -> {"nom": "Alice", "age": 25, "ville": "Paris"}
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_2():
    pass


# =============================================================================
# EXERCICE 9.3 - COMBINAISON *ARGS ET **KWARGS
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction afficher_commande(plat, *extras, **details)
# qui affiche le plat, les extras, et les details.
#
# EXEMPLE:
# afficher_commande("Pizza", "fromage", "champignons",
#                   taille="large",boisson="coca")
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_3():
    pass


# =============================================================================
# EXERCICE 9.4 - POSITIONAL-ONLY
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une fonction calculer_carre(base, /, exposant=2) ou
# base ne peut etre passe qu'en positionnel.
#
# EXEMPLE:
# calculer_carre(5) -> 25
# calculer_carre(5, 3) -> 125
# calculer_carre(base=5) # ERREUR!
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_4():
    pass


# =============================================================================
# EXERCICE 9.5 - KEYWORD-ONLY
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une fonction send_email(to, /, *, subject, body, cc=None)
# ou subject et body doivent etre nommes.
#
# EXEMPLE:
# send_email("alice@email.com", subject="Hello", body="...")
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_5():
    pass


# =============================================================================
# EXERCICE 9.6 - DEBALLAGE D'ARGUMENTS
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une fonction creer_rectangle(longueur, largeur) et appelez-la
# avec une liste [5, 3] deballee.
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_6():
    pass


# =============================================================================
# EXERCICE 9.7 - DECORATEUR SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez un decorateur dire_bonjour_avant qui affiche "Bonjour!"
# avant d'appeler la fonction decoree.
#
# INDICE:
# def decorateur(func):
#     def wrapper(*args, **kwargs):
#         print("Bonjour!")
#         return func(*args, **kwargs)
#     return wrapper
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_7():
    pass


# =============================================================================
# EXERCICE 9.8 - DECORATEUR DE TIMING
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez un decorateur timer qui mesure et affiche le temps
# d'execution de la fonction.
#
# INDICE: import time
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_8():
    pass


# =============================================================================
# EXERCICE 9.9 - FONCTION FLEXIBLE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une fonction api_request(url, method="GET", **headers)
# qui formate et affiche la requete.
#
# EXEMPLE:
# api_request("/users", Authorization="Bearer token")
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_9():
    pass


# =============================================================================
# EXERCICE 9.10 - ORDRE DES PARAMETRES
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une fonction avec tous les types de parametres dans le bon ordre:
# def complexe(a, /, b, *args, c, d=10, **kwargs)
# Affichez les valeurs de chaque parametre.
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_10():
    pass


# =============================================================================
# EXERCICE 9.11 - DECORATEUR AVEC ARGUMENTS
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un decorateur repeat(n) qui repete la fonction n fois.
#
# @repeat(3)
# def dire_oui():
#     print("Oui!")
#
# Resultat:
# Oui!
# Oui!
# Oui!
#
# INDICE: Le decorateur doit prendre des arguments
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_11():
    pass


# =============================================================================
# EXERCICE 9.12 - VALIDATEUR AVEC *ARGS
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une fonction valider(*valeurs, min_val=0, max_val=100)
# qui verifie que toutes les valeurs sont dans l'intervalle.
#
# EXEMPLE:
# valider(10, 20, 30, min_val=0, max_val=50) -> True
# valider(10, 60, 30, min_val=0, max_val=50) -> False
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_12():
    pass


# =============================================================================
# EXERCICE 9.13 - LOGGER AVANCE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un decorateur log qui affiche:
# - Le nom de la fonction
# - Les arguments
# - Le resultat
# Avec option pour activer/desactiver l'affichage.
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_13():
    pass


# =============================================================================
# EXERCICE 9.14 - CONSTRUCTEUR DE REQUETES
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une fonction build_query(table, *, select="*", where=None,
#                               order_by=None, limit=None)
# qui construit une requete SQL.
#
# EXEMPLE:
# build_query("users", select="name, email", where="age > 18")
# -> "SELECT name, email FROM users WHERE age > 18"
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_14():
    pass


# =============================================================================
# EXERCICE 9.15 - DECORATEUR DE CACHE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un decorateur cache qui stocke les resultats des appels
# precedents (memoization).
#
# INDICE: Utilisez un dictionnaire dans le wrapper
#
# VOTRE CODE CI-DESSOUS:
def exercice_9_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 9 - EXERCICES")
    print("=" * 50)
    print("Executez python verification.py pour valider")
    print("=" * 50)
