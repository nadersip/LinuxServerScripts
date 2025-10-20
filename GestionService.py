import os

def service_mgm_menu_fr():
    while True:
        print("Option 1 : Afficher le statut d'un service")
        print("Option 2 : Démarrer un service")
        print("Option 3 : Arrêter un service")
        print("Option 4 : Redémarrer un service")
        print("Option 5 : Quitter")
        subOption = input("Veuillez sélectionner l'une des options: ")
        if subOption == "1":
            service_status()
        elif subOption == "2":
            service_start()
        elif subOption == "3":
            service_stop()
        elif subOption == "4":
            service_restart()
        elif subOption == "5":
            print("Quitter")
            break
        else:
            print ("Option invalide") 

def service_status():
    nameService = input("Veuillez entrer le nom du service dont vous voulez voir le statut : ")
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_start():
    nameService = input("Veuillez entrer le nom du service que vous voulez démarrer : ")
    serviceStart = os.system("systemctl start " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_stop():
    nameService = input("Veuillez entrer le nom du service que vous voulez arrêter : ")
    serviceStop = os.system("systemctl stop " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_restart():
    nameService = input("Veuillez entrer le nom du service que vous voulez redémarrer : ")
    serviceRestart = os.system("systemctl restart " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

#English version

def service_mgm_menu_en():
    while True:
        print("Option 1: Display the status of a service")
        print("Option 2: Start a service")
        print("Option 3: Stop a service")
        print("Option 4: Restart a service")
        print("Option 5 : Exit")
        subOption = input("Please select one of the options : ")
        if subOption == "1":
            service_status_en()
        elif subOption == "2":
            service_start_en()
        elif subOption == "3":
            service_stop_en()
        elif subOption == "4":
            service_restart_en()
        elif subOption == "5":
            print("Quitter")
            break
        else:
            print ("Invalid option") 

def service_status_en():
    nameService = input("Please enter the name of the service whose status you want to check : ")
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_start_en():
    nameService = input("Please enter the name of the service you want to start : ")
    serviceStart = os.system("systemctl start " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_stop_en():
    nameService = input("Please enter the name of the service you want to stop : ")
    serviceStop = os.system("systemctl stop " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_restart_en():
    nameService = input("Please enter the name of the service you want to restart : ")
    serviceRestart = os.system("systemctl restart " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)