"""Seed Magasin"""
from main_server.db import session
from main_server.models import Magasin


def seed_magasins():
    """Liste d'éléments dans la table magasin"""
    magasins = [

        Magasin(nom="Magasin_1"),
        Magasin(nom="Magasin_2"),
        Magasin(nom="Magasin_3"),
        Magasin(nom="Magasin_4"),
        Magasin(nom="Magasin_5"),

    ]
    session.add_all(magasins)
    session.commit()

    # Insertion magasins
    print("Magasins insérés")
