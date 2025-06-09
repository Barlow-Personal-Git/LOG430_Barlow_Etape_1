"""Consulter Controllers"""
from app.db import session
from app.models import Inventaire
from views import consulter_view


def consulter_liste_produit():
    """Consulter la liste des produits"""
    inventaires = (
        session.query(Inventaire)
        .join(Inventaire.produit)
        .order_by(Inventaire.category)
        .all()
    )
    consulter_view.afficher_titre()

    for inventaire in inventaires:
        produit = inventaire.produit
        consulter_view.afficher_inventaire(produit, inventaire)
