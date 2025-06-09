"""Consulter Controllers"""
import os
import requests
from app.db import session
from app.models import Inventaire, Produit
from app.client_session import ClientSession
from views import consulter_view

MAGASIN = os.getenv("MAGASIN")
client_session = ClientSession()


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

    client = client_session.get_client()
    while True and client.role == "admin":
        print("Veuillez sélectionner un choix")
        print("1. Alerte un produit insuffisant")
        print("2. Quitter")
        choix = input("- ")

        if choix == "1":
            envoye_approvisionnement()
        if choix == "2":
            break


def envoye_approvisionnement():
    """Envoie une alerte d'un produit insuffisant"""
    while True:
        print("Veuillez sélectionner un choix")
        produit_id = input("Produit ID : ")
        produit = session.query(Produit).filter_by(
            id_produit=produit_id).first()

        if not produit:
            print("Produit introuvable")
            continue

        texte_message = input("Message d'alerte : ")
        response = requests.post(
            "http://localhost:5000/message_alerte",
            json={
                "id_produit": produit_id,
                "magasin": MAGASIN,
                "message": texte_message
            }
        )

        if response.status_code == 201:
            print("Une demande a été envoyée")
        else:
            print("Erreur survenu :", response.text)
