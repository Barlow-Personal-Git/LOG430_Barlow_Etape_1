"""Tests unitaires Seed"""
from app import session, Produit, Inventaire
from seed import run_seed

def test_seed_produit():
    """Vérifie qu'un produit attendu existe"""
    run_seed()
    
    result = session.query(Produit).filter_by(name="Eau").first()
    assert result is not None

def test_seed_inventaire():
    """Vérifie qu'un inventaire attendu existe"""
    run_seed()
    
    result = session.query(Inventaire).filter_by(id_produit="1").first()
    assert result is not None