import os

def get_user():
    users = os.system("cat /etc/passwd | awk -F: '{print $1}' ")
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
