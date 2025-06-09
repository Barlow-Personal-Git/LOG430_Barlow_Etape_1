"""Retour vente Controllers"""
from app.db import session
from app.models import Inventaire, Transaction
from views import retour_view
from app.client_session import ClientSession

client_session = ClientSession()


def menu_retour():
    """Affiche le menu de retour vente"""
    while True:
        retour_view.afficher_choix()
        retour_view.afficher_retour()
        retour_view.afficher_consulter_liste_vente()
        retour_view.afficher_quitter()
        choix = retour_view.demander_choix()

        if choix == "1":
            retourner_transaction()
        if choix == "2":
            consulter_vente()
        if choix == "3":
            break


def retourner_transaction():
    """Retourne la vente selon l'id"""
    retour_view.afficher_vente_retour()
    transaction_id = retour_view.demander_vente_id()

    if transaction_id.lower() == "back":
        return

    client = client_session.get_client()
    transaction = session.query(Transaction).filter_by(
        id_transaction=transaction_id,
        id_client=client.id_client
    ).first()

    if not transaction:
        retour_view.afficher_vente_introuvable()
        return

    for tp in transaction.produits:
        inventaire = session.query(Inventaire).filter_by(
            id_produit=tp.id_produit
        ).first()
        if inventaire:
            inventaire.nbr += tp.nbr

    for tp in transaction.produits:
        session.delete(tp)

    session.delete(transaction)
    session.commit()
    retour_view.afficher_transaction(transaction_id)


def consulter_vente():
    """Affiche la liste de vente du client"""
    client = client_session.get_client()
    transactions = session.query(Transaction).filter_by(
        id_client=client.id_client
    ).all()

    if not transactions:
        retour_view.afficher_vente_introuvable()
        return

    for transaction in transactions:
        retour_view.afficher_vente_disponible(transaction)
