from datetime import date

from macave.enums import StatutBouteille
from macave.evaluation import Evaluation


class Bouteille:
    """Un exemplaire physique d'un Vin, rangé dans la cave d'un utilisateur."""

    def __init__(self, vin, cave, prix_achat, date_ajout: date = None, id=None):
        self.id = id
        self.vin = vin
        self.cave = cave
        self.prix_achat = prix_achat
        self.date_ajout = date_ajout or date.today()
        self.statut = StatutBouteille.EN_STOCK
        self.date_sortie = None
        self.etagere = None     # None tant qu'elle n'est pas rangée (ou une fois archivée)
        self.evaluation = None  # remplie à l'archivage
        cave.bouteilles.append(self)

    def est_en_stock(self) -> bool:
        return self.statut == StatutBouteille.EN_STOCK

    def deplacer_vers(self, destination) -> None:
        if not self.est_en_stock():
            raise ValueError("Une bouteille archivée ne peut pas être déplacée.")
        ancienne = self.etagere
        if destination is ancienne:
            return
        destination.accueillir([self])  # refuse si la destination est pleine
        if ancienne is not None:
            ancienne.retirer(self)

    def retirer(self) -> None:
        """Retrait définitif : la bouteille disparaît de la cave."""
        if not self.est_en_stock():
            raise ValueError("Une bouteille archivée ne peut pas être retirée.")
        if self.etagere is not None:
            self.etagere.retirer(self)
        self.cave.bouteilles.remove(self)

    def archiver(self, note: float, commentaire: str = None, date_sortie: date = None) -> Evaluation:
        """Archive la bouteille après dégustation et retourne son évaluation."""
        if not self.est_en_stock():
            raise ValueError("Cette bouteille est déjà archivée.")
        # on crée l'évaluation d'abord : si la note est invalide, rien n'est modifié
        evaluation = Evaluation(self.cave.proprietaire, self.vin, self, note, commentaire)
        if self.etagere is not None:
            self.etagere.retirer(self)
        self.statut = StatutBouteille.ARCHIVEE
        self.date_sortie = date_sortie or date.today()
        self.evaluation = evaluation
        self.vin.evaluations.append(evaluation)
        return evaluation
