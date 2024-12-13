
import os

def affiche_processus():
    print("Voici les processus en cours : ")
    processus = os.system("ps")
    print(processus)

def stop_processus():
    ps = input("Veuillez entrer le numéro du processus à terminer : ")
    stop = os.system("kill -9 " + ps)
