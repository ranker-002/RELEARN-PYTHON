"""
Exercice 20.10 - COMMANDES SYSTÈME
==================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Exécuter une commande système."""
    import subprocess

    resultat = subprocess.run(["echo", "Hello from subprocess!"], 
                              capture_output=True, text=True)
    print(resultat.stdout.strip())


# Pour tests manuels
if __name__ == "__main__":
    run()
