import os

def nmap_scan_menu_fr():
    while True:
        print("Option 1 : Scan les hosts sur le reseau ")
        print("Option 2 : Scan des port d'une machine")
        print("Option 3 : Scan les version des service des port sur une machine")
        print("Option 4 : Scan le os d'une machine")
        print("Option 5 : Quitter")
        subOption = input("Veuillez sélectionner l'une des options: ")
        if subOption == "1":
            network_scan()
        elif subOption == "2":
            port_scan()
        elif subOption == "3":
            version_scan()
        elif subOption == "4":
            os_scan()                                        
        elif subOption == "5":
            print("Quitter")
        else:
            print ("Option invalide")

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

def nmap_scan_menu_en():
    while True:
        print("Option 1 : Scan les hosts sur le reseau ")
        print("Option 2 : Scan des port d'une machine")
        print("Option 3 : Scan les version des service des port sur une machine")
        print("Option 4 : Scan le os d'une machine")
        print("Option 5 : Quitter")
        subOption = input("Veuillez sélectionner l'une des options: ")
        if subOption == "1":
            network_scan_en()
        elif subOption == "2":
            port_scan_en()
        elif subOption == "3":
            version_scan_en()
        elif subOption == "4":
            os_scan_en()                                        
        elif subOption == "5":
            print("Quitter")
        else:
            print ("Option invalide")

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