#!/usr/bin/env python3
"""
Models for file manager.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum
import uuid
import os


class TypeFichier(Enum):
    FICHIER = "fichier"
    DOSSIER = "dossier"
    IMAGE = "image"
    DOCUMENT = "document"
    VIDEO = "video"
    AUDIO = "audio"
    ARCHIVE = "archive"
    CODE = "code"


class TypeRecherche(Enum):
    NOM = "nom"
    EXTENSION = "extension"
    TAILLE = "taille"
    DATE = "date"
    CONTENU = "contenu"


class TypeOperation(Enum):
    COPIER = "copier"
    DEPLACER = "deplacer"
    SUPPRIMER = "supprimer"
    RENOMMER = "renommer"


@dataclass
class MetadataFichier:
    """Metadata for a file."""
    taille: int = 0
    date_creation: datetime = field(default_factory=datetime.now)
    date_modification: datetime = field(default_factory=datetime.now)
    permissions: str = "rw-rw-r--"
    proprietaire: str = ""
    est_cache: bool = False
    est_lecture_seule: bool = False


@dataclass
class Fichier:
    """Represents a file or directory."""
    chemin: str
    nom: str
    type_fichier: TypeFichier
    est_dossier: bool = False
    taille: int = 0
    metadata: Optional[MetadataFichier] = None
    parent: Optional[str] = None
    enfants: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = self._collecter_metadata()

    def _collecter_metadata(self) -> MetadataFichier:
        """Collect file metadata."""
        try:
            stat = os.stat(self.chemin)
            return MetadataFichier(
                taille=stat.st_size,
                date_creation=datetime.fromtimestamp(stat.st_ctime),
                date_modification=datetime.fromtimestamp(stat.st_mtime),
                permissions=self._get_permissions(stat.st_mode),
                est_cache=self.nom.startswith('.'),
                est_lecture_seule=not os.access(self.chemin, os.W_OK)
            )
        except (OSError, FileNotFoundError):
            return MetadataFichier()

    def _get_permissions(self, mode: int) -> str:
        """Convert file mode to permission string."""
        perms = ['r', 'w', 'x']
        result = ''
        for i in range(3):
            for j in range(3):
                if mode & (4 >> (i * 3 - j)):
                    result += perms[j]
                else:
                    result += '-'
        return result

    @property
    def extension(self) -> str:
        if self.est_dossier:
            return ""
        return self.nom.split('.')[-1].lower() if '.' in self.nom else ""

    @property
    def taille_formatee(self) -> str:
        """Return formatted file size."""
        taille = self.taille
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if taille < 1024:
                return f"{taille:.1f}{unit}"
            taille /= 1024
        return f"{taille:.1f}PB"

    @classmethod
    def depuis_chemin(cls, chemin: str) -> 'Fichier':
        """Create Fichier from path."""
        nom = os.path.basename(chemin)
        est_dossier = os.path.isdir(chemin)
        type_fichier = cls._detecter_type(nom, est_dossier)
        
        taille = 0
        if not est_dossier:
            try:
                taille = os.path.getsize(chemin)
            except OSError:
                pass
        
        return Fichier(
            chemin=chemin,
            nom=nom,
            type_fichier=type_fichier,
            est_dossier=est_dossier,
            taille=taille,
            parent=os.path.dirname(chemin)
        )

    @classmethod
    def _detecter_type(cls, nom: str, est_dossier: bool) -> TypeFichier:
        """Detect file type from extension."""
        if est_dossier:
            return TypeFichier.DOSSIER
        
        extensions_images = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp'}
        extensions_docs = {'pdf', 'doc', 'docx', 'txt', 'odt', 'rtf'}
        extensions_video = {'mp4', 'avi', 'mkv', 'mov', 'wmv'}
        extensions_audio = {'mp3', 'wav', 'ogg', 'flac', 'm4a'}
        extensions_archives = {'zip', 'tar', 'gz', 'rar', '7z'}
        extensions_code = {'py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'go', 'rs'}
        
        ext = nom.split('.')[-1].lower() if '.' in nom else ''
        
        if ext in extensions_images:
            return TypeFichier.IMAGE
        elif ext in extensions_docs:
            return TypeFichier.DOCUMENT
        elif ext in extensions_video:
            return TypeFichier.VIDEO
        elif ext in extensions_audio:
            return TypeFichier.AUDIO
        elif ext in extensions_archives:
            return TypeFichier.ARCHIVE
        elif ext in extensions_code:
            return TypeFichier.CODE
        elif est_dossier:
            return TypeFichier.DOSSIER
        else:
            return TypeFichier.FICHIER


@dataclass
class ResultatOperation:
    """Result of a file operation."""
    succes: bool
    message: str
    source: str = ""
    destination: str = ""
    fichiers_traites: int = 0
    erreurs: List[str] = field(default_factory=list)

    @classmethod
    def reussite(cls, message: str, fichiers: int = 0) -> 'ResultatOperation':
        return ResultatOperation(succes=True, message=message, fichiers_traites=fichiers)

    @classmethod
    def echec(cls, message: str, erreurs: List[str] = None) -> 'ResultatOperation':
        return ResultatOperation(succes=False, message=message, erreurs=erreurs or [])


@dataclass
class Favori:
    """Represents a favorite/shortcut."""
    id: str
    nom: str
    chemin: str
    icone: str = "⭐"
    date_ajout: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())


__all__ = [
    "Fichier", "MetadataFichier", "ResultatOperation", "Favori",
    "TypeFichier", "TypeRecherche", "TypeOperation"
]
