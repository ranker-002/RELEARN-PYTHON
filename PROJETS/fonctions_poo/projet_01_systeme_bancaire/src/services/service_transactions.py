#!/usr/bin/env python3
"""
Service for managing transactions.
"""

from typing import Optional, List, Dict
from datetime import datetime
from pathlib import Path
import json
import uuid

from models import Transaction, Compte, TypeTransaction, StatutTransaction


class ServiceTransactions:
    """Manages financial transactions."""
    
    def __init__(self, repertoire_donnees: str = "data"):
        self.repertoire = Path(repertoire_donnees)
        self.repertoire.mkdir(parents=True, exist_ok=True)
        self.transactions: Dict[str, Transaction] = {}
        self._charger_donnees()
    
    def _chemin_fichier(self) -> Path:
        return self.repertoire / "transactions.json"
    
    def _charger_donnees(self):
        try:
            with open(self._chemin_fichier(), 'r', encoding='utf-8') as f:
                donnees = json.load(f)
                for t in donnees:
                    if 'date_transaction' in t and isinstance(t['date_transaction'], str):
                        t['date_transaction'] = datetime.fromisoformat(t['date_transaction'])
                    if 'date_validation' in t and t['date_validation']:
                        t['date_validation'] = datetime.fromisoformat(t['date_validation'])
                    transaction = Transaction(**t)
                    self.transactions[transaction.id] = transaction
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    def _sauvegarder_donnees(self):
        donnees = []
        for t in self.transactions.values():
            t_dict = vars(t)
            t_dict['type_transaction'] = t.type_transaction.value
            t_dict['statut'] = t.statut.value
            donnees.append(t_dict)
        
        with open(self._chemin_fichier(), 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=2, default=str)
    
    def creer_transaction(self, compte_id: str, type_transaction: TypeTransaction,
                         montant: float, description: str = "") -> Optional[Transaction]:
        """Create a new transaction."""
        from models import Compte
        try:
            with open(self.repertoire.parent.parent / "data" / "comptes.json", 'r') as f:
                comptes_data = json.load(f)
                compte_dict = next((c for c in comptes_data if c.get('id') == compte_id), None)
                if compte_dict:
                    type_compte = compte_dict.get('type_compte', {}).value if hasattr(compte_dict.get('type_compte'), 'value') else compte_dict.get('type_compte')
                    from models import TypeCompte, StatutCompte
                    statut = StatutCompte.ACTIF
                    if hasattr(compte_dict.get('statut'), 'value'):
                        statut = StatutCompte(compte_dict['statut']['value'])
                    else:
                        statut = StatutCompte(compte_dict.get('statut', 'actif'))
                    compte = Compte(**compte_dict)
                    compte.type_compte = TypeCompte(type_compte) if isinstance(type_compte, str) else type_compte
                    compte.statut = statut
                else:
                    return None
        except (FileNotFoundError, StopIteration):
            return None
        
        if montant <= 0:
            return None
        
        solde_avant = compte.solde
        
        if type_transaction in [TypeTransaction.RETRAIT, TypeTransaction.VIREMENT_SORTANT, 
                                  TypeTransaction.PAIEMENT_CARTE]:
            if not compte.retirer(montant, description):
                return None
        else:
            if not compte.deposer(montant, description):
                return None
        
        transaction = Transaction(
            id="",
            compte_id=compte_id,
            type_transaction=type_transaction,
            montant=montant,
            solde_avant=solde_avant,
            solde_apres=compte.solde,
            description=description,
            statut=StatutTransaction.VALIDEE,
            date_validation=datetime.now()
        )
        
        self.transactions[transaction.id] = transaction
        self._sauvegarder_donnees()
        return transaction
    
    def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        return self.transactions.get(transaction_id)
    
    def get_transactions_compte(self, compte_id: str, limite: int = 50) -> List[Transaction]:
        transactions = [t for t in self.transactions.values() if t.compte_id == compte_id]
        transactions.sort(key=lambda x: x.date_transaction, reverse=True)
        return transactions[:limite]
    
    def get_all_transactions(self) -> List[Transaction]:
        return list(self.transactions.values())
    
    def get_transactions_par_periode(self, debut: datetime, fin: datetime) -> List[Transaction]:
        return [t for t in self.transactions.values() 
                if debut <= t.date_transaction <= fin]
    
    def get_stats_transactions(self, compte_id: str = None) -> Dict:
        transactions = self.get_transactions_compte(compte_id) if compte_id else self.get_all_transactions()
        
        total_depots = sum(t.montant for t in transactions 
                          if t.type_transaction == TypeTransaction.DEPOT and t.statut == StatutTransaction.VALIDEE)
        total_retraits = sum(t.montant for t in transactions 
                            if t.type_transaction == TypeTransaction.RETRAIT and t.statut == StatutTransaction.VALIDEE)
        
        return {
            "total_transactions": len(transactions),
            "total_depots": total_depots,
            "total_retraits": total_retraits,
            "solde_net": total_depots - total_retraits
        }
