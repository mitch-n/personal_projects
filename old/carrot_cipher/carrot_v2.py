def iterate_word(start_pos, word):
    if not len(word)%2:
        word=word[:-1]
    
    if start_pos>len(word):
        start_pos=start_pos%len(word)

    new_word=''
    i=start_pos
    for counter in range(int(len(word)/2)):
        if i>=len(word):
            i=i%len(word)
        new_word+=word[i]
        i+=2
    
    return new_word
        
def encode(message, key):
    #encode message
    encoded_message=''

    key_iterator=0
    for letter_a in message:
        for letter_b in iterate_word(key_iterator,key):
            letter_a=chr(ord(letter_a)^ord(letter_b))

        encoded_message+=str(ord(letter_a))+" "
        key_iterator+=1

    encoded_message=encoded_message[:-1]

    return encoded_message

def decode(message, key):
    #decode message
    decoded_message=''

    key_iterator=0
    for letter_a in message.split(" "):
        letter_a=int(letter_a)
        for letter_b in iterate_word(key_iterator,key):
            letter_a=(letter_a^ord(letter_b))

        decoded_message+=str(chr(letter_a))
        key_iterator+=1

    return decoded_message

if __name__=="__main__":
    #encoded_message=encode(message, key)
    message=input("Message: ")
    key=input("Key: ")
    encoded_message=encode(message, key)
    print(encoded_message)

    for char in encoded_message.split(' '):
        print(chr(int(char)), end='')

    print()

    while True:
        key=input("Key: ")
        print(decode(encoded_message, key))
    
