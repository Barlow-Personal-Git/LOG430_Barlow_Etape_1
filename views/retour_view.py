"""Retour vente View"""


def afficher_choix():
    """Affiche le message des choix"""
    print("\nVeuillez sélectionner une des choix")


def afficher_retour():
    """Affiche l'option 1"""
    print("1. Retourner une vente")


def afficher_consulter_liste_vente():
    """Affiche l'option 2"""
    print("2. Consulter les ventes")


def afficher_quitter():
    """Affiche l'option 3"""
    print("3. Quitter")


def demander_choix():
    """Demande le choix"""
    return input("Choix : ")


def afficher_vente_retour():
    """Affiche la demande du id transaction"""
    print("\nVeuillez inscrire l'id de la vente ou taper 'Back' pour retourner en arrière")


def demander_vente_id():
    """Demande l'id de la vente"""
    return input("Vente ID : ")


def afficher_vente_introuvable():
    """Message d'erreur"""
    print("Vente introuvable.")


def afficher_transaction(transaction_id):
    """Affiche l'annulation de la vente"""
    print(f"Vente {transaction_id} annulée.")


def afficher_vente_disponible(transaction):
    """Affiche la transaction du client"""
    print(f"ID : {transaction.id_transaction} | Total: {transaction.total}$")
