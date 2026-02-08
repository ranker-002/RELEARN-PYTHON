#!/usr/bin/env python3
"""
Calculatrice CLI - Projet d'apprentissage.

ÉNONCÉ:
--------
Implémentez une calculatrice en ligne de commande avec:
- Opérations de base: +, -, *, /
- Opérations avancées: puissance, racine carrée, modulo
- Historique des calculs
- Variables utilisateur
- Conversion d'unités

TODO: Implémenter la logique du projet.
"""


class Calculatrice:
    """Calculatrice à implémenter."""
    
    def __init__(self):
        self.historique = []
        self.variables = {}
    
    def calculer(self, expression: str) -> float:
        """Évaluer une expression."""
        raise NotImplementedError
    
    def get_historique(self) -> list:
        """Retourner l'historique."""
        raise NotImplementedError
    
    def set_variable(self, nom: str, valeur: float):
        """Définir une variable."""
        raise NotImplementedError


def main():
    """Point d'entrée."""
    print("=== Calculatrice CLI ===")
    print("TODO: Implémenter l'interface interactive")
    
    while True:
        try:
            expression = input("\n> ").strip()
            if expression in ['quit', 'exit', 'q']:
                break
            # TODO: Appeler Calculatrice().calculer(expression)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
