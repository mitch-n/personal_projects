import msvcrt

while True:
	try:
		key = msvcrt.getch()
		if key == b'\r':
			key = "<ENTER>"
		elif key == b'\x08':
			key = "<BACK>"
		else:
			key = key.decode('utf-8')
		
		print(key, end="", flush=True)
	except Exception as e:
		#print(e)
		pass
		
