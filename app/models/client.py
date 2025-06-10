"""Client model"""
from sqlalchemy import Column, Integer, String, CheckConstraint, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base


class Client(Base):
    """"Illustre la tableau client"""
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)
    created_at = Column(DateTime, default=func.now)
    updated_at = Column(DateTime, default=func.now, onupdate=func.now)

    transactions = relationship("Transaction", back_populates="client")

    __table_args__ = (
        CheckConstraint(
            "role IN ('super_admin', 'admin', 'user')", name='check_role'),
    )
