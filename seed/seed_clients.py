"""Seed Client"""
from app import session, Client


def seed_clients():
    """Liste d'éléments dans la table client"""
    client = [
        Client(role="super_admin", nom="superadmin"),
        Client(role="admin", nom="admin"),
    ]
    session.add_all(client)
    session.commit()

    # Insertion Client
    print("Client insérés")
