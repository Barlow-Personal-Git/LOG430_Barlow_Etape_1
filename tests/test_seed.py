"""Tests unitaires Seed"""
import pytest
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
    result = session.query(Inventaire).filter_by(id_produit="1").first()
    assert result is not None
