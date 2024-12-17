import os

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

def password_change_en():
    user = input("Please enter the name of the user to change the password : ")
    chPassword = os.system("passwd " + user)

def block_access_en():
    user = input("Please enter the name of the user to block access : ")
    blAccess = os.system("passwd -l " + user)

def unblock_access_en():
    user = input("Please enter the name of the user to unblock access : ")
    blAccess = os.system("passwd -u " + user)   