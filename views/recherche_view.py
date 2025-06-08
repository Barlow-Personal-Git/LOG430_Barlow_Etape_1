def afficher_choix():
    print("\nVeuillez sélectionner une des choix")

def afficher_identifiant():
    print("1. Par identifiant")

def afficher_nom():
    print("2. Par nom")

def afficher_categorie():
    print("3. Par catégorie")    

def afficher_quitter():
    print("4. Quitter")

def demander_choix():
    return input("Choix : ")

def afficher_recherche_choix(recherche):
    if recherche == "nom": 
        print("\nInscriver le nom du produit ou taper 'Back' pour retourner en arrière")

    if recherche == "id":
        print("\nInscriver l'id du produit ou taper 'Back' pour retourner en arrière")

    if recherche == "categorie":
        print("\nInscriver le catégorie du produit ou taper 'Back' pour retourner en arrière")

def demander_recherche_choix(recherche):
    if recherche == "nom": 
        return input("Nom du produit : ")

    if recherche == "id":
        return input("Id du produit : ")

    if recherche == "categorie":
        return input("Catégorie du produit : ")

def afficher_titre_liste():
    print("Liste de produits :")

def afficher_titre_produit():
    print("Produit :")

def afficher_produits(p):
    print(f"- {p.id_produit}  {p.nom} ({p.prix} $)")

def afficher_indisponible():
    print("Aucun produit trouvé")

def afficher_erreur():
    print("Veuillez reessayer de nouveau!")