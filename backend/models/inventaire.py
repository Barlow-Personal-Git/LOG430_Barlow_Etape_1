from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Inventaire(Base):
    __tablename__ = 'inventaires'

    id_inventaire = Column(Integer, primary_key=True)
    id_produit = Column(Integer, ForeignKey('produits.id_produit'), nullable= False)
    category = Column(String)
    nbr = Column(Integer)

    produit = relationship("Produit", back_populates="inventaires")
