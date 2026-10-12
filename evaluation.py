from datetime import datetime


def verifier_note(note) -> None:
    if not 0 <= note <= 20:
        raise ValueError("The ")


class Evaluation:
    def __init__(self, auteur, vin, bouteille, note: float, commentaire: str = None, id=None):
        verifier_note(note)
        self.id = id
        self.auteur = auteur  # un Utilisateur
        self.vin = vin
        self.bouteille = bouteille
        self.note = note
        self.commentaire = commentaire
        self.date = datetime.now()

    def est_modifiable_par(self, utilisateur) -> bool:
        # plus tard (avec la base de données) : comparer les id
        return self.auteur is utilisateur

    def modifier(self, auteur, note: float, commentaire: str = None) -> None:
        if not self.est_modifiable_par(auteur):
            raise PermissionError("Une évaluation n'est modifiable que par son auteur.")
        verifier_note(note)
        self.note = note
        self.commentaire = commentaire