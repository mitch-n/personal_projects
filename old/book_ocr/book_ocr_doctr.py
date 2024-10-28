from os import listdir
from doctr.documents import read_img

for f in listdir("."):
	if f.split(".")[-1].lower() in ("jpg","jpeg","png"):
		print(f)
		page = read_img(f)
		print(page)
		print()
