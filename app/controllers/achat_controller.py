"""Achat Controllers"""
from app.db import session
from app.models import Produit, Inventaire, Transaction, TransactionProduit
from views import achat_view
from app.client_session import ClientSession

client_session = ClientSession()


def menu_achat():
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
    while True:
        achat_view.afficher_ajouter_produit()
        produit_id = achat_view.demander_choix_ajouter()

        if produit_id.lower() == "back":
            break

        elif produit_id:
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
        elif choix == "2":
            restart_vente()
            break
        elif choix == "3":
            break


def restart_vente():
    client_session.clear_vente()


def confirmer_vente():
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

    client_session.clear_vente()
    achat_view.afficher_vente_confirmer()
