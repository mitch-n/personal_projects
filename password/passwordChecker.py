from password_utils import *
from getpass import getpass

b=True
while b:
    print("Log in to see secret\n")
    username=input("Username: ")
    password=getpass()


    if validate(username, password):
        print("\nCongratulations!\n")
        import this
        input()
        b=False
    else:
        print("\nYou are not in the system.\n")




