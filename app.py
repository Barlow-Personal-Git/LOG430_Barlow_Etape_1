from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Produit, Base  

engine = create_engine('sqlite:///database.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_produit = Produit(nom = "Café", prix = 3.50)
session.add(new_produit)
session.commit()

# session.query(Produit).delete()
# session.commit()

produits = session.query(Produit).all()
for produit in produits:
    print(produit.nom, produit.prix)
