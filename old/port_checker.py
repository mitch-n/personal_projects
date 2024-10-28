import requests, pyperclip, re, unicodedata
from bs4 import BeautifulSoup
s=requests.session()
s.verify=False
s.headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"

class PortObject:
	def __init__(self, number, name, purpose, desc):
		self.number=number
		self.name=name
		self.purpose=purpose
		self.desc=desc
		
	def all_info(self):
		return f"Port {self.number}\nName: {self.name}\nPurpose: {self.purpose}\nDesc: {self.desc}\n"

port_objects=[]

ports=pyperclip.paste().split("\n")
print(ports)

i=0
for port in ports:
	port=port.strip()
	print(f"Port {port}: {i}/{len(ports)}")
	i+=1
	response=s.get(f"https://www.grc.com/port_{port}.htm")
	soup=BeautifulSoup(response.text, features="html.parser")
	#print(soup.text)
	clean_text=unicodedata.normalize("NFKD",soup.text)
	match=re.search("Name: (?P<name>[^\n]*)\nPurpose: (?P<purpose>[^\n]*)\nDescription: (?P<desc>[^\n]*)", clean_text)
	#match=re.search("Name: (?P<name>[^\n]*)", clean_text)
	#print(match.group("name"))
	#print(match.group("purpose"))
	#print(match.group("desc"))
	try:
		port_objects.append(PortObject(port,match.group("name"),match.group("purpose"),match.group("desc")))
	except Exception:
		port_objects.append(PortObject(port,"not found","not found","not found"))
		
print("------------------\n")

for port_object in port_objects:
	print(port_object.all_info())
