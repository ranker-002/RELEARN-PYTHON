# =============================================================================
# CHAPITRE 15: FICHIERS I/O - SOLUTIONS
# =============================================================================


def exercice_15_1():
    """Lecture simple."""
    with open("test.txt", "r", encoding="utf-8") as f:
        print(f.read())


def exercice_15_2():
    """Ecriture simple."""
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Ligne 1\n")
        f.write("Ligne 2\n")


def exercice_15_3():
    """Compteur de lignes."""
    def compter_lignes(fichier):
        with open(fichier, "r") as f:
            return sum(1 for _ in f)
    
    print(f"Nombre: {compter_lignes('fichier.txt')}")


def exercice_15_4():
    """Lignes avec prefixe."""
    with open("entree.txt", "r") as entree:
        with open("sortie.txt", "w") as sortie:
            for ligne in entree:
                sortie.write(f"[INFO] {ligne}")


def exercice_15_5():
    """Lecture CSV."""
    import csv
    
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def exercice_15_6():
    """Ecriture CSV."""
    import csv
    
    donnees = [
        ["Nom", "Age", "Ville"],
        ["Alice", 30, "Paris"],
        ["Bob", 25, "Lyon"]
    ]
    
    with open("output.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(donnees)


def exercice_15_7():
    """JSON."""
    import json
    
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def exercice_15_8():
    """Chemins."""
    import os
    
    print(f"Absolu: {os.path.abspath('fichier.txt')}")
    print(f"Fichier: {os.path.isfile('fichier.txt')}")
    print(f"Taille: {os.path.getsize('fichier.txt')}")


def exercice_15_9():
    """Parcours."""
    import os
    
    for elem in os.listdir("."):
        print(f"{'D' if os.path.isdir(elem) else 'F'}: {elem}")


def exercice_15_10():
    """Copier."""
    def copier(source, dest):
        with open(source, "rb") as s:
            with open(dest, "wb") as d:
                d.write(s.read())
    
    copier("src.png", "dst.png")


def exercice_15_11():
    """Filtrer."""
    def filtrer(f_in, f_out, mot):
        with open(f_in, "r") as entree:
            with open(f_out, "w") as sortie:
                for ligne in entree:
                    if mot in ligne:
                        sortie.write(ligne)


def exercice_15_12():
    """Stats."""
    def analyser(fichier):
        with open(fichier, "r") as f:
            lignes = f.readlines()
        
        return {
            "lignes": len(lignes),
            "mots": sum(len(l.split()) for l in lignes),
            "caracteres": sum(len(l) for l in lignes)
        }
    
    print(analyser("fichier.txt"))


def exercice_15_13():
    """Remplacer."""
    def remplacer(fichier, ancien, nouveau):
        with open(fichier, "r") as f:
            contenu = f.read()
        with open(fichier, "w") as f:
            f.write(contenu.replace(ancien, nouveau))
    
    remplacer("fichier.txt", "test", "demo")


def exercice_15_14():
    """Temporaire."""
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Temporaire\n")
        print(f"Path: {f.name}")


def exercice_15_15():
    """Logs."""
    import datetime
    
    def log(msg, fichier="app.log"):
        ts = datetime.datetime.now().isoformat()
        with open(fichier, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {msg}\n")
    
    log("Demarrage")
    log("Fin")
