# Welcome to the scripting project for the Linux Server course.
from UsersGroups import creat_user, creat_group, delete_user, delete_group, creat_user_en, creat_group_en, delete_user_en, delete_group_en, get_user
from PasswordMgm import password_change, block_access, unblock_access, password_change_en, block_access_en, unblock_access_en
from FileFolMgm import file_permission, folder_permission, change_filepermission, change_folderpermission, file_permission_en, folder_permission_en, change_filepermission_en, change_folderpermission_en
from GestionService import service_status, service_start, service_stop, service_restart, service_status_en, service_start_en ,service_stop_en ,service_restart_en
from ProcessusMgm import affiche_processus, stop_processus, affiche_processus_en, stop_processus_en
from appMgm import app_installation, app_deletion, system_update



print("############################################################")
print("Project Owner : Nader Sipahy")
print("Owner Contact : m.sipahy99@gmail.com")
print("Date : 03/12/2024")
print("############################################################")
print("")
print("")
print("")

print ("Veuillez vous utiliser le script dans la langue francaise (option 1) / Would you like to use the script in english language (option 2) ")
languageOption = input("Veuillez choisir la langues de votre choix : ")
while True:



    if languageOption == "1":
        print("Veuillez choisir l'une des options suivantes: ")
        print("Option 1 : Gestion des utilisateurs et des groupes")
        print("Option 2 : Gestion des mots de passe (réinitialiser, modifier, bloquer l'accès)")
        print("Option 3 : Gestion des permissions des dossiers et fichiers")
        print("Option 4 : Gestion des services")
        print("Option 5 : Gestion des processus")
        print("Option 6 : Quitter")

        option = input("Veuillez sélectionner l'une des options: ")

        while True:
            if option == "1":
                print("Option 1 : Créer un utilisateur")
                print("Option 2 : Créer un groupe")
                print("Option 3 : Supprimer un utilisateur")
                print("Option 4 : Supprimer un groupe")
                print("Option 5 : Liste d'utilisateurs")
                print("Option 6 : Quitter")
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
                    get_user()
                elif subOption == "6":
                    print("Quitter")
                    break
                else:
                    print ("Option invalide")


            elif option == "2":
                print("Option 1 : Changement de mot de passe")
                print("Option 2 : Bloquer l'accès")
                print("Option 3 : Debloquer l'accès")
                print("Option 4 : Quitter")
                subOption = input("Veuillez sélectionner l'une des options: ")
                if subOption == "1":
                    password_change()
                elif subOption == "2":
                    block_access()
                elif subOption == "3":
                    unblock_access()
                elif subOption == "4":
                    print("Quitter")
                    break
                else:
                    print ("Option invalide")

            elif option == "3":
                print("Option 1 : Afficher les permissions d'un fichier")
                print("Option 2 : Afficher les permissions d'un dossier")
                print("Option 3 : Changer les permissions d'un fichier")
                print("Option 4 : Changer les permissions d'un dossier")
                print("Option 5 : Quitter")
                subOption = input("Veuillez sélectionner l'une des options: ")
                if subOption == "1":
                    file_permission()
                elif subOption == "2":
                    folder_permission()
                elif subOption == "3":
                    change_filepermission()
                elif subOption == "4":
                    change_folderpermission()
                elif subOption == "5":
                    print("Quitter")
                    break
                else:
                    print ("Option invalide")    


            elif option == "4":
                print("Option 1 : Afficher le statut d'un service")
                print("Option 2 : Démarrer un service")
                print("Option 3 : Arrêter un service")
                print("Option 4 : Redémarrer un service")
                print("Option 5 : Quitter")
                subOption = input("Veuillez sélectionner l'une des options: ")
                if subOption == "1":
                    service_status()
                elif subOption == "2":
                    service_start()
                elif subOption == "3":
                    service_stop()
                elif subOption == "4":
                    service_restart()
                elif subOption == "5":
                    print("Quitter")
                    break
                else:
                    print ("Option invalide") 

            elif option == "5":
                print("Option 1 : Afficher les processus")
                print("Option 2 : Arrêter un processus")
                print("Option 3 : Quitter")
                subOption = input("Veuillez sélectionner l'une des options: ")
                if subOption == "1":
                    affiche_processus()
                elif subOption == "2":
                    affiche_processus()
                    stop_processus()
                elif subOption == "3":
                    print("Quitter")
                else:
                    print ("Option invalide")
            elif option == "6":
                break
        if option == "6":
            break
   
    #English version 
    if languageOption == "2":
        print("Please choose one of the following options : ")
        print("Option 1 : User and Group Management")
        print("Option 2 : Password Management (reset, modify, block access)")
        print("Option 3 : Management of Folder and File Permissions")
        print("Option 4 : Service Management")
        print("Option 5 : Process Management")
        print("Option 6 : System Updates and Application/Tool Management")
        print("Option 7 : Exit")

        option = input("Please select one of the options:")

        while True:
            if option == "1":
                print("Option 1 : Create a user")
                print("Option 2 : Create a group")
                print("Option 3 : Delete a user")
                print("Option 4 : Delete a group")
                print("Option 5 : User list")
                print("Option 6 : Exit")
                subOption = input("Please select one of the options : ")
                if subOption == "1":
                    creat_user_en()
                elif subOption == "2":
                    creat_group_en()
                elif subOption == "3":
                    delete_user_en()
                elif subOption == "4":
                    delete_group_en()
                elif subOption == "5":
                    get_user()
                elif subOption == "6":
                    print("Exit")
                    break
                else:
                    print ("Invalid option")


            elif option == "2":
                print("Option 1 : Change password")
                print("Option 2 : Block access")
                print("Option 3 : Unblock access")
                print("Option 4 : Exit")
                subOption = input("Please select one of the options : ")
                if subOption == "1":
                    password_change_en()
                elif subOption == "2":
                    block_access_en()
                elif subOption == "3":
                    unblock_access_en()
                elif subOption == "4":
                    print("Exit")
                    break
                else:
                    print ("Invalid option")

            elif option == "3":
                print("Option 1: Display file permissions")
                print("Option 2: Display folder permissions")
                print("Option 3: Change file permissions")
                print("Option 4: Change folder permissionsns")
                print("Option 5 : Exit")
                subOption = input("Please select one of the options : ")
                if subOption == "1":
                    file_permission_en()
                elif subOption == "2":
                    folder_permission_en()
                elif subOption == "3":
                    change_filepermission_en()
                elif subOption == "4":
                    change_folderpermission_en()
                elif subOption == "5":
                    print("Exit")
                    break
                else:
                    print ("Invalid option")    


            elif option == "4":
                print("Option 1: Display the status of a service")
                print("Option 2: Start a service")
                print("Option 3: Stop a service")
                print("Option 4: Restart a service")
                print("Option 5 : Exit")
                subOption = input("Please select one of the options : ")
                if subOption == "1":
                    service_status_en()
                elif subOption == "2":
                    service_start_en()
                elif subOption == "3":
                    service_stop_en()
                elif subOption == "4":
                    service_restart_en()
                elif subOption == "5":
                    print("Quitter")
                    break
                else:
                    print ("Invalid option") 

            elif option == "5":
                print("Option 1: Display processes")
                print("Option 2: Stop a process")
                print("Option 3 : Exit")
                subOption = input("Please select one of the options : ")
                if subOption == "1":
                    affiche_processus_en()
                elif subOption == "2":
                    affiche_processus_en()
                    stop_processus()
                elif subOption == "3":
                    print("Exit")
                    break
                else:
                    print ("Invalid option")
            elif option == "6":
                print("Option 1 : System Updates")
                print("Option 2 : Application or Tool Installation")
                print("Option 3 : Application or Tool Removal")
                print("Option 4 : Exit")
                subOption = input("Please select one of the options : ")
                if subOption == "1":
                    system_update()
                elif subOption == "2":
                    app_installation()
                elif subOption == "3":
                    app_deletion()
                elif subOption == "4":
                    print("Exit")
                    break
                else:
                    print ("Invalid option")
            elif option == "7":
                break
        if option == "7":
            break        
