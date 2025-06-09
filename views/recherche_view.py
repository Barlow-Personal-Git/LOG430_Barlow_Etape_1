"""Recherche menu View"""


def afficher_choix():
    """Affiche le message des choix"""
    print("\nVeuillez sélectionner une des choix")


def afficher_identifiant():
    """Affiche option 1"""
    print("1. Par identifiant")


def afficher_nom():
    """Affiche option 2"""
    print("2. Par nom")


def afficher_categorie():
    """Affiche option 3"""
    print("3. Par catégorie")


def afficher_quitter():
    """Affiche option 4"""
    print("4. Quitter")


def demander_choix():
    """Demande le choix"""
    return input("Choix : ")


def afficher_recherche_choix(recherche):
    """Affiche la demande au client de présenter une valeur selon l'option"""
    if recherche == "nom":
        print("\nInscriver le nom du produit ou taper 'Back' pour retourner en arrière")

    if recherche == "id":
        print("\nInscriver l'id du produit ou taper 'Back' pour retourner en arrière")

    if recherche == "categorie":
        print(
            "\nInscriver le catégorie du produit ou taper 'Back' pour retourner en arrière"
        )


def demander_recherche_choix(recherche):
    """Demande une valeur selon l'option"""
    if recherche == "nom":
        return input("Nom du produit : ")

    if recherche == "id":
        return input("Id du produit : ")

    if recherche == "categorie":
        return input("Catégorie du produit : ")

    return ""


def afficher_titre_liste():
    """Affiche l'en-tête de la liste des produits"""
    print("---Liste de produits---")


def afficher_titre_produit():
    """Affiche l'en-tête du produit """
    print("---Produit---")


def afficher_produits(p):
    """Affiche le produit"""
    print(f"- ID : {p.id_produit} | Nom : {p.nom} | Prix : ({p.prix} $)")


def afficher_indisponible():
    """Message d'erreur"""
    print("Aucun produit trouvé")


def afficher_erreur():
    """Message d'erreur"""
    print("Veuillez reessayer de nouveau!")
