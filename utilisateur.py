import hashlib
import os


def hacher_mot_de_passe(mdp: str) -> str:
    """Returns 'sel$hash' (never the password in clear)."""
    sel = os.urandom(16)
    hache = hashlib.pbkdf2_hmac("sha256", mdp.encode(), sel, 100_000)
    return sel.hex() + "$" + hache.hex()


class Utilisateur:
    def __init__(self, identifiant: str, email: str, mot_de_passe: str, id=None):
        self.id = id
        self.identifiant = identifiant
        self.email = email
        self.mot_de_passe_hash = hacher_mot_de_passe(mot_de_passe)

    def verifier_mot_de_passe(self, mdp: str) -> bool:
        sel_hex, hache_hex = self.mot_de_passe_hash.split("$")
        hache = hashlib.pbkdf2_hmac("sha256", mdp.encode(), bytes.fromhex(sel_hex), 100_000)
        return hache.hex() == hache_hex

    def modifier_profil(self, email: str, mdp: str = None) -> None:
        self.email = email
        if mdp is not None:
            self.mot_de_passe_hash = hacher_mot_de_passe(mdp)