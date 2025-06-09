""""Test consulter vente"""
from unittest.mock import patch
from app.controllers.consulter_controller import consulter_liste_produit


def test_consulter_liste_produit(setup_db):
    """"Test une consulter la liste des ventes"""
    consulter_liste_produit()
    with patch("views.consulter_view.afficher_inventaire") as mock_afficher_inventaire:
        consulter_liste_produit()

    # Vérifie que la console a été appelé deux fois
    assert mock_afficher_inventaire.call_count == 2
