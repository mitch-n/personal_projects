import re
from statistics import median

s1="a certain string here"
s2="a very different thing I have"
s3="a CERTAIN similar sTring"
s4="You have a voicemail 5-22-23"
s5="You have a voicemail 6-13-66"

def string_similarity(s1,s2,recurse=True):
	s1=s1.strip().lower()
	s2=s2.strip().lower()
	
	s1_letters=re.findall("\D",s1)
	s2_letters=re.findall("\D",s2)
	
	s1_numbers=re.findall("\d",s1)
	s2_numbers=re.findall("\d",s2)
	
	hits=0
	for letter in s2_letters:
		if letter in s1_letters:
			hits+=1
			s1_letters.remove(letter)
	
	hits+=min(len(s1_numbers),len(s2_numbers))
	
	similarity=(hits/len(s2))*100
	
	if not recurse:
		return similarity
	else:
		#print(f"{s1}\n{s2}")
		similarity=median([similarity,string_similarity(s2,s1,recurse=False)])
		#print("%.2f%%"%similarity)
		#print()
		return similarity
	
#string_similarity(s1,s2)
#string_similarity(s1,s3)
#string_similarity(s1,s4)
#string_similarity(s1,s5)

while True:
	s1=input("s1: ")
	s2=input("s2: ")
	sim=string_similarity(s1,s2)
	print("%.2f%%"%sim)
	if  sim >= 80:
		print(True)
	else:
		print(False)
	print()



	
	
	
	
