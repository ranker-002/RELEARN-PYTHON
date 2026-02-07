"""
Exercice 9.7 - DECORATEUR SIMPLE
================================

NIVEAU: ★★★☆☆ (Moyen)
ENONCE:
Creez un decorateur dire_bonjour_avant qui affiche "Bonjour!"
avant d'appeler la fonction decoree.
INDICE:
def decorateur(func):
def wrapper(*args, **kwargs):
print("Bonjour!")
return func(*args, **kwargs)
return wrapper
"""


def run():
    """Fonction principale de l'exercice."""
    pass


# Pour tests manuels
if __name__ == "__main__":
    run()
