#!/usr/bin/env python3
"""
Service de filtrage avancé des tâches.
"""

from typing import List, Dict, Optional, Callable
from datetime import datetime, timedelta

from models.tache import Tache, StatutTache


class FiltreTache:
    """Filtre avancé pour les tâches."""
    
    CRITERES = {
        "statut": lambda t, v: t.statut == v,
        "priorite_min": lambda t, v: t.priorite >= v,
        "priorite_max": lambda t, v: t.priorite <= v,
        "projet": lambda t, v: t.projet == v,
        "tag": lambda t, v: v in t.tags,
        "sans_projet": lambda t, v: v is None and t.projet is None,
        "avec_echeance": lambda t, v: (t.echeance is not None) if v else (t.echeance is None),
        "en_retard": lambda t, v: t.est_en_retard() if v else False,
        "terminees": lambda t, v: t.statut == StatutTache.TERMINEE,
        "non_terminees": lambda t, v: t.statut != StatutTache.TERMINEE,
    }
    
    def __init__(self):
        self.criteres_personnalises: Dict[str, Callable] = {}
    
    def ajouter_critere(self, nom: str, fonction: Callable):
        self.criteres_personnalises[nom] = fonction
    
    def filtrer(self, taches: List[Tache], **criteres) -> List[Tache]:
        resultat = list(taches)
        
        for cle, valeur in criteres.items():
            if valeur is None:
                continue
            
            if cle in self.CRITERES:
                fonction = self.CRITERES[cle]
                resultat = [t for t in resultat if fonction(t, valeur)]
            elif cle in self.criteres_personnalises:
                fonction = self.criteres_personnalises[cle]
                resultat = [t for t in resultat if fonction(t, valeur)]
        
        return resultat
    
    def par_statut(self, taches: List[Tache], statut: StatutTache) -> List[Tache]:
        return [t for t in taches if t.statut == statut]
    
    def par_priorite(self, taches: List[Tache], min_val: int = 1, max_val: int = 5) -> List[Tache]:
        return [t for t in taches if min_val <= t.priorite <= max_val]
    
    def par_projet(self, taches: List[Tache], projet: Optional[str]) -> List[Tache]:
        if projet is None:
            return [t for t in taches if t.projet is None]
        return [t for t in taches if t.projet == projet]
    
    def par_tag(self, taches: List[Tache], tag: str) -> List[Tache]:
        return [t for t in taches if tag in t.tags]
    
    def par_echeance(self, taches: List[Tache], avant: Optional[datetime] = None,
                    apres: Optional[datetime] = None) -> List[Tache]:
        resultat = list(taches)
        
        if avant:
            resultat = [t for t in resultat if t.echeance and t.echeance <= avant]
        
        if apres:
            resultat = [t for t in resultat if t.echeance and t.echeance >= apres]
        
        return resultat
    
    def en_retard(self, taches: List[Tache]) -> List[Tache]:
        maintenant = datetime.now()
        return [t for t in taches if t.echeance and t.echeance < maintenant 
                and t.statut != StatutTache.TERMINEE]
    
    def aujourd_hui(self, taches: List[Tache]) -> List[Tache]:
        aujourd_hui = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        demain = aujourd_hui + timedelta(days=1)
        return [t for t in taches if t.echeance and aujourd_hui <= t.echeance < demain]
    
    def cette_semaine(self, taches: List[Tache]) -> List[Tache]:
        from datetime import datetime, timedelta
        aujourd_hui = datetime.now()
        debut_semaine = aujourd_hui - timedelta(days=aujourd_hui.weekday())
        debut_semaine = debut_semaine.replace(hour=0, minute=0, second=0, microsecond=0)
        fin_semaine = debut_semaine + timedelta(days=7)
        return [t for t in taches if t.echeance and debut_semaine <= t.echeance < fin_semaine]
    
    def rechercher(self, taches: List[Tache], terme: str) -> List[Tache]:
        terme = terme.lower()
        return [t for t in taches if (
            terme in t.titre.lower() or
            terme in t.description.lower() or
            any(terme in tag.lower() for tag in t.tags) or
            (t.projet and terme in t.projet.lower())
        )]
    
    def trier(self, taches: List[Tache], cle: str = "priorite", ordre: str = "desc") -> List[Tache]:
        reverse = ordre == "desc"
        
        if cle == "priorite":
            return sorted(taches, key=lambda t: (t.priorite, t.echeance or datetime.max), reverse=reverse)
        elif cle == "echeance":
            return sorted(taches, key=lambda t: (t.echeance or datetime.max), reverse=reverse)
        elif cle == "titre":
            return sorted(taches, key=lambda t: t.titre.lower(), reverse=reverse)
        elif cle == "date_creation":
            return sorted(taches, key=lambda t: t.cree_le, reverse=reverse)
        elif cle == "date_modification":
            return sorted(taches, key=lambda t: t.modifie_le, reverse=reverse)
        else:
            return sorted(taches, key=lambda t: t.priorite, reverse=reverse)
    
    def limiter(self, taches: List[Tache], nombre: int, debut: int = 0) -> List[Tache]:
        return taches[debut:debut + nombre]
    
    def grouper_par(self, taches: List[Tache], cle: str) -> dict:
        if cle == "statut":
            return {s.value: [t for t in taches if t.statut == s] for s in StatutTache}
        elif cle == "priorite":
            return {i: [t for t in taches if t.priorite == i] for i in range(1, 6)}
        elif cle == "projet":
            resultat = {}
            for t in taches:
                projet = t.projet or "Sans projet"
                if projet not in resultat:
                    resultat[projet] = []
                resultat[projet].append(t)
            return resultat
        elif cle == "tag":
            resultat = {}
            for t in taches:
                for tag in t.tags:
                    if tag not in resultat:
                        resultat[tag] = []
                    resultat[tag].append(t)
            return resultat
        else:
            return {"toutes": taches}
