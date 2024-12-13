import os

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