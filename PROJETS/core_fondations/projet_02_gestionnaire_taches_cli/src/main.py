"""
Gestionnaire de Tâches CLI - Starter Code
"""


class Tache:
    """Représente une tâche."""

    def __init__(self, titre: str, description: str = "", priorite: str = "moyenne"):
        self.id = 0  # Sera défini par le gestionnaire
        self.titre = titre
        self.description = description
        self.priorite = priorite  # "haute", "moyenne", "basse"
        self.completee = False
        self.date_creation = ""  # À implémenter

    def __str__(self) -> str:
        statut = "✓" if self.completee else "✗"
        return f"[{statut}] [{self.priorite.upper()}] {self.titre}"

    def to_dict(self) -> dict:
        """Convertit la tâche en dictionnaire."""
        return {
            "id": self.id,
            "titre": self.titre,
            "description": self.description,
            "priorite": self.priorite,
            "completee": self.completee,
            "date_creation": self.date_creation
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Tache":
        """Crée une tâche depuis un dictionnaire."""
        tache = cls(data["titre"], data.get("description", ""), data.get("priorite", "moyenne"))
        tache.id = data["id"]
        tache.completee = data["completee"]
        tache.date_creation = data.get("date_creation", "")
        return tache


class GestionnaireTaches:
    """Gère une collection de tâches."""

    def __init__(self, fichier: str = "data/taches.json"):
        self.fichier = fichier
        self.taches: list[Tache] = []
        self.charger()

    def creer(self, titre: str, description: str = "", priorite: str = "moyenne") -> Tache:
        """Crée une nouvelle tâche."""
        tache = Tache(titre, description, priorite)
        tache.id = len(self.taches) + 1
        self.taches.append(tache)
        self.sauvegarder()
        return tache

    def lister(self, completees: bool | None = None) -> list[Tache]:
        """Liste les tâches avec option de filtrage."""
        if completees is None:
            return self.taches
        return [t for t in self.taches if t.completee == completees]

    def marquer_completee(self, id_tache: int) -> bool:
        """Marque une tâche comme terminée."""
        for tache in self.taches:
            if tache.id == id_tache:
                tache.completee = True
                self.sauvegarder()
                return True
        return False

    def supprimer(self, id_tache: int) -> bool:
        """Supprime une tâche."""
        for i, tache in enumerate(self.taches):
            if tache.id == id_tache:
                del self.taches[i]
                self.sauvegarder()
                return True
        return False

    def sauvegarder(self) -> None:
        """Sauvegarde les tâches dans un fichier JSON."""
        import json
        import os
        os.makedirs(os.path.dirname(self.fichier), exist_ok=True)
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.taches], f, indent=2, ensure_ascii=False)

    def charger(self) -> None:
        """Charge les tâches depuis un fichier JSON."""
        import json
        import os
        if not os.path.exists(self.fichier):
            return
        with open(self.fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.taches = [Tache.from_dict(d) for d in data]


def afficher_menu() -> None:
    print("\n=== GESTIONNAIRE DE TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter\n")


def main() -> None:
    gestionnaire = GestionnaireTaches()

    while True:
        afficher_menu()
        choix = input(">>> ")

        if choix == "5":
            break

        elif choix == "1":
            titre = input("Titre: ")
            desc = input("Description (Enter pour none): ")
            prio = input("Priorité (haute/moyenne/basse): ")
            tache = gestionnaire.creer(titre, desc, prio)
            print(f"Tâche créée: {tache}")

        elif choix == "2":
            for tache in gestionnaire.lister():
                print(tache)

        elif choix == "3":
            try:
                id_tache = int(input("ID de la tâche: "))
                if gestionnaire.marquer_completee(id_tache):
                    print("Tâche marquée comme terminée!")
                else:
                    print("Tâche non trouvée.")
            except ValueError:
                print("ID invalide.")

        elif choix == "4":
            try:
                id_tache = int(input("ID de la tâche: "))
                if gestionnaire.supprimer(id_tache):
                    print("Tâche supprimée!")
                else:
                    print("Tâche non trouvée.")
            except ValueError:
                print("ID invalide.")


if __name__ == "__main__":
    main()
