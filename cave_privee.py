from macave.etagere import Etagere


class CavePrivee:
    def __init__(self, proprietaire, id=None):
        self.id = id
        self.proprietaire = proprietaire  # A user
        self.etageres = []
        self.bouteilles = []  # All bottles

    def appartient_a(self, utilisateur) -> bool:
        # plus tard (avec la base de données) : comparer les id
        return self.proprietaire is utilisateur

    def creer_etagere(self, nom: str, capacite_max: int) -> Etagere:
        if any(e.nom == nom for e in self.etageres):
            raise ValueError("Une étagère porte déjà ce nom dans cette cave.")
        etagere = Etagere(nom, capacite_max)
        self.etageres.append(etagere)
        return etagere

    def supprimer_etagere(self, etagere: Etagere) -> None:
        if not etagere.est_vide():
            raise ValueError("Impossible de supprimer une étagère qui n'est pas vide.")
        self.etageres.remove(etagere)

    def bouteilles_en_stock(self) -> list:
        return [b for b in self.bouteilles if b.est_en_stock()]

    def historique(self) -> list:
        return [b for b in self.bouteilles if not b.est_en_stock()]

    def nb_bouteilles(self) -> int:
        return len(self.bouteilles_en_stock())

    def nb_references(self) -> int:
        """Nombre de vins différents parmi les bouteilles en stock."""
        return len({b.vin for b in self.bouteilles_en_stock()})

    def capacite_totale(self) -> int:
        return sum(e.capacite_max for e in self.etageres)

    def occupation_globale(self):
        """Bouteilles / capacité totale, ou None s'il n'y a aucune étagère."""
        capacite = self.capacite_totale()
        if capacite == 0:
            return None
        return self.nb_bouteilles() / capacite

    def valeur_stock(self):
        return sum(b.prix_achat for b in self.bouteilles_en_stock())