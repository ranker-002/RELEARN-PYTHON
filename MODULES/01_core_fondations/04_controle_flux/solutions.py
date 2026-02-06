# =============================================================================
# CHAPITRE 4: CONTRÔLE DE FLUX - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 4.1 - CLASSIFICATION D'ÂGE SIMPLE
# =============================================================================
def exercice_4_1():
    """Affiche la catégorie d'âge."""
    age = int(input("Âge: "))

    if age < 12:
        print("Enfant")
    elif age < 18:
        print("Adolescent")
    elif age < 65:
        print("Adulte")
    else:
        print("Senior")


# =============================================================================
# EXERCICE 4.2 - CALCULATEUR DE PRIX AVEC TENDAIRE
# =============================================================================
def exercice_4_2():
    """Calcule le prix avec remise using ternaire."""
    prix = float(input("Prix: "))
    prix_remise = prix * 0.9 if prix > 50 else prix
    print(f"Prix avec remise: {prix_remise}")


# =============================================================================
# EXERCICE 4.3 - VÉRIFICATION DE SIGNE
# =============================================================================
def exercice_4_3():
    """Affiche le signe du nombre."""
    n = int(input("Nombre: "))

    if n > 0:
        print("Positif")
    elif n < 0:
        print("Négatif")
    else:
        print("Zéro")


# =============================================================================
# EXERCICE 4.4 - JOUR DE LA SEMAINE AVEC MATCH
# =============================================================================
def exercice_4_4():
    """Affiche le jour selon le numéro."""
    jour = int(input("Jour (1-7): "))

    match jour:
        case 1:
            print("Lundi")
        case 2:
            print("Mardi")
        case 3:
            print("Mercredi")
        case 4:
            print("Jeudi")
        case 5:
            print("Vendredi")
        case 6:
            print("Samedi")
        case 7:
            print("Dimanche")
        case _:
            print("Jour invalide")


# =============================================================================
# EXERCICE 4.5 - CALCULATEUR DE REMISE PROGRESSIVE
# =============================================================================
def exercice_4_5():
    """Calcule la remise selon le montant."""
    montant = float(input("Montant (€): "))

    if montant > 500:
        remise_pct = 20
    elif montant > 200:
        remise_pct = 10
    elif montant > 100:
        remise_pct = 5
    else:
        remise_pct = 0

    remise = montant * remise_pct / 100
    final = montant - remise

    print(f"Remise ({remise_pct}%): {remise:.2f}€")
    print(f"Prix final: {final:.2f}€")


# =============================================================================
# EXERCICE 4.6 - VALIDATION DE MOT DE PASSE
# =============================================================================
def exercice_4_6():
    """Valide un mot de passe."""
    mdp = input("Mot de passe: ")

    est_valide = (
        len(mdp) >= 8 and
        any(c.islower() for c in mdp) and
        any(c.isupper() for c in mdp) and
        any(c.isdigit() for c in mdp)
    )

    print(f"Valide: {est_valide}")


# =============================================================================
# EXERCICE 4.7 - CLASSIFICATION DE FORMES AVEC MATCH
# =============================================================================
def exercice_4_7():
    """Affiche la forme selon le nombre de côtés."""
    cotes = int(input("Nombre de côtés (3-6): "))

    match cotes:
        case 3:
            print("Triangle")
        case 4:
            print("Carré/Rectangle")
        case 5:
            print("Pentagone")
        case 6:
            print("Hexagone")
        case _:
            print("Forme non reconnue")


# =============================================================================
# EXERCICE 4.8 - CALCULATEUR DE TAXI
# =============================================================================
def exercice_4_8():
    """Calcule le prix d'une course de taxi."""
    km = float(input("Distance (km): "))
    nuit = input("Course de nuit (oui/non): ").lower() == "oui"

    base = 4.50
    km_price = km * 1.10

    if nuit:
        km_price *= 1.20

    total = base + km_price
    print(f"Prix total: {total:.2f}€")


# =============================================================================
# EXERCICE 4.9 - CONVERTISSEUR DE TEMPÉRATURE
# =============================================================================
def exercice_4_9():
    """Convertit une température selon l'unité."""
    valeur = float(input("Valeur: "))
    unite = input("Unité (C/F/K): ").upper()

    match unite:
        case "C":
            f = valeur * 9/5 + 32
            k = valeur + 273.15
            print(f"{valeur}°C = {f}°F = {k}K")
        case "F":
            c = (valeur - 32) * 5/9
            print(f"{valeur}°F = {c}°C")
        case "K":
            c = valeur - 273.15
            print(f"{valeur}K = {c}°C")
        case _:
            print("Unité invalide")


# =============================================================================
# EXERCICE 4.10 - JEU DE DEVINETTE AVEC MATCH
# =============================================================================
def exercice_4_10():
    """Jeu de devinette de nombre."""
    import random

    secret = random.randint(1, 100)
    print("Devinez le nombre entre 1 et 100!")

    while True:
        try:
            guess = int(input("Votre proposition: "))
        except ValueError:
            print("Veuillez entrer un nombre valide")
            continue

        match True:
            case _ if guess > secret:
                print("Trop grand!")
            case _ if guess < secret:
                print("Trop petit!")
            case _:
                print(f"Gagné! C'était {secret}")
                break


# =============================================================================
# EXERCICE 4.11 - SIMULATEUR DE DISTRIBUTEUR
# =============================================================================
def exercice_4_11():
    """Simule un distributeur de boissons."""
    prix = {
        "eau": 1.00,
        "café": 1.50,
        "soda": 2.00,
        "thé": 1.20
    }

    print("Boissons disponibles:", ", ".join(prix.keys()))
    choix = input("Votre choix: ").lower()

    if choix not in prix:
        print("Boisson non disponible")
        return

    prix_boisson = prix[choix]
    print(f"Prix: {prix_boisson}€")

    argent = float(input("Argent inséré: "))

    if argent < prix_boisson:
        print("Argent insuffisant")
    else:
        rendu = argent - prix_boisson
        print(f"Voici votre {choix}!")
        print(f"Monnaie: {rendu:.2f}€")


# =============================================================================
# EXERCICE 4.12 - ANALYSEUR DE CARACTÈRE AVEC MATCH
# =============================================================================
def exercice_4_12():
    """Analyse un caractère."""
    char = input("Caractère: ")

    if len(char) != 1:
        print("Erreur: entrez un seul caractère")
        return

    match char.lower():
        case c if c in "aeiouy":
            print("Voyelle")
        case c if c.isalpha():
            print("Consonne")
        case c if c.isdigit():
            print("Chiffre")
        case _:
            print("Caractère spécial")


# =============================================================================
# EXERCICE 4.13 - CALCULATEUR D'IMPÔTS SIMPLIFIÉ
# =============================================================================
def exercice_4_13():
    """Calcule l'impôt sur le revenu."""
    revenu = float(input("Revenu annuel (€): "))

    if revenu <= 10000:
        impot = 0
    elif revenu <= 30000:
        impot = (revenu - 10000) * 0.10
    elif revenu <= 60000:
        impot = 20000 * 0.10 + (revenu - 30000) * 0.20
    else:
        impot = 20000 * 0.10 + 30000 * 0.20 + (revenu - 60000) * 0.30

    print(f"Impôt: {impot:.2f}€")
    print(f"Taux effectif: {impot/revenu*100:.1f}%")


# =============================================================================
# EXERCICE 4.14 - SYSTÈME DE NOTES AVEC MATCH
# =============================================================================
def exercice_4_14():
    """Affiche la lettre de note."""
    note = float(input("Note (0-20): "))

    match note:
        case n if n >= 18:
            print("A+ (Excellent)")
        case n if n >= 16:
            print("A- (Très Bien)")
        case n if n >= 14:
            print("B (Bien)")
        case n if n >= 12:
            print("C (Satisfaisant)")
        case n if n >= 10:
            print("D (Passable)")
        case _:
            print("F (Échec)")


# =============================================================================
# EXERCICE 4.15 - SIMULATEUR DE BANQUE
# =============================================================================
def exercice_4_15():
    """Gère un compte bancaire simple."""
    solde = 1000.00

    print(f"Solde initial: {solde:.2f}€")

    while True:
        print("\nOpérations:")
        print("1. Consulter solde")
        print("2. Déposer")
        print("3. Retirer")
        print("4. Quitter")

        choix = input("Choix: ")

        match choix:
            case "1":
                print(f"Solde: {solde:.2f}€")
            case "2":
                montant = float(input("Montant à déposer: "))
                if montant > 0:
                    solde += montant
                    print(f"Nouveau solde: {solde:.2f}€")
                else:
                    print("Montant invalide")
            case "3":
                montant = float(input("Montant à retirer: "))
                if montant <= 0:
                    print("Montant invalide")
                elif montant > solde:
                    print("Solde insuffisant")
                else:
                    solde -= montant
                    print(f"Nouveau solde: {solde:.2f}€")
            case "4":
                print(f"Au revoir! Solde final: {solde:.2f}€")
                break
            case _:
                print("Choix invalide")
