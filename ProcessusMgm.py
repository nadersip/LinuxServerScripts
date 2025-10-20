
import os

def processus_mgm_menu_fr():
    while True:
        print("Option 1 : Afficher les processus")
        print("Option 2 : Arrêter un processus")
        print("Option 3 : Quitter")
        subOption = input("Veuillez sélectionner l'une des options: ")
        if subOption == "1":
            affiche_processus()
        elif subOption == "2":
            affiche_processus()
            stop_processus()
        elif subOption == "3":
            print("Quitter")
        else:
            print ("Option invalide")

def affiche_processus():
    print("Voici les processus en cours : ")
    processus = os.system("ps")
    print(processus)

def stop_processus():
    ps = input("Veuillez entrer le numéro du processus à terminer : ")
    stop = os.system("kill -9 " + ps)

#English version 

def processus_mgm_menu_en():
    while True:
        print("Option 1: Display processes")
        print("Option 2: Stop a process")
        print("Option 3 : Exit")
        subOption = input("Please select one of the options : ")
        if subOption == "1":
            affiche_processus_en()
        elif subOption == "2":
            affiche_processus_en()
            stop_processus()
        elif subOption == "3":
            print("Exit")
            break
        else:
            print ("Invalid option")

def affiche_processus_en():
    print("Here are the ongoing processes : ")
    processus = os.system("ps")
    print(processus)

def stop_processus_en():
    ps = input("Please enter the process ID to terminate : ")
    stop = os.system("kill -9 " + ps)