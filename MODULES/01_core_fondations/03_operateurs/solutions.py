# =============================================================================
# CHAPITRE 3: OPÉRATEURS - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 3.1 - CALCULATRICE AVEC OPÉRATEURS
# =============================================================================
def exercice_3_1():
    """Effectue une opération selon l'opérateur choisi."""
    n1 = float(input("Nombre 1: "))
    n2 = float(input("Nombre 2: "))
    op = input("Opérateur (+, -, *, /, //, %, **): ")

    if op == "+":
        resultat = n1 + n2
    elif op == "-":
        resultat = n1 - n2
    elif op == "*":
        resultat = n1 * n2
    elif op == "/":
        resultat = n1 / n2
    elif op == "//":
        resultat = n1 // n2
    elif op == "%":
        resultat = n1 % n2
    elif op == "**":
        resultat = n1 ** n2
    else:
        print("Opérateur invalide")
        return

    print(f"Résultat: {resultat}")


# =============================================================================
# EXERCICE 3.2 - COMPARAISON DE NOMBRES
# =============================================================================
def exercice_3_2():
    """Affiche toutes les comparaisons entre deux nombres."""
    n1 = float(input("Nombre 1: "))
    n2 = float(input("Nombre 2: "))

    print(f"{n1} == {n2}: {n1 == n2}")
    print(f"{n1} != {n2}: {n1 != n2}")
    print(f"{n1} > {n2}: {n1 > n2}")
    print(f"{n1} < {n2}: {n1 < n2}")
    print(f"{n1} >= {n2}: {n1 >= n2}")
    print(f"{n1} <= {n2}: {n1 <= n2}")


# =============================================================================
# EXERCICE 3.3 - VÉRIFICATION D'ÂGE
# =============================================================================
def exercice_3_3():
    """Vérifie différentes catégories d'âge."""
    age = int(input("Âge: "))

    est_majeur = age >= 18
    est_senior = age >= 65
    est_mineur = age < 18

    print(f"Majeur (>= 18): {est_majeur}")
    print(f"Senior (>= 65): {est_senior}")
    print(f"Mineur (< 18): {est_mineur}")


# =============================================================================
# EXERCICE 3.4 - CALCUL DE MOYENNE AVEC CONDITIONS
# =============================================================================
def exercice_3_4():
    """Calcule la moyenne et vérifie la réussite."""
    note1 = float(input("Note 1: "))
    note2 = float(input("Note 2: "))
    note3 = float(input("Note 3: "))

    moyenne = (note1 + note2 + note3) / 3
    recu = moyenne >= 10

    print(f"Moyenne: {moyenne:.2f}")
    print(f"Reçu: {recu}")


# =============================================================================
# EXERCICE 3.5 - VÉRIFICATION D'APPARTENANCE
# =============================================================================
def exercice_3_5():
    """Vérifie si un fruit est dans la liste."""
    fruits = ["pomme", "orange", "banane", "raisin", "kiwi"]
    fruit = input("Fruit: ")

    est_present = fruit in fruits
    print(f"Est dans la liste: {est_present}")


# =============================================================================
# EXERCICE 3.6 - OPÉRATEURS LOGIQUES
# =============================================================================
def exercice_3_6():
    """Vérifie les conditions avec ET et OU logiques."""
    n = int(input("Nombre: "))

    positif_et_pair = n > 0 and n % 2 == 0
    negatif_ou_zero = n < 0 or n == 0

    print(f"Positif ET pair: {positif_et_pair}")
    print(f"Négatif OU zéro: {negatif_ou_zero}")


# =============================================================================
# EXERCICE 3.7 - CALCULATEUR DE REMISE
# =============================================================================
def exercice_3_7():
    """Calcule le prix avec remise selon le montant."""
    prix = float(input("Prix: "))

    if prix > 100:
        remise = prix * 0.20
    elif prix > 50:
        remise = prix * 0.10
    else:
        remise = 0

    prix_final = prix - remise
    print(f"Remise: {remise:.2f}")
    print(f"Prix final: {prix_final:.2f}")


# =============================================================================
# EXERCICE 3.8 - CLASSIFICATION DE TRIANGLE
# =============================================================================
def exercice_3_8():
    """Vérifie le type de triangle."""
    a = float(input("Côté 1: "))
    b = float(input("Côté 2: "))
    c = float(input("Côté 3: "))

    est_triangle = (a + b > c) and (a + c > b) and (b + c > a)

    if not est_triangle:
        print("Ce n'est pas un triangle valide")
        return

    if a == b == c:
        print("Triangle équilatéral")
    elif a == b or a == c or b == c:
        print("Triangle isocèle")
    else:
        print("Triangle scalène")


# =============================================================================
# EXERCICE 3.9 - OPÉRATEURS BIT À BIT
# =============================================================================
def exercice_3_9():
    """Affiche les opérations bit à bit."""
    a = int(input("Nombre a: "))
    b = int(input("Nombre b: "))

    print(f"a & b = {a & b}")
    print(f"a | b = {a | b}")
    print(f"a ^ b = {a ^ b}")
    print(f"~a = {~a}")
    print(f"a << 1 = {a << 1}")
    print(f"a >> 1 = {a >> 1}")


# =============================================================================
# EXERCICE 3.10 - VÉRIFICATION DE BISEXTILE
# =============================================================================
def exercice_3_10():
    """Vérifie si une année est bissextile."""
    annee = int(input("Année: "))

    est_bissextile = (annee % 4 == 0) and ((annee % 100 != 0) or (annee % 400 == 0))

    print(f"Bissextile: {est_bissextile}")


# =============================================================================
# EXERCICE 3.11 - CALCULATEUR DE PRIX FINAL
# =============================================================================
def exercice_3_11():
    """Calcule le prix final avec TVA et remise membre."""
    prix_base = float(input("Prix de base (€): "))
    tvq = float(input("TVA (10 ou 20): "))
    est_membre = input("Membre (oui/non): ").lower() == "oui"

    montant_tva = prix_base * (tvq / 100)
    taux_remise = 0.05 if est_membre else 0
    montant_remise = prix_base * taux_remise

    prix_final = prix_base + montant_tva - montant_remise

    print(f"\nDétail:")
    print(f"Prix base: {prix_base:.2f}")
    print(f"TVA ({tvq}%): {montant_tva:.2f}")
    print(f"Remise ({taux_remise*100}%): {montant_remise:.2f}")
    print(f"Prix final: {prix_final:.2f}")


# =============================================================================
# EXERCICE 3.12 - VALIDATEUR DE MOT DE PASSE
# =============================================================================
def exercice_3_12():
    """Valide un mot de passe selon plusieurs critères."""
    mdp = input("Mot de passe: ")

    assez_long = len(mdp) >= 8
    majuscule = any(c.isupper() for c in mdp)
    chiffre = any(c.isdigit() for c in mdp)
    special = any(c in "!@#$%" for c in mdp)

    est_valide = assez_long and majuscule and chiffre and special

    print(f"Au moins 8 caractères: {assez_long}")
    print(f"Au moins une majuscule: {majuscule}")
    print(f"Au moins un chiffre: {chiffre}")
    print(f"Caractère spécial: {special}")
    print(f"Valide: {est_valide}")


# =============================================================================
# EXERCICE 3.13 - JEU DE PIERRE-FEUILLE-CISEAUX
# =============================================================================
def exercice_3_13():
    """Jeu Pierre-Feuille-Ciseaux contre l'ordinateur."""
    import random

    choix = ["pierre", "feuille", "ciseaux"]
    utilisateur = input("Choix (pierre/feuille/ciseaux): ").lower()
    ordinateur = random.choice(choix)

    print(f"Vous: {utilisateur}")
    print(f"Ordinateur: {ordinateur}")

    if utilisateur == ordinateur:
        print("Égalité!")
    elif (
        (utilisateur == "pierre" and ordinateur == "ciseaux") or
        (utilisateur == "feuille" and ordinateur == "pierre") or
        (utilisateur == "ciseaux" and ordinateur == "feuille")
    ):
        print("Vous gagnez!")
    else:
        print("Vous perdez!")


# =============================================================================
# EXERCICE 3.14 - CONVERTISSEUR DE NOTES EN LETTRES
# =============================================================================
def exercice_3_14():
    """Convertit une note en lettre ECTS."""
    note = float(input("Note (0-100): "))

    if note >= 90:
        lettre = "A (Excellent)"
    elif note >= 80:
        lettre = "B (Très bien)"
    elif note >= 70:
        lettre = "C (Bien)"
    elif note >= 60:
        lettre = "D (Satisfaisant)"
    elif note >= 50:
        lettre = "E (Passable)"
    else:
        lettre = "F (Insuffisant)"

    print(f"Note: {lettre}")


# =============================================================================
# EXERCICE 3.15 - SIMULATEUR DE BACCALAURÉAT
# =============================================================================
def exercice_3_15():
    """Détermine l'admission au baccalauréat."""
    print("Entrez les 12 notes du baccalauréat:")

    notes = []
    for i in range(12):
        note = float(input(f"Note {i+1}: "))
        notes.append(note)

    note_philo = notes[0]
    autres_notes = notes[1:]

    moyenne_generale = sum(notes) / len(notes)
    moyenne_autres = sum(autres_notes) / len(autres_notes)

    notes_eliminatoires = sum(1 for note in notes if note < 5)
    trop_eliminatoires = notes_eliminatoires > 2

    admis = (moyenne_generale >= 10 and
             (note_philo >= 10 or moyenne_autres >= 12) and
             not trop_eliminatoires)

    if trop_eliminatoires:
        print("Recalé (trop de notes éliminatoires)")
    elif admis:
        print(f"Admis! Moyenne: {moyenne_generale:.2f}")
    else:
        print("Oral de rattrapage")
