import os


def password_change():
    user = input("Veuillez saisir le nom du user pour chanage le mot de passe: ")
    chPassword = os.system("passwd " + user)

def block_access():
    user = input("Veuillez saisir le nom du user pour blocker l'access: ")
    blAccess = os.system("passwd -l " + user)

def unblock_access():
    user = input("Veuillez saisir le nom du user pour deblocker l'access: ")
    blAccess = os.system("passwd -u " + user)   

