import os

# Get users list
# Need to change the PATH of the file for users list
def get_user():
    users = os.system("cat /etc/group")
    print(users)

# Get groups list
# Need to change the PATH of the file for group list
def get_groups():
    groups = os.system("cat /etc/group")
    print(groups)

def creat_group():
    grp = input("Veuillez saisir le nom du groupe a creer: ")
    creatGrp = os.system("groupadd " + grp)
    print(os.system("cat /etc/group | grep -i " + grp))

def delete_group():
    grp = input("Veuillez saisir le nom du groupe a supprimer: ")
    creatGrp = os.system("groupdel " + grp)
    print(os.system("cat /etc/group | grep -i " + grp))

def creat_user():
    user = input("Veuillez saisir le nom du user a creer: ")
    creatGrp = os.system("adduser " + user)
    print(os.system("cat /etc/passwd | grep -i " + user))

def delete_user():
    user = input("Veuillez saisir le nom du user a supprimer: ")
    creatGrp = os.system("userdel " + user)
    print(os.system("cat /etc/passwd | grep -i " + user))



