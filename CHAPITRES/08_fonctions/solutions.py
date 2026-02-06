# =============================================================================
# CHAPITRE 8: FONCTIONS - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 8.1 - FONCTION SIMPLE
# =============================================================================
def exercice_8_1():
    """Affiche Bonjour."""
    def dire_bonjour():
        print("Bonjour!")

    dire_bonjour()


# =============================================================================
# EXERCICE 8.2 - FONCTION AVEC PARAMETRE
# =============================================================================
def exercice_8_2():
    """Salue une personne."""
    def saluer(nom):
        print(f"Bonjour, {nom}!")

    saluer("Alice")
    saluer("Bob")


# =============================================================================
# EXERCICE 8.3 - FONCTION AVEC RETOUR
# =============================================================================
def exercice_8_3():
    """Calcule le carre d'un nombre."""
    def carre(nombre):
        return nombre ** 2

    resultat = carre(5)
    print(f"5 carre = {resultat}")  # 25


# =============================================================================
# EXERCICE 8.4 - FONCTION AVEC PLUSIEURS PARAMETRES
# =============================================================================
def exercice_8_4():
    """Presente une personne."""
    def presenter(nom, age, ville):
        return f"{nom}, {age} ans, habite a {ville}"

    print(presenter("Alice", 25, "Paris"))
    print(presenter("Bob", 30, "Lyon"))


# =============================================================================
# EXERCICE 8.5 - PARAMETRES PAR DEFAUT
# =============================================================================
def exercice_8_5():
    """Salue avec un message personnalise."""
    def salutation(nom, message="Bonjour"):
        return f"{message}, {nom}!"

    print(salutation("Alice"))           # "Bonjour, Alice!"
    print(salutation("Bob", "Salut"))     # "Salut, Bob!"


# =============================================================================
# EXERCICE 8.6 - RETOUR MULTIPLE
# =============================================================================
def exercice_8_6():
    """Calcule quotient et reste."""
    def divmod_custom(a, b):
        return a // b, a % b

    q, r = divmod_custom(17, 5)
    print(f"17 / 5: quotient={q}, reste={r}")  # 3, 2


# =============================================================================
# EXERCICE 8.7 - ARGUMENTS NOMMES
# =============================================================================
def exercice_8_7():
    """Affiche les arguments dans n'importe quel ordre."""
    def afficher_info(prenom, nom, age):
        return f"{prenom} {nom}, {age} ans"

    # Appel avec arguments nommes
    print(afficher_info(prenom="Alice", nom="Dupont", age=25))
    print(afficher_info(age=30, prenom="Bob", nom="Martin"))


# =============================================================================
# EXERCICE 8.8 - PORTEE DES VARIABLES
# =============================================================================
def exercice_8_8():
    """Demontre la portee des variables."""
    globale = "Je suis globale"

    def fonction():
        locale = "Je suis locale"
        print(f"Dans la fonction: {locale}")
        print(f"Dans la fonction (acces global): {globale}")

    fonction()
    print(f"Globale toujours accessible: {globale}")


# =============================================================================
# EXERCICE 8.9 - FONCTION LAMBDA
# =============================================================================
def exercice_8_9():
    """Calcule les cubes avec lambda et map."""
    cube = lambda x: x ** 3
    nombres = [1, 2, 3, 4]
    cubes = list(map(cube, nombres))
    print(f"Cubes: {cubes}")  # [1, 8, 27, 64]


# =============================================================================
# EXERCICE 8.10 - FILTER AVEC LAMBDA
# =============================================================================
def exercice_8_10():
    """Filtre les nombres divisibles par 3."""
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    divisibles = list(filter(lambda x: x % 3 == 0, nombres))
    print(f"Divisibles par 3: {divisibles}")  # [3, 6, 9]


# =============================================================================
# EXERCICE 8.11 - FONCTION DE FACTORIELLE
# =============================================================================
def exercice_8_11():
    """Calcule la factorielle recursivement."""
    def factorielle(n):
        if n <= 1:
            return 1
        return n * factorielle(n - 1)

    for i in range(6):
        print(f"{i}! = {factorielle(i)}")


# =============================================================================
# EXERCICE 8.12 - DOCSTRING
# =============================================================================
def exercice_8_12():
    """Affiche la docstring de la fonction."""
    def calculer_moyenne(liste):
        """
        Calcule la moyenne d'une liste de nombres.
        
        Args:
            liste: Liste de nombres (int ou float)
        
        Returns:
            float: La moyenne des nombres
        
        Example:
            >>> calculer_moyenne([1, 2, 3])
            2.0
        """
        if not liste:
            return 0
        return sum(liste) / len(liste)

    print(calculer_moyenne.__doc__)
    help(calculer_moyenne)


# =============================================================================
# EXERCICE 8.13 - EARLY RETURN
# =============================================================================
def exercice_8_13():
    """Valide l'age avec early return."""
    def valider_age(age):
        if age < 18:
            return "Mineur"
        if age < 65:
            return "Majeur"
        return "Senior"

    print(f"15 ans: {valider_age(15)}")
    print(f"25 ans: {valider_age(25)}")
    print(f"70 ans: {valider_age(70)}")


# =============================================================================
# EXERCICE 8.14 - TRI AVEC LAMBDA
# =============================================================================
def exercice_8_14():
    """Trie par differentes cles."""
    personnes = [("Alice", 25, 170), ("Bob", 30, 165), ("Charlie", 25, 180)]

    print(f"Original: {personnes}")
    print(f"Par age: {sorted(personnes, key=lambda x: x[1])}")
    print(f"Par age puis taille: {sorted(personnes, key=lambda x: (x[1], x[2]))}")


# =============================================================================
# EXERCICE 8.15 - CALCULATRICE AVEC FONCTIONS
# =============================================================================
def exercice_8_15():
    """Systeme de calculatrice avec fonctions."""
    def addition(a, b):
        return a + b

    def soustraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b == 0:
            return "Erreur: division par zero"
        return a / b

    # Demander a l'utilisateur
    try:
        a = float(input("Nombre 1: "))
        b = float(input("Nombre 2: "))
        print("\nOperations: +, -, *, /")
        op = input("Operation: ")

        if op == "+":
            resultat = addition(a, b)
        elif op == "-":
            resultat = soustraction(a, b)
        elif op == "*":
            resultat = multiplication(a, b)
        elif op == "/":
            resultat = division(a, b)
        else:
            resultat = "Operation invalide"

        print(f"Resultat: {resultat}")
    except ValueError:
        print("Erreur: entrez des nombres valides")
