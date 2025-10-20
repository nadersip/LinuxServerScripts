import os

def file_folder_mgm_menu_fr():
    while True:
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

def file_permission():
    fileName = input("Veuillez saisir le nom du fichier : ")
    fileLocation = input("Veuillez saisir le chemein du fichier : ")
    filePermission = os.system("ls -l " + fileLocation + "/" + fileName)
    print(filePermission)

def folder_permission():
    folderName = input("Veuillez saisir le nom du dossier: ")
    folderLocation = input("Veuillez saisir le chemein du dossier: ")
    folderPermission = os.system("ls -ld " + folderLocation + "/" + folderName)
    print(folderPermission)

def change_filepermission():
    fileName = input("Veuillez saisir le nom du fichier: ")
    fileLocation = input("Veuillez saisir le chemein du fichier: ")
    print("Voici les permissions du fichier")
    filePermission = os.system("ls -l " + fileLocation + "/" + fileName)
    print(filePermission)
    print("")
    nPermission = input("Veuillez saisir les nouvelles permissions: ")
    aPermission = os.system("chmod " + nPermission + " " + fileLocation + "/" + fileName)
    print("")
    print("Voici les nouvelles permissions sur le fichier")
    filePermission = os.system("ls -l " + fileLocation + "/" + fileName)
    print(filePermission)

def change_folderpermission():
    folderName = input("Veuillez saisir le nom du dossier: ")
    folderLocation = input("Veuillez saisir le chemein du dossier: ")
    print("Voici les permissions du dossier")
    folderPermission = os.system("ls -ld " + folderLocation + "/" + folderName)
    print(folderPermission)
    print("")
    nPermission = input("Veuillez entrer les nouvelles permissions: ")
    aPermission = os.system("chmod " + nPermission + " " + folderLocation + "/" + folderName)
    print("")
    print("Voici les nouvelles permissions sur le dossier")
    folderPermission = os.system("ls -ld " + folderLocation + "/" + folderName)
    print(folderPermission)

#English version

def file_folder_mgm_menu_en():
    while True:
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

def file_permission_en():
    fileName = input("Please enter the name of the file : ")
    fileLocation = input("Please enter the file path : ")
    filePermission = os.system("ls -l " + fileLocation + "/" + fileName)
    print(filePermission)

def folder_permission_en():
    folderName = input("Please enter the name of the folder : ")
    folderLocation = input("Please enter the folder path : ")
    folderPermission = os.system("ls -ld " + folderLocation + "/" + folderName)
    print(folderPermission)

def change_filepermission_en():
    fileName = input("Please enter the file name : ")
    fileLocation = input("Please enter the file path : ")
    print("Here are the file permissions : ")
    filePermission = os.system("ls -l " + fileLocation + "/" + fileName)
    print(filePermission)
    print("")
    nPermission = input("Please enter the new permissions : ")
    aPermission = os.system("chmod " + nPermission + " " + fileLocation + "/" + fileName)
    print("")
    print("Here are the new permissions on the file : ")
    filePermission = os.system("ls -l " + fileLocation + "/" + fileName)
    print(filePermission)

def change_folderpermission_en():
    folderName = input("Please enter the folder name : ")
    folderLocation = input("Please enter the folder path : ")
    print("Here are the folder permissions : ")
    folderPermission = os.system("ls -ld " + folderLocation + "/" + folderName)
    print(folderPermission)
    print("")
    nPermission = input("Please enter the new permissions : ")
    aPermission = os.system("chmod " + nPermission + " " + folderLocation + "/" + folderName)
    print("")
    print("Here are the new permissions on the folder : ")
    folderPermission = os.system("ls -ld " + folderLocation + "/" + folderName)
    print(folderPermission)