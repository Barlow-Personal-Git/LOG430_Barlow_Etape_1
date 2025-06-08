from .recherche_controller import menu_recherche
from .achat_controller import menu_achat
# from .consulter_controller import menu_consulter
# from .retour_controller import menu_retour
from views import menu_view

def menu_principal():
    while True:
        menu_view.afficher_choix()
        menu_view.afficher_recherche()
        menu_view.afficher_achat()
        menu_view.afficher_gerer_retour()
        menu_view.afficher_consulter_stock()
        menu_view.afficher_quitter()

        choix = menu_view.demander_choix()

        if choix == "1" :
            menu_recherche()
        if choix == "2" :
            menu_achat()
        if choix == "3" :
            print("3")
        if choix == "4" :
            print("4")
            break
        if choix == "5" :
            break
