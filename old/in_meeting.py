import requests, sys, time, socket
"""
webservers = []

socket.setdefaulttimeout(.1)

for i in range(10,50):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	target = f"10.0.1.{i}"
	print(target)
	
	result = s.connect_ex((target, 80))
	if result == 0:
		print("yes")
		webservers.append(target)
	s.close()

print(webservers)

for ip in webservers:
	print(ip)	
	try:
		response = requests.get(f"http://{ip}/cm?cmnd=LedPower%20{sys.argv[1]}")
		#response = requests.get(f"http://{ip}/cm?cmnd=LedPower%201", verify=False)
		if response:
			print(response.text)
			break
	except:
		pass
"""

response = requests.get(f"http://10.0.1.34/cm?cmnd=Power%20{sys.argv[1]}")
print(response.text)
time.sleep(1)
