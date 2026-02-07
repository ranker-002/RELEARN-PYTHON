"""Extraction de code source des exercices et solutions.

Ce module permet d'extraire le code de fonctions spécifiques
à partir des fichiers exercices.py et solutions.py.
"""

import ast
import re
from pathlib import Path
from typing import Optional


def extract_exercise_code(chapter_path: Path, exercise_num: str) -> Optional[str]:
    """Extrait le code d'un exercice spécifique.
    
    Essaie d'abord dans le dossier exercices/, sinon dans exercices.py.
    
    Args:
        chapter_path: Chemin vers le dossier du chapitre
        exercise_num: Numéro de l'exercice (ex: "1.1", "2.3")
        
    Returns:
        Le code source ou None si non trouvé
    """
    # Extraire le numéro d'exercice (ex: "1.1" -> "1", "1.10" -> "10")
    ex_num = exercise_num.split('.')[-1]
    
    # Essayer d'abord le nouveau format (fichiers individuels)
    exercises_dir = chapter_path / "exercices"
    if exercises_dir.exists():
        # Chercher le fichier correspondant (ex_01_*, ex_1_*, etc.)
        for file_path in exercises_dir.glob("ex_*.py"):
            if file_path.name == "__init__.py":
                continue
            # Extraire le numéro du nom de fichier (avec ou sans zéro)
            match = re.match(r'ex_(\d+)_.*\.py', file_path.name)
            if match:
                file_num = match.group(1)
                # Comparer sans le zéro de padding (01 == 1)
                if int(file_num) == int(ex_num):
                    return extract_function_code(file_path, "run")
    
    # Fallback sur l'ancien format
    exercises_path = chapter_path / "exercices.py"
    if exercises_path.exists():
        func_name = f"exercice_{exercise_num.replace('.', '_')}"
        return extract_function_code(exercises_path, func_name)
    
    return None


def extract_solution_code(chapter_path: Path, exercise_num: str) -> Optional[str]:
    """Extrait le code d'une solution spécifique depuis solutions.py.
    
    Args:
        chapter_path: Chemin vers le dossier du chapitre
        exercise_num: Numéro de l'exercice (ex: "1.1", "2.3")
        
    Returns:
        Le code source de la fonction solution ou None si non trouvée
    """
    solutions_path = chapter_path / "solutions.py"
    
    if not solutions_path.exists():
        return None
    
    # Convertir "1.1" en "exercice_1_1"
    func_name = f"exercice_{exercise_num.replace('.', '_')}"
    
    return extract_function_code(solutions_path, func_name)


def extract_function_code(file_path: Path, func_name: str) -> Optional[str]:
    """Extrait le code source d'une fonction depuis un fichier.
    
    Cette fonction utilise une approche regex pour extraire le code,
    ce qui est plus robuste que AST pour préserver le formatage exact.
    
    Args:
        file_path: Chemin vers le fichier Python
        func_name: Nom de la fonction à extraire
        
    Returns:
        Le code source complet de la fonction ou None
    """
    content = file_path.read_text(encoding="utf-8")
    
    # Pattern pour trouver la fonction
    # Cherche: def func_name( ... ):
    pattern = rf'^def\s+{re.escape(func_name)}\s*\([^)]*\)(?:\s*->\s*[^:]+)?:\s*$'
    
    lines = content.split('\n')
    start_line = -1
    
    # Trouver la ligne de début
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_line = i
            break
    
    if start_line == -1:
        return None
    
    # Trouver la fin de la fonction
    # On compte les niveaux d'indentation
    end_line = start_line + 1
    base_indent = None
    
    for i in range(start_line + 1, len(lines)):
        line = lines[i]
        
        # Ligne vide ou commentaire - on continue
        if not line.strip() or line.strip().startswith('#'):
            end_line = i + 1
            continue
        
        # Déterminer l'indentation de base (première ligne non vide du corps)
        if base_indent is None:
            stripped = line.lstrip()
            if stripped:  # Ligne non vide
                base_indent = len(line) - len(stripped)
        
        # Vérifier si on sort de la fonction
        if base_indent is not None:
            stripped = line.lstrip()
            if stripped and len(line) - len(stripped) < base_indent:
                # C'est une ligne moins indentée - fin de la fonction
                end_line = i
                break
        
        end_line = i + 1
    
    # Extraire le code
    function_lines = lines[start_line:end_line]
    
    # Nettoyer les lignes vides à la fin
    while function_lines and not function_lines[-1].strip():
        function_lines.pop()
    
    return '\n'.join(function_lines)


def get_all_exercises(chapter_path: Path) -> list:
    """Liste tous les exercices disponibles dans un chapitre.
    
    Returns:
        Liste de tuples (numéro, nom) pour chaque exercice
    """
    exercises_path = chapter_path / "exercices.py"
    
    if not exercises_path.exists():
        return []
    
    content = exercises_path.read_text(encoding="utf-8")
    exercises = []
    
    # Chercher toutes les fonctions exercice_X_Y
    pattern = r'^def\s+exercice_(\d+)_(\d+)\s*\('
    
    for match in re.finditer(pattern, content, re.MULTILINE):
        chapter_num = match.group(1)
        exercise_num = match.group(2)
        num = f"{chapter_num}.{exercise_num}"
        
        # Essayer d'extraire le nom depuis le commentaire précédent
        func_name = f"Exercice {num}"
        
        # Chercher un commentaire juste au-dessus
        start_pos = match.start()
        lines_before = content[:start_pos].split('\n')[-5:]  # 5 lignes avant
        
        for line in reversed(lines_before):
            line = line.strip()
            if line.startswith('#') and not line.startswith('# ==='):
                # Extraire le nom du commentaire
                name = line.lstrip('# ').strip()
                if name and len(name) < 50:  # Pas trop long
                    func_name = name
                    break
            elif line.startswith('def'):
                # On est arrivé à une autre fonction
                break
        
        exercises.append((num, func_name))
    
    return sorted(exercises, key=lambda x: [int(n) for n in x[0].split('.')])


def extract_exercise_description(chapter_path: Path, exercise_num: str) -> Optional[str]:
    """Extrait la description d'un exercice depuis son docstring.
    
    Args:
        chapter_path: Chemin vers le dossier du chapitre
        exercise_num: Numéro de l'exercice (ex: "1.1", "2.3")
        
    Returns:
        La description formatée ou None
    """
    # Extraire le numéro d'exercice (ex: "1.1" -> "1", "1.10" -> "10")
    ex_num = exercise_num.split('.')[-1]
    
    # Essayer le nouveau format
    exercises_dir = chapter_path / "exercices"
    if exercises_dir.exists():
        for file_path in exercises_dir.glob("ex_*.py"):
            if file_path.name == "__init__.py":
                continue
            match = re.match(r'ex_(\d+)_.*\.py', file_path.name)
            if match:
                file_num = match.group(1)
                # Comparer sans le zéro de padding
                if int(file_num) == int(ex_num):
                    content = file_path.read_text(encoding="utf-8")
                    # Extraire le docstring
                    match = re.search(r'^"""(.+?)"""', content, re.DOTALL)
                    if match:
                        return match.group(1).strip()
    
    return None


def format_code_for_display(code: str, language: str = "python") -> str:
    """Formate le code pour l'affichage avec syntax highlighting.
    
    Args:
        code: Code source à formater
        language: Langage pour le syntax highlighting
        
    Returns:
        Code HTML formaté
    """
    # Échapper les caractères HTML
    code = code.replace('&', '&amp;')
    code = code.replace('<', '&lt;')
    code = code.replace('>', '&gt;')
    
    return f'<pre><code class="language-{language}">{code}</code></pre>'
