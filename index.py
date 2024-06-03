# TODO : Create selection for add, remove, view, clear list and exit
# TODO : Create elements for add
# TODO : Create elements for remove
# TODO : Create elements for view
# TODO : Create elements for clear list

list = [];

while True:
    choice = input("""Choisissez une option :
                   1 : Ajouter un produit
                   2 : Supprimer un produit
                   3 : Voir la liste
                   4 : Vider la liste
                   5 : Quitter : """);

    match choice:
        case "1":
            produit = input("Ajoutez le produit : ");
            list.append(produit);
            print(f"{produit} à bien été ajouté !")
        case "2":
            produit = input("Supprimez le produit : ");
            if produit in list:
                list.remove(produit);
                print(f"{produit} à bien été supprimé !");
            else:
                print(f"le produit {produit} n'existe pas ! ");
        case "3":
            if list:
                for i, item in list:
                    print(f"{i}. {item}");
            else:
                print("Cette liste est vide");
        case "4":
            list.clear();
            print("Votre liste à bien été vidé !")
        case "5":
            print("A bientôt !");
            exit();
        case _:
            print("Ce choix n'existe pas ! ");

