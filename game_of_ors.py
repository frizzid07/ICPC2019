import numpy as np

for i in range(int(input())):
	waste = int(input())
	result = []	
	lis = [int(x) for x in input().split()]
	copy = lis[:]
	happy = np.bitwise_or.reduce(np.array(lis))
	for j in range(len(lis)-1):
		val = 0
		for k in range(len(lis)):
			temp = lis[:k] + lis[k+1:]
			score = np.bitwise_or.reduce(np.array(temp))
			if score > val:
				val = score
				pos = k
		result.append(copy.index(lis[pos])+1)
		happy += val
		del lis[pos]
	result.append(copy.index(lis[0])+1)
	print(happy)
	print(*result)
