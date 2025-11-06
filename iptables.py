import os

def block_input_fr():
    protocol = input("Please enter the proctocol : ")
    source = input("Please enter the IP or Network address of the manchine or network you would like to block: ")
    destinatination=  input("Please enter the IP or network of the destination: ")
    source_port= input("Please enter the source port: ")
    destinatination_port = input("please enter the destination port: ")
    action = input ("please enter the action (ACCEPT, DROP, REJECT): ")
    rule = os.system("iptables -A INPUT " + "-p " + protocol + "-s " + source_port + "-d " + destinatination + "--dport " + destinatination_port + "-j " + action)
    print(rule)

block_input_fr()