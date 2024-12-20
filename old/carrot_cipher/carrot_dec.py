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

if __name__=="__main__":
    encoded=input("Paste encoded message: ")
    while True:
        print()
        master=input("Type Master Password: ")
        print()
        print(decode(master, encoded))



