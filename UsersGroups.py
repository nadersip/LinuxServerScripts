import os

def user_group_menu_fr():
    while True:
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


def get_user():
    users = os.system("cat /etc/passwd | awk -F: '{print $1}' | pr -2 -t")
    print(users)

def get_groups():
    groups = os.system("cat /etc/group")
    print(groups)

def creat_group():
    grp = input("Veuillez saisir le nom du groupe à créer : ")
    creatGrp = os.system("groupadd " + grp)
    print(os.system("cat /etc/group | grep -i " + grp))

def delete_group():
    grp = input("Veuillez saisir le nom du groupe à supprimer : ")
    creatGrp = os.system("groupdel " + grp)
    print(os.system("cat /etc/group | grep -i " + grp))

def creat_user():
    user = input("Veuillez saisir le nom de l'utilisateur à créer : ")
    creatGrp = os.system("adduser " + user)
    print(os.system("cat /etc/passwd | grep -i " + user))

def delete_user():
    user = input("Veuillez saisir le nom de l'utilisateur à supprimer : ")
    creatGrp = os.system("userdel " + user)
    print(os.system("cat /etc/passwd | grep -i " + user))


#English version

def user_group_menu_en():
    while True:
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


def get_user_en():
    users = os.system("cat /etc/group")
    print(users)

def get_groups_en():
    groups = os.system("cat /etc/group")
    print(groups)

def creat_group_en():
    grp = input("Please enter the name of the group to create : ")
    creatGrp = os.system("groupadd " + grp)
    print(os.system("cat /etc/group | grep -i " + grp))

def delete_group_en():
    grp = input("Please enter the name of the group to delete : ")
    creatGrp = os.system("groupdel " + grp)
    print(os.system("cat /etc/group | grep -i " + grp))

def creat_user_en():
    user = input("Please enter the name of the user to create : ")
    creatGrp = os.system("adduser " + user)
    print(os.system("cat /etc/passwd | grep -i " + user))

def delete_user_en():
    user = input("Please enter the name of the user to delete : ")
    creatGrp = os.system("userdel " + user)
    print(os.system("cat /etc/passwd | grep -i " + user))
