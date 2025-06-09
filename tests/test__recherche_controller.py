""""Test recherche produit"""
from unittest.mock import patch
from app.controllers.recherche_controller import (
    menu_recherche_categorie
)


def test_recherche_par_categorie():
    """"Test une recherche par catégorie"""
    categorie = "Breuvage"
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[categorie, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_categorie("categorie")

    # Vérifie que la console a été appelé deux fois
    assert mock_afficher_produits.call_count == 2
