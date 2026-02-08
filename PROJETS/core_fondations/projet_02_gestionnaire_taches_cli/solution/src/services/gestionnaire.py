#!/usr/bin/env python3
"""
Service de gestion des tâches.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict
from uuid import uuid4

from models.tache import Tache, StatutTache
from models.projet import Projet
from models.tag import Tag


class GestionnaireTaches:
    """Gère les tâches, projets et tags."""
    
    def __init__(self, repertoire: str = "data"):
        self.repertoire = Path(repertoire)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        
        self.taches: Dict[str, Tache] = {}
        self.projets: Dict[str, Projet] = {}
        self.tags: Dict[str, Tag] = {}
        
        self._charger()
    
    def _get_fichier(self, nom: str) -> Path:
        return self.repertoire / f"{nom}.json"
    
    def _charger(self):
        self._charger_taches()
        self._charger_projets()
        self._charger_tags()
    
    def _charger_taches(self):
        fichier = self._get_fichier("taches")
        if fichier.exists():
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.taches = {t["id"]: Tache.depuis_dict(t) for t in data}
            except (json.JSONDecodeError, KeyError):
                self.taches = {}
    
    def _charger_projets(self):
        fichier = self._get_fichier("projets")
        if fichier.exists():
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.projets = {p["id"]: Projet.depuis_dict(p) for p in data}
            except (json.JSONDecodeError, KeyError):
                self.projets = {}
    
    def _charger_tags(self):
        fichier = self._get_fichier("tags")
        if fichier.exists():
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tags = {t["id"]: Tag.depuis_dict(t) for t in data}
            except (json.JSONDecodeError, KeyError):
                self.tags = {}
    
    def _sauvegarder(self):
        self._sauvegarder_taches()
        self._sauvegarder_projets()
        self._sauvegarder_tags()
    
    def _sauvegarder_taches(self):
        with open(self._get_fichier("taches"), 'w', encoding='utf-8') as f:
            json.dump([t.vers_dict() for t in self.taches.values()], f, indent=2, ensure_ascii=False)
    
    def _sauvegarder_projets(self):
        with open(self._get_fichier("projets"), 'w', encoding='utf-8') as f:
            json.dump([p.vers_dict() for p in self.projets.values()], f, indent=2, ensure_ascii=False)
    
    def _sauvegarder_tags(self):
        with open(self._get_fichier("tags"), 'w', encoding='utf-8') as f:
            json.dump([tag.vers_dict() for tag in self.tags.values()], f, indent=2, ensure_ascii=False)
    
    def creer_tache(self, titre: str, description: str = "", priorite: int = 3,
                   projet: Optional[str] = None, tags: List[str] = None,
                   echeance: Optional[datetime] = None) -> Tache:
        tache = Tache(
            id=str(uuid4())[:8],
            titre=titre,
            description=description,
            priorite=priorite,
            projet=projet,
            tags=tags or [],
            echeance=echeance,
        )
        self.taches[tache.id] = tache
        
        if projet and projet in self.projets:
            self.projets[projet].ajouter_tache(tache.id)
        
        for tag_nom in tache.tags:
            if tag_nom in self.tags:
                self.tags[tag_nom].incrementer_utilisations()
        
        self._sauvegarder_taches()
        return tache
    
    def get_tache(self, tache_id: str) -> Optional[Tache]:
        return self.taches.get(tache_id)
    
    def get_toutes_taches(self) -> List[Tache]:
        return list(self.taches.values())
    
    def modifier_tache(self, tache_id: str, **kwargs) -> Optional[Tache]:
        if tache_id not in self.taches:
            return None
        
        tache = self.taches[tache_id]
        ancien_projet = tache.projet
        
        for cle, valeur in kwargs.items():
            if hasattr(tache, cle) and cle not in ["id", "cree_le"]:
                if cle == "projet" and valeur != ancien_projet:
                    if ancien_projet and ancien_projet in self.projets:
                        self.projets[ancien_projet].supprimer_tache(tache_id)
                    if valeur and valeur in self.projets:
                        self.projets[valeur].ajouter_tache(tache_id)
                setattr(tache, cle, valeur)
        
        tache.modifie_le = datetime.now()
        self._sauvegarder_taches()
        return tache
    
    def supprimer_tache(self, tache_id: str) -> bool:
        if tache_id not in self.taches:
            return False
        
        tache = self.taches[tache_id]
        
        if tache.projet and tache.projet in self.projets:
            self.projets[tache.projet].supprimer_tache(tache_id)
        
        del self.taches[tache_id]
        self._sauvegarder()
        return True
    
    def marquer_terminee(self, tache_id: str) -> bool:
        if tache_id not in self.taches:
            return False
        self.taches[tache_id].marquer_terminee()
        self._sauvegarder_taches()
        return True
    
    def marquer_en_cours(self, tache_id: str) -> bool:
        if tache_id not in self.taches:
            return False
        self.taches[tache_id].marquer_en_cours()
        self._sauvegarder_taches()
        return True
    
    def filtrer_taches(self, statut: Optional[StatutTache] = None,
                       priorite_min: Optional[int] = None,
                       priorite_max: Optional[int] = None,
                       projet: Optional[str] = None,
                       tag: Optional[str] = None,
                       avec_echeance: Optional[bool] = None,
                       en_retard: bool = False) -> List[Tache]:
        resultat = list(self.taches.values())
        
        if statut:
            resultat = [t for t in resultat if t.statut == statut]
        
        if priorite_min:
            resultat = [t for t in resultat if t.priorite >= priorite_min]
        
        if priorite_max:
            resultat = [t for t in resultat if t.priorite <= priorite_max]
        
        if projet:
            resultat = [t for t in resultat if t.projet == projet]
        
        if tag:
            resultat = [t for t in resultat if tag in t.tags]
        
        if avec_echeance is not None:
            if avec_echeance:
                resultat = [t for t in resultat if t.echeance is not None]
            else:
                resultat = [t for t in resultat if t.echeance is None]
        
        if en_retard:
            resultat = [t for t in resultat if t.est_en_retard()]
        
        return sorted(resultat)
    
    def get_statistiques(self) -> dict:
        total = len(self.taches)
        par_statut = {
            "a_faire": len([t for t in self.taches.values() if t.statut == StatutTache.A_FAIRE]),
            "en_cours": len([t for t in self.taches.values() if t.statut == StatutTache.EN_COURS]),
            "terminees": len([t for t in self.taches.values() if t.statut == StatutTache.TERMINEE]),
            "annulees": len([t for t in self.taches.values() if t.statut == StatutTache.ANNULEE]),
        }
        en_retard = len([t for t in self.taches.values() if t.est_en_retard()])
        
        return {
            "total": total,
            "par_statut": par_statut,
            "en_retard": en_retard,
            "nb_projets": len(self.projets),
            "nb_tags": len(self.tags),
        }
    
    def get_taches_par_priorite(self) -> dict:
        resultat = {1: [], 2: [], 3: [], 4: [], 5: []}
        for tache in self.taches.values():
            resultat[tache.priorite].append(tache)
        return resultat
    
    def get_taches_par_projet(self) -> dict:
        resultat = {"sans_projet": []}
        for tache in self.taches.values():
            if tache.projet:
                if tache.projet not in resultat:
                    resultat[tache.projet] = []
                resultat[tache.projet].append(tache)
            else:
                resultat["sans_projet"].append(tache)
        return resultat
    
    def get_toutes_les_tags(self) -> List[str]:
        tags = set()
        for tache in self.taches.values():
            tags.update(tache.tags)
        return sorted(list(tags))
