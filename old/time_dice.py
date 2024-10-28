from datetime import datetime
import random

result={"Mitch":0, "Jesse":0}
random_result={"Mitch":0, "Jesse":0}
sum_result={"Mitch":0, "Jesse":0}

for i in range(1000000):
	num=datetime.now().microsecond
	if not i%10000:
		print(i)
	
	if num%2:
		#print("Jesse")
		result["Jesse"]+=1
	else:
		#print("Mitch")
		result["Mitch"]+=1
	#print()
	#input(f"Enter to run again ({i})")
	#print()
	
	
	if random.randint(0,1):
		#print("Jesse")
		random_result["Jesse"]+=1
	else:
		#print("Mitch")
		random_result["Mitch"]+=1
		
		
		
	num_list=list(str(num))
	total=0
	for num in num_list:
		total+=int(num)
	
	if total%2:
		#print("Jesse")
		sum_result["Jesse"]+=1
	else:
		#print("Mitch")
		sum_result["Mitch"]+=1
	
		

print(result)
print(random_result)
print(sum_result)

input("stop")
input("stop")
input("stop")
	

	
