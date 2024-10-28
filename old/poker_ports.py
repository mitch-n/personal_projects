
# 3, 4, 5 of a kind
def kind(nums):
	if len(nums)>2 and min(nums)==max(nums):
		return True
	return False
		

# runs, reverse runs (1,2,3,4,5, 5,4,3,2,1)
def run(nums):
	is_run=True
	for i in range(len(nums)-1):
		if int(nums[i])+1!=int(nums[i+1]):
			is_run=False
	
	if not is_run:
		is_run=True
		for i in range(len(nums)-1):
			if int(nums[i])-1!=int(nums[i+1]):
				is_run=False
	
	return is_run
	
def skip(nums):
	if len(nums)==4 and nums[0]==nums[2] and nums[1]==nums[3]:
		return True
	if len(nums)==5 and nums[0]==nums[2]==nums[4] and nums[1]==nums[3]:
		return True
	
	
# LEET Ports (1337)
def leet(port):
	if port in [1337,31337]:
		return True
	return False
	

def do_log(port):
	nums=list(str(port))
	if len(nums)>3 and (kind(nums) or run(nums) or leet(port) or skip(nums)):
		return True
	return False

poker_ports=[]
for port in range(1,65535):
	if do_log(port):
		poker_ports.append(port)
		#print(port, end=", ")
		
print(len(poker_ports))
print()
print(poker_ports)

