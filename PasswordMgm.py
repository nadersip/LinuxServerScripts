#Option 1 : Changement de mot de passe
#Option 2 : Bloquer l'accès
#Option 3 : Quitter

import os


def password_change():
    user = input("Veuillez saisir le nom du user pour chanage le mot de passe: ")
    chPassword = os.system("passwd " + user)

def block_access():
    user = input("Veuillez saisir le nom du user pour blocker l'access: ")
    blAccess = os.system("passwd -l " + user)

