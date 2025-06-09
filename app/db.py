"""Connecter à la session DB"""
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Charger la variable d'environnement .ev
load_dotenv()

# Variable d'environnement
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
