"""
Exercice 1.15 - Calculateur de Temps de Trajet
==============================================
NIVEAU: ★★★★☆ (Difficile)

ÉNONCÉ:
Calculez le temps de trajet en fonction de la distance et de la vitesse.

FORMULES:
Temps (heures) = Distance / Vitesse
Temps (minutes) = Temps (heures) × 60

EXEMPLE D'EXÉCUTION:
Distance (km): 120
Vitesse moyenne (km/h): 60

Résultats:
Temps de trajet: 2.00 heures
soit 120 minutes
"""


def run():
    """Fonction principale de l'exercice."""
    distance = float(input("Distance (km): "))
    vitesse = float(input("Vitesse moyenne (km/h): "))
    
    temps_heures = distance / vitesse
    temps_minutes = temps_heures * 60
    
    print()
    print("Résultats:")
    print(f"Temps de trajet: {temps_heures:.2f} heures")
    print(f"soit {int(temps_minutes)} minutes")


# Pour tests manuels
if __name__ == "__main__":
    run()
