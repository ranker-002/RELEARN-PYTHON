# =============================================================================
# CHAPITRE 1: PREMIERS PAS AVEC PYTHON - EXERCICES
# =============================================================================
# Niveau: DEBUTANT
# Concepts abordés: print(), input(), variables, types de base, opérateurs
# =============================================================================

# REMARQUE: Écrivez votre code dans le dossier EXERCICES/projets/
# Utilisez les solutions pour vérifier vos réponses

# =============================================================================
# EXERCICE 1.1 - VOTRE PREMIER PROGRAMME
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Créez un programme qui affiche "Hello, World!" à l'écran.
#
# CONSEIL: Utilisez la fonction print()
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_1():
    pass


# =============================================================================
# EXERCICE 1.2 - PRÉSENTATION
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Demandez à l'utilisateur son prénom et affichez:
# "Bonjour [prénom] ! Bienvenue dans le monde de Python !"
#
# CONTRAINTES:
# - Utiliser la fonction input() pour récupérer le prénom
# - Afficher exactement le format demandé
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_2():
    pass


# =============================================================================
# EXERCICE 1.3 - CALCUL SIMPLE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Demandez deux nombres à l'utilisateur et affichez leur somme.
#
# EXEMPLE D'EXÉCUTION:
# Entrez le premier nombre: 5
# Entrez le deuxième nombre: 3
# La somme est: 8
#
# CONTRAINTES:
# - Utiliser float() pour permettre les nombres décimaux
# - Afficher exactement "La somme est: [résultat]"
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_3():
    pass


# =============================================================================
# EXERCICE 1.4 - CALCULATRICE POLYVALENTE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez deux nombres et effectuez les 4 opérations de base:
# addition, soustraction, multiplication et division.
#
# EXEMPLE D'EXÉCUTION:
# Nombre 1: 10
# Nombre 2: 2
#
# Résultats:
# Addition: 12
# Soustraction: 8
# Multiplication: 20
# Division: 5.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_4():
    pass


# =============================================================================
# EXERCICE 1.5 - CONVERSION DE TEMPÉRATURE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Convertissez une température de Celsius vers Fahrenheit.
# Formule: F = C × 9/5 + 32
#
# EXEMPLE D'EXÉCUTION:
# Température en Celsius: 25
# 25°C = 77.0°F
#
# CONTRAINTES:
# - Arrondir le résultat à 2 décimales
# - Afficher "X°C = Y°F" où X est la valeur saisie
#
# INDICE: Utilisez round(valeur, 2)
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_5():
    pass


# =============================================================================
# EXERCICE 1.6 - PÉRIMÈTRE ET AIRE D'UN CARRÉ
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez la longueur du côté d'un carré et calculez:
# - Son périmètre (côté × 4)
# - Son aire (côté²)
#
# EXEMPLE D'EXÉCUTION:
# Longueur du côté: 5
#
# Carré de côté 5:
# Périmètre: 20
# Aire: 25
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_6():
    pass


# =============================================================================
# EXERCICE 1.7 - CALCUL DE LA MOYENNE DE 3 NOMBRES
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez 3 nombres à l'utilisateur et affichez leur moyenne.
#
# EXEMPLE D'EXÉCUTION:
# Note 1: 15
# Note 2: 12
# Note 3: 18
# Moyenne: 15.0
#
# CONTRAINTES:
# - Calculer la moyenne (somme / 3)
# - Afficher "Moyenne: [résultat]"
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_7():
    pass


# =============================================================================
# EXERCICE 1.8 - CALCULATEUR DE REMISE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Un magasin offre 20% de remise sur tous ses produits.
# Calculez le prix final après remise.
#
# EXEMPLE D'EXÉCUTION:
# Prix original: 100
# Remise (20%): 20
# Prix final: 80
#
# FORMULE:
# remise = prix * 0.20
# prix_final = prix - remise
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_8():
    pass


# =============================================================================
# EXERCICE 1.9 - INFORMATIONS PERSONNELLES FORMATÉES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Demandez à l'utilisateur:
# - Son prénom
# - Son nom
# - Son âge
# - Sa ville
#
# Affichez ces informations dans un format de carte de visite:
# ╔══════════════════════════════════╗
# ║     CARTE DE VISITE              ║
# ║  Nom: DUPONT                    ║
# ║  Prénom: Jean                   ║
# ║  Âge: 30 ans                    ║
# ║  Ville: Paris                   ║
# ╚══════════════════════════════════╝
#
# CONTRAINTES:
# - Convertir le nom et prénom en majuscules
# - Afficher exactement ce format avec les bordures
#
# INDICE: Utilisez f-strings pour le formattage
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_9():
    pass


# =============================================================================
# EXERCICE 1.10 - CALCULATEUR D'INTÉRÊTS SIMPLES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Calculez les intérêts d'un placement bancaire.
#
# FORMULE:
# intérêts = capital × taux × temps
#
# EXEMPLE D'EXÉCUTION:
# Capital initial: 1000
# Taux d'intérêt (%): 5
# Durée (années): 2
#
# Résultats:
# Intérêts générés: 100.0
# Capital final: 1100.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_10():
    pass


# =============================================================================
# EXERCICE 1.11 - CONVERTISSEUR DE DEVISES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Convertissez un montant d'euros vers dollars.
# Taux de change: 1 EUR = 1.10 USD
#
# EXEMPLE D'EXÉCUTION:
# Montant en euros: 50
# 50.00 EUR = 55.00 USD
#
# CONTRAINTES:
# - Arrondir à 2 décimales
# - Afficher avec le format exact
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_11():
    pass


# =============================================================================
# EXERCICE 1.12 - CALCUL DE L'IMC (INDICE DE MASSE CORPORELLE)
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Calculez l'IMC d'une personne.
#
# FORMULE:
# IMC = poids (kg) / (taille (m))²
#
# EXEMPLE D'EXÉCUTION:
# Poids (kg): 70
# Taille (m): 1.75
# IMC: 22.86
#
# CONTRAINTES:
# - Arrondir à 2 décimales
# - Afficher "IMC: [valeur]"
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_12():
    pass


# =============================================================================
# EXERCICE 1.13 - SIMULATEUR DE PANIER DE Courses
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Un client achète 3 articles avec des prix différents.
# Calculez le sous-total, la TVA (20%), et le total.
#
# EXEMPLE D'EXÉCUTION:
# Prix article 1: 10
# Prix article 2: 25
# Prix article 3: 15
#
# ╔══════════════════════════╗
# ║     RÉSUMÉ PANIER       ║
# ╠══════════════════════════╣
# ║ Sous-total: 50.00 €     ║
# ║ TVA (20%): 10.00 €      ║
# ║ Total: 60.00 €          ║
# ╚══════════════════════════╝
#
# CONTRAINTES:
# - Afficher dans ce format exact
# - Utiliser les bordures comme indiqué
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_13():
    pass


# =============================================================================
# EXERCICE 1.14 - GÉNÉRATEUR DE COORDONNÉES
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Générez un pseudo-email basé sur les informations d'un utilisateur.
#
# RÈGLE:
# Format: prenom.nom@domaine.extension
# - Prénom en minuscules
# - Nom en minuscules
# - Les espaces supprimés
#
# EXEMPLE D'EXÉCUTION:
# Prénom: Jean
# Nom: Dupont
# Domaine: exemple
# Extension: com
#
# Email généré: jean.dupont@exemple.com
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_14():
    pass


# =============================================================================
# EXERCICE 1.15 - CALCULATEUR DE TEMPS DE TRAJET
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Calculez le temps de trajet en fonction de la distance et de la vitesse.
#
# FORMULES:
# Temps (heures) = Distance / Vitesse
# Temps (minutes) = Temps (heures) × 60
#
# EXEMPLE D'EXÉCUTION:
# Distance (km): 120
# Vitesse moyenne (km/h): 60
#
# Résultats:
# Temps de trajet: 2.00 heures
# soit 120 minutes
#
# VOTRE CODE CI-DESSOUS:
def exercice_1_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE (Ne pas modifier)
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 1 - EXERCICES")
    print("=" * 50)

    exercices = [
        ("1.1 - Premier programme", exercice_1_1),
        ("1.2 - Présentation", exercice_1_2),
        ("1.3 - Calcul simple", exercice_1_3),
        ("1.4 - Calculatrice", exercice_1_4),
        ("1.5 - Température", exercice_1_5),
        ("1.6 - Périmètre et aire", exercice_1_6),
        ("1.7 - Moyenne", exercice_1_7),
        ("1.8 - Calculateur remise", exercice_1_8),
        ("1.9 - Carte de visite", exercice_1_9),
        ("1.10 - Intérêts simples", exercice_1_10),
        ("1.11 - Convertisseur", exercice_1_11),
        ("1.12 - IMC", exercice_1_12),
        ("1.13 - Panier courses", exercice_1_13),
        ("1.14 - Email", exercice_1_14),
        ("1.15 - Temps trajet", exercice_1_15),
    ]

    for nom, fonction in exercices:
        print(f"\n{nom}")
        print("-" * 30)
        try:
            fonction()
            print("✓ Exécuté avec succès")
        except Exception as e:
            print(f"✗ Erreur: {e}")

    print("\n" + "=" * 50)
    print("Pour compléter les exercices, écrivez votre")
    print("code dans le dossier EXERCICES/projets/")
    print("=" * 50)
