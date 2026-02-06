# =============================================================================
# CHAPITRE 4: CONTRÔLE DE FLUX - EXERCICES
# =============================================================================
# Niveau: DEBUTANT
# Concepts abordés: if/elif/else, match, ternaire, conditions composées
# =============================================================================

# =============================================================================
# EXERCICE 4.1 - CLASSIFICATION D'ÂGE SIMPLE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Demandez l'âge et affichez:
# - "Enfant" si < 12 ans
# - "Adolescent" si 12-17 ans
# - "Adulte" si 18-64 ans
# - "Senior" si >= 65 ans
#
# EXEMPLE:
# Âge: 25
# Adulte
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_1():
    pass


# =============================================================================
# EXERCICE 4.2 - CALCULATEUR DE PRIX AVEC TENDAIRE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Demandez un prix et appliquez une remise de 10%.
# Utilisez l'opérateur ternaire.
#
# EXEMPLE:
# Prix: 100
# Prix avec remise: 90.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_2():
    pass


# =============================================================================
# EXERCICE 4.3 - VÉRIFICATION DE SIGNE
# =============================================================================
# NIVEAU: ★☆☆☆☆ (Très facile)
#
# ÉNONCÉ:
# Vérifiez si un nombre est positif, négatif ou zéro.
# Utilisez if/elif/else.
#
# EXEMPLE:
# Nombre: -5
# Négatif
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_3():
    pass


# =============================================================================
# EXERCICE 4.4 - JOUR DE LA SEMAINE AVEC MATCH
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Demandez un jour (1-7) et affichez son nom.
# Utilisez l'opérateur match (Python 3.10+)
#
# 1: Lundi, 2: Mardi, 3: Mercredi, 4: Jeudi, 5:Vendredi, 6:Samedi, 7:Dimanche
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_4():
    pass


# =============================================================================
# EXERCICE 4.5 - CALCULATEUR DE REMISE PROGRESSIVE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Calculez la remise selon le montant:
# - > 500€: 20%
# - > 200€: 10%
# - > 100€: 5%
# - Sinon: 0%
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_5():
    pass


# =============================================================================
# EXERCICE 4.6 - VALIDATION DE MOT DE PASSE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Vérifiez si un mot de passe est valide:
# - Au moins 8 caractères
# - Contient une lettre minuscule
# - Contient une lettre majuscule
# - Contient un chiffre
#
# EXEMPLE:
# Mot de passe: Python123
# Valide: True
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_6():
    pass


# =============================================================================
# EXERCICE 4.7 - CLASSIFICATION DE FORMES AVEC MATCH
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ÉNONCÉ:
# Classifiez une forme géométrique selon le nombre de côtés (3-6).
# Utilisez match pour gérer:
# 3: Triangle, 4: Carré/Rectangle, 5: Pentagone, 6: Hexagone
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_7():
    pass


# =============================================================================
# EXERCICE 4.8 - CALCULATEUR DE TAXI
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Calculez le prix d'une course de taxi:
# - Prix de base: 4.50€
# - Prix au km: 1.10€
# - Supplément nuit (22h-6h): +20%
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_8():
    pass


# =============================================================================
# EXERCICE 4.9 - CONVERTISSEUR DE TEMPÉRATURE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Convertissez une température selon l'unité:
# - "C" ou "c": Celsius → Fahrenheit
# - "F" ou "f": Fahrenheit → Celsius
# - "K" ou "k": Celsius → Kelvin
#
# FORMULES:
# C → F: F = C × 9/5 + 32
# F → C: C = (F - 32) × 5/9
# C → K: K = C + 273.15
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_9():
    pass


# =============================================================================
# EXERCICE 4.10 - JEU DE DEVINETTE AVEC MATCH
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# L'ordinateur choisit un nombre entre 1 et 100.
# L'utilisateur devine avec des indices:
# - "Trop grand!"
# - "Trop petit!"
# - "Gagné!"
#
# INDICE: import random, random.randint(1, 100)
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_10():
    pass


# =============================================================================
# EXERCICE 4.11 - SIMULATEUR DE DISTRIBUTEUR
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Simulez un distributeur de boissons:
# - L'utilisateur choisit une boisson
# - Le système vérifie l'argent inséré
# - Rendu de monnaie si nécessaire
#
# BOISSONS:
# Eau: 1.00€, Café: 1.50€, Soda: 2.00€, Thé: 1.20€
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_11():
    pass


# =============================================================================
# EXERCICE 4.12 - ANALYSEUR DE CARACTÈRE AVEC MATCH
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ÉNONCÉ:
# Analysez un caractère avec match:
# - Voyelle (a, e, i, o, u, y)
# - Consonne
# - Chiffre
# - Caractère spécial
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_12():
    pass


# =============================================================================
# EXERCICE 4.13 - CALCULATEUR D'IMPÔTS SIMPLIFIÉ
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Calculez l'impôt sur le revenu simplifié:
# - 0-10000€: 0%
# - 10001-30000€: 10%
# - 30001-60000€: 20%
# - 60001€+: 30%
#
# EXEMPLE:
# Revenu: 50000
# Impôt: 4000.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_13():
    pass


# =============================================================================
# EXERCICE 4.14 - SYSTÈME DE NOTES AVEC MATCH
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ÉNONCÉ:
# Système de notation avancé avec match:
# - 0-9: F (Échec)
# - 10-11: D (Passable)
# - 12-13: C (Satisfaisant)
# - 14-15: B (Bien)
# - 16-17: A- (Très Bien)
# - 18-20: A+ (Excellent)
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_14():
    pass


# =============================================================================
# EXERCICE 4.15 - SIMULATEUR DE BANQUE
# =============================================================================
# NIVEAU: ★★★★★ (Très difficile)
#
# ÉNONCÉ:
# Gérez un compte bancaire avec:
# - Consultation du solde
# - Dépôt
# - Retrait (avec vérification du solde)
# - Virement (vers un autre compte)
#
# Affichez les opérations et le solde final.
#
# INDICE: Fonctions imbriquées avec conditions
#
# VOTRE CODE CI-DESSOUS:
def exercice_4_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 4 - EXERCICES")
    print("=" * 50)
    print("Exécutez python verification.py pour valider")
    print("=" * 50)
