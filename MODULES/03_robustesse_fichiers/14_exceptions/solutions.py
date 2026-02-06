# =============================================================================
# CHAPITRE 14: EXCEPTIONS - SOLUTIONS
# =============================================================================


# =============================================================================
# EXERCICE 14.1 - TRY/EXCEPT SIMPLE
# =============================================================================
def exercice_14_1():
    """Division avec gestion d'erreur."""
    def diviser(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None
    
    print(diviser(10, 2))
    print(diviser(10, 0))


# =============================================================================
# EXERCICE 14.2 - PLUSIEURS EXCEPTIONS
# =============================================================================
def exercice_14_2():
    """Analyse avec plusieurs exceptions."""
    def analyser(valeur):
        try:
            return int(valeur)
        except ValueError:
            print(f"Erreur: '{valeur}' n'est pas un entier")
        except ZeroDivisionError:
            print("Division par zéro lors de la conversion")
    
    print(analyser("42"))
    print(analyser("abc"))


# =============================================================================
# EXERCICE 14.3 - ELSE ET FINALLY
# =============================================================================
def exercice_14_3():
    """Demonstration de else et finally."""
    def compter_lignes(fichier):
        try:
            # Simulation: lire des donnees
            donnees = ["ligne1", "ligne2", "ligne3"]
            nb_lignes = len(donnees)
        except Exception as e:
            print(f"Erreur: {e}")
        else:
            print(f"Nombre de lignes: {nb_lignes}")
        finally:
            print("Fermeture du fichier")
    
    compter_lignes("fichier.txt")


# =============================================================================
# EXERCICE 14.4 - EXCEPTION PERSONNALISEE
# =============================================================================
def exercice_14_4():
    """Exception personnalisee avec attributs."""
    class ErreurPersonnalisee(Exception):
        def __init__(self, code, message):
            self.code = code
            self.message = message
            super().__init__(f"[{code}] {message}")
    
    try:
        raise ErreurPersonnalisee(404, "Ressource non trouvee")
    except ErreurPersonnalisee as e:
        print(e)


# =============================================================================
# EXERCICE 14.5 - VALIDATION SIMPLE
# =============================================================================
def exercice_14_5():
    """Validation d'email avec exceptions."""
    def valider_email(email):
        if '@' not in email:
            raise ValueError("Email doit contenir '@'")
        if '.' not in email:
            raise ValueError("Email doit contenir '.'")
        return True
    
    try:
        valider_email("test@email.com")
        print("Email valide!")
    except ValueError as e:
        print(f"Erreur: {e}")


# =============================================================================
# EXERCICE 14.6 - HIERARCHIE D'EXCEPTIONS
# =============================================================================
def exercice_14_6():
    """Hierarchie d'exceptions."""
    class ApplicationError(Exception):
        pass
    
    class ValidationError(ApplicationError):
        pass
    
    class DatabaseError(ApplicationError):
        pass
    
    class NetworkError(ApplicationError):
        pass
    
    def traiter_donnees():
        raise ValidationError("Donnees invalides")
    
    try:
        traiter_donnees()
    except ApplicationError as e:
        print(f"Erreur d'application: {e}")


# =============================================================================
# EXERCICE 14.7 - PROPAGATION
# =============================================================================
def exercice_14_7():
    """Propagation d'exceptions."""
    def niveau3():
        raise ValueError("Erreur au niveau 3")
    
    def niveau2():
        niveau3()
    
    def niveau1():
        try:
            niveau2()
        except ValueError as e:
            print(f"Attrapee au niveau 1: {e}")
    
    niveau1()


# =============================================================================
# EXERCICE 14.8 - RELANCER EXCEPTION
# =============================================================================
def exercice_14_8():
    """Relancer une exception."""
    def operation_risquee():
        try:
            raise ValueError("Erreur originale")
        except ValueError as e:
            print(f"Traitement: {e}")
            raise
    
    try:
        operation_risquee()
    except ValueError:
        print("Exception geree au plus haut niveau")


# =============================================================================
# EXERCICE 14.9 - CONTEXT MANAGER
# =============================================================================
def exercice_14_9():
    """Context manager pour mesurer le temps."""
    import time
    
    class Timer:
        def __enter__(self):
            self.start = time.time()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.time()
            self.duree = self.end - self.start
            print(f"Temps d'execution: {self.duree:.4f}s")
            return False
    
    with Timer():
        total = sum(range(1000000))


# =============================================================================
# EXERCICE 14.10 - RETRY PATTERN
# =============================================================================
def exercice_14_10():
    """Retry avec delai."""
    import time
    
    def avec_retry(max_attempts=3, delay=0.1):
        def decorator(func):
            def wrapper():
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func()
                    except Exception as e:
                        if attempt == max_attempts:
                            raise
                        print(f"Tentative {attempt} echouee: {e}")
                        time.sleep(delay)
                return None
            return wrapper
        return decorator
    
    @avec_retry(max_attempts=3, delay=0.1)
    def operation_aleatoire():
        import random
        if random.random() < 0.7:
            raise ConnectionError("Connexion refusee")
        return "Succes!"
    
    print(avec_retry()())


# =============================================================================
# EXERCICE 14.11 - VALIDATEUR COMPLET
# =============================================================================
def exercice_14_11():
    """Systeme de validation complet."""
    class ValidationError(Exception):
        def __init__(self, champ, valeur, message):
            self.champ = champ
            self.valeur = valeur
            self.message = message
            super().__init__(f"[{champ}] {message}")
    
    class Validator:
        @staticmethod
        def required(value, champ):
            if value is None or value == "":
                raise ValidationError(champ, value, "requis")
        
        @staticmethod
        def min(value, min_val, champ):
            if value < min_val:
                raise ValidationError(champ, value, f"min: {min_val}")
        
        @staticmethod
        def max(value, max_val, champ):
            if value > max_val:
                raise ValidationError(champ, value, f"max: {max_val}")
        
        @staticmethod
        def pattern(value, regex, champ):
            import re
            if not re.match(regex, value):
                raise ValidationError(champ, value, f"pattern non matche")
    
    def validate(data, rules):
        for champ, regles in rules.items():
            valeur = data.get(champ)
            for validateur, arg in regles:
                validateur(valeur, arg, champ)
    
    data = {"age": 25, "nom": "Alice"}
    rules = {
        "age": [(Validator.required, None), (Validator.min, 0), (Validator.max, 120)],
        "nom": [(Validator.required, None)]
    }
    
    try:
        validate(data, rules)
        print("Validation reussie!")
    except ValidationError as e:
        print(f"Erreur: {e}")


# =============================================================================
# EXERCICE 14.12 - SYSTÈME DE FICHIERS SÉCURISÉ
# =============================================================================
def exercice_14_12():
    """Operations sur fichiers avec gestion d'erreurs."""
    class FileError(Exception):
        pass
    
    def lire_fichier_securise(chemin):
        try:
            with open(chemin, 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise FileError(f"Fichier non trouve: {chemin}")
        except PermissionError:
            raise FileError(f"Permission refusee: {chemin}")
        except Exception as e:
            raise FileError(f"Erreur inattendue: {e}")
    
    def ecrire_fichier_securise(chemin, contenu):
        try:
            with open(chemin, 'w') as f:
                f.write(contenu)
        except PermissionError:
            raise FileError(f"Permission refusee: {chemin}")
        except Exception as e:
            raise FileError(f"Erreur inattendue: {e}")


# =============================================================================
# EXERCICE 14.13 - EXCEPTION CHAINEE
# =============================================================================
def exercice_14_13():
    """Chainage d'exceptions avec 'from'."""
    try:
        raise ValueError("Erreur initiale")
    except ValueError as e:
        raise RuntimeError("Erreur secondaire") from e


# =============================================================================
# EXERCICE 14.14 - PAGINATION SÉCURISÉE
# =============================================================================
def exercice_14_14():
    """Pagination avec validation."""
    class PaginationError(Exception):
        pass
    
    class Pagination:
        def __init__(self, total_items, page=1, page_size=10):
            self.total_items = total_items
            self._page = page
            self._page_size = page_size
        
        @property
        def page(self):
            return self._page
        
        @page.setter
        def page(self, value):
            if value < 1:
                raise PaginationError("La page doit etre >= 1")
            if value > self.total_pages:
                raise PaginationError(f"La page doit etre <= {self.total_pages}")
            self._page = value
        
        @property
        def page_size(self):
            return self._page_size
        
        @page_size.setter
        def page_size(self, value):
            if value < 1:
                raise PaginationError("La taille doit etre >= 1")
            if value > 100:
                raise PaginationError("La taille maximale est 100")
            self._page_size = value
        
        @property
        def total_pages(self):
            return (self.total_items + self.page_size - 1) // self.page_size
        
        def get_offset(self):
            return (self.page - 1) * self.page_size
    
    p = Pagination(100, page=1, page_size=10)
    print(f"Total pages: {p.total_pages}")
    print(f"Offset: {p.get_offset()}")


# =============================================================================
# EXERCICE 14.15 - SYSTÈME DE LOGGING COMPLET
# =============================================================================
def exercice_14_15():
    """Systeme avec logging et gestion d'erreurs."""
    import logging
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    class AppError(Exception):
        pass
    
    class DatabaseError(AppError):
        pass
    
    class ValidationError(AppError):
        pass
    
    class DatabaseOperation:
        def __init__(self):
            self.retry_count = 0
        
        def execute(self, query):
            try:
                if self.retry_count < 2:
                    self.retry_count += 1
                    raise DatabaseError("Connexion echouee")
                return f"Resultat: {query}"
            except DatabaseError as e:
                logger.error(f"Database error: {e}")
                raise
    
    def valider_donnees(data):
        if not data:
            raise ValidationError("Donnees vides")
        return True
    
    try:
        db = DatabaseOperation()
        resultat = db.execute("SELECT * FROM users")
        valider_donnees(resultat)
    except AppError as e:
        logger.critical(f"Erreur critique: {e}")
