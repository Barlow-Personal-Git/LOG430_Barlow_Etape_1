def afficher_titre():
    print("---Inventaires---")

def afficher_inventaire(produit, inventaire):
    print(f"- Nom : {produit.nom} | Prix: {produit.prix:.2f} | Quantité: {inventaire.nbr}")