"""
Exercice 12.13 - __STR__ ET __REPR__ AVEC HERITAGE
==================================================

NIVEAU: ★★★★★ (Tres difficile)
ENONCE:
Creez une classe Person avec nom, age
- Methode: __str__ et __repr__
Creez une classe Employe(Person) avec poste, salaire
- Methode: __str__ qui utilise super()
EXEMPLE:
p = Person("Alice", 30)
print(str(p))    # "Person: Alice (30 ans)"
print(repr(p))   # "Person('Alice', 30)"
e = Employe("Bob", 25, "Dev")
print(str(e))    # "Employe: Bob (25 ans) - Dev"
"""


def run():
    """Fonction principale de l'exercice."""
    pass


# Pour tests manuels
if __name__ == "__main__":
    run()
