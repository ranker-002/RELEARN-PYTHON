"""
Exercice 8.17 - ARGUMENTS KEYWORD-ONLY
=====================================

NIVEAU: ★★★☆☆ (Intermédiaire)
ENONCE:
Créez des fonctions utilisant des arguments keyword-only (après le *).
Ces arguments doivent obligatoirement être passés par nom explicite.

FONCTIONS A CREER:
1. creer_utilisateur(*, nom, email, actif=True) -> dict
   Crée un dictionnaire représentant un utilisateur.
   - nom et email: obligatoires (keyword-only)
   - actif: optionnel, True par défaut
   Ex: creer_utilisateur(nom="Alice", email="alice@test.com")
   
2. connecter_bdd(*, host, port=5432, user, password, database) -> str
   Simule une connexion à une base de données.
   Tous les arguments sont keyword-only.
   Retourne une chaîne de connexion formatée.
   Ex: connecter_bdd(host="localhost", user="admin", password="secret", database="mydb")
   
3. envoyer_email(destinataire, /, *, sujet, corps, cc=None, bcc=None) -> dict
   Simule l'envoi d'un email.
   - destinataire: position-only (obligatoire)
   - sujet et corps: keyword-only obligatoires
   - cc et bcc: keyword-only optionnels
   
4. configurer_application(debug=False, /, *, host="localhost", port=8080, ssl=True) -> dict
   Configure une application.
   - debug: position-only (optionnel)
   - host, port, ssl: keyword-only avec valeurs par défaut

TESTS ATTENDUS:
- creer_utilisateur(nom="Alice", email="alice@test.com") -> {'nom': 'Alice', ...}
- creer_utilisateur("Alice", "alice@test.com") -> Erreur (doit être nommé)
- connecter_bdd(host="localhost", user="admin", password="secret") -> OK
- connecter_bdd("localhost", "admin", "secret") -> Erreur
"""


def creer_utilisateur(*, nom, email, actif=True):
    """
    Crée un dictionnaire représentant un utilisateur.
    
    Args:
        nom: Nom de l'utilisateur (keyword-only, obligatoire)
        email: Email de l'utilisateur (keyword-only, obligatoire)
        actif: Statut actif (keyword-only, optionnel, défaut: True)
    
    Returns:
        dict: Informations de l'utilisateur
    
    Example:
        >>> creer_utilisateur(nom="Alice", email="alice@test.com")
        {'nom': 'Alice', 'email': 'alice@test.com', 'actif': True}
    """
    # TODO: Retournez un dictionnaire avec les clés 'nom', 'email', 'actif'
    pass


def connecter_bdd(*, host, port=5432, user, password, database):
    """
    Simule une connexion à une base de données.
    
    Args:
        host: Adresse du serveur (keyword-only, obligatoire)
        port: Port de connexion (keyword-only, optionnel, défaut: 5432)
        user: Nom d'utilisateur (keyword-only, obligatoire)
        password: Mot de passe (keyword-only, obligatoire)
        database: Nom de la base (keyword-only, obligatoire)
    
    Returns:
        str: Chaîne de connexion formatée
    
    Example:
        >>> connecter_bdd(host="localhost", user="admin", password="secret", database="mydb")
        'postgresql://admin:***@localhost:5432/mydb'
    """
    # TODO: Retournez une chaîne formatée (masquez le password avec ***)
    pass


def envoyer_email(destinataire, /, *, sujet, corps, cc=None, bcc=None):
    """
    Simule l'envoi d'un email.
    
    Args:
        destinataire: Email du destinataire (position-only, obligatoire)
        sujet: Sujet de l'email (keyword-only, obligatoire)
        corps: Contenu de l'email (keyword-only, obligatoire)
        cc: Email en copie (keyword-only, optionnel)
        bcc: Email en copie cachée (keyword-only, optionnel)
    
    Returns:
        dict: Résumé de l'email envoyé
    
    Example:
        >>> envoyer_email("alice@test.com", sujet="Hello", corps="Message")
        {'destinataire': 'alice@test.com', 'sujet': 'Hello', 'corps': 'Message'}
    """
    # TODO: Créez un dictionnaire avec les informations de l'email
    # N'incluez cc et bcc que s'ils ne sont pas None
    pass


def configurer_application(debug=False, /, *, host="localhost", port=8080, ssl=True):
    """
    Configure une application.
    
    Args:
        debug: Mode debug (position-only, optionnel, défaut: False)
        host: Adresse hôte (keyword-only, défaut: "localhost")
        port: Port (keyword-only, défaut: 8080)
        ssl: Utiliser SSL (keyword-only, défaut: True)
    
    Returns:
        dict: Configuration de l'application
    
    Example:
        >>> configurer_application(host="0.0.0.0", port=3000)
        {'debug': False, 'host': '0.0.0.0', 'port': 3000, 'ssl': True}
    """
    # TODO: Retournez un dictionnaire avec toutes les configurations
    pass


def run():
    """Fonction principale de l'exercice."""
    print("=== Test des arguments keyword-only ===\n")
    
    # Test 1: Création utilisateur
    print("Test de creer_utilisateur(nom='Alice', email='alice@test.com'):")
    try:
        resultat = creer_utilisateur(nom="Alice", email="alice@test.com")
        print(f"  ✅ Utilisateur créé: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    print("\nTest de creer_utilisateur avec actif=False:")
    try:
        resultat = creer_utilisateur(nom="Bob", email="bob@test.com", actif=False)
        print(f"  ✅ Utilisateur inactif: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    # Test 2: Connexion BDD
    print("\nTest de connecter_bdd:")
    try:
        resultat = connecter_bdd(
            host="localhost",
            user="admin",
            password="secret123",
            database="production"
        )
        print(f"  ✅ Connexion: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    # Test 3: Envoi email
    print("\nTest d'envoyer_email:")
    try:
        resultat = envoyer_email(
            "client@example.com",
            sujet="Commande confirmée",
            corps="Votre commande #12345 est en cours de préparation."
        )
        print(f"  ✅ Email envoyé: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    print("\nTest d'envoyer_email avec CC:")
    try:
        resultat = envoyer_email(
            "client@example.com",
            sujet="Facture",
            corps="Veuillez trouver ci-joint votre facture.",
            cc="comptabilite@entreprise.com"
        )
        print(f"  ✅ Email avec CC: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    # Test 4: Configuration
    print("\nTest de configurer_application:")
    try:
        resultat = configurer_application(host="0.0.0.0", port=3000)
        print(f"  ✅ Config: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    print("\nTest avec debug=True:")
    try:
        resultat = configurer_application(True, port=5000, ssl=False)
        print(f"  ✅ Config debug: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    # Tests d'erreurs
    print("\n=== Test des erreurs (doivent échouer) ===")
    print("Tentative de creer_utilisateur('Alice', 'alice@test.com'):")
    try:
        resultat = creer_utilisateur("Alice", "alice@test.com")
        print(f"  ❌ Ne devrait pas fonctionner ! Résultat: {resultat}")
    except TypeError as e:
        print(f"  ✅ Bonne erreur: {e}")
    
    print("\nTentative de connecter_bdd('localhost', 'admin', 'secret'):")
    try:
        resultat = connecter_bdd("localhost", "admin", "secret")
        print(f"  ❌ Ne devrait pas fonctionner ! Résultat: {resultat}")
    except TypeError as e:
        print(f"  ✅ Bonne erreur: {e}")


# Pour tests manuels
if __name__ == "__main__":
    run()
