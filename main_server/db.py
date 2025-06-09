"""Connecter à la session DB Mère"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Charger la variable d'environnement .env
load_dotenv()

# Variable d'environnement
DATABASE_URL = os.getenv('DATABASE_URL_MERE')

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
