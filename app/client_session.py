"""Instance Client""" 
class ClientSession:
    """variables"""
    _instance = None

    def __new__(cls):
        if cls._instance is None :
            cls._instance = super(ClientSession, cls).__new__(cls)
            cls._instance.client = None
            cls._instance.produit_ventes = {}
            cls._instance.total = 0
        return cls._instance

    """Set client"""
    def set_client(self, client):
        self.client = client

    """Get client"""
    def get_client(self):
        return self.client

    """Ajouter produit"""
    def add_produit(self, produit, nbr):
        if produit.id_produit in self.produit_ventes:
            self.produit_ventes[produit.id_produit]['nbr'] += nbr
        else:
            self.produit_ventes[produit.id_produit] = {
                'produit' : produit,
                'nbr' : nbr
            }

    """Get produits"""
    def get_produits(self):
        return list(self.produit_ventes.values())

    """Vider vente"""
    def clear_vente(self):
        self.produit_ventes = {}
