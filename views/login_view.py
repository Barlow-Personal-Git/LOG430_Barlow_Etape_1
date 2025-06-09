"""Connecter View""" 
def afficher_bienvenue_magasin():
    print("Bienvenue au magasin Barlow Supermarket!")

def demander_nom():
    return input("\nVeuillez inscrire votre nom : ").strip()

def afficher_nom_invalide():
    print("Nom invalide. Veuillez réessayer.")

def afficher_bienvenue(nom):
    print(f"Bienvenue {nom}")
