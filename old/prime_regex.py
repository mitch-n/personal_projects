def is_prime_number(num):
    isprime=True
    for i in range(2,num):
        if num%i==0:
            isprime=False

    return isprime

regex_str=""

for i in range(10000):
    if is_prime_number(i):
        regex_str+="^x{"+str(i)+"}$|"

print(regex_str[:-1])
