a=''
b=''

while not type(a) is int:
    a = input("Enter value for a: ")

    try:
        a=int(a)
    except ValueError:
        print("You did not enter a number")
        print()

while not type(b) is int:   
    b = input("Enter value for b: ")

    try:
        b=int(b)
    except ValueError:
        print("You did not enter a number")
        print()

c = a+b

print()
print(str(a)+" + "+str(b)+" = "+str(c))


















