# =============================================================================
# CHAPITRE 11: CLASSES ET OBJETS - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 11.1 - CLASSE SIMPLE
# =============================================================================
def exercice_11_1():
    """Demonstration d'une classe simple."""
    class Chien:
        def __init__(self, nom, race):
            self.nom = nom
            self.race = race
        
        def aboyer(self):
            print("Wouf!")
    
    medor = Chien("Medor", "Berger Allemand")
    print(f"{medor.nom} est un {medor.race}")
    medor.aboyer()


# =============================================================================
# EXERCICE 11.2 - CLASSE AVEC CONSTRUCTEUR
# =============================================================================
def exercice_11_2():
    """Classe Rectangle avec aire."""
    class Rectangle:
        def __init__(self, largeur, hauteur):
            self.largeur = largeur
            self.hauteur = hauteur
        
        def aire(self):
            return self.largeur * self.hauteur
    
    r = Rectangle(5, 3)
    print(f"Aire de 5x3: {r.aire()}")  # 15


# =============================================================================
# EXERCICE 11.3 - ATTRIBUTS ET METHODES
# =============================================================================
def exercice_11_3():
    """Classe CompteBancaire."""
    class CompteBancaire:
        def __init__(self, titulaire, solde=0):
            self.titulaire = titulaire
            self.solde = solde
        
        def deposer(self, montant):
            self.solde += montant
        
        def retirer(self, montant):
            if montant <= self.solde:
                self.solde -= montant
                return True
            return False
        
        def afficher(self):
            print(f"Solde de {self.titulaire}: {self.solde}€")
    
    compte = CompteBancaire("Alice", 100)
    compte.deposer(50)
    compte.retirer(30)
    compte.afficher()  # 120€


# =============================================================================
# EXERCICE 11.4 - VALEURS PAR DEFAUT
# =============================================================================
def exercice_11_4():
    """Classe Livre avec valeurs par defaut."""
    class Livre:
        def __init__(self, titre, auteur, annee=2024, prix=0):
            self.titre = titre
            self.auteur = auteur
            self.annee = annee
            self.prix = prix
    
    livre1 = Livre("1984", "George Orwell")
    livre2 = Livre("Harry Potter", "J.K. Rowling", 1997, 20)
    print(f"{livre1.titre} ({livre1.annee})")
    print(f"{livre2.titre} - {livre2.prix}€")


# =============================================================================
# EXERCICE 11.5 - METHODE DE CLASSE
# =============================================================================
def exercice_11_5():
    """Temperature avec methode de classe."""
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius
        
        @classmethod
        def from_fahrenheit(cls, f):
            celsius = (f - 32) * 5/9
            return cls(celsius)
    
    t1 = Temperature(25)
    t2 = Temperature.from_fahrenheit(77)  # 25°C
    print(f"25°C = {t1.celsius}°C")
    print(f"77°F = {t2.celsius}°C")


# =============================================================================
# EXERCICE 11.6 - METHODE STATIQUE
# =============================================================================
def exercice_11_6():
    """MathUtils avec methodes statiques."""
    class MathUtils:
        @staticmethod
        def est_pair(n):
            return n % 2 == 0
        
        @staticmethod
        def factorielle(n):
            if n <= 1:
                return 1
            return n * MathUtils.factorielle(n - 1)
    
    print(f"10 est pair: {MathUtils.est_pair(10)}")
    print(f"5! = {MathUtils.factorielle(5)}")


# =============================================================================
# EXERCICE 11.7 - PROPRIETE SIMPLE
# =============================================================================
def exercice_11_7():
    """Personne avec proprietes."""
    class Personne:
        def __init__(self, nom, age):
            self._nom = nom
            self._age = age
        
        @property
        def nom(self):
            return self._nom
        
        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, valeur):
            if valeur < 0:
                raise ValueError("L'age ne peut pas etre negatif")
            self._age = valeur
        
        @property
        def est_majeur(self):
            return self._age >= 18
    
    p = Personne("Alice", 25)
    print(f"{p.nom}, {p.age} ans, majeur: {p.est_majeur}")
    p.age = 26
    print(f"Nouvel age: {p.age}")


# =============================================================================
# EXERCICE 11.8 - PROPRIETE CALCULEE
# =============================================================================
def exercice_11_8():
    """Rectangle avec proprietes employees."""
    class Rectangle:
        def __init__(self, largeur, hauteur):
            self.largeur = largeur
            self.hauteur = hauteur
        
        @property
        def aire(self):
            return self.largeur * self.hauteur
        
        @property
        def perimetre(self):
            return 2 * (self.largeur + self.hauteur)
        
        @property
        def est_carre(self):
            return self.largeur == self.hauteur
    
    r1 = Rectangle(5, 5)
    r2 = Rectangle(4, 6)
    print(f"5x5 - Aire: {r1.aire()}, Carre: {r1.est_carre}")
    print(f"4x6 - Aire: {r2.aire()}, Carre: {r2.est_carre}")


# =============================================================================
# EXERCICE 11.9 - ATTRIBUT DE CLASSE
# =============================================================================
def exercice_11_9():
    """Compteur avec attribut de classe."""
    class Compteur:
        total = 0  # Attribut de classe
        
        def __init__(self, valeur):
            self.valeur = valeur
            Compteur.total += 1
    
    c1 = Compteur(10)
    c2 = Compteur(20)
    c3 = Compteur(30)
    print(f"Nombre d'instances: {Compteur.total}")
    print(f"Valeurs: {c1.valeur}, {c2.valeur}, {c3.valeur}")


# =============================================================================
# EXERCICE 11.10 - __STR__ ET __REPR__
# =============================================================================
def exercice_11_10():
    """Voiture avec __str__ et __repr__."""
    class Voiture:
        def __init__(self, marque, modele, annee):
            self.marque = marque
            self.modele = modele
            self.annee = annee
        
        def __str__(self):
            return f"{self.marque} {self.modele} ({self.annee})"
        
        def __repr__(self):
            return f"Voiture('{self.marque}', '{self.modele}', {self.annee})"
    
    v = Voiture("Toyota", "Corolla", 2022)
    print(f"str: {str(v)}")
    print(f"repr: {repr(v)}")


# =============================================================================
# EXERCICE 11.11 - VALIDATION DANS LE SETTER
# =============================================================================
def exercice_11_11():
    """MotDePasse avec validation."""
    class MotDePasse:
        def __init__(self):
            self._mot_de_passe = ""
        
        @property
        def mot_de_passe(self):
            return self._mot_de_passe
        
        @mot_de_passe.setter
        def mot_de_passe(self, valeur):
            if len(valeur) < 8:
                raise ValueError("8 caracteres minimum")
            if not any(c.isupper() for c in valeur):
                raise ValueError("1 majuscule minimum")
            if not any(c.isdigit() for c in valeur):
                raise ValueError("1 chiffre minimum")
            self._mot_de_passe = valeur
    
    mdp = MotDePasse()
    mdp.mot_de_passe = "Python123"
    print("Mot de passe defini avec succes!")


# =============================================================================
# EXERCICE 11.12 - CLASSE ETUDIANT
# =============================================================================
def exercice_11_12():
    """Etudiant avec moyenne calculee."""
    class Etudiant:
        def __init__(self, nom):
            self.nom = nom
            self.notes = []
        
        def ajouter_note(self, note):
            self.notes.append(note)
        
        @property
        def moyenne(self):
            if not self.notes:
                return 0
            return sum(self.notes) / len(self.notes)
        
        def est_recu(self):
            return self.moyenne >= 10
    
    e = Etudiant("Alice")
    e.ajouter_note(15)
    e.ajouter_note(12)
    e.ajouter_note(14)
    print(f"{e.nom} - Moyenne: {e.moyenne:.2f}, Recu: {e.est_recu()}")


# =============================================================================
# EXERCICE 11.13 - SYSTEME BANCAIRE
# =============================================================================
def exercice_11_13():
    """Systeme bancaire avec CompteBancaire et CompteEpargne."""
    class CompteBancaire:
        def __init__(self, titulaire, solde=0):
            self.titulaire = titulaire
            self._solde = solde
        
        @property
        def solde(self):
            return self._solde
        
        def deposer(self, montant):
            self._solde += montant
        
        def retirer(self, montant):
            if montant <= self._solde:
                self._solde -= montant
                return True
            return False
        
        def frais_bancaires(self):
            return 5
    
    class CompteEpargne(CompteBancaire):
        def __init__(self, titulaire, solde=0, taux=0.02):
            super().__init__(titulaire, solde)
            self.taux = taux
        
        def ajouter_interets(self):
            interets = self._solde * self.taux
            self._solde += interets
    
    compte = CompteEpargne("Alice", 1000, 0.03)
    compte.ajouter_interets()
    print(f"Solde avec interets: {compte.solde:.2f}€")


# =============================================================================
# EXERCICE 11.14 - CLASSE PRODUIT
# =============================================================================
def exercice_11_14():
    """Produit avec __eq__."""
    class Produit:
        def __init__(self, nom, prix, quantite):
            self.nom = nom
            self.prix = prix
            self.quantite = quantite
        
        @property
        def valeur_totale(self):
            return self.prix * self.quantite
        
        def __str__(self):
            return f"{self.nom} ({self.prix}€) x {self.quantite}"
        
        def __eq__(self, autre):
            return self.nom == autre.nom and self.prix == autre.prix
    
    p1 = Produit("Pomme", 1.50, 100)
    p2 = Produit("Pomme", 1.50, 50)
    print(f"{p1}")
    print(f"p1 == p2: {p1 == p2}")  # True


# =============================================================================
# EXERCICE 11.15 - SYSTEME DE GESTION
# =============================================================================
def exercice_11_15():
    """Systeme avec Employe et Departement."""
    class Employe:
        def __init__(self, nom, salaire, poste):
            self.nom = nom
            self._salaire = salaire
            self.poste = poste
        
        @property
        def bonus(self):
            return self._salaire * 0.2 if self.poste == "manager" else 0
        
        def augmenter_pourcentage(self, pourcentage):
            self._salaire *= (1 + pourcentage / 100)
        
        def __str__(self):
            return f"{self.nom} - {self.poste}: {self._salaire}€"
    
    class Departement:
        def __init__(self, nom):
            self.nom = nom
            self.employes = []
        
        def ajouter_employe(self, employe):
            self.employes.append(employe)
        
        def masse_salaire(self):
            return sum(e._salaire for e in self.employes)
        
        def trouver_max_salaire(self):
            return max(self.employes, key=lambda e: e._salaire)
    
    dept = Departement("IT")
    e1 = Employe("Alice", 50000, "manager")
    e2 = Employe("Bob", 40000, "developpeur")
    dept.employes.extend([e1, e2])
    
    print(f"Masse salariale: {dept.masse_salaire()}€")
    print(f"Plus haut salaire: {dept.trouver_max_salaire().nom}")
