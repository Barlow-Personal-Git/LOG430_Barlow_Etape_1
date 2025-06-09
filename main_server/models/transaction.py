"""Transaction model"""
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base


class Transaction(Base):
    """"Illustre la tableau transaction"""
    __tablename__ = 'transactions'

    id_transaction = Column(Integer, primary_key=True)
    id_magasin = Column(Integer, ForeignKey(
        'magasins.id_magasin'), nullable=False)
    total = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    produits = relationship(
        "TransactionProduit",
        back_populates="transaction",
        cascade="all, delete-orphan"
    )
    magasin = relationship("Magasin", back_populates="transactions")
