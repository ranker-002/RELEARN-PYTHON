"""
Exercice 9.14 - CONSTRUCTEUR DE REQUETES
========================================

NIVEAU: ★★★★★ (Tres difficile)
ENONCE:
Creez une fonction build_query(table, *, select="*", where=None,
order_by=None, limit=None)
qui construit une requete SQL.
EXEMPLE:
build_query("users", select="name, email", where="age > 18")
-> "SELECT name, email FROM users WHERE age > 18"
"""


def run():
    """Fonction principale de l'exercice."""
    pass


# Pour tests manuels
if __name__ == "__main__":
    run()
