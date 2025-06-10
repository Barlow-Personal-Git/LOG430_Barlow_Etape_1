"""Client model"""
from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship
from .base import Base


class Client(Base):
    """"Illustre la tableau client"""
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)

    transactions = relationship("Transaction", back_populates="client")

    __table_args__ = (
        CheckConstraint(
            "role IN ('super_admin', 'admin', 'user')", name='check_role'),
    )
