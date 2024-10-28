import requests, json
from bs4 import BeautifulSoup

ports = []

port_info=""

for port in range(49151):
	print(port)
	response = requests.get(f"https://wintelguy.com/port-search/{port}")
	soup = BeautifulSoup(response.text, 'html.parser')

	row_num = 0
	services = set([])
	descriptions = set([])
	info = set([])
	for row in soup.find_all('tr'):
		if row_num > 0:
			items = row.find_all('td')
			service = items[0].text.strip()
			description = items[3].text.strip()
			if service:
				services.add(service)
			if description:
				descriptions.add(description)
			if service or description:
				info.add(f"{'['+str(service)+'] ' if service else ''}{description}")
		row_num+=1
		
	port_info={
		"port_num": port,
		"services": list(services),
		"descriptions": list(descriptions),
		"info": list(info)
	}

	#print(ports)
	with open("port_info.txt", "a") as f:
		f.write(json.dumps(port_info, indent=2))
		f.write(",")
		f.write("\n")
	
	
