# =============================================================================
# CHAPITRE 14: EXCEPTIONS - EXERCICES
# =============================================================================
# Niveau: INTERMEDIAIRE
# Concepts abordes: try/except, exceptions personnalisees, finally
# =============================================================================

# =============================================================================
# EXERCICE 14.1 - TRY/EXCEPT SIMPLE
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction diviser(a, b) qui:
# - Retourne a / b
# - Attrape ZeroDivisionError et retourne None
#
# EXEMPLE:
# print(diviser(10, 2))  # 5.0
# print(diviser(10, 0))  # None
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_1():
    pass


# =============================================================================
# EXERCICE 14.2 - PLUSIEURS EXCEPTIONS
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Creez une fonction analyser(valeur) qui:
# - Retourne int(valeur)
# - Attrape ValueError (pas un entier)
# - Attrape ZeroDivisionError (devinez pourquoi?)
#
# EXEMPLE:
# print(analyser("42"))    # 42
# print(analyser("abc"))   # "Erreur: ..."
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_2():
    pass


# =============================================================================
# EXERCICE 14.3 - ELSE ET FINALLY
# =============================================================================
# NIVEAU: ★★☆☆☆ (Facile)
#
# ENONCE:
# Utilisez try/except/else/finally pour:
# - Ouvrir un fichier (simulation)
# - Compter les lignes
# - Toujours fermer le fichier
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_3():
    pass


# =============================================================================
# EXERCICE 14.4 - EXCEPTION PERSONNALISEE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une classe ErreurPersonnalisee(Exception) avec:
# - Attributs: code, message
# - Methode: __str__ personalisee
#
# EXEMPLE:
# raise ErreurPersonnalisee(404, "Ressource non trouvee")
# # Affiche: "[404] Ressource non trouvee"
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_4():
    pass


# =============================================================================
# EXERCICE 14.5 - VALIDATION SIMPLE
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez une fonction valider_email(email) qui:
# - Verifie la presence de '@' et '.'
# - Leve ValueError si invalide
#
# EXEMPLE:
# valider_email("test@email.com")  # OK
# valider_email("invalid")         # ValueError
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_5():
    pass


# =============================================================================
# EXERCICE 14.6 - HIERARCHIE D'EXCEPTIONS
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez:
# - Exception de base: ApplicationError
# - Sous-classes: ValidationError, DatabaseError, NetworkError
# - Demonstration d'utilisation
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_6():
    pass


# =============================================================================
# EXERCICE 14.7 - PROPAGATION
# =============================================================================
# NIVEAU: ★★★☆☆ (Moyen)
#
# ENONCE:
# Creez 3 fonctions:
# - niveau3() qui leve une exception
# - niveau2() qui appelle niveau3()
# - niveau1() qui appelle niveau2() et attrape l'erreur
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_7():
    pass


# =============================================================================
# EXERCICE 14.8 - RELANCER EXCEPTION
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une fonction qui:
# - Attrape une exception
# - Effectue un traitement
# - Relance l'exception
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_8():
    pass


# =============================================================================
# EXERCICE 14.9 - CONTEXT MANAGER
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez un context manager Timer qui:
# - Mesure le temps d'execution
# - Affiche le temps dans __exit__
#
# EXEMPLE:
# with Timer():
#     sum(range(1000000))
# # Affiche: "Temps d'execution: 0.05s"
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_9():
    pass


# =============================================================================
# EXERCICE 14.10 - RETRY PATTERN
# =============================================================================
# NIVEAU: ★★★★☆ (Difficile)
#
# ENONCE:
# Creez une fonction avec retry:
# - Maximum 3 tentatives
# - Delai de 0.1s entre tentatives
# - Retourne le resultat ou leve l'exception finale
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_10():
    pass


# =============================================================================
# EXERCICE 14.11 - VALIDATEUR COMPLET
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme de validation avec:
# - ValidationError avec champ et valeur
# - Validateurs: required, min, max, pattern
# - Methode validate(donnees, regles)
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_11():
    pass


# =============================================================================
# EXERCICE 14.12 - SYSTÈME DE FICHIERS SÉCURISÉ
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez des fonctions securisees pour:
# - Lire un fichier (FileNotFoundError)
# - Ecrire un fichier (PermissionError)
# - Supprimer un fichier
# - Retourne resultat ou erreur personnalisee
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_12():
    pass


# =============================================================================
# EXERCICE 14.13 - EXCEPTION CHAINEE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Demontrer l'utilisation de 'from e' pour:
# - Convertir une exception en une autre
# - Conserver la trace originale
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_13():
    pass


# =============================================================================
# EXERCICE 14.14 - PAGINATION SÉCURISÉE
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez une classe Pagination avec:
# - Propriete: page (validee, 1 <= page <= total)
# - Propriete: page_size (validee, 1 <= size <= 100)
# - Methode: get_offset() et get_limit()
# - Leve des exceptions personalisees
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_14():
    pass


# =============================================================================
# EXERCICE 14.15 - SYSTÈME DE logging COMPLET
# =============================================================================
# NIVEAU: ★★★★★ (Tres difficile)
#
# ENONCE:
# Creez un systeme avec:
# - Exceptions hierarchisees
# - Logging des erreurs
# - Context manager pour les operations
# - Retry automatique
#
# VOTRE CODE CI-DESSOUS:
def exercice_14_15():
    pass


# =============================================================================
# TESTEUR AUTOMATIQUE
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("CHAPITRE 14 - EXERCICES")
    print("=" * 50)
    print("Exercices disponibles:")
    print("  14.1 - try/except simple")
    print("  14.2 - Plusieurs exceptions")
    print("  14.3 - else et finally")
    print("  14.4 - Exception personnalisee")
    print("  14.5 - Validation simple")
    print("  14.6 - Hierarchie d'exceptions")
    print("  14.7 - Propagation")
    print("  14.8 - Relancer exception")
    print("  14.9 - Context manager")
    print("  14.10 - Retry pattern")
    print("  14.11 - Validateur complet")
    print("  14.12 - Fichiers securises")
    print("  14.13 - Exception chainee")
    print("  14.14 - Pagination securisee")
    print("  14.15 - Systeme de logging complet")
    print("=" * 50)
