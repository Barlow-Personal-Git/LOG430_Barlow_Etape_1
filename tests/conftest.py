""""Partage setup"""
import pytest
from sqlalchemy import text
from app.models import Base, Produit, Inventaire, Client
from app.db import engine, session
from app.client_session import ClientSession


@pytest.fixture
def setup_db():
    """"Réinitialise la base de donnée pour chaque test"""

    Base.metadata.create_all(engine)

    try:
        session.execute(text("DELETE FROM transaction_produits"))
        session.execute(text("DELETE FROM transactions"))
        session.execute(text("DELETE FROM inventaires"))
        session.execute(text("DELETE FROM produits"))
        session.execute(text("DELETE FROM clients"))
        session.commit()
    except Exception as e:
        session.rollback()
        raise RuntimeError("Erreur de nettoyage") from e

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
    client_session = ClientSession()
    client_session.set_client(client)
    client_session.clear_vente()
    client_session.add_produit(produit, 2)
