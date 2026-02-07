"""
Exercice 16.5 - CONFIG.JSON
===========================


"""


def run():
    """Fonction principale de l'exercice."""
    """Systeme de configuration JSON."""
    import json

    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "app_db"
        },
        "logging": {
            "level": "INFO"
        }
    }

    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

    with open("config.json", "r") as f:
        loaded = json.load(f)
        print(f"Database: {loaded['database']['host']}")


# Pour tests manuels
if __name__ == "__main__":
    run()
