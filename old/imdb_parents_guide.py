import requests, sys
from bs4 import BeautifulSoup as bs4
s = requests.session()

s.headers = {
"Accept": "application/json, text/plain, */*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br"
}

while True:
	title = input("Title: ")

	response = s.get(f"https://v3.sg.media-imdb.com/suggestion/x/{title}.json?includeVideos=1")

	titles = []
	i = 0
	for film in response.json()["d"][:10]:
		title_id = film["id"]
		title_name = film["l"]
		titles.append(title_id)
		print(f"{i}: {title_name}")
		i += 1
	print()
	
	choice = int(input("Choice: "))
	print()
	parents_guide_link = f"https://www.imdb.com/title/{titles[choice]}/parentalguide"

	response = s.get(parents_guide_link)
	soup = bs4(response.text, features="html5lib")

	sections = soup.find_all("section")
	for section in sections:
		title = section.find(class_="ipl-list-title")
		rating = section.find(class_="ipl-status-pill")
		if title and rating:
			print(f"{title.text}: {rating.text}")
	print()
	print("-------------------")
	print()
