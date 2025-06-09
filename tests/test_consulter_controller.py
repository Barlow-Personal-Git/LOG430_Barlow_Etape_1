""""Test consulter vente"""
from app.models import Produit, Inventaire
from app.controllers.consulter_controller import consulter_liste_produit
from app.db import session
from unittest.mock import patch


def setup_function():
    """"Réinitialise la base de donnée pour chaque test"""
    session.query(Inventaire).delete()
    session.query(Produit).delete()
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


def test_consulter_liste_produit():
    """"Test une consulter la liste des ventes"""
    consulter_liste_produit()
    with patch("views.consulter_view.afficher_inventaire") as mock_afficher_inventaire:
        consulter_liste_produit()

    # Vérifie que la console a été appelé deux fois
    assert mock_afficher_inventaire.call_count == 2
