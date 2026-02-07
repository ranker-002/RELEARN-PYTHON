"""Serveur FastAPI pour la vérification des exercices.

Fournit une interface web moderne pour exécuter et visualiser
les résultats des tests de vérification.
"""

import json
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from .verifier import run_verification, run_single_verification, get_chapter_info
from .parser import extract_exercise_code, extract_solution_code, extract_exercise_description

# Déterminer le chemin du dossier static
STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="RELEARN-PYTHON Verify Server")

# Monter les fichiers statiques
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Variable globale pour stocker le chemin du chapitre courant
CHAPTER_PATH: Optional[Path] = None


def set_chapter_path(path: Path):
    """Définit le chemin du chapitre courant."""
    global CHAPTER_PATH
    CHAPTER_PATH = path


@app.get("/", response_class=HTMLResponse)
async def root():
    """Sert la page HTML principale."""
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=500, detail="Template index.html non trouvé")
    return index_path.read_text(encoding="utf-8")


@app.post("/api/verify")
async def verify_exercises():
    """Lance la vérification de tous les exercices du chapitre."""
    if not CHAPTER_PATH:
        raise HTTPException(status_code=500, detail="Chapitre non configuré")
    
    try:
        results = run_verification(CHAPTER_PATH)
        return JSONResponse(content=results)
    except Exception as e:
        return JSONResponse(
            content={"error": str(e), "detail": getattr(e, "__traceback__", None)},
            status_code=500
        )


@app.get("/api/chapter-info")
async def chapter_info():
    """Retourne les informations du chapitre courant."""
    if not CHAPTER_PATH:
        raise HTTPException(status_code=500, detail="Chapitre non configuré")
    
    try:
        info = get_chapter_info(CHAPTER_PATH)
        return JSONResponse(content=info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/solution/{exercise_num}")
async def get_solution(exercise_num: str):
    """Retourne le code de la solution pour un exercice spécifique."""
    if not CHAPTER_PATH:
        raise HTTPException(status_code=500, detail="Chapitre non configuré")
    
    try:
        code = extract_solution_code(CHAPTER_PATH, exercise_num)
        if code is None:
            raise HTTPException(status_code=404, detail=f"Solution {exercise_num} non trouvée")
        return PlainTextResponse(content=code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/code/{exercise_num}")
async def get_user_code(exercise_num: str):
    """Retourne le code de l'apprenant pour un exercice spécifique."""
    if not CHAPTER_PATH:
        raise HTTPException(status_code=500, detail="Chapitre non configuré")
    
    try:
        code = extract_exercise_code(CHAPTER_PATH, exercise_num)
        if code is None:
            raise HTTPException(status_code=404, detail=f"Exercice {exercise_num} non trouvé")
        return PlainTextResponse(content=code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/verify/{exercise_num}")
async def verify_single_exercise(exercise_num: str):
    """Lance la vérification d'un seul exercice."""
    if not CHAPTER_PATH:
        raise HTTPException(status_code=500, detail="Chapitre non configuré")
    
    try:
        result = run_single_verification(CHAPTER_PATH, exercise_num)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )


@app.get("/api/description/{exercise_num}")
async def get_exercise_description(exercise_num: str):
    """Retourne la description d'un exercice."""
    if not CHAPTER_PATH:
        raise HTTPException(status_code=500, detail="Chapitre non configuré")
    
    try:
        description = extract_exercise_description(CHAPTER_PATH, exercise_num)
        if description is None:
            raise HTTPException(status_code=404, detail=f"Description {exercise_num} non trouvée")
        return PlainTextResponse(content=description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def run_server(
    port: int = 5000,
    auto_open: bool = True,
    chapter_path: Optional[Path] = None
):
    """Démarre le serveur de vérification.
    
    Args:
        port: Port du serveur (défaut: 5000)
        auto_open: Ouvrir automatiquement le navigateur
        chapter_path: Chemin vers le dossier du chapitre
    """
    # Déterminer le chemin du chapitre
    if chapter_path is None:
        # Par défaut, utiliser le répertoire courant
        chapter_path = Path.cwd()
    else:
        chapter_path = Path(chapter_path)
    
    # Vérifier que c'est bien un dossier de chapitre
    has_exercises = (chapter_path / "exercices.py").exists() or (chapter_path / "exercices").exists()
    if not has_exercises:
        print(f"❌ Erreur: {chapter_path} ne semble pas être un dossier de chapitre valide")
        print("   Vérifiez que vous êtes dans le bon dossier")
        sys.exit(1)
    
    set_chapter_path(chapter_path)
    
    print(f"🚀 Démarrage du serveur de vérification...")
    print(f"📁 Chapitre: {chapter_path.name}")
    print(f"🌐 URL: http://localhost:{port}")
    
    if auto_open:
        # Ouvrir le navigateur après un court délai
        import threading
        import time
        
        def open_browser():
            time.sleep(1.5)  # Attendre que le serveur démarre
            webbrowser.open(f"http://localhost:{port}")
        
        threading.Thread(target=open_browser, daemon=True).start()
        print("🌐 Ouverture automatique du navigateur...")
    
    print("\n⚡ Serveur en cours d'exécution...")
    print("   Appuyez sur Ctrl+C pour arrêter\n")
    
    try:
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
    except KeyboardInterrupt:
        print("\n\n👋 Serveur arrêté")
        sys.exit(0)


if __name__ == "__main__":
    run_server()
