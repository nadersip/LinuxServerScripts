#Option 1 : Afficher les processus
#Option 2 : Arrêter un processus
#Option 3 : Quitter

import os

def affiche_processus():
    print("Voici les processus qui sont en cours: ")
    processus = os.system("ps")
    print(processus)

def stop_processus():
    ps = input("Veuillez entrer le numero du processus a terminer: ")
    stop = os.system("kill -9 " + ps)
