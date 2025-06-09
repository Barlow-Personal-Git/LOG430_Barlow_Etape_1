""""Test retour controller"""
from unittest.mock import patch
from app.models import Transaction
from app.controllers.retour_controller import (
    retourner_transaction,
    client_session
)
from app.controllers.achat_controller import (
    confirmer_vente,
)
from app.db import session


def test_retour_transaction(setup_db):
    """"Test une retour transaction"""
    confirmer_vente()
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
