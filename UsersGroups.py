import os

# Get users list
# Need to change the PATH of the file for users list
def get_user():
    users = os.system("cat /Users/nadersip/Downloads/user")
    print(users)

# Get groups list
# Need to change the PATH of the file for group list
def get_groups():
    groups = os.system("cat /Users/nadersip/Downloads/group")
    print(groups)

get_user()

