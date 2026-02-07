"""
Exercice 19.1 - TYPES SIMPLES
=============================


"""


def run():
    """Fonction principale de l'exercice."""
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


# Pour tests manuels
if __name__ == "__main__":
    run()
