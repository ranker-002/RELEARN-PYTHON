#!/usr/bin/env python3
"""
Script de migration automatique pour RELEARN-PYTHON
Convertit l'ancien format (exercices.py) vers le nouveau format (dossier exercices/)

Usage:
    python migrate_chapter.py <chemin_vers_chapitre>
    
Exemple:
    python migrate_chapter.py MODULES/01_core_fondations/02_variables_types/
"""

import re
import sys
import shutil
from pathlib import Path
from typing import List, Tuple, Optional


def extract_exercise_name(comment_block: str) -> str:
    """Extrait le nom de l'exercice depuis le bloc de commentaires."""
    # Chercher la ligne avec le titre de l'exercice
    lines = comment_block.split('\n')
    for line in lines:
        line = line.strip().lstrip('#').strip()
        # Pattern: "EXERCICE X.Y - NOM"
        if line.startswith('EXERCICE') and '-' in line:
            parts = line.split('-', 1)
            if len(parts) > 1:
                return parts[1].strip()
    return "Exercice"


def extract_exercise_description(comment_block: str) -> str:
    """Extrait la description complète depuis le bloc de commentaires."""
    lines = comment_block.split('\n')
    description_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Ignorer les lignes de séparation
        if stripped.startswith('# ==='):
            continue
        # Garder les lignes avec du contenu
        if stripped.startswith('#'):
            content = stripped.lstrip('#').strip()
            if content and not content.startswith('EXERCICE') and not content.startswith('VOTRE CODE'):
                description_lines.append(content)
    
    return '\n'.join(description_lines)


def parse_exercises(file_path: Path) -> List[Tuple[str, str, str, str]]:
    """
    Parse le fichier exercices.py pour extraire tous les exercices.
    
    Returns:
        Liste de tuples (numero, nom, description, code_complet)
    """
    content = file_path.read_text(encoding='utf-8')
    exercises = []
    
    # Pattern pour trouver chaque exercice
    # Format: "# EXERCICE X.Y - NOM" suivi de commentaires puis "def exercice_X_Y():"
    pattern = r'#\s*={10,}\s*\n#\s*EXERCICE\s+(\d+)\.(\d+)\s*-\s*(.+?)\n#\s*={10,}(.*?)(?=def\s+exercice_\d+_\d+)'
    
    matches = list(re.finditer(pattern, content, re.DOTALL))
    print(f"  📖 {len(matches)} exercices trouvés (étape 1)")
    
    # Si le pattern principal ne fonctionne pas, essayer un autre
    if not matches:
        # Pattern alternatif plus simple
        pattern = r'#\s*EXERCICE\s+(\d+)\.(\d+)\s*-\s*(.+?)(?=\n#\s*VOTRE CODE|$)'
        matches = list(re.finditer(pattern, content, re.DOTALL))
        print(f"  📖 {len(matches)} exercices trouvés (étape 2)")
    
    # Trouver toutes les fonctions
    func_pattern = r'def\s+(exercice_(\d+)_(\d+))\(\):\s*(.*?)(?=\n\n|def\s+exercice_|if\s+__name__|$)'
    func_matches = list(re.finditer(func_pattern, content, re.DOTALL))
    print(f"  📖 {len(func_matches)} fonctions trouvées")
    
    # Associer les noms aux fonctions
    func_dict = {}
    for func_match in func_matches:
        func_name = func_match.group(1)
        chapter_num = func_match.group(2)
        exercise_num = func_match.group(3)
        func_body = func_match.group(4)
        key = f"{chapter_num}.{exercise_num}"
        func_dict[key] = (func_name, chapter_num, exercise_num, func_body)
    
    # Extraire les descriptions
    for match in matches:
        chapter_num = match.group(1)
        exercise_num = match.group(2)
        name = match.group(3).strip()
        description_block = match.group(4)
        
        full_num = f"{chapter_num}.{exercise_num}"
        key = full_num
        
        if key in func_dict:
            func_name, _, _, func_body = func_dict[key]
            description = extract_exercise_description(description_block)
            func_code = f"def {func_name}():\n{func_body}"
            exercises.append((full_num, name, description, func_code))
        else:
            # Fallback: chercher la fonction directement
            func_pattern = rf'def\s+exercice_{chapter_num}_{exercise_num}\(\):\s*(.*?)(?=\n\n|def\s+exercice_|if\s+__name__|$)'
            func_match = re.search(func_pattern, content, re.DOTALL)
            if func_match:
                func_body = func_match.group(1)
                func_code = f"def exercice_{chapter_num}_{exercise_num}():\n{func_body}"
                description = extract_exercise_description(description_block)
                exercises.append((full_num, name, description, func_code))
    
    print(f"  📖 {len(exercises)} exercices parsés avec succès")
    return exercises


def generate_filename(chapter_num: str, exercise_num: str, name: str) -> str:
    """Génère le nom de fichier pour un exercice."""
    # Convertir le nom en snake_case
    name_clean = re.sub(r'[^\w\s-]', '', name.lower())
    name_snake = re.sub(r'[-\s]+', '_', name_clean)
    name_snake = name_snake[:30]  # Limiter la longueur
    
    # Format: ex_XX_nom.py où XX est le numéro d'exercice (pas le chapitre)
    return f"ex_{int(exercise_num):02d}_{name_snake}.py"


def create_exercise_file(exercise_dir: Path, filename: str, num: str, name: str, description: str, func_code: str) -> None:
    """Crée un fichier d'exercice individuel."""
    # Extraire le corps de la fonction (sans 'def exercice_X_Y():')
    body_match = re.search(r'def\s+exercice_\d+_\d+\(\):\s*\n(.*)', func_code, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        # Nettoyer l'indentation - supprimer l'indentation de base (4 espaces ou 1 tab)
        lines = body.split('\n')
        cleaned_lines = []
        for line in lines:
            # Supprimer les 4 premiers espaces ou 1 tab au début
            if line.startswith('    '):
                cleaned_lines.append(line[4:])
            elif line.startswith('\t'):
                cleaned_lines.append(line[1:])
            else:
                cleaned_lines.append(line)
        body = '\n'.join(cleaned_lines)
    else:
        body = '    pass'
    
    # Réindenter le corps avec 4 espaces
    indented_body = '\n'.join('    ' + line if line.strip() else line for line in body.split('\n'))
    
    content = f'''"""
Exercice {num} - {name}
{'=' * (len(num) + len(name) + 12)}

{description}
"""


def run():
    """Fonction principale de l'exercice."""
{indented_body}


# Pour tests manuels
if __name__ == "__main__":
    run()
'''
    
    file_path = exercise_dir / filename
    file_path.write_text(content, encoding='utf-8')
    print(f"    ✅ {filename}")


def create_init_file(exercise_dir: Path, exercises: List[Tuple]) -> None:
    """Crée le fichier __init__.py."""
    chapter_num = exercises[0][0].split('.')[0] if exercises else "0"
    
    imports = []
    all_list = []
    
    for num, name, description, func_code in exercises:
        exercise_num = num.split('.')[1]
        filename = generate_filename(chapter_num, exercise_num, name)
        module_name = filename[:-3]  # Enlever .py
        
        imports.append(f"from .{module_name} import run as exercice_{num.replace('.', '_')}")
        all_list.append(f'"exercice_{num.replace(".", "_")}"')
    
    content = f'''"""Package des exercices du Chapitre {int(chapter_num)}.

Ce package contient tous les exercices du chapitre {int(chapter_num)} sous forme
de modules individuels pour une meilleure organisation.
"""

# Import de tous les exercices
{chr(10).join(imports)}

__all__ = [
    {', '.join(all_list)}
]
'''
    
    init_file = exercise_dir / "__init__.py"
    init_file.write_text(content, encoding='utf-8')
    print(f"    ✅ __init__.py")


def create_verify_server(chapter_dir: Path) -> None:
    """Crée le fichier verify_server.py."""
    content = '''#!/usr/bin/env python3
"""Serveur de vérification - Interface web moderne pour les exercices.

Lance un serveur web local pour vérifier les exercices avec une interface
moderne et intuitive.

Utilisation:
    python verify_server.py
    # ou
    uv run python verify_server.py

Le serveur démarre sur http://localhost:5000 et s'ouvre automatiquement
dans le navigateur par défaut.
"""
import sys
from pathlib import Path

# Ajouter le package relearn_python au path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from relearn_python.verify_server import run_server

if __name__ == "__main__":
    run_server(port=5000, auto_open=True)
'''
    
    server_file = chapter_dir / "verify_server.py"
    server_file.write_text(content, encoding='utf-8')
    print(f"    ✅ verify_server.py")


def backup_original(chapter_dir: Path) -> Optional[Path]:
    """Crée une sauvegarde du fichier exercices.py original."""
    original = chapter_dir / "exercices.py"
    backup = chapter_dir / "exercices.py.backup"
    
    if original.exists():
        shutil.copy2(original, backup)
        print(f"  💾 Sauvegarde créée: exercices.py.backup")
        return backup
    
    return None


def migrate_chapter(chapter_path: str) -> bool:
    """
    Migre un chapitre vers le nouveau format.
    
    Args:
        chapter_path: Chemin vers le dossier du chapitre
        
    Returns:
        True si la migration a réussi, False sinon
    """
    chapter_dir = Path(chapter_path).resolve()
    
    print(f"\n{'='*60}")
    print(f"🚀 Migration du chapitre: {chapter_dir.name}")
    print(f"{'='*60}\n")
    
    # Vérifier que le dossier existe
    if not chapter_dir.exists():
        print(f"❌ Erreur: Le dossier {chapter_dir} n'existe pas")
        return False
    
    # Vérifier que exercices.py existe
    exercices_file = chapter_dir / "exercices.py"
    if not exercices_file.exists():
        print(f"❌ Erreur: {exercices_file} n'existe pas")
        print("   Ce chapitre semble déjà être au nouveau format ou n'est pas un chapitre d'exercices")
        return False
    
    # Vérifier que le dossier exercices n'existe pas déjà
    exercise_dir = chapter_dir / "exercices"
    if exercise_dir.exists():
        print(f"⚠️  Attention: Le dossier {exercise_dir} existe déjà")
        response = input("   Voulez-vous le remplacer? (oui/non): ")
        if response.lower() != 'oui':
            print("   Migration annulée")
            return False
        shutil.rmtree(exercise_dir)
    
    # Étape 1: Sauvegarde
    print("📦 Étape 1: Création de la sauvegarde...")
    backup_original(chapter_dir)
    
    # Étape 2: Parser les exercices
    print("\n📖 Étape 2: Analyse du fichier exercices.py...")
    exercises = parse_exercises(exercices_file)
    
    if not exercises:
        print("❌ Erreur: Aucun exercice trouvé dans le fichier")
        return False
    
    # Étape 3: Créer le dossier exercices
    print("\n📁 Étape 3: Création du dossier exercices/...")
    exercise_dir.mkdir(exist_ok=True)
    
    # Étape 4: Créer les fichiers individuels
    print("\n📝 Étape 4: Création des fichiers d'exercices...")
    chapter_num = exercises[0][0].split('.')[0]
    
    for num, name, description, func_code in exercises:
        exercise_num = num.split('.')[1]
        filename = generate_filename(chapter_num, exercise_num, name)
        create_exercise_file(exercise_dir, filename, num, name, description, func_code)
    
    # Étape 5: Créer __init__.py
    print("\n📦 Étape 5: Création de __init__.py...")
    create_init_file(exercise_dir, exercises)
    
    # Étape 6: Créer verify_server.py
    print("\n🌐 Étape 6: Création de verify_server.py...")
    create_verify_server(chapter_dir)
    
    # Étape 7: Supprimer l'ancien fichier (optionnel)
    print("\n🗑️  Étape 7: Suppression de l'ancien fichier...")
    print(f"   L'ancien fichier exercices.py est sauvegardé dans exercices.py.backup")
    exercices_file.unlink()
    print("   ✅ exercices.py supprimé")
    
    # Résumé
    print(f"\n{'='*60}")
    print(f"✅ Migration terminée avec succès!")
    print(f"{'='*60}")
    print(f"\n📊 Résumé:")
    print(f"   • {len(exercises)} exercices migrés")
    print(f"   • Dossier créé: {exercise_dir}")
    print(f"   • Serveur web créé: verify_server.py")
    print(f"\n🚀 Pour tester:")
    print(f"   cd {chapter_dir}")
    print(f"   uv run python verify_server.py")
    print(f"\n💾 Sauvegarde: exercices.py.backup")
    
    return True


def main():
    """Point d'entrée principal."""
    if len(sys.argv) < 2:
        print("Usage: python migrate_chapter.py <chemin_vers_chapitre>")
        print("\nExemples:")
        print("  python migrate_chapter.py MODULES/01_core_fondations/02_variables_types/")
        print("  python migrate_chapter.py /chemin/absolu/vers/chapitre/")
        sys.exit(1)
    
    chapter_path = sys.argv[1]
    
    success = migrate_chapter(chapter_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
