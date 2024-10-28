import re
from statistics import median

def string_similarity(s1,s2,recurse=True):
	s1=s1.strip().lower()
	s2=s2.strip().lower()
	
	s1_letters=re.findall(".",s1)
	s2_letters=re.findall(".",s2)

	hits=0
	for letter in s2_letters:
		if letter in s1_letters:
			hits+=1
			s1_letters.remove(letter)
	
	similarity=(hits/len(s2))*100
	
	if not recurse:
		return similarity
	else:
		#print(f"{s1}\n{s2}")
		similarity=median([similarity,string_similarity(s2,s1,recurse=False)])
		#print("%.2f%%"%similarity)
		#print()
		return similarity

while False:
	s1=input("s1: ")
	s2=input("s2: ")
	sim=string_similarity(s1,s2)
	print(sim)
	if  sim >= 80:
		print(True)
	else:
		print(False)
	print()

words=[]
with open(r'C:\Users\nelson66t\Documents\misc\words.txt') as f:
	for word in f.readlines():
		words.append(word.strip())
		#print(word)
		

#words=list(set(words))

i=0
while i<len(words):
	j=i
	while j<len(words):
		sim = string_similarity(words[i],words[j])
		#print("%s %s %.2f%"%(words[i],words[j],sim))
		if  sim >= 100 and words[i]!=words[j] and len(words[i])>3:
			print("%s %s %.2f%%"%(words[i],words[j],sim))
			with open("matching_words.txt",'a') as f:
                                f.write("%s %s %.2f%%\n"%(words[i],words[j],sim))
		j+=1
	i+=1



	
	
	
	
