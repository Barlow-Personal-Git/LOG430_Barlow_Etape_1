"""Init app"""
from .db import session
from .models import Produit, Inventaire, Client, Transaction
from .controllers import (
    login_controller,
    recherche_controller,
    achat_controller,
    consulter_controller,
    retour_controller
)
from .client_session import ClientSession
