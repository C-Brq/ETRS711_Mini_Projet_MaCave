class Vin:
    """Une référence de vin du catalogue (pas un exemplaire physique)."""

    def __init__(self, domaine: str, nom: str, type, millesime: int, region: str,
                 description: str = "", photo_etiquette: str = "", id=None):
        self.id = id
        self.domaine = domaine
        self.nom = nom
        self.type = type  # un TypeVin
        self.millesime = millesime
        self.region = region
        self.description = description
        self.photo_etiquette = photo_etiquette
        self.evaluations = []  # les Evaluation reçues par ce vin

    def nb_evaluations(self) -> int:
        return len(self.evaluations)

    def note_moyenne(self):
        """Moyenne des notes, ou None si le vin n'a aucune évaluation (« Non évalué »)."""
        if self.nb_evaluations() == 0:
            return None
        total = sum(e.note for e in self.evaluations)
        return total / self.nb_evaluations()
