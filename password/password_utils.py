def make_key(word):
    key=sum([ord(c) for c in word])
    while key-58>=65:
        key-=58
    return key

def word_scramble(word, key):
    new_word=''
    for letter in word:
        c=ord(letter)
        for i in range(key):
            if c in range(91,97):
                c=97
            if c<122:
                c+=1
            else:
                c=65
        new_word+=chr(c)
    return new_word

def user_exists(username):
    exists=False
    with open("passwd.txt") as f:
        for line in f:
            pair=line.split(':')
            if pair[0]==username.lower():
                exists=True
    return exists    

def add_user(username, password):
    key=make_key(password)
    new_password=word_scramble(password, key)

    if user_exists(username):
        print("\nUser already exists.\n")
    else:
        with open("passwd.txt",'a') as f:
            key=0
            
            f.write(username.lower()+":"+new_password+'\n')

def validate(username, password):
    valid=False

    key=make_key(password)
    new_password=word_scramble(password, key)
    
    with open("passwd.txt") as f:
        for line in f:
            pair=line.split(':')
            if pair[0]==username.lower() and pair[1].strip()==new_password:
                valid=True
    return valid





