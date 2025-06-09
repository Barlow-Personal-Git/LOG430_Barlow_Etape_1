"""Connecter à la session DB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine(
    'postgresql://log430:laboratoirelog430@localhost:5432/log430_lab',
    echo=False
)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
