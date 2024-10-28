from random import randint
from pprint import pprint
from datetime import datetime
import hashlib
import requests
import json

def real_randint(minimum=0, maximum=100):
	charmap={
		'0':0,
		'1':1,
		'2':2,
		'3':3,
		'4':4,
		'5':5,
		'6':6,
		'7':7,
		'8':8,
		'9':9,
		'a':10,
		'b':11,
		'c':12,
		'd':13,
		'e':14,
		'f':15
	}
	seed=str(datetime.now().microsecond).encode()
	seed_hash=str(hashlib.md5(seed).hexdigest())
	total=maximum
	for char in seed_hash:
		total+=charmap[char]
	return total%(maximum+1)

def test_real_randint(minimum=0, maximum=100, iterations=1000):
	results={}
	for i in range(minimum, maximum+1):
		results[i]=0
	
	for iters in range(iterations):
		results[real_randint()]+=1
	
	for key,val in results.items():
		print(f"{key}: {((val/iterations)*100):.2f}%")

def test_randomorg(minimum=0, maximum=100, iterations=1000):
	s=requests.session()
	
	results={}
	for i in range(minimum, maximum+1):
		results[i]=0
		
	all_nums=[]
	for i in range(int(iterations/9999)):	#Random.org api only allows 10000 nums at a time
		print(i)
		data={
			"jsonrpc": "2.0",
			"method": "generateIntegers",
			"params": {
				"apiKey": "f4be1b78-0980-4d02-88a1-9424ff6ac1a4",
				"n": iterations,
				"min": minimum,
				"max": maximum,
				"replacement": True
			},
			"id": 42
		}
		
		s.headers['content-type']="application/json"
		api_results=s.post("https://api.random.org/json-rpc/4/invoke", data=json.dumps(data))
		print(api_results,api_results.text)
		all_nums+=api_results.json()['result']['random']['data']
	#print(api_results,api_results.text)
	
	for num in all_nums:
		results[real_randint()]+=1
	
	for key,val in results.items():
		print(f"{key}: {((val/iterations)*100):.2f}%")

def test_std_randint(minimum=0, maximum=100, iterations=1000):
	results={}
	for i in range(minimum, maximum+1):
		results[i]=0
	
	for iters in range(iterations):
		results[randint(minimum, maximum)]+=1
	
	for key,val in results.items():
		print(f"{key}: {((val/iterations)*100):.2f}%")

iterations=10000

print("STD Test")
test_std_randint(iterations=iterations)

print()
print("New Test")
test_real_randint(iterations=iterations)

print()
print("Random.org")
test_randomorg(iterations=iterations)

#print(real_randint())

























