"""
Système Bancaire - Starter Code
"""


class DecouvertAutoriseException(Exception):
    """Exception levée quand le solde est insuffisant."""
    pass


class CompteBancaire:
    """Classe de base pour un compte bancaire."""

    def __init__(self, numero: str, titulaire: str, solde_initial: float = 0.0):
        self._numero = numero
        self._titulaire = titulaire
        self._solde = solde_initial
        self._historique: list[dict] = []

    @property
    def solde(self) -> float:
        """Retourne le solde actuel."""
        return self._solde

    @property
    def numero(self) -> str:
        """Retourne le numéro de compte."""
        return self._numero

    @property
    def titulaire(self) -> str:
        """Retourne le nom du titulaire."""
        return self._titulaire

    def deposer(self, montant: float) -> None:
        """Dépose de l'argent sur le compte."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._solde += montant
        self._enregistrer_transaction("dépôt", montant)

    def retirer(self, montant: float) -> None:
        """Retire de l'argent du compte."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        if montant > self._solde:
            raise DecouvertAutoriseException(
                f"Solde insuffisant. Solde: {self._solde}€, Demande: {montant}€"
            )
        self._solde -= montant
        self._enregistrer_transaction("retrait", montant)

    def _enregistrer_transaction(self, type_trans: str, montant: float) -> None:
        """Enregistre une transaction dans l'historique."""
        from datetime import datetime
        self._historique.append({
            "type": type_trans,
            "montant": montant,
            "date": datetime.now().isoformat(),
            "solde": self._solde
        })

    def afficher_historique(self) -> None:
        """Affiche l'historique des transactions."""
        for trans in self._historique:
            print(f"[{trans['date']}] {trans['type']}: {trans['montant']}€ (solde: {trans['solde']}€)")

    def __str__(self) -> str:
        return f"Compte {self._numero} - {self._titulaire} - Solde: {self._solde}€"


class CompteCourant(CompteBancaire):
    """Compte courant avec frais de transaction."""

    def __init__(self, numero: str, titulaire: str, solde_initial: float = 0.0,
                 frais_transactions: float = 0.5, plafond_decouvert: float = 200.0):
        super().__init__(numero, titulaire, solde_initial)
        self._frais_transactions = frais_transactions
        self._plafond_decouvert = plafond_decouvert

    def retirer(self, montant: float) -> None:
        """Retire avec application des frais et gestion du découvert."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        if montant > self._solde + self._plafond_decouvert:
            raise DecouvertAutoriseException(
                f"Dépassement du découvert autorisé. Max: {self._plafond_decouvert}€"
            )
        self._solde -= montant
        self._solde -= self._frais_transactions  # Frais de retrait
        self._enregistrer_transaction("retrait avec frais", montant + self._frais_transactions)


class CompteEpargne(CompteBancaire):
    """Compte épargne avec intérêts."""

    def __init__(self, numero: str, titulaire: str, solde_initial: float = 0.0,
                 taux_interet_annuel: float = 0.02):
        super().__init__(numero, titulaire, solde_initial)
        self._taux_interet = taux_interet_annuel

    def calculer_interets(self) -> float:
        """Calcule les intérêts annuels."""
        return self._solde * self._taux_interet

    def ajouter_interets(self) -> None:
        """Ajoute les intérêts au solde."""
        interets = self.calculer_interets()
        self._solde += interets
        self._enregistrer_transaction("intérêts", interets)


class Client:
    """Représente un client de la banque."""

    def __init__(self, nom: str, email: str):
        self.id = ""  # À générer
        self.nom = nom
        self.email = email
        self.comptes: list[CompteBancaire] = []

    def ajouter_compte(self, compte: CompteBancaire) -> None:
        """Ajoute un compte au client."""
        self.comptes.append(compte)

    def __str__(self) -> str:
        return f"Client {self.id}: {self.nom} ({self.email}) - {len(self.comptes)} compte(s)"


# Point d'entrée pour tests
if __name__ == "__main__":
    print("=== SYSTÈME BANCAIRE ===")
    print("Ce projet nécessite l'implémentation complète.")
