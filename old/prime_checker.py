primes = []

def is_prime(num):
	global primes
	if not num%2:
		return False
	if num < 2:
		return True
	for each in primes:
		if each!=num and not num%each:
			return False
	primes.append(num)
	return True
			
			
for i in range(2, 1000000):
	if is_prime(i):
		print(i, end=", ")
