import hashlib

chars=list("0123456789")


passes=[]

password=""
i=0
for char1 in chars:
	for char2 in chars:
		for char3 in chars:
			for char4 in chars:
				for char5 in chars:
					for char6 in chars:
						for char7 in chars:
							if not i%100000:
								print(i)
							i+=1
							password=f"{char1}{char2}{char3}{char4}{char5}{char6}{char7}"
							#print(password)
							passes.append(password)
							
	
"""
with open('7digitpasses.txt', 'w') as f:					
	for password in passes:
		f.write(f"{password}\n")
"""
hashes=[]
i=0
for password in passes:
	hashed=hashlib.sha256(password.encode('utf-8')).hexdigest()
	hashes.append(f"{hashed}:{password}")
	if not i%100000:
		print(i)
	i+=1
	
"""
with open('7digithashes.txt', 'w') as f:					
	for hashed in hashes:
		f.write(f"{hashed}\n")
"""

matched_hashes=[]
for hashed in hashes:
	#print(hashed[0:10])
	if hashed[0:11]=="add87082ca6":
		matched_hashes.append(hashed)

"""
with open('7digitmatchedhashes.txt', 'w') as f:					
	for hashed in matched_hashes:
		f.write(f"{hashed}\n")
"""

for hashed in matched_hashes:
	print(hashed)
