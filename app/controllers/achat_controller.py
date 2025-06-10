"""Achat Controllers"""
import os
import requests
from app.client_session import ClientSession
from app.db import session
from app.models import Produit, Inventaire, Transaction, TransactionProduit
from views import achat_view

MAGASIN = os.getenv("MAGASIN")
client_session = ClientSession()


def menu_achat():
    """Affiche le menu pour consulter ou acheter des produits"""
    while True:
        achat_view.afficher_choix()
        achat_view.afficher_achat()
        achat_view.afficher_produits()
        achat_view.afficher_quitter()
        choix = achat_view.demander_choix()

        if choix == "1":
            ajouter_produit()
        if choix == "2":
            consulter_produit()
        if choix == "3":
            break


def ajouter_produit():
    """Ajouter des produits dans la vente"""
    while True:
        achat_view.afficher_ajouter_produit()
        produit_id = achat_view.demander_choix_ajouter()

        if produit_id.lower() == "back":
            break

        if produit_id:
            resultat = session.query(Produit).get(int(produit_id))
            nbr = int(achat_view.demande_quantite())

            if nbr <= 0:
                achat_view.afficher_zero()
                continue

            inventaire = session.query(Inventaire).filter(
                Inventaire.id_produit == resultat.id_produit
            ).first()

            if not inventaire:
                achat_view.afficher_inventaire_pas_enregistrer()
                continue

            if inventaire.nbr < nbr:
                achat_view.afficher_insuffisant()
                continue

            client_session.add_produit(resultat, nbr)
            achat_view.afficher_produit_ajouter(resultat, nbr)


def consulter_produit():
    """Consulter le panier et visualiser le total"""
    produits = client_session.get_produits()
    if not produits:
        achat_view.afficher_aucun_produit()
        return

    achat_view.afficher_ventes()
    total = 0

    for item in produits:
        produit = item['produit']
        nbr = item['nbr']
        produit_total = nbr * produit.prix
        total += produit_total

        achat_view.afficher_produit_total(produit, nbr, produit_total)

    achat_view.afficher_total(total)

    while True:
        achat_view.afficher_choix()
        achat_view.afficher_confirmer()
        achat_view.afficher_effacer()
        achat_view.afficher_quitter()
        choix = achat_view.demander_choix()
        if choix == "1":
            confirmer_vente()
            break
        if choix == "2":
            restart_vente()
            break
        if choix == "3":
            break


def restart_vente():
    """Recommencer la vente"""
    client_session.clear_vente()


def confirmer_vente():
    """Confirmer les produits dans le panier"""
    client = client_session.get_client()
    produits = client_session.get_produits()

    total_transaction = 0
    transaction = Transaction(id_client=client.id_client, total=0.0)
    session.add(transaction)
    session.flush()

    for item in produits:
        produit = item['produit']
        nbr = item['nbr']
        total_produit = produit.prix * nbr

        inventaire = session.query(Inventaire).filter(
            Inventaire.id_produit == produit.id_produit
        ).first()
        if not inventaire or inventaire.nbr < nbr:
            achat_view.afficher_insuffisant()
            session.rollback()
            return
        inventaire.nbr -= nbr

        tp = TransactionProduit(
            id_transaction=transaction.id_transaction,
            id_produit=produit.id_produit,
            nbr=nbr,
            total=total_produit
        )
        session.add(tp)
        total_transaction += total_produit

    transaction.total = total_transaction
    session.commit()
    envoyer_requete_mere(transaction.id_transaction)

    client_session.clear_vente()
    achat_view.afficher_vente_confirmer()


def envoyer_requete_mere(transaction_id):

    url = "http://localhost:5000/transactions"
    transaction = session.query(Transaction).get(transaction_id)
    trans_prod = session.query(TransactionProduit).filter_by(
        id_transaction=transaction_id).all()

    data = {
        "magasin": MAGASIN,
        "total": transaction.total,
        "produits": [
            {
                "id_produit": tp.id_produit,
                "nbr": tp.nbr
            }
            for tp in trans_prod
        ]
    }

    try:
        requests.post(url, json=data)
    except requests.RequestException as e:
        print("Probleme connection avec la server mère")
