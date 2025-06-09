""""Test achat controller"""
from app.models import (
    Produit, 
    Inventaire, 
    Client, 
    Transaction
)
from app.controllers.achat_controller import (
    confirmer_vente, 
    client_session
)
from app.db import session

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
    session.flush()
    
    # Ajouter un inventaire
    inventaire = Inventaire(
        id_produit=produit.id_produit, 
        categorie="Breuvage",
        nbr=30
    )
    session.add(inventaire)
    
    # Créer un client
    client = Client(nom="Test")
    session.add(client)
    session.commit()
    
    # Ajoute le client dans le singleton
    client_session.set_client(client)
    client_session.clear_vente()
    client_session.add_produit(produit, 2)

def test_confirmer_vente():
    """"Test une vente confirmée"""
    confirmer_vente()
    transactions = session.query(Transaction).all()
    assert len(transactions) == 1
    assert transactions[0].total == 2.0
