from enum import Enum

class TypeVin(Enum):
    ROUGE = "rouge"
    BLANC = "blanc"
    ROSE = "rose"
    EFFERVESCENT = "effervescent"
    
class StatutBouteille(Enum):
    EN_STOCK = "en_stock"
    ARCHIVEE = "archivee"