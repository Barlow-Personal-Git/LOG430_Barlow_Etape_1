"""Recherche menu Controllers"""
from app.db import session
from app.models import Produit, Inventaire
from views import recherche_view


def menu_recherche():
    """Affiche le menu recherche"""
    while True:
        recherche_view.afficher_choix()
        recherche_view.afficher_identifiant()
        recherche_view.afficher_nom()
        recherche_view.afficher_categorie()
        recherche_view.afficher_quitter()
        choix = recherche_view.demander_choix()

        if choix == "1":
            menu_recherche_id("id")
        if choix == "2":
            menu_recherche_nom("nom")
        if choix == "3":
            menu_recherche_categorie("categorie")
        if choix == "4":
            break


def menu_recherche_nom(recherche):
    """Affiche le menu recherche par nom"""
    while True:
        recherche_view.afficher_recherche_choix(recherche)
        produit = recherche_view.demander_recherche_choix(recherche)
        if produit.lower() == "back":
            break

        if produit:
            produits = session.query(Produit).filter(
                Produit.nom.ilike(f"%{produit}%")
            ).all()

            if produits:
                recherche_view.afficher_titre_liste()
                for p in produits:
                    recherche_view.afficher_produits(p)
            else:
                print("Aucun produit trouvé")
        else:
            print("Veuillez reessayer de nouveau!")


def menu_recherche_id(recherche):
    """Affiche le menu recherche par id"""
    while True:
        recherche_view.afficher_recherche_choix(recherche)
        produit = recherche_view.demander_recherche_choix(recherche)
        if produit.lower() == "back":
            break

        if produit:
            resultat = session.query(Produit).get(int(produit))

            if resultat:
                recherche_view.afficher_titre_produit()
                recherche_view.afficher_produits(resultat)
            else:
                recherche_view.afficher_indisponible()
        else:
            recherche_view.afficher_erreur()


def menu_recherche_categorie(recherche):
    """Affiche le menu recherche par catégorie"""
    while True:
        recherche_view.afficher_recherche_choix(recherche)
        categorie = recherche_view.demander_recherche_choix(recherche)

        if categorie.lower() == "back":
            break

        if categorie:
            inventaires = session.query(Inventaire).filter(
                Inventaire.category == categorie
            ).all()

            if inventaires:
                recherche_view.afficher_titre_liste()
                for inventaire in inventaires:
                    produit = inventaire.produit
                    recherche_view.afficher_produits(produit)
            else:
                recherche_view.afficher_indisponible()
        else:
            recherche_view.afficher_erreur()
