"""Executer seed"""
from .seed_produits import seed_produits
from .seed_magasins import seed_magasins


def run_all():
    """Executer les seeds"""
    seed_produits()
    seed_magasins()


if __name__ == "__main__":
    run_all()
