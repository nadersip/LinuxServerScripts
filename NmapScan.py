import os

def network_scan():
    network = input("Veuillez saisir le réseau à scanner avec le masque, ex. : 192.168.10.0/24 : ")
    scan = os.system("nmap -sn " + network)
    print(scan)

def port_scan():
    network = input("Veuillez saisir le réseau ou host à scanner pour les ports avec masque, ex. : 192.168.10.0/24 ou 192.168.10.100 :  ")
    scan = os.system("nmap -p- " + network)
    print(scan)

def version_scan():
    network = input("Veuillez saisir l'adresse IP de la machine dont vous voulez détecter les versions : ")
    scan = os.system("nmap -p- -sV " +network)
    print(scan)

def os_scan():
    network = input("Veuillez saisir l'adresse IP de la machine dont vous souhaitez détecter le système d'exploitation : ")
    scan = os.system("nmap -O " + network)
    print(scan)

#English version


def network_scan_en():
    network = input("Please enter the network to scan with mask e.g. 192.168.10.0/24 : ")
    scan = os.system("nmap -sn " + network)
    print(scan)

def port_scan_en():
    network = input("Please enter the network to scan ports with mask, e.g., 192.168.10.0/24 :  ")
    scan = os.system("nmap -p- " + network)
    print(scan)

def version_scan_en():
    network = input("Please enter the IP address of the machine whose versions you want to detect : ")
    scan = os.system("nmap -p- -sV " +network)
    print(scan)

def os_scan_en():
    network = input("Please enter the IP address of the machine whose operating system you want to detect : ")
    scan = os.system("nmap -O " + network)
    print(scan)