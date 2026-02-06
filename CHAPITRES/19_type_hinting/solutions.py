# =============================================================================
# CHAPITRE 19: TYPE HINTING - SOLUTIONS
# =============================================================================

from typing import List, Dict, Optional, Union, Callable, Tuple, TypedDict, Protocol
from dataclasses import dataclass


def exercice_19_1():
    """Types simples."""
    nom: str = "Alice"
    age: int = 25
    taille: float = 1.75
    est_etudiant: bool = True
    
    print(f"{nom}, {age} ans, {taille}m, étudiant: {est_etudiant}")


def exercice_19_2():
    """Listes typées."""
    nombres: List[int] = [1, 2, 3, 4, 5]
    noms: List[str] = ["Alice", "Bob", "Charlie"]
    
    print(f"Nombres: {nombres}")
    print(f"Noms: {noms}")


def exercice_19_3():
    """Dictionnaires typés."""
    ages: Dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}
    
    for nom, age in ages.items():
        print(f"{nom}: {age} ans")


def exercice_19_4():
    """Fonction avec types."""
    def additionner(a: int, b: int) -> int:
        return a + b
    
    print(f"5 + 3 = {additionner(5, 3)}")


def exercice_19_5():
    """Optional."""
    def saluer(nom: Optional[str]) -> str:
        return f"Bonjour, {nom or 'inconnu'}!"
    
    print(saluer("Alice"))
    print(saluer(None))


def exercice_19_6():
    """Union."""
    def afficher(valeur: Union[int, str]) -> str:
        return f"Valeur: {valeur}"
    
    print(afficher(42))
    print(afficher("texte"))


def exercice_19_7():
    """Callable."""
    def appliquer(fonction: Callable[[int], int], x: int) -> int:
        return fonction(x)
    
    def doubler(n: int) -> int:
        return n * 2
    
    print(f"appliquer(doubler, 5) = {appliquer(doubler, 5)}")


def exercice_19_8():
    """Tuple."""
    personne: Tuple[str, int, str] = ("Alice", 25, "Paris")
    print(f"Personne: {personne}")
    print(f"Nom: {personne[0]}")


def exercice_19_9():
    """TypedDict."""
    class Personne(TypedDict):
        nom: str
        age: int
        ville: str
    
    alice: Personne = {
        "nom": "Alice",
        "age": 25,
        "ville": "Paris"
    }
    
    print(f"{alice['nom']}, {alice['age']} ans")


def exercice_19_10():
    """Dataclass."""
    @dataclass
    class Utilisateur:
        nom: str
        age: int
        email: str
    
    user = Utilisateur("Alice", 25, "alice@email.com")
    print(user)


def exercice_19_11():
    """Generic."""
    from typing import TypeVar, Generic
    
    T = TypeVar('T')
    
    class Pile(Generic[T]):
        def __init__(self):
            self.elements: List[T] = []
        
        def push(self, element: T) -> None:
            self.elements.append(element)
        
        def pop(self) -> T:
            return self.elements.pop()
    
    pile: Pile[int] = Pile()
    pile.push(1)
    pile.push(2)
    pile.push(3)
    
    print(f"Popped: {pile.pop()}")


def exercice_19_12():
    """Protocol."""
    class Rendu(Protocol):
        def render(self) -> str:
            ...
    
    class Image:
        def __init__(self, data: bytes):
            self.data = data
        
        def render(self) -> str:
            return f"[Image: {len(self.data)} octets]"
    
    class Texte:
        def __init__(self, contenu: str):
            self.contenu = contenu
        
        def render(self) -> str:
            return self.contenu
    
    def afficher(objet: Rendu) -> None:
        print(objet.render())
    
    img = Image(b"data")
    txt = Texte("Bonjour")
    
    afficher(img)
    afficher(txt)


def exercice_19_13():
    """Système Employé."""
    class Employe:
        def __init__(self, nom: str, dept: str, salaire: float):
            self.nom = nom
            self.departement = dept
            self.salaire = salaire
    
    employes: List[Employe] = []
    
    def ajouter_employe(nom: str, dept: str, salaire: float) -> None:
        employes.append(Employe(nom, dept, salaire))
    
    def lister_par_departement(dept: str) -> List[Employe]:
        return [e for e in employes if e.departement == dept]
    
    def masse_salariale() -> float:
        return sum(e.salaire for e in employes)
    
    ajouter_employe("Alice", "IT", 50000)
    ajouter_employe("Bob", "IT", 45000)
    
    print(f"Masse: {masse_salariale()}")


def exercice_19_14():
    """Calcul TVA."""
    def calculer_tva(prix: float, taux: float = 0.20) -> float:
        return prix * taux
    
    resultat: float = calculer_tva(100)
    print(f"TVA: {resultat}€")


def exercice_19_15():
    """Inventaire complet."""
    @dataclass
    class Produit:
        nom: str
        prix: float
        quantite: int
    
    class Inventaire:
        def __init__(self):
            self.produits: List[Produit] = []
        
        def ajouter(self, nom: str, prix: float, qte: int) -> None:
            self.produits.append(Produit(nom, prix, qte))
        
        def valeur(self) -> float:
            return sum(p.prix * p.quantite for p in self.produits)
    
    inv = Inventaire()
    inv.ajouter("Ordinateur", 1000, 5)
    inv.ajouter("Souris", 25, 10)
    
    print(f"Valeur: {inv.valeur()}€")
