import random, re

def scramble(word):
	scrambled_word=word
	if len(word)>2:
		scrambled_word=word[0]
		mid_letters=list(word[1:-1])
		#print(mid_letters)
		while len(mid_letters)>0:
			letter=random.choice(mid_letters)
			#print("LETTER",letter)
			scrambled_word+=letter
			mid_letters.remove(letter)
		scrambled_word+=word[-1]
	return scrambled_word

sentence="""There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, “Oh dear! Oh dear! I shall be late!” (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge. """
scrambled=""

word=""
for letter in sentence:
	is_letter=re.search('[a-zA-Z\']',letter)
	#print(is_letter)
	if is_letter:
		word+=letter
	else:
		if word:
			scrambled+=scramble(word)
			word=""
		scrambled+=letter
print(scrambled)
	
