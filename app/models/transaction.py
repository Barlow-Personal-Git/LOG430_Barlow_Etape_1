from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id_transaction = Column(Integer, primary_key=True)
    id_client = Column(Integer, ForeignKey('clients.id_client'), nullable= False)
    total = Column(Float)

    produits = relationship("TransactionProduit", back_populates="transaction", cascade="all, delete-orphan")
    client = relationship("Client", back_populates="transactions")