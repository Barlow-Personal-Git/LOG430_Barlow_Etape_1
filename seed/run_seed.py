"""Executer seed"""
from .seed_produits import seed_produits
from .seed_inventaires import seed_inventaires


def run_all():
    """Executer les seeds"""
    seed_produits()
    seed_inventaires()


if __name__ == "__main__":
    run_all()
