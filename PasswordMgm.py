import os

def password_mgm_menu_fr():
    while True:
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


def password_change():
    user = input("Veuillez saisir le nom de l'utilisateur pour changer le mot de passe : ")
    chPassword = os.system("passwd " + user)

def block_access():
    user = input("Veuillez saisir le nom de l'utilisateur pour bloquer l'accès : ")
    blAccess = os.system("passwd -l " + user)

def unblock_access():
    user = input("Veuillez saisir le nom de l'utilisateur pour débloquer l'accès : ")
    blAccess = os.system("passwd -u " + user)   

#English version 

def password_mgm_menu_en():
    while True:
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



def password_change_en():
    user = input("Please enter the name of the user to change the password : ")
    chPassword = os.system("passwd " + user)

def block_access_en():
    user = input("Please enter the name of the user to block access : ")
    blAccess = os.system("passwd -l " + user)

def unblock_access_en():
    user = input("Please enter the name of the user to unblock access : ")
    blAccess = os.system("passwd -u " + user)   