import requests, pprint
from bs4 import BeautifulSoup

url = "https://www.kali.org/tools/"#all-tools/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

cards = soup.find_all(class_ = "card")

command_details=[]

for card in cards:
	tools = card.find("ul")
	for tool in tools:
		#print(tool.prettify())
		url = tool.find_all("a")[0]["href"]
		tool_name = tool.find_all("a")[0].text.replace("\n"," ").strip()
		if "$" in tool_name:
			tool_name = tool_name.replace(" $","")
			if len(tool_name)>4:
				command_details.append({
					"Class":"Kali Tools",
					"Tool":tool_name,
					"Severity":"High",
					"Confidence":"Medium",
					"Pattern":f'*{tool_name}*',
					"Reference":url})
		#print(tool_name, url)
		#print()
		#input()
		try:
			commands = tool.find("li").find("ul")
			for command in commands:
				#print(command.prettify())
				#input()
				command_name = command.find_all("a")[0].text
				if "$" in command_name:
					command_name = command_name.replace("$ ","")
					if len(command_name)>4:
						command_details.append({
							"Class":"Kali Tools",
							"Tool":tool_name,
							"Severity":"High",
							"Confidence":"Medium",
							"Pattern":f'*{command_name}*',
							"Reference":url})
		except:
			pass
			
#pprint.pprint(command_details)

with open("kali_tools.csv", 'w') as f:
	f.write("Class,Tool,Severity,Confidence,Original_Pattern,Pattern,Reference\n")
	for command in command_details:
		f.write(f'{command["Class"]},{command["Tool"]},{command["Severity"]},{command["Confidence"]},{command["Pattern"]},{command["Pattern"]},{command["Reference"]}\n')
