from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Produit(Base):
    __tablename__ = 'produits'

    id_produit = Column(Integer, primary_key=True)
    nom = Column(String)
    prix = Column(Float)

    inventaires = relationship("Inventaire", back_populates="produit")
    transactions = relationship("TransactionProduit", back_populates="produit")

