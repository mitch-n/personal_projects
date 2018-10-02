from password_utils import *
from getpass import getpass

print("To create a new user, enter a username and password:\n")
b=True
while b:
    username=input("Username: ")
    password=getpass()
    password_conf=getpass(prompt='Confirm Password: ')

    if password==password_conf:
        add_user(username, password)
        b=False
    else:
        input("\nPasswords do not match. Please try again...\n")




