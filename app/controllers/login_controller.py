"""Connecter Controllers"""
import os
import requests
from app.client_session import ClientSession
from app.db import session
from app.models import Client, Inventaire
from views import login_view
from .menu_controller import menu_principal


def login():
    """Connecter à un compte"""
    login_view.afficher_bienvenue_magasin()
    while True:
        nom = login_view.demander_nom()

        if not nom:
            login_view.afficher_nom_invalide()
            continue

        client = session.query(Client).filter(Client.nom == nom).first()
        if client:
            login_view.afficher_bienvenue(nom)
        else:
            client = Client(nom=nom)
            session.add(client)
            session.commit()
            login_view.afficher_bienvenue(f"{nom} (Nouveau)")

        client_session = ClientSession()
        client_session.set_client(client)

        envoyer_inventaire_vers_mere()
        menu_principal()
        break


def envoyer_inventaire_vers_mere():
    """Mise à jour du inventaire mère"""
    magasin_nom = os.getenv("MAGASIN")

    inventaires = session.query(Inventaire).all()

    data = {
        "magasin": magasin_nom,
        "inventaire": [
            {
                "id_produit": inventaire.id_produit,
                "nbr": inventaire.nbr
            }
            for inventaire in inventaires
        ]
    }

    try:
        requests.post("http://localhost:5000/inventaires",
                      json=data, timeout=10)
    except Exception as e:
        print("Erreur de synchroniser", e)
