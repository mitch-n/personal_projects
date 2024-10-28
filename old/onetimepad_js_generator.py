from random import randint, choice
letters=r'abcdefghijklmnopqrstuvwxyz'
code={}

for letter in letters:
    while True:
        value=choice(letters)
        if value not in code.values():
            code[letter]=value
            break


print("function encode(a){")
print("\ta=a.toLowerCase();")
for key, value in code.items():
    print (f"\ta=a.replace(/{key}/g,'{value}');")
print("\treturn a;\n}")

print("function decode(a){")
for key, value in code.items():
    print (f'\ta=a.replace(/{value}/g,"{key}");')
print("\treturn a;\n}")

