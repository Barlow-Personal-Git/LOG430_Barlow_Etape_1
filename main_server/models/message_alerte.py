"""Message d'alerte model"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from .base import Base


class MessageAlerte(Base):
    """"Illustre la tableau message_alertes"""
    __tablename__ = 'message_alertes'

    id_message = Column(Integer, primary_key=True)
    id_produit = Column(Integer, ForeignKey('produits.id_produit'))
    magasin = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
