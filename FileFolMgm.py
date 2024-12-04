#Afficher les permissions d'un fichier
#Option 2 : Afficher les permissions d'un dossier
#Option 3 : Changer les permissions d'un fichier
#Option 4 : Changer les permissions d'un dossier
#Option 5 : Quitter

import os

def file_permission():
    fileName = input("Veuillex saisir le nom du fichier: ")
    fileLocation = input("Veuillez entrer le chemein du fichier: ")

    