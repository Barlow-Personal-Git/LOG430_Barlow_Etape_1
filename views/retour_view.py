"""Retour vente View"""


def afficher_choix():
    print("\nVeuillez sélectionner une des choix")


def afficher_retour():
    print("1. Retourner une vente")


def afficher_consulter_liste_vente():
    print("2. Consulter les ventes")


def afficher_quitter():
    print("3. Quitter")


def demander_choix():
    return input("Choix : ")


def afficher_vente_retour():
    print("\nVeuillez inscrire l'id de la vente ou taper 'Back' pour retourner en arrière")


def demander_vente_id():
    return input("Vente ID : ")


def afficher_vente_introuvable():
    print("Vente introuvable.")


def afficher_transaction(transaction_id):
    print(f"Vente {transaction_id} annulée.")


def afficher_vente_disponible(transaction):
    print(f"ID : {transaction.id_transaction} | Total: {transaction.total}$")
