# =============================================================================
# CHAPITRE 1: PREMIERS PAS AVEC PYTHON - SOLUTIONS
# =============================================================================
# Niveau: DEBUTANT
# Corrections commentées pour chaque exercice
# =============================================================================

# =============================================================================
# EXERCICE 1.1 - VOTRE PREMIER PROGRAMME
# =============================================================================
def exercice_1_1():
    """
    Solution de l'exercice 1.1
    Affiche "Hello, World!" à l'écran.
    """
    # La fonction print() affiche du texte à l'écran
    # Le texte doit être entre guillemets (simples ou doubles)
    print("Hello, World!")


# =============================================================================
# EXERCICE 1.2 - PRÉSENTATION
# =============================================================================
def exercice_1_2():
    """
    Solution de l'exercice 1.2
    Demande le prénom et affiche un message de bienvenida.
    """
    # La fonction input() affiche un message et attend une réponse
    # Le résultat est stocké dans la variable 'prenom'
    prenom = input("Quel est votre prénom? ")

    # Concaténation avec l'opérateur +
    # On peut utiliser des guillemets simples ou doubles
    print("Bonjour " + prenom + " ! Bienvenue dans le monde de Python !")


# =============================================================================
# EXERCICE 1.3 - CALCUL SIMPLE
# =============================================================================
def exercice_1_3():
    """
    Solution de l'exercice 1.3
    Demande deux nombres et affiche leur somme.
    """
    # input() retourne toujours une chaîne de caractères (str)
    # On doit convertir avec int() ou float() pour faire des calculs
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxième nombre: "))

    # Calcul de la somme
    somme = nombre1 + nombre2

    # Affichage avec une f-string (format moderne et lisible)
    # Les f-strings permettent d'insérer des variables avec {}
    print(f"La somme est: {somme}")


# =============================================================================
# EXERCICE 1.4 - CALCULATRICE POLYVALENTE
# =============================================================================
def exercice_1_4():
    """
    Solution de l'exercice 1.4
    Effectue les 4 opérations de base sur deux nombres.
    """
    # Récupération des nombres
    nombre1 = float(input("Nombre 1: "))
    nombre2 = float(input("Nombre 2: "))

    # Les 4 opérations arithmétiques
    addition = nombre1 + nombre2
    soustraction = nombre1 - nombre2
    multiplication = nombre1 * nombre2
    division = nombre1 / nombre2

    # Affichage formaté
    print(f"\nRésultats:")
    print(f"Addition: {addition}")
    print(f"Soustraction: {soustraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")


# =============================================================================
# EXERCICE 1.5 - CONVERSION DE TEMPÉRATURE
# =============================================================================
def exercice_1_5():
    """
    Solution de l'exercice 1.5
    Convertit une température de Celsius vers Fahrenheit.
    """
    # Formule: F = C × 9/5 + 32
    celsius = float(input("Température en Celsius: "))

    # Calcul de la conversion
    # 9/5 = 1.8, donc C * 1.8 + 32
    fahrenheit = celsius * 9/5 + 32

    # round(valeur, 2) arrondit à 2 décimales
    fahrenheit_rounded = round(fahrenheit, 2)

    # Affichage
    print(f"{celsius}°C = {fahrenheit_rounded}°F")


# =============================================================================
# EXERCICE 1.6 - PÉRIMÈTRE ET AIRE D'UN CARRÉ
# =============================================================================
def exercice_1_6():
    """
    Solution de l'exercice 1.6
    Calcule le périmètre et l'aire d'un carré.
    """
    # Récupération du côté
    cote = float(input("Longueur du côté: "))

    # Calculs
    # Périmètre = côté × 4
    perimetre = cote * 4
    # Aire = côté² (ou cote * cote ou cote ** 2)
    aire = cote ** 2

    # Affichage
    print(f"\nCarré de côté {cote}:")
    print(f"Périmètre: {perimetre}")
    print(f"Aire: {aire}")


# =============================================================================
# EXERCICE 1.7 - CALCUL DE LA MOYENNE DE 3 NOMBRES
# =============================================================================
def exercice_1_7():
    """
    Solution de l'exercice 1.7
    Calcule la moyenne de 3 nombres.
    """
    # Récupération des 3 notes
    note1 = float(input("Note 1: "))
    note2 = float(input("Note 2: "))
    note3 = float(input("Note 3: "))

    # Calcul de la moyenne
    # Moyenne = somme / nombre
    moyenne = (note1 + note2 + note3) / 3

    # Affichage
    print(f"Moyenne: {moyenne}")


# =============================================================================
# EXERCICE 1.8 - CALCULATEUR DE REMISE
# =============================================================================
def exercice_1_8():
    """
    Solution de l'exercice 1.8
    Calcule le prix après une remise de 20%.
    """
    # Prix original
    prix = float(input("Prix original: "))

    # Calcul de la remise (20% = 0.20)
    remise = prix * 0.20

    # Prix final
    prix_final = prix - remise

    # Affichage
    print(f"Remise (20%): {remise}")
    print(f"Prix final: {prix_final}")


# =============================================================================
# EXERCICE 1.9 - INFORMATIONS PERSONNELLES FORMATÉES
# =============================================================================
def exercice_1_9():
    """
    Solution de l'exercice 1.9
    Affiche une carte de visite formatée.
    """
    # Récupération des informations
    prenom = input("Prénom: ")
    nom = input("Nom: ")
    age = int(input("Âge: "))
    ville = input("Ville: ")

    # Conversion en majuscules pour le nom
    nom_maj = nom.upper()
    prenom_maj = prenom.upper()

    # Affichage avec bordures
    print(f"""
╔══════════════════════════════════╗
║     CARTE DE VISITE              ║
║  Nom: {nom_maj:<26}║
║  Prénom: {prenom_maj:<23}║
║  Âge: {age:<28}║
║  Ville: {ville:<25}║
╚══════════════════════════════════╝
""")

    # Note: La syntaxe {:<N} aligne le texte à gauche dans N caractères
    # C'est utile pour formatter les tableaux


# =============================================================================
# EXERCICE 1.10 - CALCULATEUR D'INTÉRÊTS SIMPLES
# =============================================================================
def exercice_1_10():
    """
    Solution de l'exercice 1.10
    Calcule les intérêts d'un placement bancaire.
    """
    # Données du placement
    capital = float(input("Capital initial: "))
    taux = float(input("Taux d'intérêt (%): "))
    temps = float(input("Durée (années): "))

    # Calcul des intérêts simples
    # Formule: I = C × t × n (où t est en décimal)
    interets = capital * (taux / 100) * temps

    # Capital final
    capital_final = capital + interets

    # Affichage
    print(f"\nRésultats:")
    print(f"Intérêts générés: {interets}")
    print(f"Capital final: {capital_final}")


# =============================================================================
# EXERCICE 1.11 - CONVERTISSEUR DE DEVISES
# =============================================================================
def exercice_1_11():
    """
    Solution de l'exercice 1.11
    Convertit des euros vers dollars.
    """
    # Taux de change
    taux_eur_usd = 1.10

    # Montant en euros
    euros = float(input("Montant en euros: "))

    # Conversion
    dollars = euros * taux_eur_usd

    # Affichage avec formatage
    print(f"{euros:.2f} EUR = {dollars:.2f} USD")

    # Note: {:.2f} formate avec exactement 2 décimales


# =============================================================================
# EXERCICE 1.12 - CALCUL DE L'IMC
# =============================================================================
def exercice_1_12():
    """
    Solution de l'exercice 1.12
    Calcule l'Indice de Masse Corporelle.
    """
    # Données
    poids = float(input("Poids (kg): "))
    taille = float(input("Taille (m): "))

    # Calcul de l'IMC
    # Formule: IMC = poids / taille²
    imc = poids / (taille ** 2)

    # Arrondir à 2 décimales
    imc_rounded = round(imc, 2)

    # Affichage
    print(f"IMC: {imc_rounded}")


# =============================================================================
# EXERCICE 1.13 - SIMULATEUR DE PANIER DE Courses
# =============================================================================
def exercice_1_13():
    """
    Solution de l'exercice 1.13
    Calcule le total d'un panier avec TVA.
    """
    # Prix des 3 articles
    prix1 = float(input("Prix article 1: "))
    prix2 = float(input("Prix article 2: "))
    prix3 = float(input("Prix article 3: "))

    # Calculs
    sous_total = prix1 + prix2 + prix3
    tva = sous_total * 0.20
    total = sous_total + tva

    # Affichage avec bordures
    print(f"""
╔══════════════════════════╗
║     RÉSUMÉ PANIER       ║
╠══════════════════════════╣
║ Sous-total: {sous_total:.2f} €     ║
║ TVA (20%): {tva:.2f} €       ║
║ Total: {total:.2f} €          ║
╚══════════════════════════╝
""")


# =============================================================================
# EXERCICE 1.14 - GÉNÉRATEUR DE COORDONNÉES
# =============================================================================
def exercice_1_14():
    """
    Solution de l'exercice 1.14
    Génère un email basé sur les informations utilisateur.
    """
    # Récupération des données
    prenom = input("Prénom: ")
    nom = input("Nom: ")
    domaine = input("Domaine: ")
    extension = input("Extension: ")

    # Nettoyage et formatage
    # .lower() convertit en minuscules
    # .strip() supprime les espaces au début et à la fin
    email = f"{prenom.lower().strip()}.{nom.lower().strip()}@{domaine.strip()}.{extension.strip()}"

    # Affichage
    print(f"\nEmail généré: {email}")


# =============================================================================
# EXERCICE 1.15 - CALCULATEUR DE TEMPS DE TRAJET
# =============================================================================
def exercice_1_15():
    """
    Solution de l'exercice 1.15
    Calcule le temps de trajet en fonction de la distance et de la vitesse.
    """
    # Données
    distance = float(input("Distance (km): "))
    vitesse = float(input("Vitesse moyenne (km/h): "))

    # Calcul du temps en heures
    temps_heures = distance / vitesse

    # Conversion en minutes
    temps_minutes = temps_heures * 60

    # Affichage
    print(f"\nRésultats:")
    print(f"Temps de trajet: {temps_heures:.2f} heures")
    print(f"soit {temps_minutes:.0f} minutes")


# =============================================================================
# BONUS: VERSION ALTERNATIVE PLUS CONCISE
# =============================================================================

# Vous pouvez souvent écrire le code de manière plus concise:

def exemple_concis():
    """Exemple de code concis pour les exercices 1.3 et 1.7."""
    # Tout sur une ligne quand c'est simple
    a, b = float(input("A: ")), float(input("B: "))
    print(f"Somme: {a + b}")

    # Moyenne avec list comprehension
    notes = [float(input(f"Note {i+1}: ")) for i in range(3)]
    print(f"Moyenne: {sum(notes) / len(notes)}")
