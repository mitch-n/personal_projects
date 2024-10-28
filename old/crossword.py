import random, requests, os
from math import sqrt

def shallow_copy_2level_array(orig_array):
	new_array=[]
	
	for row in orig_array:
		new_array.append(row.copy())

	return new_array	

def gen_crossword():
	letters="abcdefghijklmnopqrstuvwxyz"

	words=requests.get("https://random-word-api.herokuapp.com/word?number=10&swear=0").json()
	#input(words)

	#words=[
	#	"melon",
	#	"basket",
	#	"limes",
	#	"lemon",
	#	"grapes",
	#	"icecream",
	#	"snacks",
	#	"candy",
	#	"ramen",
	#	"venison"
	#]

	density=2.5
	total_letters=0
	for word in words:
		total_letters+=len(word)
	
	size=int(sqrt(total_letters*density))
	if size<len(max(words)):
		size=len(max(words))+2

	width=size
	height=size

	letter_array=[]
	overlay_array=[]

	for w in range(width):
		letter_array.append([])
		overlay_array.append([])
		for h in range(height):
			letter_array[w].append(random.choice(letters))
			#letter_array[w].append(".")
			overlay_array[w].append(0)
			
	#for line in letter_array:
	#	print(line)
	#print()
	#for line in overlay_array:
	#	print(line)
		

	
	for word in words:
		fits=False
		total_failure=0
		#print(word)
		while not fits:
			if total_failure>100:
				raise Exception('Too many attempts to generate crossword') 
			fits=True
			horizontal=random.randint(0,10)%2
			
			if horizontal:
				x=random.randint(0,width-len(word)-1)
				y=random.randint(0,height-1)
			else:
				x=random.randint(0,width-1)
				y=random.randint(0,height-len(word)-1)
				
			index_history=[]
			temp_array=shallow_copy_2level_array(letter_array)
			temp_overlay=shallow_copy_2level_array(overlay_array)
			for letter in word:
				index_history.append((x,y))
				if not temp_overlay[x][y] or overlay_array[x][y]==letter:
					temp_array[x][y]=letter
					temp_overlay[x][y]=1
				else:
					fits=False
					#print("failed")
					break
				
				if horizontal:
					x+=1
				else:
					y+=1
				
			if fits:
				#print("adding",word)
				letter_pointer=0
				for index in index_history:
					letter_array[index[0]][index[1]]=word[letter_pointer]
					overlay_array[index[0]][index[1]]=1
					letter_pointer+=1
					
	#for line in overlay_array:
	#	for letter in line:
	#		print(letter,end=" ")
	#	print()
	#print()
	print()
	for line in letter_array:
		print(end="    ")
		for letter in line:
			print(letter,end=" ")
		print()
	print()
	for word in words:
		print("    "+word)
	print()
		
while True:
	try:
		os.system("cls")
	except Exception:
		os.system("clear")
	try:
		gen_crossword()
		input()
	except Exception:
		pass

