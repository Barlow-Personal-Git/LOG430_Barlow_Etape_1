"""Créaction d'un PDF"""
from fpdf import FPDF
from sqlalchemy import func
from .db import session
from .models import Transaction, Produit, Magasin, Inventaire, TransactionProduit


class Rapport(FPDF):
    """Configuration du rapport PDF"""

    def header(self):
        """L'en-tête"""
        self.set_font('Arial', 'B', 16)
        self.cell(0, 12, 'Rapport des ventes', ln=1, align='C')
        self.ln(9)

    def section_title(self, title):
        """Titre"""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1)

    def add_table_model(self, data, col_widths):
        """Tableau"""
        for row in data:
            for index, value in enumerate(row):
                self.cell(col_widths[index], 10, str(value), border=1)
            self.ln()


def generer_rapport_pdf():
    """Générer le rapport pdf"""
    pdf = Rapport()
    pdf.add_page()

    pdf.section_title("Ventes par magasin")
    ventes_magasin = session.query(
        Magasin.nom,
        func.sum(TransactionProduit.nbr)
    ).select_from(Magasin)\
        .join(Transaction, Transaction.id_magasin == Magasin.id_magasin)\
        .join(
            TransactionProduit,
            TransactionProduit.id_transaction == Transaction.id_transaction)\
        .group_by(Magasin.nom)\
        .all()

    pdf.add_table_model(ventes_magasin, [60, 40])
    pdf.ln(10)

    pdf.section_title("Produits les plus vendus")
    produit_ventes = session.query(
        Produit.nom,
        func.sum(TransactionProduit.nbr)
    ).join(TransactionProduit).group_by(Produit.nom).order_by(func.sum(TransactionProduit.nbr).desc()).limit(5).all()

    pdf.add_table_model(produit_ventes, [80, 40])
    pdf.ln(10)

    pdf.section_title("Stocks restants par produit")
    stocks = session.query(
        Produit.nom,
        func.sum(Inventaire.nbr)
    ).join(Inventaire).group_by(Produit.nom).all()

    pdf.add_table_model(stocks, [80, 40])

    fichier = "rapport_ventes.pdf"
    pdf.output(fichier)
    print(f"Rapport PDF généré: {fichier}")
    return fichier
