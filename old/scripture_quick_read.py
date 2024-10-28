from bs4 import BeautifulSoup
import requests, sys

verses = []
filename = "quick_read.txt"
with open(filename, "w") as f:
	#f.write("# Book of Mormon Quick Read\n")
	f.write("")


for i in range(1,22 + 1):
	print(i)
	url = f"https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/{i}?lang=eng"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, features="html5lib")
	
	# Remove references
	references = soup.find_all('sup', {"class": "marker"})
	for reference in references:
		reference.extract()

	cur_verses = soup.find_all('p', {"class": "verse"})
	
	with open(filename, "a", errors="ignore") as f:
		f.write(f"# Chapter {i}\n")
		for verse in cur_verses:
			quick_verse = verse.text.split(".")[0].split("!")[0].split("?")[0].split(";")[0].strip()
			num = quick_verse.split(" ")[0]
			text = quick_verse.split(" ")[1:]
			text = " ".join(text)
			
			f.write(f"\n**{num}** {text}.\n")
	

