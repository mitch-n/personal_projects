import random

colors=[]
with open('colors.txt', 'r') as f:
	for line in f.readlines():
		colors.append(line.strip())

with open('colors.csv', 'w') as f:
	f.write("color,length\n")
	for color in colors:
		f.write(f"{color},{len(color)}\n")


















#colors=["red", "blue", "orange", "burgandy", "yellow", "sissors", "gray", "cyan", "hot pink", "maroon", "green", "brown", "black", "dark black", "sun yellow"]
#colors=["red", "blue", "orange"]
##with open('colors.txt', 'w') as f:
#	for color in colors:#
#		f.write(color+"\n")

#with open('colors.txt', 'a') as f:
#	f.write("charcoal\n")
#	f.write("rose\n")
