""""Test recherche produit"""
from unittest.mock import patch
from app.controllers.recherche_controller import (
    menu_recherche_categorie,
    menu_recherche_id,
    menu_recherche_nom
)


def test_recherche_par_categorie(setup_db):  # pylint: disable=unused-argument
    """"Test une recherche par catégorie"""
    categorie = "Breuvage"
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[categorie, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_categorie("categorie")

    # Vérifie que la console a été appelé deux fois
    assert mock_afficher_produits.call_count == 2


def test_recherche_par_id(setup_db):  # pylint: disable=unused-argument
    """"Test une recherche par id"""
    id_ = 1
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[id_, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_id("id")

    # Vérifie que la console a été appelé une fois
    assert mock_afficher_produits.call_count == 1


def test_recherche_par_nom(setup_db):  # pylint: disable=unused-argument
    """"Test une recherche par id"""
    nom = "Eau"
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[nom, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_nom("nom")

    # Vérifie que la console a été appelé une fois
    assert mock_afficher_produits.call_count == 1
