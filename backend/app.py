from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Produit, Inventaire, Base  

engine = create_engine('sqlite:///database.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_produit = Produit(nom = "Café", prix = 3.50)
session.add(new_produit)
session.flush()

new_inventaire = Inventaire(id_produit = new_produit.id_produit, nbr = 10)
session.add(new_inventaire)
session.commit()

# session.query(Produit).delete()
# session.query(Inventaire).delete()
# session.commit()

inventaires = session.query(Inventaire).all()
for inventaire in inventaires:
    print(inventaire.id_produit)

# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/test", methods=["GET"])
# def test():
#     return jsonify({"message": "Test"})

# if __name__ == "__main__":
#     app.run(debug=True, port=5100 )
