# =============================================================================
# CHAPITRE 5: BOUCLES - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 5.1 - COMPTEUR SIMPLE
# =============================================================================
def exercice_5_1():
    """Affiche les nombres de 1 a 10 avec for."""
    for i in range(1, 11):
        print(i)


# =============================================================================
# EXERCICE 5.2 - COMPTEUR A REBOURS
# =============================================================================
def exercice_5_2():
    """Affiche les nombres de 10 a 1 avec while."""
    compteur = 10
    while compteur >= 1:
        print(compteur)
        compteur -= 1


# =============================================================================
# EXERCICE 5.3 - SOMME DES NOMBRES
# =============================================================================
def exercice_5_3():
    """Calcule la somme de 1 a 100."""
    total = 0
    for i in range(1, 101):
        total += i
    print(f"Somme de 1 a 100: {total}")


# =============================================================================
# EXERCICE 5.4 - TABLE DE MULTIPLICATION
# =============================================================================
def exercice_5_4():
    """Affiche la table de 7."""
    for i in range(1, 11):
        print(f"7 x {i} = {7 * i}")


# =============================================================================
# EXERCICE 5.5 - LISTE AVEC ENUMERATE
# =============================================================================
def exercice_5_5():
    """Affiche les elements avec index."""
    fruits = ["pomme", "banane", "orange"]
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit}")


# =============================================================================
# EXERCICE 5.6 - NOMBRES PAIRS
# =============================================================================
def exercice_5_6():
    """Affiche les nombres pairs avec continue."""
    for i in range(1, 21):
        if i % 2 != 0:
            continue
        print(i)


# =============================================================================
# EXERCICE 5.7 - RECHERCHE DE NOMBRE
# =============================================================================
def exercice_5_7():
    """Cherche 25 dans la liste avec break."""
    nombres = [5, 10, 15, 20, 25, 30]
    for n in nombres:
        if n == 25:
            print("Trouve!")
            break
    else:
        print("Non trouve")


# =============================================================================
# EXERCICE 5.8 - FACTORIELLE
# =============================================================================
def exercice_5_8():
    """Calcule 5! avec une boucle."""
    n = 5
    factorielle = 1
    for i in range(1, n + 1):
        factorielle *= i
    print(f"{n}! = {factorielle}")


# =============================================================================
# EXERCICE 5.9 - NOMBRE MYSTERE
# =============================================================================
def exercice_5_9():
    """Jeu de devinette avec indices."""
    import random
    secret = random.randint(1, 100)
    print("Devinez le nombre entre 1 et 100!")

    while True:
        guess = int(input("Votre proposition: "))
        if guess > secret:
            print("Plus petit!")
        elif guess < secret:
            print("Plus grand!")
        else:
            print(f"Gagne! C'etait {secret}!")
            break


# =============================================================================
# EXERCICE 5.10 - PYRAMIDE D'ETOILES
# =============================================================================
def exercice_5_10():
    """Affiche une pyramide d'etoiles."""
    for i in range(1, 6):
        print("*" * i)


# =============================================================================
# EXERCICE 5.11 - VALIDATION D'ENTREE
# =============================================================================
def exercice_5_11():
    """Valide l'entree utilisateur."""
    while True:
        try:
            nombre = int(input("Entrez un nombre (1-10): "))
            if 1 <= nombre <= 10:
                print(f"Merci! Vous avez entre: {nombre}")
                break
            else:
                print("Entrez un nombre entre 1 et 10.")
        except ValueError:
            print("Entrez un nombre valide.")


# =============================================================================
# EXERCICE 5.12 - SEQUENCE DE FIBONACCI
# =============================================================================
def exercice_5_12():
    """Affiche les 10 premiers nombres de Fibonacci."""
    fib = [0, 1]

    for i in range(2, 10):
        fib.append(fib[i - 1] + fib[i - 2])

    print("Fibonacci:", ", ".join(map(str, fib)))


# =============================================================================
# EXERCICE 5.13 - COMPTEUR DE VOYELLES
# =============================================================================
def exercice_5_13():
    """Compte les voyelles dans une phrase."""
    phrase = input("Phrase: ")
    voyelles = "aeiouyAEIOUY"
    compteur = 0

    for lettre in phrase:
        if lettre in voyelles:
            compteur += 1

    print(f"Voyelles: {compteur}")


# =============================================================================
# EXERCICE 5.14 - TRIANGLE DE PASCAL
# =============================================================================
def exercice_5_14():
    """Affiche les 5 premieres rangees du triangle de Pascal."""
    n = 5
    triangle = []

    for i in range(n):
        rangee = [1] * (i + 1)
        for j in range(1, i):
            rangee[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(rangee)

    for rangee in triangle:
        print(" ".join(map(str, rangee)).center(10))


# =============================================================================
# EXERCICE 5.15 - JEU DE DEVINETTE AVEC LIMITE
# =============================================================================
def exercice_5_15():
    """Jeu avec 5 essais maximum."""
    import random
    secret = random.randint(1, 20)
    print("Devinez le nombre (1-20)! Vous avez 5 essais.")

    for essai in range(5, 0, -1):
        guess = int(input(f"Essai {6 - essai}: "))

        if guess == secret:
            print("Gagne!")
            break
        elif guess > secret:
            print("Plus petit!")
        else:
            print("Plus grand!")

        print(f"Il vous reste {essai - 1} essai(s)")
    else:
        print(f"Perdu! Le nombre etait {secret}")
