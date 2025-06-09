""""Test recherche produit"""
from unittest.mock import patch
from app.models import Produit, Inventaire
from app.controllers.recherche_controller import (
    menu_recherche_categorie
)
from app.db import session


def setup_function():
    """"Réinitialise la base de donnée pour chaque test"""
    session.query(Inventaire).delete()
    session.query(Produit).delete()
    session.commit()

    # Ajouter un produit
    produit_recherche = Produit(nom="Chocolat", prix=1.00)
    session.add(produit_recherche)
    session.flush()

    # Ajouter un inventaire
    inventaire_recherche = Inventaire(
        id_produit=produit_recherche.id_produit,
        category="Dessert",
        nbr=30
    )
    session.add(inventaire_recherche)
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
