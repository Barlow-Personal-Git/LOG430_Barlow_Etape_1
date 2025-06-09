""""Test achat controller"""
from app.models import Transaction
from app.controllers.achat_controller import (
    confirmer_vente,
    restart_vente,
    client_session
)
from app.db import session


def test_confirmer_vente(setup_db):  # pylint: disable=unused-argument
    """"Test une vente confirmée"""
    confirmer_vente()
    transactions = session.query(Transaction).all()
    assert len(transactions) == 1
    assert transactions[0].total == 2.0


def test_recommencer_vente(setup_db):  # pylint: disable=unused-argument
    """"Test une recommencer une vente"""
    restart_vente()
    produits = client_session.get_produits()
    assert len(produits) == 0
