"""Transaction Produit model"""
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base


class TransactionProduit(Base):
    """"Illustre la tableau transaction produit"""
    __tablename__ = 'transaction_produits'

    id_transaction_produit = Column(Integer, primary_key=True)
    id_transaction = Column(Integer, ForeignKey(
        'transactions.id_transaction'), nullable=False)
    id_produit = Column(Integer, ForeignKey(
        'produits.id_produit'), nullable=False)
    nbr = Column(Integer)
    total = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    transaction = relationship("Transaction", back_populates="produits")
    produit = relationship("Produit", back_populates="transactions")
