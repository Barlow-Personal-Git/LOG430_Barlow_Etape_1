""""Test retour controller"""
from app.models import (
    Produit,
    Inventaire,
    Client,
    Transaction
)
from app.controllers.retour_controller import (
    retourner_transaction,
    client_session
)
from app.controllers.achat_controller import (
    confirmer_vente,
)
from app.db import session
from unittest.mock import patch


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
        category="Breuvage",
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

    # Ajouter une vente
    confirmer_vente()


def test_retour_transaction():
    """"Test une retour transaction"""
    client = client_session.get_client()
    transaction = (
        session.query(Transaction)
        .filter_by(id_client=client.id_client)
        .first()
    )
    with patch(
        "views.retour_view.demander_vente_id",
        return_value=str(transaction.id_transaction)
    ):
        retourner_transaction()

    assert session.query(Transaction).get(transaction.id_transaction) is None
