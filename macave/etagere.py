class Etagere:
    def __init__(self, nom: str, capacite_max: int, id=None):
        if capacite_max <= 0:
            raise ValueError("La capacité doit être un entier strictement positif.")
        self.id = id
        self.nom = nom
        self.capacite_max = capacite_max
        self.bouteilles = []  # les bouteilles actuellement en stock sur cette étagère

    @property
    def occupation(self) -> int:
        return len(self.bouteilles)

    def places_libres(self) -> int:
        return self.capacite_max - self.occupation

    def taux_occupation(self) -> float:
        return self.occupation / self.capacite_max

    def est_vide(self) -> bool:
        return self.occupation == 0

    def modifier_capacite(self, capacite_max: int) -> None:
        if capacite_max <= 0:
            raise ValueError("La capacité doit être un entier strictement positif.")
        if capacite_max < self.occupation:
            raise ValueError("La capacité ne peut pas être inférieure à l'occupation actuelle.")
        self.capacite_max = capacite_max

    def accueillir(self, bouteilles: list) -> None:
        """Ajoute les bouteilles, ou n'en ajoute aucune si ça dépasse la capacité."""
        if len(bouteilles) > self.places_libres():
            raise ValueError("Capacité de l'étagère dépassée.")
        for bouteille in bouteilles:
            self.bouteilles.append(bouteille)
            bouteille.etagere = self

    def retirer(self, bouteille) -> None:
        self.bouteilles.remove(bouteille)
        if bouteille.etagere is self:
            bouteille.etagere = None
