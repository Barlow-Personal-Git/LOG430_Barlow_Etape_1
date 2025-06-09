""""Test recherche produit"""
from unittest.mock import patch
from app.models import Produit, Inventaire
from app.controllers.recherche_controller import (
    menu_recherche_categorie,
    menu_recherche_id,
    menu_recherche_nom
)
from app.db import session


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


def test_recherche_par_categorie():
    """"Test une recherche par catégorie"""
    categorie = "Breuvage"
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[categorie, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_categorie("categorie")

    # Vérifie que la console a été appelé deux fois
    assert mock_afficher_produits.call_count == 2


def test_recherche_par_id():
    """"Test une recherche par id"""
    id_ = 1
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[id_, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_id("id")

    # Vérifie que la console a été appelé un fois
    assert mock_afficher_produits.call_count == 1


def test_recherche_par_nom():
    """"Test une recherche par nom"""
    nom = "Eau"
    with patch(
            "views.recherche_view.demander_recherche_choix", side_effect=[nom, "back"]), \
            patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        menu_recherche_nom("nom")

    # Vérifie que la console a été appelé un fois
    assert mock_afficher_produits.call_count == 1
