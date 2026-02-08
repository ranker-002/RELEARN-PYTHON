"""
Exercice 8.16 - ARGUMENTS POSITION-ONLY
======================================

NIVEAU: ★★★☆☆ (Intermédiaire)
ENONCE:
Créez des fonctions utilisant des arguments position-only (avant le /).
Ces arguments doivent obligatoirement être passés par position, pas par nom.

FONCTIONS A CREER:
1. diviser(a, b, /) -> float
   Divise a par b. Les arguments doivent être position-only.
   
2. calculer_prix_ht(prix_ttc, taux_tva, /) -> float
   Calcule le prix HT à partir du prix TTC et du taux de TVA.
   Formule: prix_ht = prix_ttc / (1 + taux_tva)
   Ex: calculer_prix_ht(120, 0.20) -> 100.0
   
3. formater_nombre(nombre, decimales, /, separateur=',') -> str
   Formate un nombre avec un nombre de décimales fixe.
   - nombre et decimales: position-only
   - separateur: peut être passé par nom
   Ex: formater_nombre(1234.5678, 2) -> "1,234.57"
   Ex: formater_nombre(1234.5678, 2, separateur=' ') -> "1 234.57"

TESTS ATTENDUS:
- diviser(10, 2) doit retourner 5.0
- diviser(a=10, b=2) doit provoquer une erreur (TypeError)
- calculer_prix_ht(120, 0.20) -> 100.0
- formater_nombre(1234.5678, 2) -> "1,234.57"
"""


def diviser(a, b, /):
    """
    Divise a par b.
    Les arguments doivent être passés par position.
    
    Args:
        a: Dividende (position-only)
        b: Diviseur (position-only)
    
    Returns:
        float: Résultat de a / b
    
    Example:
        >>> diviser(10, 2)
        5.0
    """
    # TODO: Implémentez cette fonction avec des arguments position-only
    pass


def calculer_prix_ht(prix_ttc, taux_tva, /):
    """
    Calcule le prix HT à partir du prix TTC.
    
    Args:
        prix_ttc: Prix toutes taxes comprises (position-only)
        taux_tva: Taux de TVA (ex: 0.20 pour 20%) (position-only)
    
    Returns:
        float: Prix hors taxe
    
    Example:
        >>> calculer_prix_ht(120, 0.20)
        100.0
    """
    # TODO: Implémentez le calcul
    pass


def formater_nombre(nombre, decimales, /, separateur=','):
    """
    Formate un nombre avec séparateur de milliers.
    
    Args:
        nombre: Nombre à formater (position-only)
        decimales: Nombre de décimales (position-only)
        separateur: Caractère séparateur (par défaut: ',')
    
    Returns:
        str: Nombre formaté
    
    Example:
        >>> formater_nombre(1234.5678, 2)
        '1,234.57'
        >>> formater_nombre(1234.5678, 2, separateur=' ')
        '1 234.57'
    """
    # TODO: Formatez le nombre avec le séparateur
    # Indice: Utilisez f-string ou format() avec les bonnes options
    pass


def run():
    """Fonction principale de l'exercice."""
    print("=== Test des arguments position-only ===\n")
    
    # Test 1: Division
    print("Test de diviser(10, 2):")
    try:
        resultat = diviser(10, 2)
        print(f"  ✅ Résultat: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    # Test 2: Prix HT
    print("\nTest de calculer_prix_ht(120, 0.20):")
    try:
        resultat = calculer_prix_ht(120, 0.20)
        print(f"  ✅ Prix HT: {resultat}€ (pour un prix TTC de 120€ et TVA 20%)")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    # Test 3: Formatage
    print("\nTest de formater_nombre(1234.5678, 2):")
    try:
        resultat = formater_nombre(1234.5678, 2)
        print(f"  ✅ Formaté: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    print("\nTest de formater_nombre(1234.5678, 2, separateur=' '):")
    try:
        resultat = formater_nombre(1234.5678, 2, separateur=' ')
        print(f"  ✅ Formaté avec espace: {resultat}")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")
    
    print("\n=== Test des erreurs (doivent échouer) ===")
    print("Tentative de diviser(a=10, b=2):")
    try:
        resultat = diviser(a=10, b=2)
        print(f"  ❌ Ne devrait pas fonctionner ! Résultat: {resultat}")
    except TypeError as e:
        print(f"  ✅ Bonne erreur: {e}")


# Pour tests manuels
if __name__ == "__main__":
    run()
