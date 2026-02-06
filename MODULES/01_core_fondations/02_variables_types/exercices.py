# =============================================================================
# CHAPITRE 2: VARIABLES ET TYPES DE DONNÉES - EXERCICES
# =============================================================================
# Niveau: DEBUTANT
# Concepts abordés: variables, types, conversion, mutabilité
# =============================================================================

# =============================================================================
# EXERCICE 2.1 - AFFICHAGE DE VARIABLES
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Créez un programme qui déclare 4 variables:
# - nom (chaîne)
# - age (entier)
# - taille (décimal)
# - est_etudiant (booléen)
#
# Affichez-les dans ce format:
# Nom: [nom]
# Âge: [age]
# Taille: [taille] m
# Étudiant: [Oui/Non]
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_1():
    pass


# =============================================================================
# EXERCICE 2.2 - CONVERSION DE TEMPÉRATURE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Demandez une température en Fahrenheit et convertissez-la en Celsius.
# Affichez le résultat avec 1 décimale.
#
# FORMULE: C = (F - 32) × 5/9
#
# EXEMPLE:
# Température en Fahrenheit: 77
# 77.0°F = 25.0°C
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_2():
    pass


# =============================================================================
# EXERCICE 2.3 - CALCUL DE MOYENNE AVEC PRÉCISION
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez 4 nombres et calculez leur moyenne.
# Affichez la moyenne avec 2 décimales.
#
# EXEMPLE:
# Entrez 4 nombres: 10, 15, 20, 25
# Moyenne: 17.50
#
# CONTRAINTES:
# - Utiliser float pour les calculs
# - Afficher avec round(moyenne, 2)
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_3():
    pass


# =============================================================================
# EXERCICE 2.4 - VALIDATION D'ÂGE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez l'âge d'une personne et affichez:
# - Si elle est mineure (moins de 18 ans)
# - Si elle est majeure (18 ans ou plus)
#
# EXEMPLE:
# Âge: 15
# Mineur: True / Majeur: False
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_4():
    pass


# =============================================================================
# EXERCICE 2.5 - ANALYSEUR DE NOMBRE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez un nombre et affichez ses propriétés:
# - Type (int ou float)
# - Valeur absolue
# - Partie entière (si décimal)
# - Arrondi à l'entier le plus proche
#
# EXEMPLE:
# Nombre: -7.5
# Type: float
# Valeur absolue: 7.5
# Partie entière: 7
# Arrondi: -8
#
# INDICES: type(), abs(), int() (tronque), round()
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_5():
    pass


# =============================================================================
# EXERCICE 2.6 - MANIPULATION DE CHAÎNES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Demandez un mot et affichez:
# - Le mot en majuscules
# - Le mot en minuscules
# - La première lettre
# - La dernière lettre
# - Le mot inversé
# - La longueur du mot
#
# EXEMPLE:
# Mot: Python
# Majuscules: PYTHON
# Minuscules: python
# Première lettre: P
# Dernière lettre: n
# Inversé: nohtyP
# Longueur: 6
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_6():
    pass


# =============================================================================
# EXERCICE 2.7 - FORMATEUR DE PRIX
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Demandez un prix et affichez-le formaté:
# - Avec 2 décimales
# - Avec le symbole €
# - Séparateur de milliers
#
# EXEMPLE:
# Prix: 1234567.891
# Formaté: 1 234 567.89 €
#
# INDICE: f"{prix:,.2f} €" (utilise virgule comme séparateur)
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_7():
    pass


# =============================================================================
# EXERCICE 2.8 - CALCULATEUR DE BMR (BASAL METABOLIC RATE)
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Calculez le métabolisme de base (BMR) pour un homme.
#
# FORMULE (Harris-Benedict):
# BMR = 88.362 + (13.397 × poids_kg) + (4.799 × taille_cm) - (5.677 × age)
#
# EXEMPLE:
# Poids (kg): 70
# Taille (cm): 175
# Âge: 30
# BMR: ~1680 kcal/jour
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_8():
    pass


# =============================================================================
# EXERCICE 2.9 - VALIDATEUR D'EMAIL SIMPLIFIÉ
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Validez un email simplifié (doit contenir @ et .)
# Affichez True/False
#
# RÈGLES:
# - Doit contenir @
# - Doit contenir un point après @
# - Ne doit pas commencer ou finir par @
#
# EXEMPLE:
# Email: test@example.com
# Valide: True
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_9():
    pass


# =============================================================================
# EXERCICE 2.10 - CONVERTISSEUR DE DURÉE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Convertissez une durée en secondes vers:
# - Minutes et secondes
# - Heures, minutes et secondes
#
# EXEMPLE:
# Secondes: 3661
# Minutes: 61 minutes et 1 seconde
# Heures: 1 heure, 1 minute et 1 seconde
#
# INDICE: divmod(3661, 60) donne (61, 1)
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_10():
    pass


# =============================================================================
# EXERCICE 2.11 - CALCULATEUR D'INTÉRÊTS COMPOSÉS
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Calculez le capital final avec intérêts composés.
#
# FORMULE:
# Capital final = Capital × (1 + taux)^temps
#
# EXEMPLE:
# Capital initial: 1000
# Taux (%): 5
# Durée (années): 10
# Capital final: 1628.89 €
#
# CONTRAINTES:
# - Afficher avec 2 décimales
# - Afficher le montant des intérêts gagnés
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_11():
    pass


# =============================================================================
# EXERCICE 2.12 - GÉNÉRATEUR D'ACRONYME
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Créez un acronyme à partir d'une phrase.
#
# RÈGLES:
# - Prendre la première lettre de chaque mot
# - Les mettre en majuscules
# - Ignorer les mots courts (articles, prépositions)
#
# EXEMPLE:
# Phrase: "Python est vraiment génial"
# Acronyme: PEG
#
# INDICE: split() pour les mots, upper() pour majuscules
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_12():
    pass


# =============================================================================
# EXERCICE 2.13 - CONVERTISSEUR ROMAIN
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Convertissez un nombre entre 1 et 10 en chiffres romains.
#
# TABLEAU:
# 1 = I, 2 = II, 3 = III, 4 = IV, 5 = V
# 6 = VI, 7 = VII, 8 = VIII, 9 = IX, 10 = X
#
# EXEMPLE:
# Nombre: 7
# Chiffre romain: VII
#
# CONTRAINTES:
# - Gérer les erreurs si nombre hors plage
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_13():
    pass


# =============================================================================
# EXERCICE 2.14 - CALCULATEUR DE NOTE AVEC LETTRE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Convertissez une note numérique en lettre.
#
# BARÈME:
# 16-20: A (Excellent)
# 14-15.99: B (Très bien)
# 12-13.99: C (Bien)
# 10-11.99: D (Passable)
# 0-9.99: F (Insuffisant)
#
# EXEMPLE:
# Note: 14.5
# Lettre: B (Très bien)
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_14():
    pass


# =============================================================================
# EXERCICE 2.15 - CALCULATEUR DE POURCENTAGE DE VOTES
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Calculez les pourcentages de votes pour 3 candidats.
#
# EXEMPLE:
# Votes candidat A: 1500
# Votes candidat B: 2000
# Votes candidat C: 500
#
# Total: 4000
# A: 37.5%
# B: 50.0%
# C: 12.5%
#
# VOTRE CODE CI-DESSOUS:
def exercice_2_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 2 - EXERCICES")
    print("=" * 50)
    print("Exécutez python verification.py pour valider")
    print("=" * 50)
