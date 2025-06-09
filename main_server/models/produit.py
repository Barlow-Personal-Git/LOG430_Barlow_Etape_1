"""Produit model"""
from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base


class Produit(Base):
    """"Illustre la tableau produit"""
    __tablename__ = 'produits'

    id_produit = Column(Integer, primary_key=True)
    nom = Column(String)
    prix = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    inventaires = relationship("Inventaire", back_populates="produit")
    transactions = relationship("TransactionProduit", back_populates="produit")
