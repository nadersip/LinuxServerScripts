import os

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