# =============================================================================
# CHAPITRE 9: ARGUMENTS AVANCÉS - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 9.1 - *ARGS SIMPLE
# =============================================================================
def exercice_9_1():
    """Calcule la moyenne avec *args."""
    def moyenne(*notes):
        if not notes:
            return 0
        return sum(notes) / len(notes)

    print(f"moyenne(10, 20, 30) = {moyenne(10, 20, 30)}")
    print(f"moyenne(15, 25) = {moyenne(15, 25)}")


# =============================================================================
# EXERCICE 9.2 - **KWARGS SIMPLE
# =============================================================================
def exercice_9_2():
    """Cree un profil avec **kwargs."""
    def creer_profil(**info):
        return info

    profil = creer_profil(nom="Alice", age=25, ville="Paris")
    print(f"Profil: {profil}")


# =============================================================================
# EXERCICE 9.3 - COMBINAISON *ARGS ET **KWARGS
# =============================================================================
def exercice_9_3():
    """Affiche une commande avec tous les types d'arguments."""
    def afficher_commande(plat, *extras, **details):
        print(f"Plat: {plat}")
        print(f"Extras: {extras}")
        print(f"Détails: {details}")

    afficher_commande("Pizza", "fromage", "champignons",
                      taille="large", boissons="coca")


# =============================================================================
# EXERCICE 9.4 - POSITIONAL-ONLY
# =============================================================================
def exercice_9_4():
    """Calcule avec positional-only."""
    def calculer_carre(base, /, exposant=2):
        return base ** exposant

    print(f"carre(5) = {calculer_carre(5)}")
    print(f"carre(5, 3) = {calculer_carre(5, 3)}")


# =============================================================================
# EXERCICE 9.5 - KEYWORD-ONLY
# =============================================================================
def exercice_9_5():
    """Envoie un email avec keyword-only."""
    def send_email(to, /, *, subject, body, cc=None):
        print(f"To: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        if cc:
            print(f"CC: {cc}")

    send_email("alice@email.com", subject="Hello", body="...")


# =============================================================================
# EXERCICE 9.6 - DEBALLAGE D'ARGUMENTS
# =============================================================================
def exercice_9_6():
    """Demontration du deballage."""
    def creer_rectangle(longueur, largeur):
        return longueur * largeur

    dimensions = [5, 3]
    # Deballage de liste
    aire = creer_rectangle(*dimensions)
    print(f"Rectangle {dimensions} -> Aire: {aire}")


# =============================================================================
# EXERCICE 9.7 - DECORATEUR SIMPLE
# =============================================================================
def exercice_9_7():
    """Decorateur qui dit bonjour avant l'appel."""
    def dire_bonjour_avant(func):
        def wrapper(*args, **kwargs):
            print("Bonjour!")
            return func(*args, **kwargs)
        return wrapper

    @dire_bonjour_avant
    def dire_au_revoir():
        print("Au revoir!")

    dire_au_revoir()


# =============================================================================
# EXERCICE 9.8 - DECORATEUR DE TIMING
# =============================================================================
def exercice_9_8():
    """Decorateur qui mesure le temps d'execution."""
    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            debut = time.time()
            resultat = func(*args, **kwargs)
            temps = time.time() - debut
            print(f"{func.__name__}: {temps:.6f}s")
            return resultat
        return wrapper

    @timer
    def fonction_lente():
        time.sleep(0.1)
        return "Terminé"

    resultat = fonction_lente()
    print(f"Résultat: {resultat}")


# =============================================================================
# EXERCICE 9.9 - FONCTION FLEXIBLE
# =============================================================================
def exercice_9_9():
    """Cree une requete API flexible."""
    def api_request(url, method="GET", **headers):
        print(f"{method} {url}")
        print("Headers:")
        for key, value in headers.items():
            print(f"  {key}: {value}")

    api_request("/users", Authorization="Bearer token")
    api_request("/data", "POST", Content_Type="application/json")


# =============================================================================
# EXERCICE 9.10 - ORDRE DES PARAMETRES
# =============================================================================
def exercice_9_10():
    """Demontration de tous les types de parametres."""
    def complexe(a, /, b, *args, c, d=10, **kwargs):
        print(f"a (positional-only): {a}")
        print(f"b (normal): {b}")
        print(f"args (variables): {args}")
        print(f"c (keyword-only): {c}")
        print(f"d (default): {d}")
        print(f"kwargs (variables nommees): {kwargs}")

    complexe(1, 2, 3, 4, c="obligatoire", extra=99)


# =============================================================================
# EXERCICE 9.11 - DECORATEUR AVEC ARGUMENTS
# =============================================================================
def exercice_9_11():
    """Decorateur qui repete la fonction n fois."""
    def repeat(n):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func(*args, **kwargs)
            return wrapper
        return decorator

    @repeat(3)
    def dire_oui():
        print("Oui!")

    dire_oui()


# =============================================================================
# EXERCICE 9.12 - VALIDATEUR AVEC *ARGS
# =============================================================================
def exercice_9_12():
    """Valide que toutes les valeurs sont dans un intervalle."""
    def valider(*valeurs, min_val=0, max_val=100):
        for v in valeurs:
            if not (min_val <= v <= max_val):
                return False
        return True

    print(f"valider(10, 20, 30) = {valider(10, 20, 30)}")
    print(f"valider(10, 60, 30, min_val=0, max_val=50) = {valider(10, 60, 30, min_val=0, max_val=50)}")


# =============================================================================
# EXERCICE 9.13 - LOGGER AVANCE
# =============================================================================
def exercice_9_13():
    """Decorateur de logging configurable."""
    def log(enabled=True):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if enabled:
                    print(f"[LOG] Appel de {func.__name__}")
                    print(f"[LOG] Args: {args}")
                    print(f"[LOG] Kwargs: {kwargs}")
                resultat = func(*args, **kwargs)
                if enabled:
                    print(f"[LOG] Résultat: {resultat}")
                return resultat
            return wrapper
        return decorator

    @log(enabled=True)
    def additionner(a, b):
        return a + b

    resultat = additionner(5, 3)
    print(f"Résultat final: {resultat}")


# =============================================================================
# EXERCICE 9.14 - CONSTRUCTEUR DE REQUETES
# =============================================================================
def exercice_9_14():
    """Construit une requete SQL."""
    def build_query(table, *, select="*", where=None,
                   order_by=None, limit=None):
        query = f"SELECT {select} FROM {table}"
        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"
        return query

    q1 = build_query("users", select="name, email", where="age > 18")
    q2 = build_query("products", select="*", order_by="price", limit=10)
    print(f"Requete 1: {q1}")
    print(f"Requete 2: {q2}")


# =============================================================================
# EXERCICE 9.15 - DECORATEUR DE CACHE
# =============================================================================
def exercice_9_15():
    """Decorateur de memoization."""
    def cache(func):
        cache_dict = {}
        def wrapper(*args):
            if args in cache_dict:
                print(f"Cache hit pour {args}")
                return cache_dict[args]
            print(f"Calcul pour {args}")
            resultat = func(*args)
            cache_dict[args] = resultat
            return resultat
        return wrapper

    @cache
    def carre(n):
        return n ** 2

    print(carre(5))
    print(carre(5))
    print(carre(6))
    print(carre(6))
