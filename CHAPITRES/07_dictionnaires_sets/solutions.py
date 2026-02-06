# =============================================================================
# CHAPITRE 7: DICTIONNAIRES ET SETS - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 7.1 - CREATION DE DICTIONNAIRE
# =============================================================================
def exercice_7_1():
    """Cree un dictionnaire de livre."""
    livre = {
        "titre": "Le Petit Prince",
        "auteur": "Antoine de Saint-Exupery",
        "annee": 1943
    }
    print(livre)


# =============================================================================
# EXERCICE 7.2 - ACCES AUX VALEURS
# =============================================================================
def exercice_7_2():
    """Accede aux valeurs d'un dictionnaire."""
    capitales = {"France": "Paris", "Allemagne": "Berlin", "Espagne": "Madrid"}

    # Acces direct
    print(f"France: {capitales['France']}")

    # Avec valeur par defaut
    italie = capitales.get("Italie", "Inconnue")
    print(f"Italie: {italie}")


# =============================================================================
# EXERCICE 7.3 - MODIFICATION DE DICTIONNAIRE
# =============================================================================
def exercice_7_3():
    """Modifie un dictionnaire."""
    personne = {"nom": "Alice", "age": 25}
    print(f"Original: {personne}")

    personne["ville"] = "Paris"
    print(f"Ajout ville: {personne}")

    personne["age"] = 26
    print(f"Age modifie: {personne}")

    del personne["age"]
    print(f"Apres suppression: {personne}")


# =============================================================================
# EXERCICE 7.4 - CREATION DE SET
# =============================================================================
def exercice_7_4():
    """Cree un set et montre l'unicite."""
    liste_avec_doublons = [1, 2, 2, 3, 3, 3]
    print(f"Liste originale: {liste_avec_doublons}")

    mon_set = set(liste_avec_doublons)
    print(f"Set cree: {mon_set}")


# =============================================================================
# EXERCICE 7.5 - OPERATIONS SUR SETS
# =============================================================================
def exercice_7_5():
    """Demontre les operations sur les sets."""
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    print(f"A: {A}")
    print(f"B: {B}")
    print(f"Union: {A | B}")
    print(f"Intersection: {A & B}")
    print(f"Difference A - B: {A - B}")
    print(f"Difference symetrique: {A ^ B}")


# =============================================================================
# EXERCICE 7.6 - BOUTIQUE SIMPLE
# =============================================================================
def exercice_7_6():
    """Gere un inventaire simple."""
    inventaire = {}

    # Ajouter des produits
    inventaire["pomme"] = 1.50
    inventaire["banane"] = 1.20
    inventaire["orange"] = 1.80

    # Afficher le prix
    print(f"Prix de la pomme: {inventaire.get('pomme', 'Indisponible')}")

    # Afficher tous les produits
    for produit, prix in inventaire.items():
        print(f"{produit}: {prix:.2f}€")


# =============================================================================
# EXERCICE 7.7 - VERIFICATION D'APPARTENANCE
# =============================================================================
def exercice_7_7():
    """Verifie l'appartenance a un set."""
    couleurs = {"rouge", "vert", "bleu", "jaune"}

    print(f"Couleurs: {couleurs}")
    print(f"Est-ce que 'rouge' est present? {'rouge' in couleurs}")
    print(f"Est-ce que 'violet' est present? {'violet' in couleurs}")


# =============================================================================
# EXERCICE 7.8 - COMPTEUR DE LETTRES
# =============================================================================
def exercice_7_8():
    """Compte les lettres dans un mot."""
    mot = "programmation"
    print(f"Mot: {mot}")

    compteur = {}
    for lettre in mot:
        compteur[lettre] = compteur.get(lettre, 0) + 1

    print(f"Occurrences: {compteur}")


# =============================================================================
# EXERCICE 7.9 - COMPREHENSION DE DICTIONNAIRE
# =============================================================================
def exercice_7_9():
    """Utilise les comprehensions de dictionnaires."""
    # Carres de 1 a 10
    carres = {x: x ** 2 for x in range(1, 11)}
    print(f"Carres: {carres}")

    # Parite
    parite = {x: "pair" if x % 2 == 0 else "impair" for x in range(1, 11)}
    print(f"Parite: {parite}")


# =============================================================================
# EXERCICE 7.10 - GESTION D'ETUDIANTS
# =============================================================================
def exercice_7_10():
    """Gere les notes des etudiants."""
    notes = {}

    # Ajouter
    notes["Alice"] = 15
    notes["Bob"] = 12
    notes["Charlie"] = 18

    # Modifier
    notes["Bob"] = 14

    # Moyenne
    if notes:
        moyenne = sum(notes.values()) / len(notes)
        print(f"Notes: {notes}")
        print(f"Moyenne: {moyenne:.2f}")


# =============================================================================
# EXERCICE 7.11 - DEDOUBLONNAGE
# =============================================================================
def exercice_7_11():
    """Supprime les doublons en conservant l'ordre."""
    liste = [3, 1, 2, 3, 1, 4, 2, 5]
    print(f"Originale: {liste}")

    vus = set()
    resultat = []
    for elem in liste:
        if elem not in vus:
            vus.add(elem)
            resultat.append(elem)

    print(f"Sans doublons: {resultat}")


# =============================================================================
# EXERCICE 7.12 - GROUPEMENT PAR CATEGORIE
# =============================================================================
def exercice_7_12():
    """Regroupe les fruits par premiere lettre."""
    fruits = ["pomme", "abricot", "banane", "cerise", "avocat"]

    resultat = {}
    for fruit in fruits:
        initiale = fruit[0]
        if initiale not in resultat:
            resultat[initiale] = []
        resultat[initiale].append(fruit)

    print(f"Fruits: {fruits}")
    print(f"Par initiale: {resultat}")


# =============================================================================
# EXERCICE 7.13 - UNION D'INVENTAIRES
# =============================================================================
def exercice_7_13():
    """Fusionne deux inventaires en additionnant."""
    inv1 = {"pomme": 50, "banane": 30}
    inv2 = {"banane": 20, "orange": 40}

    print(f"INV1: {inv1}")
    print(f"INV2: {inv2}")

    # Fusion avec addition des quantites
    fusion = inv1.copy()
    for produit, qte in inv2.items():
        fusion[produit] = fusion.get(produit, 0) + qte

    print(f"Fusion: {fusion}")


# =============================================================================
# EXERCICE 7.14 - JEU DE CARTES
# =============================================================================
def exercice_7_14():
    """Represente un jeu de cartes."""
    couleurs = {"pique", "coeur", "carreau", "trefle"}
    valeurs = {"7", "8", "9", "10", "Valet", "Dame", "Roi", "As"}

    # Generer toutes les cartes
    jeu = {f"{valeur} de {couleur}" for couleur in couleurs for valeur in valeurs}

    print(f"Couleurs: {couleurs}")
    print(f"Nombre de cartes: {len(jeu)}")


# =============================================================================
# EXERCICE 7.15 - ANALYSEUR DE TEXTE
# =============================================================================
def exercice_7_15():
    """Analyse un texte avec dict et set."""
    texte = "le chat le chien et le canard"
    mots = texte.split()

    print(f"Texte: {texte}")
    print(f"Mots: {mots}")

    # Total de mots
    print(f"Nombre de mots: {len(mots)}")

    # Mots uniques
    print(f"Mots uniques: {set(mots)}")

    # Mots de plus de 4 lettres
    longs = [m for m in mots if len(m) > 4]
    print(f"Mots de plus de 4 lettres: {longs}")

    # Occurrences
    occ = {}
    for m in mots:
        occ[m] = occ.get(m, 0) + 1
    print(f"Occurrences: {occ}")
