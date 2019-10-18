for i in range(int(input())):
	string = input()
	val = int(string[1:])
	for x in range(len(string)):
		temp = int(string[:x] + string[x+1:])	
		if temp < val:
			val = temp
	print(val)
