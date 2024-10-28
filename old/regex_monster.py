import re

symbols=list("\!@#$%^&*()[]{}|`~,./<>?-=_+'\"")

def multiline_input():
	lines=[]
	done=False
	while not done:
		line=input(">> ")
		if not line:
			done=True
		else:
			lines.append(line)
	return lines

print("Enter lines you would like to match:")	
lines=multiline_input()

regex=""
for line in lines:
	for symbol in symbols:
		line=line.replace(f"{symbol}",f"\{symbol}")
	line=re.sub("\s+","\\\s+",line)
	regex+=line+"|"

print()
print("Regex:")
print(regex[:-1])
