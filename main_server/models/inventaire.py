"""Inventaire model""" 
from sqlalchemy import Column, ForeignKey, Integer, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class Inventaire(Base):
    """"Illustre la tableau inventaire"""
    __tablename__ = 'inventaires'

    id_inventaire = Column(Integer, primary_key=True)
    id_produit = Column(Integer, ForeignKey('produits.id_produit'), nullable= False)
    id_magasin = Column(Integer, ForeignKey('magasins.id_magasin'), nullable= False)
    nbr = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    produit = relationship("Produit", back_populates="inventaires")
    magasin = relationship("Magasin", back_populates="inventaires")
