# =============================================================================
# CHAPITRE 16: SERIALISATION - SOLUTIONS
# =============================================================================

import json
import pickle


def exercice_16_1():
    data = {"nom": "Alice", "age": 30}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)


def exercice_16_2():
    class P:
        def __init__(self, n, a): self.nom=n; self.age=a
    p = P("Bob", 25)
    with open("p.pkl", "wb") as f: pickle.dump(p, f)
    with open("p.pkl", "rb") as f:
        p2 = pickle.load(f)
        print(p2.nom, p2.age)


def exercice_16_3():
    import csv
    with open("out.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["nom", "age"])
        w.writeheader()
        w.writerow({"nom": "A", "age": 30})


def exercice_16_4():
    import yaml
    data = {"cle": "valeur"}
    with open("out.yaml", "w") as f:
        yaml.dump(data, f)


def exercice_16_5():
    import json
    c = {"db": {"host": "localhost"}}
    with open("c.json", "w") as f:
        json.dump(c, f, indent=2)


def exercice_16_6():
    data = {"score": 100}
    with open("s.dat", "wb") as f: pickle.dump(data, f)
    with open("s.dat", "rb") as f: print(pickle.load(f))


def exercice_16_7():
    import xml.etree.ElementTree as ET
    r = ET.Element("root")
    ET.SubElement(r, "child").text = "text"
    ET.ElementTree(r).write("out.xml")


def exercice_16_8():
    import json
    msgs = [{"t": "text", "c": "hi"}]
    with open("msgs.json", "w") as f:
        json.dump(msgs, f)


def exercice_16_9():
    class G:
        def __init__(self): self.joueurs = []
        def add(self, n): self.joueurs.append(n)
    g = G()
    g.add("A")
    with open("g.dat", "wb") as f: pickle.dump(g, f)


def exercice_16_10():
    import json
    data = {"nom": "X"}
    if "nom" in data:
        print("Valide")
