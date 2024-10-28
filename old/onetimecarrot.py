import sys
message="https://servicenow.churchofjesuschrist.org/sn_si_incident.do?sys_id=79fcb8f41bf5d450b60afc43cd4bcbd3&sysparm_stack=&sysparm_view="
key='carrot'

def encode(message, key):
    #encode message
    encoded_message=''
    key_index=0
    for letter in message:
        try:
            encoded_message+=str(ord(letter)+ord(key[key_index]))+' '
        except Exception:
            pass
        if key_index<len(key)-1:
            key_index+=1
        else:
            key_index=0

    encoded_message=encoded_message[:-1]

    return encoded_message

def decode(message, key):
    #decode message
    decoded_message=''
    key_index=0
    for chunk in encoded_message.split(' '):
        try:
            decoded_message+=chr(int(chunk)-ord(key[key_index]))
        except Exception:
            pass
        
        if key_index<len(key)-1:
            key_index+=1
        else:
            key_index=0

    return decoded_message

encoded_message=encode(message, key)
#encoded_message=encode(message, key)
message=input("Message: ")
key=input("Key: ")
encoded_message=encode(message, key)
print(encoded_message)

while True:
    key=input("Key: ")
    print(decode(encoded_message, key))
    
