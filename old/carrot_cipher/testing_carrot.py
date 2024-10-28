import carrot

while True:
    message=input("Type Message: ")
    master =input("Create Password: ")

    message_encoded=str(carrot.encode(master, message))

    print(message_encoded)

    print()

    print("Messge Length: "+str(len(message)))
    print("Enc Message length: "+str(len(message_encoded)))
    print(int((len(message)/len(message_encoded))*100))
    print()
