def isDivisible(num):
	for i in range(20, 1, -1):
		if num % i != 0:
			return False
	return True

i = 45

while(True):
	if(isDivisible(i)):
		print(i)
		break
	i += 1