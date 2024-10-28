
import random, re

sentence="So she was considering in her own mind whether the pleasure of making a daisy chain would be worth the trouble of getting up and picking the daisies when suddenly a White Rabbit with pink eyes ran close by her"

scrambled=""

for word in sentence.split(' '):
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
		
	scrambled+=scrambled_word+" "
	
print(scrambled)
