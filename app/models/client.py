"""Client model""" 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Client(Base):
    """"Illustre la tableau client"""
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True)
    nom = Column(String)

    transactions = relationship("Transaction", back_populates="client")
