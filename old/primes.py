from datetime import datetime
from time import sleep

def check_prime(num):
	is_prime=True
	for i in range(3,num,2):
		if num%i==0 and num!=i:
			is_prime=False
			#print("Divisible by",i)
			break
	return is_prime

def print_primes(num):
	primes=[]
	start=datetime.now()
	
	for i in range(3,num):
		if check_prime(i):
			primes.append(i)
			#print(i, end=",")
	
	print(primes)
	
	end=datetime.now()
	duration=end-start
	print()
	print(len(primes))
	print()
	print(duration)

while True:
	#print(check_prime(int(input("Num: "))))
	print_primes(int(input("Max Num: ")))
	#try:
	#	print_primes(int(input("Max Num: ")))
	#	print(check_prime(int(input("Num: "))))
	
	#except Exception:
	#	pass
	print()

#start=datetime.now()
#sleep(7)
#end=datetime.now()

#duration=end-start

#print(duration)
#print(duration.seconds, duration.microseconds)
