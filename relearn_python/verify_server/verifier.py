"""Logique d'exécution des tests de vérification.

Ce module gère l'exécution de verification.py et le parsing des résultats.
"""

import re
import subprocess
import sys
import tempfile
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict


@dataclass
class ExerciseResult:
    """Résultat d'un exercice individuel."""
    num: str
    name: str
    status: str  # "passed", "failed", "error"
    output: str = ""
    error_message: str = ""
    suggestion: str = ""


@dataclass
class VerificationResults:
    """Résultats complets de la vérification."""
    chapter: str
    title: str
    total: int
    passed: int
    failed: int
    exercises: List[ExerciseResult] = field(default_factory=list)
    error: str = ""


def detect_verification_pattern(verif_path: Path) -> str:
    """Détecte le pattern de vérification utilisé.
    
    Returns:
        "pattern_a" si mock.patch présent (chapitres 1-16)
        "pattern_b" sinon (chapitres 17-26)
    """
    content = verif_path.read_text(encoding="utf-8")
    if "mock.patch" in content:
        return "pattern_a"
    return "pattern_b"


def extract_chapter_title(readme_path: Path) -> str:
    """Extrait le titre du chapitre depuis README.md."""
    if not readme_path.exists():
        return "Chapitre"
    
    content = readme_path.read_text(encoding="utf-8")
    # Chercher le premier titre markdown
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        title = match.group(1)
        # Nettoyer le titre
        title = re.sub(r"Chapitre \d+ :\s*", "", title)
        return title.strip()
    return "Chapitre"


def get_chapter_info(chapter_path: Path) -> Dict[str, Any]:
    """Récupère les informations du chapitre."""
    readme_path = chapter_path / "README.md"
    verif_path = chapter_path / "verification.py"
    
    title = extract_chapter_title(readme_path)
    pattern = detect_verification_pattern(verif_path) if verif_path.exists() else "unknown"
    
    # Compter le nombre d'exercices
    exercises_count = 0
    exercises_path = chapter_path / "exercices.py"
    if exercises_path.exists():
        content = exercises_path.read_text(encoding="utf-8")
        # Compter les fonctions exercice_X_Y
        exercises_count = len(re.findall(r"^def\s+exercice_\d+_\d+", content, re.MULTILINE))
    
    return {
        "chapter": chapter_path.name,
        "title": title,
        "pattern": pattern,
        "total_exercises": exercises_count
    }


def parse_verification_output(output: str) -> List[ExerciseResult]:
    """Parse la sortie de verification.py pour extraire les résultats.
    
    Format attendu:
    ✓ Exercice X.Y: Nom - CORRECT
    ✗ X.Y: ERREUR - Message
    ✗ X.Y: EXCEPTION - Message
    """
    results = []
    
    lines = output.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Pattern pour exercice réussi
        # ✓ Exercice 1.1: Hello World - CORRECT
        # ✓ 1.1: Nom - CORRECT
        success_match = re.match(r'^[✓√]\s*(?:Exercice\s+)?(\d+\.\d+)[:\s]+(.+?)\s*[-–]\s*CORRECT', line)
        if success_match:
            num = success_match.group(1)
            name = success_match.group(2).strip()
            results.append(ExerciseResult(
                num=num,
                name=name,
                status="passed",
                output=""
            ))
            continue
        
        # Pattern pour erreur
        # ✗ 1.3: ERREUR
        # ✗ Exercice 1.3: ERREUR - Message
        error_match = re.match(r'^[✗×X]\s*(?:Exercice\s+)?(\d+\.\d+)[:\s]+(.+)', line)
        if error_match:
            num = error_match.group(1)
            rest = error_match.group(2).strip()
            
            # Extraire le nom et le message d'erreur
            name = rest
            error_msg = ""
            
            if "ERREUR" in rest:
                parts = rest.split("ERREUR", 1)
                name = parts[0].replace(":", "").strip()
                error_msg = parts[1].strip(" -:")
            elif "EXCEPTION" in rest:
                parts = rest.split("EXCEPTION", 1)
                name = parts[0].replace(":", "").strip()
                error_msg = parts[1].strip(" -:")
            
            # Générer une suggestion basée sur l'erreur
            suggestion = generate_suggestion(error_msg)
            
            results.append(ExerciseResult(
                num=num,
                name=name,
                status="failed",
                error_message=error_msg,
                suggestion=suggestion
            ))
            continue
    
    return results


def generate_suggestion(error_msg: str) -> str:
    """Génère une suggestion basée sur le message d'erreur."""
    error_lower = error_msg.lower()
    
    if "input" in error_lower or "float" in error_lower or "int" in error_lower:
        return "Vérifiez que vous convertissez bien les inputs en nombres avec float() ou int()"
    
    if "somme" in error_lower or "addition" in error_lower:
        return "Assurez-vous d'additionner les valeurs numériques, pas de les concaténer comme du texte"
    
    if "print" in error_lower:
        return "Vérifiez l'utilisation de print() et le format de votre sortie"
    
    if "variable" in error_lower or "définie" in error_lower:
        return "Assurez-vous de définir la variable avant de l'utiliser"
    
    if "syntax" in error_lower or "indentation" in error_lower:
        return "Vérifiez la syntaxe Python (indentation, parenthèses, deux-points)"
    
    return "Relisez attentivement l'énoncé et comparez avec la solution"


def run_verification(chapter_path: Path) -> Dict[str, Any]:
    """Exécute le script de vérification et retourne les résultats structurés.
    
    Args:
        chapter_path: Chemin vers le dossier du chapitre
        
    Returns:
        Dictionnaire avec les résultats de vérification
    """
    verif_path = chapter_path / "verification.py"
    
    if not verif_path.exists():
        raise FileNotFoundError(f"Fichier verification.py non trouvé dans {chapter_path}")
    
    # Récupérer les infos du chapitre
    info = get_chapter_info(chapter_path)
    
    # Créer un script temporaire pour capturer les résultats
    script_content = f"""
import sys
sys.path.insert(0, str({repr(str(chapter_path))}))

# Exécuter verification.py
try:
    exec(open({repr(str(verif_path))}).read())
except Exception as e:
    print(f"ERREUR_GLOBALE: {{e}}")
    sys.exit(1)
"""
    
    # Exécuter dans un subprocess pour isoler
    try:
        result = subprocess.run(
            [sys.executable, "-c", script_content],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(chapter_path)
        )
        
        output = result.stdout + result.stderr
        
    except subprocess.TimeoutExpired:
        return asdict(VerificationResults(
            chapter=info["chapter"],
            title=info["title"],
            total=info["total_exercises"],
            passed=0,
            failed=0,
            error="Timeout - La vérification a pris trop de temps"
        ))
    except Exception as e:
        return asdict(VerificationResults(
            chapter=info["chapter"],
            title=info["title"],
            total=info["total_exercises"],
            passed=0,
            failed=0,
            error=f"Erreur lors de l'exécution: {str(e)}"
        ))
    
    # Parser les résultats
    exercises = parse_verification_output(output)
    
    # Si aucun exercice trouvé, essayer de parser différemment
    if not exercises:
        # Essayer de parser la sortie brute
        exercises = parse_raw_output(output, info["total_exercises"])
    
    # Compter les succès/échecs
    passed = sum(1 for ex in exercises if ex.status == "passed")
    failed = len(exercises) - passed
    
    # Si pas d'exercices trouvés mais pas d'erreur globale
    error_msg = ""
    if "ERREUR_GLOBALE" in output:
        match = re.search(r'ERREUR_GLOBALE:\s*(.+)', output)
        if match:
            error_msg = match.group(1)
    
    results = VerificationResults(
        chapter=info["chapter"],
        title=info["title"],
        total=len(exercises) or info["total_exercises"],
        passed=passed,
        failed=failed,
        exercises=exercises,
        error=error_msg
    )
    
    return asdict(results)


def parse_raw_output(output: str, expected_count: int) -> List[ExerciseResult]:
    """Parse la sortie brute quand le format standard n'est pas trouvé.
    
    Cette fonction est un fallback pour gérer différents formats de sortie.
    """
    exercises = []
    
    # Chercher des patterns alternatifs
    lines = output.split('\n')
    
    for line in lines:
        # Chercher des numéros d'exercice
        match = re.search(r'(\d+)\.(\d+)', line)
        if match:
            num = f"{match.group(1)}.{match.group(2)}"
            
            # Déterminer le statut
            status = "unknown"
            if any(c in line for c in ['✓', '√', 'CORRECT', 'SUCCESS']):
                status = "passed"
            elif any(c in line for c in ['✗', '×', 'X', 'ERREUR', 'ERROR', 'FAIL']):
                status = "failed"
            
            if status != "unknown":
                exercises.append(ExerciseResult(
                    num=num,
                    name=f"Exercice {num}",
                    status=status,
                    output=line
                ))
    
    return exercises


def run_single_verification(chapter_path: Path, exercise_num: str) -> Dict[str, Any]:
    """Exécute la vérification d'un seul exercice.
    
    Args:
        chapter_path: Chemin vers le dossier du chapitre
        exercise_num: Numéro de l'exercice (ex: "1.1", "1.2")
        
    Returns:
        Dictionnaire avec le résultat de l'exercice
    """
    verif_path = chapter_path / "verification.py"
    
    if not verif_path.exists():
        raise FileNotFoundError(f"Fichier verification.py non trouvé dans {chapter_path}")
    
    # Convertir le numéro en nom de fonction
    func_name = f"verifier_exercice_{exercise_num.replace('.', '_')}"
    
    # Créer un script temporaire pour tester un seul exercice
    script_content = f"""
import sys
sys.path.insert(0, str({repr(str(chapter_path))}))

# Importer et exécuter la fonction de vérification spécifique
try:
    from verification import {func_name}
    {func_name}()
    print("✓ Exercice {exercise_num}: CORRECT")
except Exception as e:
    print(f"✗ {exercise_num}: ERREUR - {{e}}")
    sys.exit(1)
"""
    
    try:
        result = subprocess.run(
            [sys.executable, "-c", script_content],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(chapter_path)
        )
        
        output = result.stdout + result.stderr
        
        # Parser le résultat
        exercises = parse_verification_output(output)
        
        if exercises:
            return asdict(exercises[0])
        else:
            # Fallback
            return {
                "num": exercise_num,
                "name": f"Exercice {exercise_num}",
                "status": "passed" if result.returncode == 0 else "failed",
                "output": output,
                "error_message": "",
                "suggestion": ""
            }
            
    except subprocess.TimeoutExpired:
        return {
            "num": exercise_num,
            "name": f"Exercice {exercise_num}",
            "status": "failed",
            "output": "",
            "error_message": "Timeout - La vérification a pris trop de temps",
            "suggestion": ""
        }
    except Exception as e:
        return {
            "num": exercise_num,
            "name": f"Exercice {exercise_num}",
            "status": "failed",
            "output": "",
            "error_message": str(e),
            "suggestion": ""
        }
