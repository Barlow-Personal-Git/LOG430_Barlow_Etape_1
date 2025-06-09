"""Seed Produit"""
from app import session, session, Produit


def seed_produits():
    """Liste d'éléments dans la table produit"""
    produits = [
        # Breuvage
        Produit(nom="Eau", prix="1.00"),
        Produit(nom="Café", prix="1.50"),
        Produit(nom="Thé", prix="1.25"),

        # Fruits
        Produit(nom="Pomme", prix="0.30"),
        Produit(nom="Orange", prix="0.10"),
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
