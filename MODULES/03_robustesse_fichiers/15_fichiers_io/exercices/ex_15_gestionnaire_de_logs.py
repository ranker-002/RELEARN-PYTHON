"""
Exercice 15.15 - GESTIONNAIRE DE LOGS
=====================================


"""


def run():
    """Fonction principale de l'exercice."""
    """Systeme de logs simple."""
    import datetime

    def log(message, fichier="app.log"):
        with open(fichier, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[{timestamp}] {message}\n")

    log("Demarrage de l'application")
    log("Operation effectuee")
    log("Arret de l'application")


# Pour tests manuels
if __name__ == "__main__":
    run()
