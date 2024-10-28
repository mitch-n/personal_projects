import json

port_info = ""
with open("port_info.txt") as f:
	port_info = json.load(f)
	
print(len(port_info))

with open("port_lookup.csv","w", errors="ignore") as f:
	port_num = 0
	for port in port_info:
		port_num = port['port_num']
		info = port["info"]
		info = " | ".join(info).replace('"',"'")
		if info and not info == "Unassigned":
			f.write(f"{port['port_num']},\"{info}\"\n")
