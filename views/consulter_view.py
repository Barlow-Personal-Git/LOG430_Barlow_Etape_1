"""Consulter View"""


def afficher_titre():
    """Affiche l'en-tete"""
    print("---Inventaires---")


def afficher_inventaire(produit, inventaire):
    """Affiche les produits consultés"""
    print(
        f"- Nom : {produit.nom} | Prix: {produit.prix:.2f} | Quantité: {inventaire.nbr}")
