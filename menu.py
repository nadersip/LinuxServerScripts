# Welcome to the scripting project for the Linux Server course.
from UsersGroups import creat_user
from UsersGroups import creat_group
from UsersGroups import delete_user
from UsersGroups import delete_group

print("############################################################")
print("Project Owner : Nader Sipahy")
print("Owner Contact : m.sipahy99@gmail.com")
print("Date : 03/12/2024")
print("############################################################")
print("")
print("")
print("")


print("Veuillez choisir l'une des options suivantes: ")
print("Option 1 : Gestion des utilisateurs et des groupes")
print("Option 2 : Gestion des mots de passe (réinitialiser, modifier, bloquer l'accès)")
print("Option 3 : Gestion des permissions des dossiers et fichiers")
print("Option 4 : Gestion des services")
print("Option 5 : Gestion des processus")
print("Option 6 : Quitter")

option = input("Veuillez sélectionner l'une des options: ")


if option == "1":
    print("Option 1 : Créer un utilisateur")
    print("Option 2 : Créer un groupe")
    print("Option 3 : Supprimer un utilisateur")
    print("Option 4 : Supprimer un groupe")
    print("Option 5 : Quitter")
    subOption = input("Veuillez sélectionner l'une des options: ")
    if subOption == "1":
        creat_user()
    elif subOption == "2":
        creat_group()
    elif subOption == "3":
        delete_user()
    elif subOption == "4":
        delete_group()
    elif subOption == "5":
        print("Quitter")
    else:
        print ("Option invalide")

        
elif option == "2":
    print("Option 1 : Changement de mot de passe")
    print("Option 2 : Bloquer l'accès")
    print("Option 3 : Quitter")

elif option == "3":
    print("Option 1 : Afficher les permissions d'un fichier")
    print("Option 2 : Afficher les permissions d'un dossier")
    print("Option 3 : Changer les permissions d'un fichier")
    print("Option 4 : Changer les permissions d'un dossier")
    print("Option 5 : Quitter")

elif option == "4":
    print("Option 1 : Afficher le statut d'un service")
    print("Option 2 : Démarrer un service")
    print("Option 3 : Arrêter un service")
    print("Option 4 : Redémarrer un service")
    print("Option 5 : Quitter")

elif option == "5":
    print("Option 1 : Afficher les processus")
    print("Option 2 : Arrêter un processus")
    print("Option 3 : Quitter")

elif option == "6":
    print("Quitter")

else :
    print("Option invalide")