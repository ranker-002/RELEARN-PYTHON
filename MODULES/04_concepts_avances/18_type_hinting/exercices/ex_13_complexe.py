"""
Exercice 19.13 - COMPLEXE
=========================


"""


def run():
    """Fonction principale de l'exercice."""
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


# Pour tests manuels
if __name__ == "__main__":
    run()
