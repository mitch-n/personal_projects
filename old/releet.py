
mods=['a@4', 'e3', 'il1', 'o0', 's5', 'g9', 'h4']
spaces='(\s+)?'

string="If you can decode this, then you are a champion!"

regex=''
for letter in string:
	found=False
	if letter==' ':
		regex+=spaces
	else:
		for mod in mods:
			if letter in mod:
				regex+=f"[{mod}]"
				found=True
		if not found:
			regex+=letter
	regex+=spaces
			
print(regex)
	
		
