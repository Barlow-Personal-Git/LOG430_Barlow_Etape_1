"""Magasin model"""
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base


class Magasin(Base):
    """"Illustre la tableau magasin"""
    __tablename__ = 'magasins'

    id_magasin = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now)
    updated_at = Column(DateTime, default=func.now, onupdate=func.now)

    transactions = relationship("Transaction", back_populates="magasin")
    inventaires = relationship("Inventaire", back_populates="magasin")
