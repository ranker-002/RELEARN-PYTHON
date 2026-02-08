#!/usr/bin/env python3
"""
Service d'exportation des tâches.
"""

import json
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from models.tache import Tache


class ExporteurTaches:
    """Export les tâches vers différents formats."""
    
    def __init__(self, repertoire: str = "exports"):
        self.repertoire = Path(repertoire)
        self.repertoire.mkdir(parents=True, exist_ok=True)
    
    def exporter_json(self, taches: List[Tache], nom_fichier: Optional[str] = None) -> str:
        if nom_fichier is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"taches_export_{timestamp}.json"
        
        chemin = self.repertoire / nom_fichier
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump([t.vers_dict() for t in taches], f, indent=2, ensure_ascii=False)
        
        return str(chemin)
    
    def exporter_csv(self, taches: List[Tache], nom_fichier: Optional[str] = None,
                   delimiter: str = ";") -> str:
        if nom_fichier is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"taches_export_{timestamp}.csv"
        
        chemin = self.repertoire / nom_fichier
        
        with open(chemin, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=delimiter)
            
            writer.writerow([
                "ID", "Titre", "Description", "Statut", "Priorité",
                "Projet", "Tags", "Échéance", "Créé le", "Terminé le"
            ])
            
            for tache in taches:
                writer.writerow([
                    tache.id,
                    tache.titre,
                    tache.description,
                    tache.statut.value,
                    tache.priorite,
                    tache.projet or "",
                    ", ".join(tache.tags),
                    tache.echeance.strftime("%Y-%m-%d %H:%M") if tache.echeance else "",
                    tache.cree_le.strftime("%Y-%m-%d %H:%M"),
                    tache.terminee_le.strftime("%Y-%m-%d %H:%M") if tache.terminee_le else "",
                ])
        
        return str(chemin)
    
    def exporter_texte(self, taches: List[Tache], nom_fichier: Optional[str] = None) -> str:
        if nom_fichier is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"taches_export_{timestamp}.txt"
        
        chemin = self.repertoire / nom_fichier
        
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"EXPORT DES TÂCHES - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("=" * 60 + "\n\n")
            
            par_statut = {}
            for tache in taches:
                statut = tache.statut.value
                if statut not in par_statut:
                    par_statut[statut] = []
                par_statut[statut].append(tache)
            
            for statut, liste in sorted(par_statut.items()):
                f.write(f"\n[{statut.upper()}]\n")
                f.write("-" * 40 + "\n")
                for tache in sorted(liste, key=lambda t: t.priorite):
                    priorite = "★" * tache.priorite + "☆" * (5 - tache.priorite)
                    projet = f" [{tache.projet}]" if tache.projet else ""
                    tags = f" #{', '.join(tache.tags)}" if tache.tags else ""
                    echeance = f" 📅 {tache.echeance.strftime('%d/%m')}" if tache.echeance else ""
                    f.write(f"{priorite} {tache.titre}{projet}{tags}{echeance}\n")
            
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Total: {len(taches)} tâches\n")
        
        return str(chemin)
    
    def exporter_markdown(self, taches: List[Tache], nom_fichier: Optional[str] = None) -> str:
        if nom_fichier is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"taches_export_{timestamp}.md"
        
        chemin = self.repertoire / nom_fichier
        
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write("# Export des Tâches\n")
            f.write(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"\nTotal: {len(taches)} tâches\n")
            
            par_priorite = {1: [], 2: [], 3: [], 4: [], 5: []}
            for tache in taches:
                par_priorite[tache.priorite].append(tache)
            
            emojis = {1: "🔴", 2: "🟠", 3: "🟡", 4: "🟢", 5: "⚪"}
            
            for priorite in range(1, 6):
                if par_priorite[priorite]:
                    f.write(f"\n## Priorité {priorite} {emojis[priorite]}\n")
                    for tache in sorted(par_priorite[priorite], key=lambda t: t.titre):
                        statut = "✅" if tache.statut.value == "terminee" else "📋"
                        projet = f" **[{tache.projet}]**" if tache.projet else ""
                        tags = f" _{', '.join(tache.tags)}_" if tache.tags else ""
                        echeance = f" 📅 {tache.echeance.strftime('%d/%m')}" if tache.echeance else ""
                        f.write(f"- {statut} {tache.titre}{projet}{tags}{echeance}\n")
        
        return str(chemin)
    
    def importer_json(self, chemin: str) -> List[Tache]:
        with open(chemin, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Tache.depuis_dict(t) for t in data]
    
    def get_chemins_export(self) -> List[Path]:
        return list(self.repertoire.glob("*"))
    
    def supprimer_export(self, nom_fichier: str) -> bool:
        chemin = self.repertoire / nom_fichier
        if chemin.exists():
            chemin.unlink()
            return True
        return False
