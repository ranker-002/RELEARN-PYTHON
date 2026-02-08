"""
Exercice 12.8 - MRO ET ORDRE D'HERITAGE
=======================================

NIVEAU: ★★★★☆ (Difficile)
ENONCE:
Creez un heritage en diamant:
A
/ \
B   C
\ /
D
Chaque classe a une methode test() qui affiche son nom
Verifiez l'ordre MRO de D
EXEMPLE:
d = D()
d.test()  # Affiche "D" puis les parents selon MRO
print(D.mro())  # [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, ...]
"""


def run():
    """Fonction principale de l'exercice."""
    pass


# Pour tests manuels
if __name__ == "__main__":
    run()
