import hashlib

for i in range(1000000, 9999999):
	
	hashed = hashed=hashlib.sha256(str(i).encode('utf-8')).hexdigest()
	if not i%100000:
		print(f'{i}:{hashed}')

