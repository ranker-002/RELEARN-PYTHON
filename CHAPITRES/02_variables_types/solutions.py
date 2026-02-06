# =============================================================================
# CHAPITRE 2: VARIABLES ET TYPES DE DONNÉES - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 2.1 - AFFICHAGE DE VARIABLES
# =============================================================================
def exercice_2_1():
    """Déclare et affiche 4 variables de types différents."""
    nom = "Alice"
    age = 25
    taille = 1.65
    est_etudiant = True

    print(f"Nom: {nom}")
    print(f"Âge: {age}")
    print(f"Taille: {taille} m")
    print(f"Étudiant: {'Oui' if est_etudiant else 'Non'}")


# =============================================================================
# EXERCICE 2.2 - CONVERSION DE TEMPÉRATURE
# =============================================================================
def exercice_2_2():
    """Convertit Fahrenheit vers Celsius."""
    fahrenheit = float(input("Température en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")


# =============================================================================
# EXERCICE 2.3 - CALCUL DE MOYENNE AVEC PRÉCISION
# =============================================================================
def exercice_2_3():
    """Calcule la moyenne de 4 nombres."""
    # Méthode 1: Une variable par entrée
    n1 = float(input("Nombre 1: "))
    n2 = float(input("Nombre 2: "))
    n3 = float(input("Nombre 3: "))
    n4 = float(input("Nombre 4: "))

    moyenne = (n1 + n2 + n3 + n4) / 4
    print(f"Moyenne: {round(moyenne, 2)}")

    # Méthode 2: Liste (appris plus tard)
    # nombres = [float(input(f"Nombre {i+1}: ")) for i in range(4)]
    # print(f"Moyenne: {round(sum(nombres) / len(nombres), 2)}")


# =============================================================================
# EXERCICE 2.4 - VALIDATION D'ÂGE
# =============================================================================
def exercice_2_4():
    """Détermine si une personne est majeure."""
    age = int(input("Âge: "))
    est_mineur = age < 18
    est_majeur = age >= 18

    print(f"Mineur: {est_mineur}")
    print(f"Majeur: {est_majeur}")


# =============================================================================
# EXERCICE 2.5 - ANALYSEUR DE NOMBRE
# =============================================================================
def exercice_2_5():
    """Analyse les propriétés d'un nombre."""
    nombre = float(input("Nombre: "))

    print(f"Type: {type(nombre).__name__}")
    print(f"Valeur absolue: {abs(nombre)}")
    print(f"Partie entière: {int(nombre)}")
    print(f"Arrondi: {round(nombre)}")


# =============================================================================
# EXERCICE 2.6 - MANIPULATION DE CHAÎNES
# =============================================================================
def exercice_2_6():
    """Manipule une chaîne de caractères."""
    mot = input("Mot: ")

    print(f"Majuscules: {mot.upper()}")
    print(f"Minuscules: {mot.lower()}")
    print(f"Première lettre: {mot[0]}")
    print(f"Dernière lettre: {mot[-1]}")
    print(f"Inversé: {mot[::-1]}")
    print(f"Longueur: {len(mot)}")


# =============================================================================
# EXERCICE 2.7 - FORMATEUR DE PRIX
# =============================================================================
def exercice_2_7():
    """Formate un prix avec séparateurs de milliers."""
    prix = float(input("Prix: "))

    # La virgule est le séparateur par défaut
    print(f"Formaté: {prix:,.2f} €")


# =============================================================================
# EXERCICE 2.8 - CALCULATEUR DE BMR
# =============================================================================
def exercice_2_8():
    """Calcule le métabolisme de base (homme)."""
    poids = float(input("Poids (kg): "))
    taille = float(input("Taille (cm): "))
    age = int(input("Âge: "))

    bmr = 88.362 + (13.397 * poids) + (4.799 * taille) - (5.677 * age)

    print(f"BMR: {round(bmr)} kcal/jour")


# =============================================================================
# EXERCICE 2.9 - VALIDATEUR D'EMAIL SIMPLIFIÉ
# =============================================================================
def exercice_2_9():
    """Valide un email simplifié."""
    email = input("Email: ")

    # Vérifications
    a_le_symbole = "@" in email
    a_un_point = "." in email
    a_position_valide = "@" in email and email.index("@") > 0
    ne_finit_pas_avec_arrobase = not email.endswith("@")

    # Validation complète
    est_valide = a_le_symbole and a_un_point and a_position_valide and ne_finit_pas_avec_arrobase

    print(f"Valide: {est_valide}")


# =============================================================================
# EXERCICE 2.10 - CONVERTISSEUR DE DURÉE
# =============================================================================
def exercice_2_10():
    """Convertit des secondes en minutes/heures."""
    total_secondes = int(input("Secondes: "))

    # Minutes et secondes
    minutes, secondes = divmod(total_secondes, 60)
    print(f"Minutes: {minutes} minute(s) et {secondes} seconde(s)")

    # Heures, minutes et secondes
    heures, reste = divmod(total_secondes, 3600)
    minutes, secondes = divmod(reste, 60)
    print(f"Heures: {heures} heure(s), {minutes} minute(s) et {secondes} seconde(s)")


# =============================================================================
# EXERCICE 2.11 - CALCULATEUR D'INTÉRÊTS COMPOSÉS
# =============================================================================
def exercice_2_11():
    """Calcule les intérêts composés."""
    capital = float(input("Capital initial: "))
    taux = float(input("Taux (%): "))
    temps = int(input("Durée (années): "))

    capital_final = capital * (1 + taux / 100) ** temps
    interets = capital_final - capital

    print(f"Capital final: {capital_final:.2f} €")
    print(f"Intérêts gagnés: {interets:.2f} €")


# =============================================================================
# EXERCICE 2.12 - GÉNÉRATEUR D'ACRONYME
# =============================================================================
def exercice_2_12():
    """Génère un acronyme à partir d'une phrase."""
    phrase = input("Phrase: ")

    # Mots à ignorer
    mots_ignorés = {"le", "la", "les", "un", "une", "de", "du", "des", "et", "à", "en", "est", "n'est"}

    # Extraire les premières lettres
    mots = phrase.split()
    premiere_lettres = [mot[0].upper() for mot in mots if mot.lower() not in mots_ignorés]

    acronyme = "".join(premiere_lettres)
    print(f"Acronyme: {acronyme}")


# =============================================================================
# EXERCICE 2.13 - CONVERTISSEUR ROMAIN
# =============================================================================
def exercice_2_13():
    """Convertit un nombre (1-10) en chiffres romains."""
    nombre = int(input("Nombre (1-10): "))

    if 1 <= nombre <= 10:
        romains = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
            6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"
        }
        print(f"Chiffre romain: {romains[nombre]}")
    else:
        print("Erreur: Le nombre doit être entre 1 et 10")


# =============================================================================
# EXERCICE 2.14 - CALCULATEUR DE NOTE AVEC LETTRE
# =============================================================================
def exercice_2_14():
    """Convertit une note numérique en lettre."""
    note = float(input("Note: "))

    if note >= 16:
        lettre = "A (Excellent)"
    elif note >= 14:
        lettre = "B (Très bien)"
    elif note >= 12:
        lettre = "C (Bien)"
    elif note >= 10:
        lettre = "D (Passable)"
    else:
        lettre = "F (Insuffisant)"

    print(f"Lettre: {lettre}")


# =============================================================================
# EXERCICE 2.15 - CALCULATEUR DE POURCENTAGE DE VOTES
# =============================================================================
def exercice_2_15():
    """Calcule les pourcentages de votes."""
    votes_a = int(input("Votes candidat A: "))
    votes_b = int(input("Votes candidat B: "))
    votes_c = int(input("Votes candidat C: "))

    total = votes_a + votes_b + votes_c

    pct_a = (votes_a / total) * 100
    pct_b = (votes_b / total) * 100
    pct_c = (votes_c / total) * 100

    print(f"\nTotal: {total}")
    print(f"A: {pct_a:.1f}%")
    print(f"B: {pct_b:.1f}%")
    print(f"C: {pct_c:.1f}%")
