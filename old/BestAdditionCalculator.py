import math

def get_int(prompt):
    num=''
    while not type(num) is int:
        num = input(prompt)

        try:
            num=int(num)
        except ValueError:
            print("You did not enter a number")
            print()
    return num
    
while True:
    a=get_int("Enter value for a: ")
    b=get_int("Enter value for b: ")

    c = math.sqrt(pow(a,2)+pow(b,2))

    print()
    #print(str(a)+"^2 + "+str(b)+"^2 = "+str(c)+"^2")
    print("%d^2 + %d^2 = %.2f^2" % (a,b,c))

    print()
    again=input("Run again? Y/n")

    if again.lower()=='n':
        break

















