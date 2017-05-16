count=0
for i in range(1000):
	if i%3==0:
		count+=i
	elif i%5==0:
		count+=i
print("The sum of all the multiples of 3 or 5 below 1000 is " + str(count))