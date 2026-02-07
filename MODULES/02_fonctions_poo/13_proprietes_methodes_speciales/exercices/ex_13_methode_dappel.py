"""
Exercice 13.13 - METHODE D'APPEL
================================

NIVEAU: ★★★★★ (Tres difficile)
ENONCE:
Creez une classe FunctionWrapper qui:
- Prend une fonction dans __init__
- Utilise __call__ pour executer la fonction
- Compte le nombre d'appels
EXEMPLE:
def double(x): return x * 2
f = FunctionWrapper(double)
print(f(5))      # 10
print(f(10))     # 20
print(f.nb_appels)  # 2
"""


def run():
    """Fonction principale de l'exercice."""
    pass


# Pour tests manuels
if __name__ == "__main__":
    run()
