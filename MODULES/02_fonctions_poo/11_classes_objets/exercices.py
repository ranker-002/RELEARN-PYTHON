# =============================================================================
# CHAPITRE 11: CLASSES ET OBJETS - EXERCICES
# =============================================================================
# Niveau: INTERMEDIAIRE
# Concepts abordes: classes, objets, attributs, methodes, __init__, @property
# =============================================================================

# =============================================================================
# EXERCICE 11.1 - CLASSE SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Chien avec:
# - Attributs: nom, race
# - Methode: aboyer() qui affiche "Wouf!"
#
# EXEMPLE:
# medor = Chien("Medor", "Berger Allemand")
# medor.aboyer()  # Affiche "Wouf!"
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_1():
    pass


# =============================================================================
# EXERCICE 11.2 - CLASSE AVEC CONSTRUCTEUR
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Rectangle avec:
# - Constructeur: largeur, hauteur
# - Methode: aire() qui retourne l'aire
#
# EXEMPLE:
# r = Rectangle(5, 3)
# print(r.aire())  # 15
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_2():
    pass


# =============================================================================
# EXERCICE 11.3 - ATTRIBUTS ET METHODES
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe CompteBancaire avec:
# - Attributs: titulaire, solde
# - Methodes: deposer(montant), retirer(montant), afficher()
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_3():
    pass


# =============================================================================
# EXERCICE 11.4 - VALEURS PAR DEFAUT
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Livre avec:
# - Attributs: titre, auteur (obligatoires)
# - Annee et prix (avec valeurs par defaut)
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_4():
    pass


# =============================================================================
# EXERCICE 11.5 - METHODE DE CLASSE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Temperature avec:
# - Attribut: celsius
# - Methode de classe: from_fahrenheit(f) pour creer depuis Fahrenheit
#
# FORMULE: C = (F - 32) * 5/9
#
# EXEMPLE:
# t = Temperature.from_fahrenheit(32)
# print(t.celsius)  # 0.0
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_5():
    pass


# =============================================================================
# EXERCICE 11.6 - METHODE STATIQUE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe MathUtils avec:
# - est_premier(n)
# - factorielle(n)
# - Ces deux methodes doivent etre statiques (pas de self)
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_6():
    pass


# =============================================================================
# EXERCICE 11.7 - PROPRIETE SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Personne avec:
# - Attributs prives: _nom, _age
# - Proprietes: nom (lecture seule), age (lecture/écriture)
# - Si age < 0, levez une ValueError
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_7():
    pass


# =============================================================================
# EXERCICE 11.8 - PROPRIETE CALCULEE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Rectangle avec propriete calculee:
# - Attributs: largeur, hauteur
# - Proprietes: aire, perimetre, est_carre
#
# EXEMPLE:
# r = Rectangle(5, 5)
# print(r.aire)         # 25
# print(r.est_carre)    # True
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_8():
    pass


# =============================================================================
# EXERCICE 11.9 - ATTRIBUT DE CLASSE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Compteur avec:
# - Attribut de classe: total (compte toutes les instances)
# - Attribut d'instance: valeur
# - Incrementez total a chaque creation
#
# EXEMPLE:
# c1 = Compteur(10)
# c2 = Compteur(20)
# print(Compteur.total)  # 2
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_9():
    pass


# =============================================================================
# EXERCICE 11.10 - __STR__ ET __REPR__
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Ajoutez les methodes __str__ et __repr__ a la classe Voiture:
# - __str__: "Marque Modele (Annee)"
# - __repr__: "Voiture('Marque', 'Modele', Annee)"
#
# EXEMPLE:
# v = Voiture("Toyota", "Corolla", 2022)
# print(str(v))    # "Toyota Corolla (2022)"
# print(repr(v))   # "Voiture('Toyota', 'Corolla', 2022)"
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_10():
    pass


# =============================================================================
# EXERCICE 11.11 - VALIDATION DANS LE SETTER
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une classe MotDePasse avec:
# - Propriete mot_de_passe avec setter qui verifie:
#   - Au moins 8 caracteres
#   - Au moins une majuscule
#   - Au moins un chiffre
# - Sinon levez ValueError
#
# EXEMPLE:
# mdp = MotDePasse()
# mdp.mot_de_passe = "Python123"  # Valide
# mdp.mot_de_passe = "abc"        # ValueError
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_11():
    pass


# =============================================================================
# EXERCICE 11.12 - CLASSE COMPLETE: ETUDIANT
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une classe Etudiant avec:
# - Attributs: nom, notes (liste)
# - Moyenne calculee via propriete
# - Methode: ajouter_note(note)
# - Methode: est_recu() (moyenne >= 10)
#
# EXEMPLE:
# e = Etudiant("Alice")
# e.ajouter_note(15)
# e.ajouter_note(12)
# print(e.moyenne)      # 13.5
# print(e.est_recu())   # True
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_12():
    pass


# =============================================================================
# EXERCICE 11.13 - CLASSE COMPLETE: BANQUE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme bancaire avec:
# - Classe CompteBancaire avec:
#   - Titulaire, solde (propriete)
#   - Methodes: deposer, retirer, frais_bancaires()
# - Classe CompteEpargne (herite de CompteBancaire):
#   - Attribut: taux_interet
#   - Methode: ajouter_interets()
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_13():
    pass


# =============================================================================
# EXERCICE 11.14 - CLASSE INVENTAIRE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe Produit avec:
# - Attributs: nom, prix, quantite
# - Proprietes: valeur_totale (prix * quantite)
# - Methode: __str__ formate
# - Methode: __eq__ compare nom et prix
#
# EXEMPLE:
# p1 = Produit("Pomme", 1.50, 100)
# p2 = Produit("Pomme", 1.50, 50)
# print(p1 == p2)  # True (meme nom et prix)
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_14():
    pass


# =============================================================================
# EXERCICE 11.15 - SYSTEME DE GESTION
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme de gestion avec:
# - Classe Employe avec:
#   - nom, salaire, poste
#   - propriete: bonus (20% du salaire si poste == "manager")
#   - methode: augmenter_pourcentage(pourcentage)
# - Classe Departement avec:
#   - nom, liste d'employes
#   - methode: masse_salaire()
#   - methode: trouver_max_salaire()
#
# VOTRE CODE CI-DESSOUS:
def exercice_11_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 11 - EXERCICES")
    print("=" * 50)
    print("Executez python verification.py pour valider")
    print("=" * 50)
