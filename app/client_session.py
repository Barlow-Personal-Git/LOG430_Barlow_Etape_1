"""Instance Client""" 
class ClientSession:
    """Classe Singleton"""
    _instance = None

    def __new__(cls):
        if cls._instance is None :
            cls._instance = super(ClientSession, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialise les attributs de la session client"""
        self.client = None
        self.produit_ventes = {}
        self.total = 0

    def set_client(self, client):
        """Définit le client"""
        self.client = client

    def get_client(self):
        """Retourne le client"""
        return self.client

    def add_produit(self, produit, nbr):
        """Ajoute un produit au panier
        
        Agrs :
            produit: Objet produit
            nbr: Quantité du produit
        """
        if produit.id_produit in self.produit_ventes:
            self.produit_ventes[produit.id_produit]['nbr'] += nbr
        else:
            self.produit_ventes[produit.id_produit] = {
                'produit' : produit,
                'nbr' : nbr
            }

    def get_produits(self):
        """Retourne la liste des produits"""
        return list(self.produit_ventes.values())

    def clear_vente(self):
        """Vide le panier"""
        self.produit_ventes = {}
