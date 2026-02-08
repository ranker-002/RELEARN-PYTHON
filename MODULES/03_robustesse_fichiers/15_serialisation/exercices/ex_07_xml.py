"""
Exercice 16.7 - XML
===================


"""


def run():
    """Fonction principale de l'exercice."""
    """Lire et ecrire XML."""
    import xml.etree.ElementTree as ET

    root = ET.Element("racine")
    enfant = ET.SubElement(root, "enfant")
    enfant.text = "Bonjour"

    tree = ET.ElementTree(root)
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)


# Pour tests manuels
if __name__ == "__main__":
    run()
