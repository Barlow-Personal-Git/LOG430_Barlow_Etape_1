from app import session, Produit, Inventaire

def seed_inventaires():
    produits = session.query(Produit).all()

    inventaires = [
        Inventaire(id_produit=produits[0].id_produit, category="Breuvage", nbr=25),
        Inventaire(id_produit=produits[1].id_produit, category="Breuvage", nbr=25),
        Inventaire(id_produit=produits[2].id_produit, category="Breuvage", nbr=25),
        Inventaire(id_produit=produits[3].id_produit, category="Fruit", nbr=35),
        Inventaire(id_produit=produits[4].id_produit, category="Fruit", nbr=30),
        Inventaire(id_produit=produits[5].id_produit, category="Fruit", nbr=40),
        Inventaire(id_produit=produits[6].id_produit, category="Collation", nbr=40),
        Inventaire(id_produit=produits[7].id_produit, category="Collation", nbr=40),
        Inventaire(id_produit=produits[8].id_produit, category="Collation", nbr=30),
    ]
    session.add_all(inventaires)
    session.commit()

    ##Insertion inventaires
    print("Inventaires insérés")