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


def run_test_recherche(value, func, expected_call_count, recherche):
    """Exécution du test de recherche"""
    with patch(
        "views.recherche_view.demander_recherche_choix",
        side_effect=[value, "back"]
    ), patch("views.recherche_view.afficher_produits") as mock_afficher_produits:
        func(recherche)
    assert mock_afficher_produits.call_count == expected_call_count


def test_recherche_par_categorie():
    """"Test une recherche par catégorie"""
    run_test_recherche("Breuvage", menu_recherche_categorie, 2, "categorie")


def test_recherche_par_id():
    """"Test une recherche par id"""
    run_test_recherche(1, menu_recherche_id, 1, "id")


def test_recherche_par_nom():
    """"Test une recherche par nom"""
    run_test_recherche("Eau", menu_recherche_nom, 1, "nom")
