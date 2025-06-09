from flask import Flask, jsonify, request, send_file
from .db import session
from .models import Inventaire, MessageAlerte, Magasin, Transaction, TransactionProduit, Produit
from .rapport import generer_rapport_pdf
from sqlalchemy import func, extract
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/')
def home():
    return "Magasin LOG430 Server"


@app.route('/inventaires', methods=['POST'])
def synchroniser_inventaire():
    data = request.get_json()
    magasin_nom = data.get('magasin')
    inventaires = data.get('inventaire', [])

    magasin = session.query(Magasin).filter_by(nom=magasin_nom).first()

    for inventaire in inventaires:
        id_produit = inventaire.get("id_produit")
        nbr = inventaire.get('nbr')

        inv = session.query(Inventaire).filter_by(
            id_magasin=magasin.id_magasin, id_produit=id_produit).first()
        if inv:
            inv.nbr = nbr
        else:
            inv = Inventaire(id_magasin=magasin.id_magasin,
                             id_produit=id_produit, nbr=nbr)
            session.add(inv)
    session.commit()
    return jsonify({"message": "Inventaire synchronisé"}), 200


@app.route('/message_alerte', methods=['POST'])
def ajouter_alerte():
    data = request.get_json()
    id_produit = data.get("id_produit")
    magasin = data.get("magasin")
    message = data.get("message")

    if not all([id_produit, magasin, message]):
        return jsonify({"error": "Message incomplet"}), 400

    alerte = MessageAlerte(
        id_produit=id_produit,
        magasin=magasin,
        message=message
    )
    session.add(alerte)
    session.commit()

    return jsonify({"message": "Message envoyé"}), 201


@app.route('/dashboard', methods=['GET'])
def dashboard():
    chiffre_affaires_par_magasin = (
        session.query(
            Magasin.nom,
            func.sum(Transaction.total).label('chiffre_affaires')
        )
        .join(Transaction, Transaction.id_magasin == Magasin.id_magasin)
        .group_by(Magasin.nom)
        .all()
    )

    ruptures = (
        session.query(Magasin.nom, Produit.nom, Inventaire.nbr)
        .join(Inventaire, Inventaire.id_magasin == Magasin.id_magasin)
        .join(Produit, Produit.id_produit == Inventaire.id_produit)
        .filter(Inventaire.nbr < 5)
        .all()
    )

    surstock = (
        session.query(Magasin.nom, Produit.nom, Inventaire.nbr)
        .join(Inventaire, Inventaire.id_magasin == Magasin.id_magasin)
        .join(Produit, Produit.id_produit == Inventaire.id_produit)
        .filter(Inventaire.nbr > 30)
        .all()
    )

    une_semaine = datetime.now() - timedelta(days=7)
    tendances = (
        session.query(
            Magasin.nom,
            func.date(Transaction.updated_at).label('date'),
            func.sum(Transaction.total).label('chiffre_affaires')
        )
        .join(Magasin, Magasin.id_magasin == Transaction.id_magasin)
        .filter(Transaction.updated_at >= une_semaine)
        .group_by(Magasin.nom, func.date(Transaction.updated_at))
        .order_by(func.date(Transaction.updated_at))
        .all()
    )

    data = {
        "ca_par_magasin": [{"magasin": m, "chiffre_affaires": ca} for m, ca in chiffre_affaires_par_magasin],
        "ruptures_stock": [{"magasin": m, "produit": p, "quantite": q} for m, p, q in ruptures],
        "surstock": [{"magasin": m, "produit": p, "quantite": q} for m, p, q in surstock],
        "tendances_hebdomadaires": [
            {"magasin": m, "date": d.isoformat(), "chiffre_affaires": ca} for m, d, ca in tendances
        ]
    }

    return jsonify(data)


@app.route('/rapport', methods=['GET'])
def telecharger_rapport():
    fichier_pdf = generer_rapport_pdf()
    return send_file(
        fichier_pdf,
        download_name="rapport_ventes.pdf",
        as_attachment=True,
        mimetype='application/pdf'
    )


@app.route('/transactions', methods=['POST'])
def ajouter_transaction():
    data = request.get_json()
    magasin_nom = data.get("magasin")
    total = data.get("total")
    produits = data.get("produits")

    magasin = session.query(Magasin).filter_by(nom=magasin_nom).first()
    transaction = Transaction(id_magasin=magasin.id_magasin, total=total)
    session.add(transaction)
    session.flush()
    
    total_transaction = 0

    for item in produits:
        id_produit = item.get("id_produit")
        nbr = item.get("nbr")

        inventaire = session.query(Inventaire).filter_by(
            id_magasin=magasin.id_magasin, id_produit=id_produit).first()

        inventaire.nbr -= nbr
        produit = session.query(Produit).filter_by(
            id_produit=id_produit).first()
        prix = produit.prix
        total_produit = prix * nbr

        tp = TransactionProduit(
            id_transaction=transaction.id_transaction,
            id_produit=id_produit,
            nbr=nbr,
            total=total_produit
        )

        session.add(tp)

        total_transaction += total_produit

    transaction.total = total
    session.commit()

    return jsonify({"message": "Mettre à jour"}), 200


if __name__ == '__main__':
    app.run(debug=True)
