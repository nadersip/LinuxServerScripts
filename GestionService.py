import os

def service_status():
    nameService = input("Veuillez entrer le nom du service que vous voulez voir le status: ")
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_start():
    nameService = input("Veuillez entrer le nom du service que vous voulez demarrer: ")
    serviceStart = os.system("systemctl start " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_stop():
    nameService = input("Veuillez entrer le nom du service que vous voulez stoper: ")
    serviceStop = os.system("systemctl stop " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def service_restart():
    nameService = input("Veuillez entrer le nom du service que vous voulez demarrer: ")
    serviceRestart = os.system("systemctl restart " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)