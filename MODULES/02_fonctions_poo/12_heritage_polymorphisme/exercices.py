# =============================================================================
# CHAPITRE 12: HERITAGE ET POLYMORPHISME - EXERCICES
# =============================================================================
# Niveau: INTERMEDIAIRE
# Concepts abordes: heritage, polymorphisme, super(), classes abstraites
# =============================================================================

# =============================================================================
# EXERCICE 12.1 - HERITAGE SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Animal avec:
# - Attributs: nom, age
# - Methode: presenter() qui affiche "Je m'appelle X, j'ai Y ans"
# Creez une classe Chien qui herite d'Animal avec:
# - Attribut supplementaire: race
# - Methode: aboyer() qui affiche "Wouf!"
#
# EXEMPLE:
# medor = Chien("Medor", 5, "Berger")
# medor.presenter()  # "Je m'appelle Medor, j'ai 5 ans"
# medor.aboyer()     # "Wouf!"
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_1():
    pass


# =============================================================================
# EXERCICE 12.2 - SUPER() ET CONSTRUCTEUR
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Vehicule avec:
# - Attributs: marque, modele
# Creez une classe Voiture qui herite de Vehicule avec:
# - Attribut supplementaire: nombre de portes
# - Utilisez super() dans le constructeur
#
# EXEMPLE:
# ma_voiture = Voiture("Toyota", "Corolla", 4)
# print(f"{ma_voiture.marque} {ma_voiture.modele}")  # "Toyota Corolla"
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_2():
    pass


# =============================================================================
# EXERCICE 12.3 - METHODE DE SUBSTITUTION
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une classe Forme avec:
# - Methode: aire() qui retourne 0
# Creez des classes Carre, Triangle qui:
# - Substituent la methode aire()
#
# EXEMPLE:
# c = Carre(5)
# print(c.aire())  # 25
# t = Triangle(4, 3)
# print(t.aire())  # 6
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_3():
    pass


# =============================================================================
# EXERCICE 12.4 - APPELER LE PARENT
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe Employe avec:
# - Methode: calculer_salaire() qui retourne 2000
# Creez une classe Manager qui herite d'Employe avec:
# - Methode: calculer_salaire() qui retourne (salaire parent + 500)
#
# EXEMPLE:
# e = Employe()
# print(e.calculer_salaire())  # 2000
# m = Manager()
# print(m.calculer_salaire())  # 2500
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_4():
    pass


# =============================================================================
# EXERCICE 12.5 - POLYMORPHISME SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez des classes Chien, Chat, Oiseau avec:
# - Methode: parler() qui retourne "Wouf!", "Miaou!", "Cui-cui!"
# Creez une fonction faire_parler(animal) qui appelle animal.parler()
#
# EXEMPLE:
# animaux = [Chien(), Chat(), Oiseau()]
# for a in animaux:
#     print(faire_parler(a))
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_5():
    pass


# =============================================================================
# EXERCICE 12.6 - HIERARCHIE DE FORMES
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une hierarchie:
# - Forme (base)
#   - Rectangle (largeur, hauteur)
#   - Cercle (rayon)
#   - Triangle (base, hauteur)
# Chaque forme a une methode aire() et perimetre()
#
# EXEMPLE:
# r = Rectangle(4, 5)
# print(r.aire())      # 20
# c = Cercle(3)
# print(c.perimetre()) # 18.84...
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_6():
    pass


# =============================================================================
# EXERCICE 12.7 - HERITAGE MULTIPLE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez:
# - Classe Volant avec: methode voler()
# - Classe Nageant avec: methode nage()
# - Classe Canard qui herite des deux
# - Canard peut voler ET nager
#
# EXEMPLE:
# c = Canard()
# print(c.voler())   # "Je vole!"
# print(c.nage())    # "Je nage!"
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_7():
    pass


# =============================================================================
# EXERCICE 12.8 - MRO ET ORDRE D'HERITAGE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez un heritage en diamant:
#       A
#      / \
#     B   C
#      \ /
#       D
# Chaque classe a une methode test() qui affiche son nom
# Verifiez l'ordre MRO de D
#
# EXEMPLE:
# d = D()
# d.test()  # Affiche "D" puis les parents selon MRO
# print(D.mro())  # [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, ...]
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_8():
    pass


# =============================================================================
# EXERCICE 12.9 - CLASSE ABSTRAITE
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une classe abstraite Utilisateur avec:
# - Methode abstraite: get_permissions()
# - Methode concrete: se_presenter() qui affiche "Utilisateur"
# Creez classes Admin et User qui implementent get_permissions()
#
# EXEMPLE:
# admin = Admin()
# print(admin.get_permissions())  # ["read", "write", "delete"]
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_9():
    pass


# =============================================================================
# EXERCICE 12.10 - SYSTEME DE PAIEMENT
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme de paiement avec:
# - Classe abstraite Paiement avec:
#   - Methode abstraite: traiter(montant)
# - Classe CarteBancaire qui utilise carte et code
# - Classe PayPal qui utilise email
# - Classe Especes (pas de traitement reel)
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_10():
    pass


# =============================================================================
# EXERCICE 12.11 - HIERARCHIE D'EMPLOYES
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez:
# - Employe (nom, salaire)
#   - Developpeur (langage)
#   - Designer (logiciel)
#   - Manager (equipe)
#     - CTO (budget)
# Methode: decrire() polimorphique
#
# EXEMPLE:
# dev = Developpeur("Alice", 50000, "Python")
# mgr = Manager("Bob", 70000, [dev])
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_11():
    pass


# =============================================================================
# EXERCICE 12.12 - DUCK TYPING
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez des classes независимые (sans heritage commun):
# - Canard (methode: nager())
# - Bateau (methode: nager())
# - Fonction faire_nager(obj) qui appelle obj.nager()
# Demontrer le duck typing
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_12():
    pass


# =============================================================================
# EXERCICE 12.13 - __STR__ ET __REPR__ AVEC HERITAGE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe Person avec nom, age
# - Methode: __str__ et __repr__
# Creez une classe Employe(Person) avec poste, salaire
# - Methode: __str__ qui utilise super()
#
# EXEMPLE:
# p = Person("Alice", 30)
# print(str(p))    # "Person: Alice (30 ans)"
# print(repr(p))   # "Person('Alice', 30)"
# e = Employe("Bob", 25, "Dev")
# print(str(e))    # "Employe: Bob (25 ans) - Dev"
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_13():
    pass


# =============================================================================
# EXERCICE 12.14 - COMPARAISON ET HERITAGE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe Crochet avec __eq__, __lt__, etc.
# - Deux objets sont egaux si meme type et meme attributs
# Methode: __hash__ aussi
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_14():
    pass


# =============================================================================
# EXERCICE 12.15 - SYSTEME DE NOTIFICATIONS
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme de notifications:
# - Classe abstraite Notificateur avec:
#   - Methode abstraite: envoyer(message)
# - Classe Email, SMS, Push avec leurs specifics
# - Classe NotificationBuilder pour composer
#
# VOTRE CODE CI-DESSOUS:
def exercice_12_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 12 - EXERCICES")
    print("=" * 50)
    print("Exercices disponibles:")
    print("  12.1 - Heritage simple")
    print("  12.2 - Super() et constructeur")
    print("  12.3 - Methode de substitution")
    print("  12.4 - Appeler le parent")
    print("  12.5 - Polymorphisme simple")
    print("  12.6 - Hierarchie de formes")
    print("  12.7 - Heritage multiple")
    print("  12.8 - MRO et heritage")
    print("  12.9 - Classe abstraite")
    print("  12.10 - Systeme de paiement")
    print("  12.11 - Hierarchie d'employes")
    print("  12.12 - Duck typing")
    print("  12.13 - __str__ et __repr__ avec heritage")
    print("  12.14 - Comparaison et heritage")
    print("  12.15 - Systeme de notifications")
    print("=" * 50)
