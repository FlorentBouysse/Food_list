import os;
import json;

# STEP ONE
# TODO : Create selection for add, remove, view, clear list and exit
# TODO : Create elements for add
# TODO : Create elements for remove
# TODO : Create elements for view
# TODO : Create elements for clear list

# STEP TWO
# TODO : Create new folder ok
# TODO : Create new file JSON
# TODO : Update crud for file JSON


# here, get path absolute
way = os.path.dirname(__file__);
shopping_list = [];
# print(chemin + "lala");
# exit();

# create folder with condition for check if folder exist or not
name_folder = "list";
name_file = "list.json";
folder = os.path.join(way, name_folder);

if not os.path.exists(folder):
     os.makedirs(folder);
else:
    with open(f"{way}\{name_folder}\{name_file}", "r") as f:
        shopping_list = json.load(f);
    print("Dossier déjà existant");

while True:
    choice = input("""Choisissez une option :
                   1 : Ajouter un produit
                   2 : Supprimer un produit
                   3 : Voir la liste
                   4 : Vider la liste
                   5 : Quitter : """);

    match choice:
        case "1":
            product = input("Ajoutez le produit : ");
            shopping_list.append(product);
            with open(f"{way}\{name_folder}\{name_file}", "w") as f:
                json.dump(shopping_list, f, indent=4);
            print(f"{product} à bien été ajouté !")
        case "2":
            product = input("Supprimez le produit : ");
            if product in shopping_list:
                shopping_list.remove(product);
                with open(f"{way}\{name_folder}\{name_file}", "w") as f:
                    json.dump(shopping_list, f, indent=4);
                print(f"{product} à bien été supprimé !");
            else:
                print(f"le produit {product} n'existe pas ! ");
        case "3":
            if shopping_list:
                with open(f"{way}\{name_folder}\{name_file}", "r") as f:
                    data = json.load(f);
                    print(data);
                # for i, item in list:
                #     print(f"{i}. {item}");
            else:
                print("Cette liste est vide");
        case "4":
            shopping_list.clear();
            with open(f"{way}\{name_folder}\{name_file}", "w") as f:
                json.dump(shopping_list, f, indent=4);
            print("Votre liste à bien été vidé !")
        case "5":
            print("A bientôt !");
            exit();
        case _:
            print("Ce choix n'existe pas ! ");

