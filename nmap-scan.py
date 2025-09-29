import os

def network_scan():
    network = input("Veuillez saisir le reseau pour scanner avec mask ex: 192.168.10.0/24 : ")
    scan = os.system("nmap -sn " + network)
    print(scan)