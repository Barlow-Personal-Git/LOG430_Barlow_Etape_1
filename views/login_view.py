"""Connecter View"""


def afficher_bienvenue_magasin():
    """Affiche le bienvenue"""
    print("Bienvenue au magasin Barlow Supermarket!")


def demander_nom():
    """Demande son nom"""
    return input("\nVeuillez inscrire votre nom : ").strip()


def afficher_nom_invalide():
    """Message d'erreur"""
    print("Nom invalide. Veuillez réessayer.")


def afficher_bienvenue(nom):
    """Message de bienvenue"""
    print(f"Bienvenue {nom}")
