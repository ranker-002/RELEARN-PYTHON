# =============================================================================
# CHAPITRE 12: HERITAGE ET POLYMORPHISME - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 12.1 - HERITAGE SIMPLE
# =============================================================================
def exercice_12_1():
    """Demonstration de l'heritage simple."""
    class Animal:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age
        
        def presenter(self):
            return f"Je m'appelle {self.nom}, j'ai {self.age} ans"
    
    class Chien(Animal):
        def __init__(self, nom, age, race):
            super().__init__(nom, age)
            self.race = race
        
        def aboyer(self):
            return "Wouf!"
    
    medor = Chien("Medor", 5, "Berger")
    print(medor.presenter())
    print(medor.aboyer())


# =============================================================================
# EXERCICE 12.2 - SUPER() ET CONSTRUCTEUR
# =============================================================================
def exercice_12_2():
    """Utilisation de super() dans le constructeur."""
    class Vehicule:
        def __init__(self, marque, modele):
            self.marque = marque
            self.modele = modele
    
    class Voiture(Vehicule):
        def __init__(self, marque, modele, portes):
            super().__init__(marque, modele)
            self.portes = portes
        
        def __str__(self):
            return f"{self.marque} {self.modele} ({self.portes} portes)"
    
    ma_voiture = Voiture("Toyota", "Corolla", 4)
    print(ma_voiture)


# =============================================================================
# EXERCICE 12.3 - METHODE DE SUBSTITUTION
# =============================================================================
def exercice_12_3():
    """Substitution de methode dans les classes derivees."""
    class Forme:
        def aire(self):
            return 0
    
    class Carre(Forme):
        def __init__(self, cote):
            self.cote = cote
        
        def aire(self):
            return self.cote ** 2
    
    class Triangle(Forme):
        def __init__(self, base, hauteur):
            self.base = base
            self.hauteur = hauteur
        
        def aire(self):
            return (self.base * self.hauteur) / 2
    
    c = Carre(5)
    t = Triangle(4, 3)
    print(f"Carre: {c.aire()}")     # 25
    print(f"Triangle: {t.aire()}")  # 6


# =============================================================================
# EXERCICE 12.4 - APPELER LE PARENT
# =============================================================================
def exercice_12_4():
    """Appeler la methode du parent avec super()."""
    class Employe:
        def calculer_salaire(self):
            return 2000
    
    class Manager(Employe):
        def calculer_salaire(self):
            return super().calculer_salaire() + 500
    
    e = Employe()
    m = Manager()
    print(f"Employe: {e.calculer_salaire()}")  # 2000
    print(f"Manager: {m.calculer_salaire()}")  # 2500


# =============================================================================
# EXERCICE 12.5 - POLYMORPHISME SIMPLE
# =============================================================================
def exercice_12_5():
    """Demonstration du polymorphisme."""
    class Chien:
        def parler(self):
            return "Wouf!"
    
    class Chat:
        def parler(self):
            return "Miaou!"
    
    class Oiseau:
        def parler(self):
            return "Cui-cui!"
    
    def faire_parler(animal):
        return animal.parler()
    
    animaux = [Chien(), Chat(), Oiseau()]
    for animal in animaux:
        print(faire_parler(animal))


# =============================================================================
# EXERCICE 12.6 - HIERARCHIE DE FORMES
# =============================================================================
def exercice_12_6():
    """Hierarchie de classes avec substitution de methodes."""
    import math
    
    class Forme:
        def aire(self):
            pass
        
        def perimetre(self):
            pass
    
    class Rectangle(Forme):
        def __init__(self, largeur, hauteur):
            self.largeur = largeur
            self.hauteur = hauteur
        
        def aire(self):
            return self.largeur * self.hauteur
        
        def perimetre(self):
            return 2 * (self.largeur + self.hauteur)
    
    class Cercle(Forme):
        def __init__(self, rayon):
            self.rayon = rayon
        
        def aire(self):
            return math.pi * self.rayon ** 2
        
        def perimetre(self):
            return 2 * math.pi * self.rayon
    
    class Triangle(Forme):
        def __init__(self, base, hauteur):
            self.base = base
            self.hauteur = hauteur
        
        def aire(self):
            return (self.base * self.hauteur) / 2
        
        def perimetre(self):
            return 3 * self.base  # Triangle equilateral
    
    r = Rectangle(4, 5)
    c = Cercle(3)
    t = Triangle(4, 3)
    
    print(f"Rectangle aire: {r.aire()}, perimetre: {r.perimetre()}")
    print(f"Cercle aire: {c.aire():.2f}, perimetre: {c.perimetre():.2f}")
    print(f"Triangle aire: {t.aire()}, perimetre: {t.perimetre()}")


# =============================================================================
# EXERCICE 12.7 - HERITAGE MULTIPLE
# =============================================================================
def exercice_12_7():
    """Heritage multiple en Python."""
    class Volant:
        def voler(self):
            return "Je vole!"
    
    class Nageant:
        def nager(self):
            return "Je nage!"
    
    class Canard(Volant, Nageant):
        pass
    
    c = Canard()
    print(c.voler())   # "Je vole!"
    print(c.nager())   # "Je nage!"
    print(f"MRO: {Canard.mro()}")


# =============================================================================
# EXERCICE 12.8 - MRO ET ORDRE D'HERITAGE
# =============================================================================
def exercice_12_8():
    """Heritage en diamant et MRO."""
    class A:
        def test(self):
            print("A")
            return "A"
    
    class B(A):
        def test(self):
            print("B")
            super().test()
            return "B"
    
    class C(A):
        def test(self):
            print("C")
            super().test()
            return "C"
    
    class D(B, C):
        def test(self):
            print("D")
            super().test()
            return "D"
    
    d = D()
    print("\nAppel de test():")
    resultat = d.test()
    print(f"\nMRO: {D.mro()}")


# =============================================================================
# EXERCICE 12.9 - CLASSE ABSTRAITE
# =============================================================================
def exercice_12_9():
    """Classes abstraites avec ABC."""
    from abc import ABC, abstractmethod
    
    class Utilisateur(ABC):
        def se_presenter(self):
            return "Utilisateur"
        
        @abstractmethod
        def get_permissions(self):
            pass
    
    class Admin(Utilisateur):
        def get_permissions(self):
            return ["read", "write", "delete"]
    
    class User(Utilisateur):
        def get_permissions(self):
            return ["read"]
    
    admin = Admin()
    user = User()
    print(f"Admin: {admin.get_permissions()}")
    print(f"User: {user.get_permissions()}")


# =============================================================================
# EXERCICE 12.10 - SYSTEME DE PAIEMENT
# =============================================================================
def exercice_12_10():
    """Systeme de paiement avec heritage."""
    from abc import ABC, abstractmethod
    
    class Paiement(ABC):
        @abstractmethod
        def traiter(self, montant):
            pass
    
    class CarteBancaire(Paiement):
        def __init__(self, carte, code):
            self.carte = carte
            self.code = code
        
        def traiter(self, montant):
            return f"Carte {self.carte}: {montant}€ traite"
    
    class PayPal(Paiement):
        def __init__(self, email):
            self.email = email
        
        def traiter(self, montant):
            return f"PayPal {self.email}: {montant}€ traite"
    
    class Especes(Paiement):
        def traiter(self, montant):
            return f"Especes: {montant}€ recu"
    
    paiements = [
        CarteBancaire("1234", "123"),
        PayPal("test@email.com"),
        Especes()
    ]
    
    for p in paiements:
        print(p.traiter(100))


# =============================================================================
# EXERCICE 12.11 - HIERARCHIE D'EMPLOYES
# =============================================================================
def exercice_12_11():
    """Hierarchie d'employes avec polymorphisme."""
    class Employe:
        def __init__(self, nom, salaire):
            self.nom = nom
            self._salaire = salaire
        
        def decrire(self):
            return f"{self.nom}, {self._salaire}€"
        
        def augmenter(self, pourcentage):
            self._salaire *= (1 + pourcentage / 100)
    
    class Developpeur(Employe):
        def __init__(self, nom, salaire, langage):
            super().__init__(nom, salaire)
            self.langage = langage
        
        def decrire(self):
            return f"{super().decrire()} - Developpeur {self.langage}"
    
    class Designer(Employe):
        def __init__(self, nom, salaire, logiciel):
            super().__init__(nom, salaire)
            self.logiciel = logiciel
        
        def decrire(self):
            return f"{super().decrire()} - Designer {self.logiciel}"
    
    class Manager(Employe):
        def __init__(self, nom, salaire, equipe=None):
            super().__init__(nom, salaire)
            self.equipe = equipe or []
        
        def decrire(self):
            return f"{super().decrire()} - Manager ({len(self.equipe)} employes)"
        
        def ajouter_employe(self, employe):
            self.equipe.append(employe)
    
    dev = Developpeur("Alice", 50000, "Python")
    designer = Designer("Bob", 45000, "Figma")
    mgr = Manager("Charlie", 70000)
    
    print(dev.decrire())
    print(designer.decrire())
    print(mgr.decrire())


# =============================================================================
# EXERCICE 12.12 - DUCK TYPING
# =============================================================================
def exercice_12_12():
    """Demonstration du duck typing."""
    class Canard:
        def nager(self):
            return "Le canard nage"
        
        def voler(self):
            return "Le canard vole"
    
    class Bateau:
        def nager(self):
            return "Le bateau flotte"
        
        def avancer(self):
            return "Le bateau avance"
    
    class SousMarin:
        def nager(self):
            return "Le sous-marin plonge"
    
    def faire_nager(obj):
        return obj.nager()
    
    def faire_avancer(obj):
        return obj.avancer()
    
    c = Canard()
    b = Bateau()
    s = SousMarin()
    
    print(faire_nager(c))  # Le canard nage
    print(faire_nager(b))  # Le bateau flotte
    print(faire_nager(s))  # Le sous-marin plonge
    
    # Canard peut aussi voler et avancer via duck typing
    print(c.voler())
    b.avancer()


# =============================================================================
# EXERCICE 12.13 - __STR__ ET __REPR__ AVEC HERITAGE
# =============================================================================
def exercice_12_13():
    """__str__ et __repr__ avec heritage."""
    class Person:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age
        
        def __str__(self):
            return f"Person: {self.nom} ({self.age} ans)"
        
        def __repr__(self):
            return f"Person('{self.nom}', {self.age})"
    
    class Employe(Person):
        def __init__(self, nom, age, poste, salaire):
            super().__init__(nom, age)
            self.poste = poste
            self.salaire = salaire
        
        def __str__(self):
            return f"Employe: {self.nom} ({self.age} ans) - {self.poste}"
        
        def __repr__(self):
            return f"Employe('{self.nom}', {self.age}, '{self.poste}', {self.salaire})"
    
    p = Person("Alice", 30)
    e = Employe("Bob", 25, "Dev", 50000)
    
    print("Person:")
    print(f"  str: {str(p)}")
    print(f"  repr: {repr(p)}")
    
    print("Employe:")
    print(f"  str: {str(e)}")
    print(f"  repr: {repr(e)}")


# =============================================================================
# EXERCICE 12.14 - COMPARAISON ET HERITAGE
# =============================================================================
def exercice_12_14():
    """Methodes de comparaison avec heritage."""
    class Crochet:
        def __init__(self, taille, couleur):
            self.taille = taille
            self.couleur = couleur
        
        def __eq__(self, autre):
            if type(self) != type(autre):
                return False
            return self.taille == autre.taille and self.couleur == autre.couleur
        
        def __lt__(self, autre):
            if type(self) != type(autre):
                return NotImplemented
            return self.taille < autre.taille
        
        def __le__(self, autre):
            return self == autre or self < autre
        
        def __gt__(self, autre):
            if type(self) != type(autre):
                return NotImplemented
            return self.taille > autre.taille
        
        def __ge__(self, autre):
            return self == autre or self > autre
        
        def __ne__(self, autre):
            return not self.__eq__(autre)
        
        def __hash__(self):
            return hash((self.taille, self.couleur))
    
    c1 = Crochet(5, "rouge")
    c2 = Crochet(5, "rouge")
    c3 = Crochet(3, "bleu")
    
    print(f"c1 == c2: {c1 == c2}")  # True
    print(f"c1 == c3: {c1 == c3}")  # False
    print(f"c1 < c3: {c1 < c3}")    # False
    print(f"c1 > c3: {c1 > c3}")    # True


# =============================================================================
# EXERCICE 12.15 - SYSTEME DE NOTIFICATIONS
# =============================================================================
def exercice_12_15():
    """Systeme de notifications avec heritage et polymorphisme."""
    from abc import ABC, abstractmethod
    
    class Notificateur(ABC):
        @abstractmethod
        def envoyer(self, message):
            pass
    
    class Email(Notificateur):
        def __init__(self, destinataire):
            self.destinaire = destinataire
        
        def envoyer(self, message):
            return f"Email a {self.destinaire}: {message}"
    
    class SMS(Notificateur):
        def __init__(self, telephone):
            self.telephone = telephone
        
        def envoyer(self, message):
            return f"SMS a {self.telephone}: {message[:160]}..."
    
    class Push(Notificateur):
        def __init__(self, appareil):
            self.appareil = appareil
        
        def envoyer(self, message):
            return f"Push a {self.appareil}: {message}"
    
    class NotificationBuilder:
        def __init__(self):
            self.notifications = []
        
        def ajouter_notification(self, notificateur):
            self.notifications.append(notificateur)
        
        def envoyer_tous(self, message):
            for n in self.notifications:
                print(n.envoyer(message))
    
    builder = NotificationBuilder()
    builder.ajouter_notification(Email("user@email.com"))
    builder.ajouter_notification(SMS("+123456789"))
    builder.ajouter_notification(Push("iphone"))
    
    builder.envoyer_tous("Alerte: Mise a jour disponible!")
