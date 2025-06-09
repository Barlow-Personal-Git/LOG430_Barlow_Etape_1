""""Partage setup"""
from unittest.mock import patch
from app.models import Produit, Inventaire, Client, Transaction
from app.controllers.consulter_controller import consulter_liste_produit
from app.db import session
from app.client_session import ClientSession


def setup_function():
    """"Réinitialise la base de donnée pour chaque test"""
    session.query(Transaction).delete()
    session.query(Inventaire).delete()
    session.query(Produit).delete()
    session.query(Client).delete()
    session.commit()

    # Ajouter un produit
    produit = Produit(nom="Eau", prix=1.00)
    session.add(produit)
    produit2 = Produit(nom="Cafe", prix=2.00)
    session.add(produit2)
    session.flush()

    # Ajouter un inventaire
    inventaire = Inventaire(
        id_produit=produit.id_produit,
        category="Breuvage",
        nbr=30
    )
    inventaire2 = Inventaire(
        id_produit=produit2.id_produit,
        category="Breuvage",
        nbr=40
    )
    session.add(inventaire)
    session.add(inventaire2)
    session.commit()
    
    # Ajouter un client
    client = Client(nom="Test")
    session.add(client)
    session.commit()
    
    # Préparer le singleton
    ClientSession.set_client(client)
    ClientSession.clear_vente()
    ClientSession.add_produit(produit, 2)