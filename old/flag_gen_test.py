from random import randint

multiplier = 32993
flag = randint(10000,90000)*multiplier

print("flag{"+str(flag)+"}")

print(flag%multiplier)
