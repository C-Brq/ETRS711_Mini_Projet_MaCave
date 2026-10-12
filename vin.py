class Vin:
    """A reference of wine from catalogue (not a physical copy)."""

    def __init__(self, domaine: str, nom: str, type, millesime: int, region: str,
                 description: str = "", photo_etiquette: str = "", id=None):
        self.id = id
        self.domaine = domaine
        self.nom = nom
        self.type = type  # Type of wine
        self.millesime = millesime
        self.region = region
        self.description = description
        self.photo_etiquette = photo_etiquette
        self.evaluations = []  # Evaluations received by the wine

    def nb_evaluations(self) -> int:
        return len(self.evaluations)

    def note_moyenne(self):
        """Average note of the wine or none if it has no notes"""
        if self.nb_evaluations() == 0:
            return None
        total = sum(e.note for e in self.evaluations)
        return total / self.nb_evaluations()