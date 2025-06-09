"""Consulter View"""


def afficher_titre():
    """Affiche l'en-tete"""
    print("---Inventaires---")


def afficher_inventaire(produit, inventaire):
    """Affiche les produits consultés"""
    print(
        f"- Nom : {produit.nom} | "
        f"Prix : {produit.prix:.2f} | "
        f"Catégorie : {inventaire.category} | "
        f"Quantité : {inventaire.nbr}"
    )
