def main():
    print("Bienvenue! Sélectionnez une des commande en écrivant le number indiquier : ")
    print("1. Recherche un produit")
    print("2. Enregistrer une vente")
    print("3. Annuler une vente")
    print("4. Consulter l'état du stock des produits")
    print("5. Quitter")

    while True:
        commande = input("> ")
        
        if commande == "1":
            while True:
                print("Voulez-vous faire votre recherche par :")
                print("1. identifiant")
                print("2. nom")
                print("3. catégorie")
                print("4. Quitter")
                
                second_command = input("> ")
                
                if second_command == "4": 
                    break
                while True: 
                    if second_command == "1": 
                        print("Inscriver l'identifiant")
                    if second_command == "2": 
                        print("Inscriver le nom")
                    if second_command == "3": 
                        print("Inscriver le catégorie")
                    
                    third_command = input("> ")
                    
        if commande == "2":
            print("Liste")

        if commande == "3":
            print("0")

        if commande == "4":
            print("Liste")

        if commande == "5":
            print("Merci")
            break
        else :
            break

if __name__ == "__main__":
    main()
