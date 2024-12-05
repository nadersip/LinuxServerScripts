# Option 1 : Afficher le statut d'un service
# Option 2 : Démarrer un service
# Option 3 : Arrêter un service
# Option 4 : Redémarrer un service
# Option 5 : Quitter
import os

def service_status():
    nameService = input("Veuillez entrer le nom du service que vous voulez voir le status: ")
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def start_service():
    nameService = input("Veuillez entrer le nom du service que vous voulez demarrer: ")
    serviceStart = os.system("systemctl start " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def stop_service():
    nameService = input("Veuillez entrer le nom du service que vous voulez demarrer: ")
    serviceStop = os.system("systemctl stop " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)

def restart_service():
    nameService = input("Veuillez entrer le nom du service que vous voulez demarrer: ")
    serviceRestart = os.system("systemctl restart " + nameService)
    serviceStatus = os.system("systemctl status " + nameService)
    print(serviceStatus)