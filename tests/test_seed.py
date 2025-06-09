"""Tests unitaires Seed"""
from app import session, Produit, Inventaire
from seed import run_all


def test_seed_produit():
    """Vérifie qu'un produit attendu existe"""
    run_all()
    result = session.query(Produit).filter_by(nom="Eau").first()
    assert result is not None


def test_seed_inventaire():
    """Vérifie qu'un inventaire attendu existe"""
    run_all()
    produit = session.query(Produit).filter_by(nom="Eau").first()
    result = session.query(Inventaire).filter_by(id_produit=produit.id_produit).first()
    assert result is not None
