def afficher_choix():
    print("\nVeuillez sélectionner une des choix")

def afficher_achat():
    print("1. Ajouter des produits")

def afficher_produits():
    print("2. Consulter la vente")

def afficher_quitter():
    print("3. Retour")

def demander_choix():
    return input("Choix : ")

def afficher_ajouter_produit():
    print("\nVeuillez inscrire l'identifiant du produit ou taper 'Back' pour retourner en arrière")

def demander_choix_ajouter():
    return input("Produit ID : ")

def demande_quantite():
    return input("Quantites : ")

def afficher_zero():
    print("\nVeuillez recommencer et ajouter une quantite supérieure ou égale à 1")

def afficher_insuffisant():
    print("Il n'a pas suffisament de produit disponible")

def afficher_inventaire_pas_enregistrer():
    print("Aucun inventaire trouvé pour ce produit.")

def afficher_aucun_produit():
    print("Aucun produit")

def afficher_ventes():
    print("---- Ventes ----")

def afficher_produit_total(produit, nbr, produit_total):
    print(f"- {produit.nom} x{nbr} = {produit_total:.2f}$")

def afficher_total(total):
    print(f"Total : {total:.2f}$")

def afficher_confirmer():
    print("1. Confirmer votre vente")

def afficher_effacer():
    print("2. Recommencer la vente")

def afficher_vente_confirmer():
    print("Vente confirmer")

def afficher_produit_ajouter(produit, nbr):
    print(f"Ajouter au panier : {produit.nom} x{nbr}")
