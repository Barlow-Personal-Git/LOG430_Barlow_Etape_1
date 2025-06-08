from app.db import session
from app.models import Client
from views import login_view
from .menu_controller import menu_principal
from app.client_session import ClientSession

def login():
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

        menu_principal()
        break