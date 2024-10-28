import sys
message="https://servicenow.churchofjesuschrist.org/sn_si_incident.do?sys_id=79fcb8f41bf5d450b60afc43cd4bcbd3&sysparm_stack=&sysparm_view="
pubkey='carrot'
prikey='private carrot'

def encode(message, pubkey, prikey):
    #encode message
    encoded_message=''
    pubkey_index=0
    prikey_index=0
    for letter in message:
        try:
            encoded_message+=str(ord(letter)+ord(pubkey[key_index])^ord(prikey[prikey_index]))+' '
        except Exception:
            pass
        
        if pubkey_index<len(pubkey)-1:
            pubkey_index+=1
        else:
            key_index=0
        if prikey_index<len(prikey)-1:
            prikey_index+=1
        else:
            prikey_index=0

    encoded_message=encoded_message[:-1]

    return encoded_message

def decode(message, pubkey, prikey):
    #decode message
    decoded_message=''
    key_index=0
    for chunk in encoded_message.split(' '):
        try:
            decoded_message+=chr(int(chunk)-ord(pubkey[key_index])^ord(prikey[prikey_index]))
        except Exception:
            pass
        
        if pubkey_index<len(pubkey)-1:
            pubkey_index+=1
        else:
            key_index=0
        if prikey_index<len(prikey)-1:
            prikey_index+=1
        else:
            prikey_index=0

    return decoded_message

encoded_message=encode(message, key)
print(encoded_message)
print()

while True:
    key=input("Key: ")
    print(decode(encoded_message, key))
    
