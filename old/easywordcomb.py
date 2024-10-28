
words=[]

with open("easywords.txt") as f:
	for word in f.readlines():
		words.append(word.strip().lower())
		
print(words)

mutations=[]
for i in range(len(words)):
	print(i)
	for j in range(len(words)):
		for k in range(len(words)):
			#print(words[i],words[j],words[k])
			mutations.append((words[i],words[j],words[k]))

print(len(mutations))
			
