n = input('Enter a number: ')
val = int(n[1:])
for x in range(len(n)):
	temp = int(n[:x] + n[x+1:])	
	if temp < val:
		val = temp
print(val)
