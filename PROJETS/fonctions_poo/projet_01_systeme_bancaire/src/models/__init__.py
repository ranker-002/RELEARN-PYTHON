#!/usr/bin/env python3
"""
Models for the banking system.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from enum import Enum
import uuid


class TypeCompte(Enum):
    COURANT = "courant"
    EPARGNE = "epargne"
    PROFESSIONNEL = "professionnel"
    JOINT = "joint"


class StatutCompte(Enum):
    ACTIF = "actif"
    INACTIF = "inactif"
    BLOQUE = "bloque"
    FERME = "ferme"


class TypeTransaction(Enum):
    DEPOT = "depot"
    RETRAIT = "retrait"
    VIREMENT_ENTRANT = "virement_entrant"
    VIREMENT_SORTANT = "virement_sortant"
    PAIEMENT_CARTE = "paiement_carte"
    REMBOURSEMENT_PRET = "remboursement_pret"
    FRAIS = "frais"


class StatutTransaction(Enum):
    EN_ATTENTE = "en_attente"
    VALIDEE = "validee"
    ANNULEE = "annulee"
    ECHOUEE = "echouee"


class TypeCarte(Enum):
    DEBIT = "debit"
    CREDIT = "credit"
    PREPAYE = "prepaye"


class StatutCarte(Enum):
    ACTIVE = "active"
    BLOQUEE = "bloquee"
    EXPIREE = "expiree"


@dataclass
class Client:
    """Represents a bank client."""
    id: str
    nom: str
    prenom: str
    email: str
    telephone: str
    adresse: str = ""
    date_naissance: Optional[datetime] = None
    date_inscription: datetime = field(default_factory=datetime.now)
    identifiant: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.identifiant:
            self.identifiant = f"CLI-{self.id[:8].upper()}"

    @property
    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom}"


@dataclass
class Compte:
    """Represents a bank account."""
    id: str
    numero: str
    client_id: str
    type_compte: TypeCompte
    solde: float = 0.0
    decouvert_autorise: float = 0.0
    taux_interet: float = 0.0
    statut: StatutCompte = StatutCompte.ACTIF
    date_ouverture: datetime = field(default_factory=datetime.now)
    date_fermeture: Optional[datetime] = None
    historique: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.numero:
            self.numero = self._generer_numero()

    def _generer_numero(self) -> str:
        import random
        return ''.join(str(random.randint(0, 9)) for _ in range(12))

    def deposer(self, montant: float, description: str = "") -> bool:
        if montant <= 0:
            return False
        self.solde += montant
        self.historique.append(f"{datetime.now().isoformat()}: Depôt de {montant}€ - {description}")
        return True

    def retirer(self, montant: float, description: str = "") -> bool:
        if montant <= 0:
            return False
        if self.solde - montant < -self.decouvert_autorise:
            return False
        self.solde -= montant
        self.historique.append(f"{datetime.now().isoformat()}: Retrait de {montant}€ - {description}")
        return True

    def get_solde_disponible(self) -> float:
        return self.solde + self.decouvert_autorise


@dataclass
class Transaction:
    """Represents a financial transaction."""
    id: str
    compte_id: str
    type_transaction: TypeTransaction
    montant: float
    solde_avant: float
    solde_apres: float
    description: str = ""
    statut: StatutTransaction = StatutTransaction.EN_ATTENTE
    date_transaction: datetime = field(default_factory=datetime.now)
    date_validation: Optional[datetime] = None
    reference: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.reference:
            self.reference = f"TRX-{self.id[:12].upper()}"


@dataclass
class CarteBancaire:
    """Represents a bank card."""
    id: str
    numero: str
    compte_id: str
    type_carte: TypeCarte
    titulaire: str
    date_expiration: datetime
    cvv: str
    statut: StatutCarte = StatutCarte.ACTIVE
    plafond_quotidien: float = 1000.0
    plafond_mensuel: float = 5000.0
    date_emission: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.numero:
            self.numero = self._generer_numero()
        if not self.cvv:
            import random
            self.cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))

    def _generer_numero(self) -> str:
        import random
        groups = ['4' + ''.join(str(random.randint(0, 9)) for _ in range(3)),
                  ''.join(str(random.randint(0, 9)) for _ in range(4)),
                  ''.join(str(random.randint(0, 9)) for _ in range(4)),
                  ''.join(str(random.randint(0, 9)) for _ in range(4))]
        return ' '.join(groups)

    @property
    def est_valide(self) -> bool:
        return self.date_expiration > datetime.now() and self.statut == StatutCarte.ACTIVE


@dataclass
class Pret:
    """Represents a loan."""
    id: str
    client_id: str
    compte_id: str
    montant: float
    taux_interet: float
    duree_mois: int
    mensualite: float
    montant_total: float
    montant_rembourse: float = 0.0
    date_debut: datetime = field(default_factory=datetime.now)
    statut: str = "actif"
    echeances: List[dict] = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        self.montant_total = self.montant * (1 + self.taux_interet / 100)
        if self.mensualite == 0 and self.duree_mois > 0:
            self.mensualite = self._calculer_mensualite()

    def _calculer_mensualite(self) -> float:
        taux_mensuel = (self.taux_interet / 100) / 12
        if taux_mensuel == 0:
            return self.montant / self.duree_mois
        return self.montant * (taux_mensuel * (1 + taux_mensuel) ** self.duree_mois) / \
               ((1 + taux_mensuel) ** self.duree_mois - 1)

    def get_montant_restant(self) -> float:
        return max(0, self.montant_total - self.montant_rembourse)

    def get_nombre_echeances_restantes(self) -> int:
        total_echeances = len(self.echeances)
        echeances_payees = sum(1 for e in self.echeances if e.get('payee', False))
        return max(0, total_echeances - echeances_payees)


__all__ = [
    "Client", "Compte", "Transaction", "CarteBancaire", "Pret",
    "TypeCompte", "StatutCompte", "TypeTransaction", "StatutTransaction",
    "TypeCarte", "StatutCarte"
]
