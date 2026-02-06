# =============================================================================
# CHAPITRE 15: FICHIERS I/O - EXERCICES
# =============================================================================

# =============================================================================
# EXERCICE 15.1 - LECTURE SIMPLE
# =============================================================================
def exercice_15_1():
    """Lire et afficher un fichier."""
    # Creez un fichier test.txt avec "Bonjour le monde!"
    # Puis lisez et affichez son contenu
    
    with open("test.txt", "r", encoding="utf-8") as f:
        print(f.read())


# =============================================================================
# EXERCICE 15.2 - ECRITURE SIMPLE
# =============================================================================
def exercice_15_2():
    """Ecrire dans un fichier."""
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Ligne 1\n")
        f.write("Ligne 2\n")


# =============================================================================
# EXERCICE 15.3 - COMPTEUR DE LIGNES
# =============================================================================
def exercice_15_3():
    """Compter les lignes d'un fichier."""
    def compter_lignes(fichier):
        with open(fichier, "r") as f:
            return sum(1 for _ in f)
    
    print(f"Nombre de lignes: {compter_lignes('fichier.txt')}")


# =============================================================================
# EXERCICE 15.4 - LIGNES AVEC PREFIXE
# =============================================================================
def exercice_15_4():
    """Ajouter un prefixe a chaque ligne."""
    with open("entree.txt", "r") as entree:
        with open("sortie.txt", "w") as sortie:
            for ligne in entree:
                sortie.write(f"[INFO] {ligne}")


# =============================================================================
# EXERCICE 15.5 - LECTURE CSV
# =============================================================================
def exercice_15_5():
    """Lire un fichier CSV."""
    import csv
    
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# =============================================================================
# EXERCICE 15.6 - ECRITURE CSV
# =============================================================================
def exercice_15_6():
    """Ecrire dans un fichier CSV."""
    import csv
    
    donnees = [
        ["Nom", "Age", "Ville"],
        ["Alice", 30, "Paris"],
        ["Bob", 25, "Lyon"]
    ]
    
    with open("output.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(donnees)


# =============================================================================
# EXERCICE 15.7 - JSON
# =============================================================================
def exercice_15_7():
    """Lire et ecrire JSON."""
    import json
    
    # Lire
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Ecrire
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# =============================================================================
# EXERCICE 15.8 - CHEMIN ABSOLU
# =============================================================================
def exercice_15_8():
    """Manipuler les chemins."""
    import os
    
    print(f"Chemin absolu: {os.path.abspath('fichier.txt')}")
    print(f"Est fichier: {os.path.isfile('fichier.txt')}")
    print(f"Est repertoire: {os.path.isdir('dossier')}")
    print(f"Taille: {os.path.getsize('fichier.txt')} octets")


# =============================================================================
# EXERCICE 15.9 - PARCOURS REPERTOIRE
# =============================================================================
def exercice_15_9():
    """Lister les fichiers d'un repertoire."""
    import os
    
    for elem in os.listdir("."):
        chemin = os.path.join(".", elem)
        if os.path.isfile(chemin):
            print(f"F: {elem}")
        elif os.path.isdir(chemin):
            print(f"D: {elem}")


# =============================================================================
# EXERCICE 15.10 - COPIER FICHIER
# =============================================================================
def exercice_15_10():
    """Copier un fichier binaire."""
    def copier(source, destination):
        with open(source, "rb") as src:
            with open(destination, "wb") as dst:
                dst.write(src.read())
    
    copier("source.png", "destination.png")


# =============================================================================
# EXERCICE 15.11 - FILTRE DE LIGNES
# =============================================================================
def exercice_15_11():
    """Filtrer les lignes contenant un mot."""
    def filtrer(fichier_in, fichier_out, mot):
        with open(fichier_in, "r") as entree:
            with open(fichier_out, "w") as sortie:
                for ligne in entree:
                    if mot in ligne:
                        sortie.write(ligne)
    
    filtrer("entree.txt", "sortie.txt", "erreur")


# =============================================================================
# EXERCICE 15.12 - STATISTIQUES
# =============================================================================
def exercice_15_12():
    """Calculer les statistiques d'un fichier."""
    def analyser(fichier):
        with open(fichier, "r") as f:
            lignes = f.readlines()
        
        return {
            "lignes": len(lignes),
            "mots": sum(len(l.split()) for l in lignes),
            "caracteres": sum(len(l) for l in lignes)
        }
    
    print(analyser("fichier.txt"))


# =============================================================================
# EXERCICE 15.13 - REMPLACER TEXTE
# =============================================================================
def exercice_15_13():
    """Remplacer un mot par un autre."""
    def remplacer(fichier, ancien, nouveau):
        with open(fichier, "r") as f:
            contenu = f.read()
        
        with open(fichier, "w") as f:
            f.write(contenu.replace(ancien, nouveau))
    
    remplacer("fichier.txt", "ancien", "nouveau")


# =============================================================================
# EXERCICE 15.14 - FICHIER TEMPORAIRE
# =============================================================================
def exercice_15_14():
    """Utiliser un fichier temporaire."""
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("Donnees temporaires\n")
        print(f"Fichier: {f.name}")
    
    print("Fichier temporaire cree")


# =============================================================================
# EXERCICE 15.15 - GESTIONNAIRE DE LOGS
# =============================================================================
def exercice_15_15():
    """Systeme de logs simple."""
    import datetime
    
    def log(message, fichier="app.log"):
        with open(fichier, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[{timestamp}] {message}\n")
    
    log("Demarrage de l'application")
    log("Operation effectuee")
    log("Arret de l'application")


if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 15 - EXERCICES")
    print("=" * 50)
    for i in range(1, 16):
        print(f"  15.{i} - Exercice {i}")
    print("=" * 50)
