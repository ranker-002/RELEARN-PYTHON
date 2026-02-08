"""
Utilitaires de Vérification Flexible
=====================================

Ce module fournit des fonctions pour valider les exercices
de manière flexible, en acceptant différentes approches
pour trouver la solution.

Fonctions:
- compare_output(): Compare deux sorties de manière flexible
- contains_terms(): Vérifie la présence de termes clés
- compare_numbers(): Compare des nombres avec tolérance
- verify_exercise(): Vérification complète d'un exercice
"""

import re
import ast
from typing import Optional, List, Tuple, Any, Union
from io import StringIO
import sys
from unittest import mock


def normalize_output(output: str) -> str:
    """
    Normalise une sortie pour comparaison flexible.
    
    - Convertit en minuscule
    - Supprime les espaces multiples
    - Supprime la ponctuation non essentielle
    """
    if not output:
        return ""
    
    # Convertir en minuscule
    normalized = output.lower()
    
    # Remplacer plusieurs espaces par un seul
    normalized = re.sub(r'\s+', ' ', normalized)
    
    # Supprimer la ponctuation pour la comparaison
    normalized = re.sub(r'[.,;:!?]', '', normalized)
    
    return normalized.strip()


def contains_terms(output: str, terms: List[str], 
                  ignore_case: bool = True,
                  allow_partial: bool = True) -> Tuple[bool, str]:
    """
    Vérifie si la sortie contient les termes attendus.
    
    Args:
        output: La sortie à vérifier
        terms: Liste des termes à chercher
        ignore_case: Ignorer la casse (défaut: True)
        allow_partial: Accepter les correspondances partielles (défaut: True)
    
    Returns:
        Tuple[bool, str]: (True si tous les termes sont présents, message)
    """
    if not output:
        return False, "La sortie est vide"
    
    normalized_output = normalize_output(output)
    
    for term in terms:
        term_lower = term.lower() if ignore_case else term
        
        if allow_partial:
            # Vérifier que le terme apparaît quelque part
            if term_lower not in normalized_output:
                return False, f"'{term}' non trouvé dans la sortie"
        else:
            # Vérifier la correspondance exacte (après normalisation)
            if term_lower != normalized_output.strip():
                return False, f"Attendu: '{term}'"
    
    return True, "Tous les termes sont présents"


def extract_numbers(output: str) -> List[Union[int, float]]:
    """
    Extrait tous les nombres d'une sortie.
    
    Returns:
        Liste des nombres trouvés (int ou float)
    """
    if not output:
        return []
    
    # Chercher les nombres (entiers, décimaux, négatifs)
    pattern = r'-?\d+(?:\.\d+)?'
    matches = re.findall(pattern, output)
    
    numbers = []
    for match in matches:
        if '.' in match:
            numbers.append(float(match))
        else:
            numbers.append(int(match))
    
    return numbers


def compare_numbers(output: str, 
                    expected: Union[int, float],
                    tolerance: float = 0.01) -> Tuple[bool, str]:
    """
    Vérifie si la sortie contient le nombre attendu.
    
    Args:
        output: La sortie à vérifier
        expected: Le nombre attendu
        tolerance: Marge d'erreur tolérée pour les floats
    
    Returns:
        Tuple[bool, str]: (True si le nombre est trouvé, message)
    """
    numbers = extract_numbers(output)
    
    for num in numbers:
        if isinstance(expected, int):
            # Pour les entiers, accepter int ou float equivalent
            if isinstance(num, float) and num.is_integer() and int(num) == expected:
                return True, f"Trouvé: {expected}"
            if isinstance(num, int) and num == expected:
                return True, f"Trouvé: {expected}"
        else:
            # Pour les floats, utiliser la tolérance
            if abs(num - expected) < tolerance:
                return True, f"Trouvé: {expected}"
    
    return False, f"Nombre {expected} non trouvé dans la sortie"


def normalize_number(num_str: str) -> Union[int, float]:
    """Convertit une chaîne en nombre (int ou float)."""
    if '.' in num_str:
        return float(num_str)
    return int(num_str)


def extract_strings(output: str) -> List[str]:
    """
    Extrait les chaînes de caractères entre guillemets.
    
    Returns:
        Liste des chaînes trouvées (sans les guillemets)
    """
    if not output:
        return []
    
    # Chercher les chaînes entre guillemets doubles ou simples
    pattern = r'["\']([^"\']*)["\']'
    matches = re.findall(pattern, output)
    
    return matches


def contains_string(output: str, 
                   expected: str,
                   ignore_case: bool = True) -> Tuple[bool, str]:
    """
    Vérifie si la sortie contient la chaîne attendue.
    
    Args:
        output: La sortie à vérifier
        expected: La chaîne attendue (sans guillemets)
        ignore_case: Ignorer la casse
    
    Returns:
        Tuple[bool, str]: (True si présent, message)
    """
    strings = extract_strings(output)
    
    for s in strings:
        if ignore_case:
            if expected.lower() in s.lower():
                return True, f"'{expected}' trouvé"
        else:
            if expected in s:
                return True, f"'{expected}' trouvé"
    
    return False, f"'{expected}' non trouvé dans les chaînes"


def run_with_mocks(func, 
                   inputs: Optional[List[str]] = None,
                   globals_dict: Optional[dict] = None) -> Tuple[str, Any]:
    """
    Exécute une fonction avec des mocks optionnels.
    
    Args:
        func: La fonction à exécuter
        inputs: Liste des valeurs à retourner pour input()
        globals_dict: Dictionnaire de globales
    
    Returns:
        Tuple[stdout, valeur de retour]
    """
    captured = StringIO()
    
    def mock_input(prompt=""):
        if inputs:
            return inputs.pop(0)
        return ""
    
    old_stdout = sys.stdout
    sys.stdout = captured
    
    mock_input_obj = mock.patch('builtins.input', side_effect=inputs or [])
    
    result = None
    try:
        mock_input_obj.start()
        if globals_dict:
            result = func(**globals_dict) if isinstance(globals_dict, dict) else func()
        else:
            result = func()
    except Exception as e:
        raise e
    finally:
        sys.stdout = old_stdout
        mock_input_obj.stop()
    
    output = captured.getvalue()
    return output, result


def capture_output(func) -> str:
    """
    Capture la sortie stdout d'une fonction.
    
    Returns:
        La sortie capturée
    """
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        func()
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout


def verify_output_contains(output: str, 
                          required_terms: List[str],
                          optional_terms: Optional[List[str]] = None,
                          optional_count: int = 1) -> Tuple[bool, str]:
    """
    Vérifie que la sortie contient les termes requis.
    
    Args:
        output: La sortie à vérifier
        required_terms: Termes obligatoires (au moins N doivent être présents)
        optional_terms: Termes optionnels
        optional_count: Nombre minimum de termes optionnels requis
    
    Returns:
        Tuple[bool, str]: (Valide, message)
    """
    if not output:
        return False, "La sortie est vide"
    
    normalized = normalize_output(output)
    found_terms = []
    missing_terms = []
    
    for term in required_terms:
        if term.lower() in normalized:
            found_terms.append(term)
        else:
            missing_terms.append(term)
    
    # Vérifier les termes optionnels
    optional_found = 0
    if optional_terms:
        for term in optional_terms:
            if term.lower() in normalized:
                optional_found += 1
    
    # Au moins un terme requis DOIT être trouvé
    # OU assez de termes optionnels
    if optional_count > 0:
        total_found = len(found_terms) + optional_found
        if total_found < optional_count:
            return False, f"Termes insuffisants: attendu ~{optional_count}, trouvé {total_found}"
    else:
        if not found_terms:
            return False, f"Aucun terme requis trouvé: {missing_terms}"
    
    return True, f"Trouvé: {', '.join(found_terms)}"


class FlexibleVerifier:
    """
    Vérificateur flexible pour les exercices Python.
    
    Supporte:
    - Comparaison insensible à la casse
    - Nombres avec tolérance
    - Termes clés plutôt que sortie exacte
    - Plusieurs approches pour une même solution
    """
    
    def __init__(self, exercise_name: str):
        self.exercise_name = exercise_name
        self.tests_passed = 0
        self.tests_failed = 0
        self.errors = []
    
    def check_output_terms(self,
                          output: str,
                          required_terms: List[str],
                          optional_terms: Optional[List[str]] = None,
                          optional_count: int = 1,
                          error_message: str = "") -> bool:
        """
        Vérifie la présence de termes dans la sortie.
        """
        valid, msg = verify_output_contains(
            output, required_terms, optional_terms, optional_count
        )
        
        if valid:
            self.tests_passed += 1
            return True
        else:
            self.tests_failed += 1
            self.errors.append(f"{self.exercise_name}: {error_message or msg}")
            return False
    
    def check_number(self,
                     output: str,
                     expected: Union[int, float],
                     tolerance: float = 0.01,
                     error_message: str = "") -> bool:
        """
        Vérifie la présence d'un nombre dans la sortie.
        """
        valid, msg = compare_numbers(output, expected, tolerance)
        
        if valid:
            self.tests_passed += 1
            return True
        else:
            self.tests_failed += 1
            self.errors.append(f"{self.exercise_name}: {error_message or msg}")
            return False
    
    def check_string(self,
                     output: str,
                     expected: str,
                     ignore_case: bool = True,
                     error_message: str = "") -> bool:
        """
        Vérifie la présence d'une chaîne dans la sortie.
        """
        valid, msg = contains_string(output, expected, ignore_case)
        
        if valid:
            self.tests_passed += 1
            return True
        else:
            self.tests_failed += 1
            self.errors.append(f"{self.exercise_name}: {error_message or msg}")
            return False
    
    def summary(self) -> str:
        """Retourne un résumé des tests."""
        if self.tests_failed == 0:
            return f"✓ {self.exercise_name} - CORRECT"
        else:
            return f"✗ {self.exercise_name}: {'; '.join(self.errors)}"


def flexible_verify(func,
                   inputs: Optional[List[str]] = None,
                   required_terms: Optional[List[str]] = None,
                   optional_terms: Optional[List[str]] = None,
                   optional_count: int = 1,
                   required_numbers: Optional[List[Union[int, float]]] = None,
                   tolerance: float = 0.01,
                   exercise_name: str = "") -> bool:
    """
    Vérification flexible d'un exercice.
    
    Args:
        func: La fonction de l'exercice
        inputs: Valeurs pour input()
        required_terms: Termes obligatoires dans la sortie
        optional_terms: Termes optionnels
        optional_count: Nombre de termes (requis + optionnels) minimum
        required_numbers: Nombres devant apparaître dans la sortie
        tolerance: Tolérance pour les comparaisons de floats
        exercise_name: Nom de l'exercice
    
    Returns:
        True si tous les tests passent
    """
    verifier = FlexibleVerifier(exercise_name)
    
    # Capturer la sortie
    if inputs:
        output, _ = run_with_mocks(func, inputs)
    else:
        output = capture_output(func)
    
    # Vérifier les termes
    if required_terms or optional_terms:
        verifier.check_output_terms(
            output, 
            required_terms or [],
            optional_terms,
            optional_count
        )
    
    # Vérifier les nombres
    if required_numbers:
        for num in required_numbers:
            verifier.check_number(output, num, tolerance)
    
    # Afficher le résultat
    print(verifier.summary())
    
    return verifier.tests_failed == 0


# Alias pour compatibilité
FlexibleVerificationError = VerificationError = Exception


def lenient_comparison(output: str, 
                      expected: str,
                      ignore_case: bool = True,
                      ignore_whitespace: bool = True,
                      ignore_punctuation: bool = True) -> bool:
    """
    Compare deux sorties de manière souple.
    
    Returns:
        True si les sorties sont "équivalentes"
    """
    if not output or not expected:
        return False
    
    o, e = output, expected
    
    if ignore_case:
        o = o.lower()
        e = e.lower()
    
    if ignore_whitespace:
        o = re.sub(r'\s+', ' ', o)
        e = re.sub(r'\s+', ' ', e)
    
    if ignore_punctuation:
        o = re.sub(r'[.,;:!?]', '', o)
        e = re.sub(r'[.,;:!?]', '', e)
    
    return o.strip() == e.strip()


# ============================================================================
# FONCTIONS DE CONVENIENCE POUR LA VÉRIFICATION RAPIDE
# ============================================================================

def check_hello_world(output: str) -> bool:
    """Vérifie que la sortie contient 'hello' et 'world'."""
    normalized = normalize_output(output)
    return 'hello' in normalized and 'world' in normalized


def check_calculator_output(output: str) -> Tuple[bool, List[str]]:
    """Vérifie les 4 opérations d'une calculatrice."""
    numbers = extract_numbers(output)
    ops_found = []
    
    if 12 in numbers or 12.0 in numbers:
        ops_found.append("Addition")
    if 8 in numbers or 8.0 in numbers:
        ops_found.append("Soustraction")
    if 20 in numbers or 20.0 in numbers:
        ops_found.append("Multiplication")
    if 5 in numbers or 5.0 in numbers:
        ops_found.append("Division")
    
    return len(ops_found) >= 4, ops_found


def check_temperature(output: str) -> bool:
    """Vérifie la conversion 25°C -> 77°F."""
    numbers = extract_numbers(output)
    return 77 in numbers or 77.0 in numbers


def check_imc(output: str) -> bool:
    """Vérifie le calcul d'IMC (70kg, 1.75m -> ~22.86)."""
    numbers = extract_numbers(output)
    for num in numbers:
        if 22 <= num <= 23:
            return True
    return False


if __name__ == "__main__":
    # Test des utilitaires
    print("=== Test de vérification flexible ===")
    
    # Test 1: Hello World
    output1 = "Hello World!"
    print(f"'{output1}' -> {check_hello_world(output1)}")  # True
    
    output2 = "HELLO WORLD"
    print(f"'{output2}' -> {check_hello_world(output2)}")  # True
    
    output3 = "hello le monde"
    print(f"'{output3}' -> {check_hello_world(output3)}")  # False
    
    # Test 2: Nombres
    print(f"\nNombres dans 'Le resultat est 42.5 et 100': {extract_numbers('Le resultat est 42.5 et 100')}")
    
    # Test 3: Vérification flexible
    verifier = FlexibleVerifier("Test Exercise")
    print(f"\n{verifier.summary()}")
