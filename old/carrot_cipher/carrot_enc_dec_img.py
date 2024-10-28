import hashlib

def numpad(num, length):
    """
    Returns a string
    """
    num=str(num)
    pad_num='0'*(len(num)%length-1)+num
    #print(pad_num)
    
    return pad_num

def str2val(string):
    val_str=''
    for letter in string:
        val=str(ord(letter))
        val_str+=numpad(val,3)
        
    return val_str

def val2str(num):
    string=''
    num=str(num)
    num='0'*(len(num)%3-1)+num
    start=0
    end=3
    while end <= len(num):
        chunk=int(num[start:end])
        string+=str(chr(int(num[start:end])))
        start+=3
        end+=3
    return string

def decode(master, secret):
    master=hashlib.sha256(str.encode(master)).hexdigest()
    master_ord=str2val(master)
    secret_ord=int(secret)
    
    master_chunks=[]
    start=0
    end=3

    while end <= len(master_ord):
        master_chunks.append(int(master_ord[start:end]))
        start+=3
        end+=3

    if len(master_chunks)%2:
        add=False
    else:
        add=True
        
    for num in reversed(master_chunks):
        if add:
            secret_ord+=num
        else:
            secret_ord=secret_ord//num
        add=not add

        secret_ord=int(secret_ord)
    
    return val2str(secret_ord)
    
def encode(master, secret):
    master=hashlib.sha256(str.encode(master)).hexdigest()
    master_ord=str2val(master)
    secret_ord=int(str2val(secret))
    
    master_chunks=[]
    start=0
    end=3

    while end <= len(master_ord):
        master_chunks.append(int(master_ord[start:end]))
        start+=3
        end+=3

    #print(secret_ord)
    sub=False
    for num in master_chunks:
        if sub:
            secret_ord-=num
        else:
            secret_ord*=num
        sub=not sub
    return secret_ord

file=input("Which file would you like to encrypt: ")
master=input("Create Master Password: ")
secret=''
with open(file,'rb') as f:
    for line in f.readlines():
        #print(line)
        secret+=str(line).strip+'\n'

encoded=encode(master, secret)
print()
print("Encoded Message:")
#print(encoded)

while True:
    print()
    master=input("Type Master Password: ")
    print()
    print("Writing File")
    #print(decode(master, encoded))
    with open(r'C:\Users\mitchell.nelson\Documents\scripts\PythonScripts\carrot_cipher\out.png','w') as f:
        f.write(str.encode(decode(master, encoded)).decode('utf-8'))

    print("Complete")



