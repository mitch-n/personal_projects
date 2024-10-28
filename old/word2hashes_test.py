import hashlib

chunk_size=1

word = "ZmxhZ3tjYW50X2RlaGFzaF9hX2hhc2h9"

for i in range(0,len(word),chunk_size):
	#print(word[i:i+3])
	print(hashlib.md5(word[i:i+chunk_size].encode('utf-8')).hexdigest())
