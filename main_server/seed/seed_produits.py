"""Seed Produit"""
from main_server.db import session
from main_server.models import Produit


def seed_produits():
    """Liste d'éléments dans la table produit"""
    produits = [
        # Breuvage
        Produit(nom="Eau", prix="1.00", description="eau QC"),
        Produit(nom="Café", prix="1.50", description="eau brun noir"),
        Produit(nom="Thé", prix="1.25", description="eau brun"),

        # Fruits
        Produit(nom="Pomme", prix="0.30", description="fruit QC"),
        Produit(nom="Orange", prix="0.10", description="fruit USA"),
        Produit(nom="Fraise", prix="0.10"),

        # Collations
        Produit(nom="Biscuits", prix="3.00"),
        Produit(nom="Chocolats", prix="2.50"),
        Produit(nom="Chips", prix="2.25")
    ]
    session.add_all(produits)
    session.commit()

    # Insertion Produits
    print("Produits insérés")
