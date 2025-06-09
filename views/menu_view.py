"""Menu principal View"""


def afficher_choix():
    """Affiche le message de sélection"""
    print("\nVeuillez sélectionner une des choix")


def afficher_recherche():
    """Affiche option 1"""
    print("1. Rechercher un prodruit")


def afficher_achat():
    """Affiche option 2"""
    print("2. Enregistrer une vente")


def afficher_gerer_retour():
    """Affiche option 3"""
    print("3. Gérer les retours")


def afficher_consulter_stock():
    """Affiche option 4"""
    print("4. Consulter l'état du stock des produits")


def afficher_quitter():
    """Affiche option 5"""
    print("5. Quitter")


def demander_choix():
    """Demande du choix"""
    return input("Choix : ")
