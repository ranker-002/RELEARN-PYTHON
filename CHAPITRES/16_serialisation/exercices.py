# =============================================================================
# CHAPITRE 16: SERIALISATION - EXERCICES
# =============================================================================

# =============================================================================
# EXERCICE 16.1 - JSON
# =============================================================================
def exercice_16_1():
    """Lire et ecrire JSON."""
    import json
    
    data = {"nom": "Alice", "age": 30, "villes": ["Paris", "Lyon"]}
    
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    with open("data.json", "r") as f:
        print(json.load(f))


# =============================================================================
# EXERCICE 16.2 - PICKLE
# =============================================================================
def exercice_16_2():
    """Serialiser avec Pickle."""
    import pickle
    
    class Personne:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age
    
    p = Personne("Bob", 25)
    
    with open("personne.pkl", "wb") as f:
        pickle.dump(p, f)
    
    with open("personne.pkl", "rb") as f:
        p2 = pickle.load(f)
        print(p2.nom, p2.age)


# =============================================================================
# EXERCICE 16.3 - CSV AVEC DICTREADER
# =============================================================================
def exercice_16_3():
    """CSV avec dictionnaires."""
    import csv
    
    data = [
        {"nom": "Alice", "age": 30},
        {"nom": "Bob", "age": 25}
    ]
    
    with open("output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nom", "age"])
        writer.writeheader()
        writer.writerows(data)


# =============================================================================
# EXERCICE 16.4 - YAML
# =============================================================================
def exercice_16_4():
    """Lire et ecrire YAML."""
    import yaml
    
    data = {
        "serveur": {
            "host": "localhost",
            "port": 8080
        },
        "debug": True
    }
    
    with open("config.yaml", "w") as f:
        yaml.dump(data, f)
    
    with open("config.yaml", "r") as f:
        print(yaml.safe_load(f))


# =============================================================================
# EXERCICE 16.5 - CONFIG.JSON
# =============================================================================
def exercice_16_5():
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


# =============================================================================
# EXERCICE 16.6 - SAUVEGARDE ETATS
# =============================================================================
def exercice_16_6():
    """Sauvegarder et charger etat."""
    import pickle
    
    etat = {
        "score": 100,
        "niveau": 5,
        "objets": ["epee", "bouclier"]
    }
    
    with open("savegame.dat", "wb") as f:
        pickle.dump(etat, f)
    
    with open("savegame.dat", "rb") as f:
        charge = pickle.load(f)
        print(charge)


# =============================================================================
# EXERCICE 16.7 - XML
# =============================================================================
def exercice_16_7():
    """Lire et ecrire XML."""
    import xml.etree.ElementTree as ET
    
    root = ET.Element("racine")
    enfant = ET.SubElement(root, "enfant")
    enfant.text = "Bonjour"
    
    tree = ET.ElementTree(root)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)


# =============================================================================
# EXERCICE 16.8 - MESSAGE JSON
# =============================================================================
def exercice_16_8():
    """Serialiser messages."""
    import json
    
    messages = [
        {"type": "text", "contenu": "Hello"},
        {"type": "image", "url": "img.png"}
    ]
    
    with open("messages.json", "w") as f:
        json.dump(messages, f)


# =============================================================================
# EXERCICE 16.9 - CLASS CUSTOM
# =============================================================================
def exercice_16_9():
    """Serialiser classe personnalisee."""
    import pickle
    
    class GameState:
        def __init__(self):
            self.joueurs = []
            self.tour = 1
        
        def ajouter_joueur(self, nom):
            self.joueurs.append(nom)
    
    etat = GameState()
    etat.ajouter_joueur("Alice")
    etat.ajouter_joueur("Bob")
    
    with open("game.dat", "wb") as f:
        pickle.dump(etat, f)


# =============================================================================
# EXERCICE 16.10 - VALIDATION JSON
# =============================================================================
def exercice_16_10():
    """Valider JSON avec schema."""
    import json
    
    schema = {
        "type": "object",
        "properties": {
            "nom": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["nom"]
    }
    
    data = {"nom": "Alice", "age": 30}
    # Validation simplifiee
    for key in schema["required"]:
        if key not in data:
            print(f"Erreur: {key} requis")
            return
    print("Valide!")


if __name__ == "__main__":
    print("Chapitre 16: Serialisation")
