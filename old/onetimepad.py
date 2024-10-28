import sys
message="a super secret sort of long message"
key='a slightly better key'

def encode(message, key):
    #encode message
    encoded_message=''
    key_index=0
    for letter in message:
        encoded_message+=str(ord(letter)^ord(key[key_index]))+'^'
        if key_index<len(key)-1:
            key_index+=1
        else:
            key_index=0
    encoded_message=encoded_message[:-1]

    #print(encoded_message)
    return encoded_message

#sys.exit()

def decode(message, key):
    #decode message
    decoded_message=''
    key_index=0
    for chunk in encoded_message.split('^'):
        decoded_message+=chr(int(chunk)^ord(key[key_index]))
        if key_index<len(key)-1:
            key_index+=1
        else:
            key_index=0
            
    #print(decoded_message)
    return decoded_message

encoded_message=encode(message, key)

while True:
    key=input("Key: ")
    print(decode(encoded_message, key))
    
