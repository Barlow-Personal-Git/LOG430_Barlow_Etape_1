"""Achat View"""


def afficher_choix():
    """Affiche le message initial"""
    print("\nVeuillez sélectionner une des choix")


def afficher_achat():
    """Affiche l'option 1"""
    print("1. Ajouter des produits")


def afficher_produits():
    """Affiche l'option 2"""
    print("2. Consulter la vente")


def afficher_quitter():
    """Affiche l'option 3"""
    print("3. Retour")


def demander_choix():
    """Demande au client de choisir"""
    return input("Choix : ")


def afficher_ajouter_produit():
    """Affiche le message d'ajout"""
    print("\nVeuillez inscrire l'identifiant du produit ou taper 'Back' pour retourner en arrière")


def demander_choix_ajouter():
    """Demande l'id du produit"""
    return input("Produit ID : ")


def demande_quantite():
    """Demande la quantite"""
    return input("Quantites : ")


def afficher_zero():
    """Affiche message d'erreur"""
    print("\nVeuillez recommencer et ajouter une quantite supérieure ou égale à 1")


def afficher_insuffisant():
    """Affiche message d'erreur"""
    print("Il n'a pas suffisament de produit disponible")


def afficher_inventaire_pas_enregistrer():
    """Affiche message d'erreur"""
    print("Aucun inventaire trouvé pour ce produit.")


def afficher_aucun_produit():
    """Affiche message d'erreur"""
    print("Aucun produit")


def afficher_ventes():
    """Affiche l'en-tete de la vente"""
    print("---- Ventes ----")


def afficher_produit_total(produit, nbr, produit_total):
    """Affiche le prix total du produit"""
    print(f"- {produit.nom} x{nbr} = {produit_total:.2f}$")


def afficher_total(total):
    """Affiche le total"""
    print(f"Total : {total:.2f}$")


def afficher_confirmer():
    """Affiche option confirmer"""
    print("1. Confirmer votre vente")


def afficher_effacer():
    """Affiche option recommencer"""
    print("2. Recommencer la vente")


def afficher_vente_confirmer():
    """Affiche confirmer la vente"""
    print("Vente confirmer")


def afficher_produit_ajouter(produit, nbr):
    """Affiche produit ajouter dans la vente"""
    print(f"Ajouter à la vente :  {produit.nom} x{nbr}")
