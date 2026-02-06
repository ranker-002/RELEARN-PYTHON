# =============================================================================
# CHAPITRE 19: TYPE HINTING - EXERCICES
# =============================================================================

# =============================================================================
# EXERCICE 19.1 - TYPES SIMPLES
# =============================================================================
def exercice_19_1():
    """Déclarer des variables avec types simples."""
    # Déclare les variables suivantes avec leur type approprié:
    # - nom (str): "Alice"
    # - age (int): 25
    # - taille (float): 1.75
    # - est_etudiant (bool): True
    
    nom: str = "Alice"
    age: int = 25
    taille: float = 1.75
    est_etudiant: bool = True
    
    print(f"{nom}, {age} ans, {taille}m, étudiant: {est_etudiant}")


# =============================================================================
# EXERCICE 19.2 - LISTES TYÉES
# =============================================================================
from typing import List

def exercice_19_2():
    """Utiliser List avec types."""
    # Déclare une liste de nombres entiers: [1, 2, 3, 4, 5]
    # Déclare une liste de textes: ["Alice", "Bob", "Charlie"]
    
    nombres: List[int] = [1, 2, 3, 4, 5]
    noms: List[str] = ["Alice", "Bob", "Charlie"]
    
    print(f"Nombres: {nombres}")
    print(f"Noms: {noms}")


# =============================================================================
# EXERCICE 19.3 - DICTIONNAIRES TYÉES
# =============================================================================
from typing import Dict

def exercice_19_3():
    """Utiliser Dict avec types."""
    # Déclare un dictionnaire age: {"Alice": 25, "Bob": 30, "Charlie": 35}
    
    ages: Dict[str, int] = {"Alice": 25, "Bob": 30, "Charlie": 35}
    
    for nom, age in ages.items():
        print(f"{nom}: {age} ans")


# =============================================================================
# EXERCICE 19.4 - FONCTION AVEC TYPES
# =============================================================================
def exercice_19_4():
    """Créer une fonction avec types."""
    # Crée une fonction qui prend deux entiers et retourne leur somme
    
    def additionner(a: int, b: int) -> int:
        return a + b
    
    resultat = additionner(5, 3)
    print(f"5 + 3 = {resultat}")


# =============================================================================
# EXERCICE 19.5 - OPTIONAL
# =============================================================================
from typing import Optional

def exercice_19_5():
    """Utiliser Optional pour valeurs possibles None."""
    # Crée une fonction qui prend un nom optionnel
    
    def saluer(nom: Optional[str]) -> str:
        if nom is None:
            return "Bonjour, inconnu!"
        return f"Bonjour, {nom}!"
    
    print(saluer("Alice"))
    print(saluer(None))


# =============================================================================
# EXERCICE 19.6 - UNION
# =============================================================================
from typing import Union

def exercice_19_6():
    """Utiliser Union pour plusieurs types possibles."""
    # Crée une fonction qui accepte int ou str
    
    def afficher(valeur: Union[int, str]) -> str:
        return f"Valeur: {valeur}"
    
    print(afficher(42))
    print(afficher("texte"))


# =============================================================================
# EXERCICE 19.7 - CALLABLE
# =============================================================================
from typing import Callable

def exercice_19_7():
    """Utiliser Callable pour fonctions."""
    # Crée une fonction qui prend un Callable
    
    def appliquer(fonction: Callable[[int], int], x: int) -> int:
        return fonction(x)
    
    def doubler(n: int) -> int:
        return n * 2
    
    resultat = appliquer(doubler, 5)
    print(f"doubler(5) = {resultat}")


# =============================================================================
# EXERCICE 19.8 - TUPLE
# =============================================================================
from typing import Tuple

def exercice_19_8():
    """Utiliser Tuple pour tuples typés."""
    # Déclare un tuple (nom, age, ville)
    
    personne: Tuple[str, int, str] = ("Alice", 25, "Paris")
    print(f"Personne: {personne}")
    print(f"Nom: {personne[0]}")


# =============================================================================
# EXERCICE 19.9 - TYPEDICT
# =============================================================================
from typing import TypedDict

class Personne(TypedDict):
    nom: str
    age: int
    ville: str

def exercice_19_9():
    """Utiliser TypedDict."""
    # Crée une personne avec le TypedDict
    
    alice: Personne = {
        "nom": "Alice",
        "age": 25,
        "ville": "Paris"
    }
    
    print(f"{alice['nom']}, {alice['age']} ans, {alice['ville']}")


# =============================================================================
# EXERCICE 19.10 - DATACLASS AVEC TYPES
# =============================================================================
from dataclasses import dataclass

@dataclass
class Utilisateur:
    nom: str
    age: int
    email: str

def exercice_19_10():
    """Utiliser dataclass avec types."""
    # Crée un utilisateur
    
    user = Utilisateur(nom="Alice", age=25, email="alice@email.com")
    print(user)


# =============================================================================
# EXERCICE 19.11 - GENERIC
# =============================================================================
from typing import Generic, TypeVar

T = TypeVar('T')

class Pile(Generic[T]):
    def __init__(self):
        self.elements: List[T] = []
    
    def push(self, element: T) -> None:
        self.elements.append(element)
    
    def pop(self) -> T:
        return self.elements.pop()

def exercice_19_11():
    """Utiliser Generic pour types génériques."""
    # Crée une pile d'entiers et une pile de textes
    
    pile_entiers: Pile[int] = Pile()
    pile_entiers.push(1)
    pile_entiers.push(2)
    pile_entiers.push(3)
    
    print(f"Élément.poppé: {pile_entiers.pop()}")


# =============================================================================
# EXERCICE 19.12 - PROTOCOL
# =============================================================================
from typing import Protocol

class Rendu(Protocol):
    def render(self) -> str:
        ...

class Image:
    def __init__(self, data: bytes):
        self.data = data
    
    def render(self) -> str:
        return f"[Image de {len(self.data)} octets]"

class Texte:
    def __init__(self, contenu: str):
        self.contenu = contenu
    
    def render(self) -> str:
        return self.contenu

def exercice_19_12():
    """Utiliser Protocol pour interfaces."""
    def afficher(objet: Rendu) -> None:
        print(objet.render())
    
    img = Image(b"data")
    txt = Texte("Bonjour")
    
    afficher(img)
    afficher(txt)


# =============================================================================
# EXERCICE 19.13 - COMPLEXE
# =============================================================================
from typing import List, Dict, Optional

class Employe:
    def __init__(self, nom: str, departement: str, salaire: float):
        self.nom = nom
        self.departement = departement
        self.salaire = salaire

def exercice_19_13():
    """Système de gestion d'employés avec types."""
    employes: List[Employe] = []
    
    def ajouter_employe(nom: str, dept: str, salaire: float) -> None:
        employes.append(Employe(nom, dept, salaire))
    
    def lister_par_departement(dept: str) -> List[Employe]:
        return [e for e in employes if e.departement == dept]
    
    def masse_salariale() -> float:
        return sum(e.salaire for e in employes)
    
    # Utiliser les fonctions
    ajouter_employe("Alice", "IT", 50000)
    ajouter_employe("Bob", "IT", 45000)
    ajouter_employe("Charlie", "RH", 40000)
    
    print(f"Masse salariale IT: {lister_par_departement('IT')}")
    print(f"Total: {masse_salariale()}")


# =============================================================================
# EXERCICE 19.14 - TYPE CHECKING SIMULE
# =============================================================================
def exercice_19_14():
    """Démontrer les types avec mypy."""
    # Ces déclarations seraient vérifiées par mypy
    
    def calculer_tva(prix: float, taux: float = 0.20) -> float:
        return prix * taux
    
    # mypy détecterait ces erreurs:
    # resultat: str = calculer_tva(100)  # ERREUR: float au lieu de str
    
    resultat: float = calculer_tva(100)
    print(f"TVA: {resultat}€")


# =============================================================================
# EXERCICE 19.15 - MODULE COMPLET
# =============================================================================
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int
    
    @property
    def valeur_totale(self) -> float:
        return self.prix * self.quantite

class Inventaire:
    def __init__(self):
        self.produits: List[Produit] = []
    
    def ajouter_produit(self, nom: str, prix: float, quantite: int) -> None:
        self.produits.append(Produit(nom, prix, quantite))
    
    def valeur_inventaire(self) -> float:
        return sum(p.valeur_totale for p in self.produits)
    
    def rechercher(self, nom: str) -> Optional[Produit]:
        for p in self.produits:
            if p.nom == nom:
                return p
        return None

def exercice_19_15():
    """Système d'inventaire avec types complets."""
    inv = Inventaire()
    
    inv.ajouter_produit("Ordinateur", 1000, 5)
    inv.ajouter_produit("Souris", 25, 10)
    inv.ajouter_produit("Clavier", 50, 8)
    
    print(f"Valeur totale: {inv.valeur_inventaire()}€")
    
    resultat = inv.rechercher("Souris")
    if resultat:
        print(f"Souris: {resultat.quantite} en stock")


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 19: TYPE HINTING")
    print("=" * 50)
    
    for i in range(1, 16):
        print(f"\n--- Exercice 19.{i} ---")
        try:
            eval(f"exercice_19_{i}()")
        except Exception as e:
            print(f"Erreur: {e}")
