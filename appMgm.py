import os

def system_update():
    sys_update = os.system("sudo apt update && sudo apt upgrade -y")
    
def app_installation():
    app_name = input("Please enter the name of the application or tool you would like to install:")
    app_install = os.system("apt install " + app_name + " -y")

def app_deletion():
    app_name = input("Please enter the name of the application or tool you would like to delete:")
    app_delete = os.system("apt purge " + app_name + " -y")
