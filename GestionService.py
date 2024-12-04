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