from app import session
from models import Produit, Inventaire

def menu():
    print("Veuillez sélectionner une des choix")
    print("1. Rechercher un prodruit")
    print("2. Enregistrer une vente")
    print("3. Gérer les retours")
    print("4. Consulter l'état du stock des produits")
    print("5. Quitter")

    while True:
        choix = input("Choix : ")

        if choix == "1" :
            menu_recherche()
        if choix == "2" :
            print("2")
        if choix == "3" :
            print("3")
        if choix == "4" :
            print("4")
            break
        if choix == "5" :
            break

def menu_recherche() : 
    while True:
        print("Veuillez sélectionner une des choix")
        print("1. Par identifiant")
        print("2. Par nom")
        print("3. Par catégorie")
        print("4. Quitter")
        choix = input("Choix : ")
        if choix == "1" :
            menu_recherche_id()
        if choix == "2" :
            menu_recherche_nom()
        if choix == "3" :
            menu_recherche_categorie()
        if choix == "4" :
            break

def menu_recherche_nom() : 
    while True :
        print("Inscriver le nom du produit ou taper 'Back' pour retourner en arrière")
        produit = input("Nom du produit : ")
        print(produit)
        if produit.lower() == "back":
            break

        elif produit:
            produits = session.query(Produit).filter(
                Produit.nom.ilike(f"%{produit}%")
            ).all()

            if produits :
                print("Liste de produits :")
                for p in produits:
                    print(f"- {p.nom} ({p.prix} $)")
            else :
                print("Aucun produit trouvé")
        else :
            print("Veuillez reessayer de nouveau!")

def menu_recherche_id() : 
    while True :
        print("Inscriver l'id du produit ou taper 'Back' pour retourner en arrière")
        produit = input("Id du produit : ")
        print(produit)
        if produit.lower() == "back":
            break

        elif produit:
            resultat = session.query(Produit).get(int(produit))

            if resultat :
                print("Produit :")
                print(f"- {resultat.nom} ({resultat.prix} $)")
            else :
                print("Aucun produit trouvé")
        else :
            print("Veuillez reessayer de nouveau!")

def menu_recherche_categorie() : 
    while True :
        print("Inscriver le catégorie du produit ou taper 'Back' pour retourner en arrière")
        categorie = input("Catégorie du produit : ")
        
        if categorie.lower() == "back":
            break

        elif categorie:
            inventaires = session.query(Inventaire).filter(
                Inventaire.category == categorie
            ).all()

            if inventaires :
                print("Liste de produits :")
                for inventaire in inventaires:
                    produit = inventaire.produit
                    print(f"- {produit.nom} ({produit.prix} $)")
            else :
                print("Aucun produit trouvé")
        else :
            print("Veuillez reessayer de nouveau!")

def login():
    print("Bienvenue au magasin Barlow Supermarket!")
    while True:
        name = input("Veuillez inscrire votre nom : ")

        if name:
            print(f"Bienvenu {name}")
            menu()
            break
        else:
            print("Nom invalide. Veuillez reessayer.")

if __name__ == "__main__":
    login()