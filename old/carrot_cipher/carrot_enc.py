import hashlib

def numpad(num, length):
    """
    Returns a string
    """
    num=str(num)
    pad_num='0'*(len(num)%length-1)+num
    
    return pad_num

def str2val(string):
    val_str=''
    for letter in string:
        val=str(ord(letter))
        val_str+=numpad(val,3)
        
    return val_str
    
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

if __name__=="__main__":
    secret=input("Type your secret message: ")
    master=input("Create Master Password: ")

    encoded=encode(master, secret)
    print()
    print("Encoded Message:")
    print(encoded)

    input()


