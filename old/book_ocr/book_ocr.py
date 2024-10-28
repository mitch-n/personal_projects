from os import listdir
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
for f in listdir("."):
	if f.split(".")[-1].lower() in ("jpg","jpeg","png"):
		print(f)
		im = Image.open(f)
		im = im.filter(ImageFilter.MedianFilter())
		enhancer = ImageEnhance.Contrast(im)
		im = enhancer.enhance(2)
		im = im.convert('1')
		enhanced_file_name = (f"enhanced_{f}")
		im.save(enhanced_file_name)
		text = pytesseract.image_to_string(Image.open(enhanced_file_name))
		print(text)
		
		print()
