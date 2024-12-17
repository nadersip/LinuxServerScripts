
import os

def affiche_processus():
    print("Voici les processus en cours : ")
    processus = os.system("ps")
    print(processus)

def stop_processus():
    ps = input("Veuillez entrer le numéro du processus à terminer : ")
    stop = os.system("kill -9 " + ps)

#English version 

def affiche_processus_en():
    print("Here are the ongoing processes : ")
    processus = os.system("ps")
    print(processus)

def stop_processus_en():
    ps = input("Please enter the process ID to terminate : ")
    stop = os.system("kill -9 " + ps)