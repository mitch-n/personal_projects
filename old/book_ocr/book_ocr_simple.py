from os import listdir
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
for f in listdir("."):
	if f.split(".")[-1].lower() in ("jpg","jpeg","png"):
		print(f)
		text = pytesseract.image_to_string(Image.open(f))
		print(text)
		
		print()
