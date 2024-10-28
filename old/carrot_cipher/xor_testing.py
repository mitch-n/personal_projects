from __future__ import print_function, unicode_literals
from os import urandom


def str2nums(elem):
    output=''
    for char in elem:
        output+=str(ord(char))

    return output

def nums2str(elem):
    output=''
    elem=str(elem)
    i=0
    while i < len(elem):
        output+=chr(int(elem[i]+elem[i+1]))
        i+=2

    return output
        
    

def encode(message, key):
    """xor two strings together."""
    # Text strings contain single characters
    message=str2nums(message)
    key=str2nums(key)
    
    for num in key:
        message=int(message) ^ int(num)

    return message

def decode(message, key):
    """xor two strings together."""
    # Text strings contain single characters
    key=str2nums(key)
    
    for num in key:
        message=int(message) ^ int(num)

    return nums2str(message)


message = 'This is a secret message'
print('Message:', message)

key = 'carrot'
print('Key:', key)

encoded=encode(message, key)
print(encoded)

print(decode(encoded, key))
