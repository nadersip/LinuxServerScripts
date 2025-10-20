# Welcome to the scripting project for the Linux Server course.
from UsersGroups import user_group_menu_fr, user_group_menu_en
from PasswordMgm import password_mgm_menu_fr, password_mgm_menu_en
from FileFolMgm import file_folder_mgm_menu_fr, file_folder_mgm_menu_en
from GestionService import service_mgm_menu_fr, service_mgm_menu_en
from ProcessusMgm import processus_mgm_menu_fr, processus_mgm_menu_en
from appMgm import app_installation, app_deletion, system_update
from NmapScan import nmap_scan_menu_fr, nmap_scan_menu_en


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
        print("Option 6 : Scan nmpa")
        print("Option 7 : Quitter")

        option = input("Veuillez sélectionner l'une des options: ")

        while True:
            if option == "1":
                user_group_menu_fr()

            elif option == "2":
                password_mgm_menu_fr()

            elif option == "3":
                file_folder_mgm_menu_fr()

            elif option == "4":
                service_mgm_menu_fr()

            elif option == "5":
                processus_mgm_menu_fr()

            elif option == "6":
                nmap_scan_menu_fr()
            elif option == "7":
                break
        if option == "7":
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
                user_group_menu_en()

            elif option == "2":
                password_mgm_menu_en()

            elif option == "3":
                file_folder_mgm_menu_en()   

            elif option == "4":
                service_mgm_menu_en()

            elif option == "5":
                processus_mgm_menu_en
                
            elif option == "6":
                nmap_scan_menu_en
                
            elif option == "7":
                break
        if option == "7":
            break        
