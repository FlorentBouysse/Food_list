# TODO : Create selection for add, remove, view, clear list and exit
# TODO : Create elements for add
# TODO : Create elements for remove
# TODO : Create elements for view
# TODO : Create elements for clear list

list = [];

while True:
    choice = input("1 : Ajouter un produit / 2 : Supprimer un produit / 3 : Voir la liste / 4 : Vider la liste / 5 : Quitter : ");

    match choice:
        case "1":
            produit = input("Ajoutez le produit : ");
            list.append(produit);
        case "2":
            produit = input("Supprimez le produit : ");
            if produit in list:
                list.remove(produit);
            else:
                print("Ce produit n'existe pas ! ");
        case "3":
            print(list);
        case "4":
            list.clear();
        case "5":
            exit();
        case _:
            print("Ce choix n'existe pas ! ");

