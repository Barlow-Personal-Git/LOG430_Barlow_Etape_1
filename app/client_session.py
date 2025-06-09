"""Instance Client""" 
class ClientSession:
    _instance = None

    def __new__(client_session):
        if client_session._instance is None :
            client_session._instance = super(ClientSession, client_session).__new__(client_session)
            client_session._instance.client = None
            client_session._instance.produit_ventes = {}
            client_session._instance.total = 0
        return client_session._instance
    
    def set_client(self, client):
        self.client = client

    def get_client(self):
        return self.client

    def add_produit(self, produit, nbr):
        if produit.id_produit in self.produit_ventes:
            self.produit_ventes[produit.id_produit]['nbr'] += nbr
        else:
            self.produit_ventes[produit.id_produit] = {
                'produit' : produit,
                'nbr' : nbr
            }

    def get_produits(self):
        return list(self.produit_ventes.values())
    
    def clear_ventes(self):
        self.produit_ventes = {}
