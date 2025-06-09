"""Connecter à la session DB"""
import os
from dotenv import load_dotenv
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
