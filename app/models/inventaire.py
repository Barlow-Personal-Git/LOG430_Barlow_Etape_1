"""Inventaire model"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Inventaire(Base):
    """"Illustre la tableau inventaire"""
    __tablename__ = 'inventaires'

    id_inventaire = Column(Integer, primary_key=True)
    id_produit = Column(Integer, ForeignKey(
        'produits.id_produit'), nullable=False, unique=True)
    category = Column(String)
    nbr = Column(Integer)

    produit = relationship("Produit", back_populates="inventaires")
