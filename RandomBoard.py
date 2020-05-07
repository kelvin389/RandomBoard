import random

def print2DArray(array):
	for i in range(len(array)):
		for j in range(len(array[0])):
			print(array[i][j], " ", end="")
		print()

def findSum(array):
	sum = 0

	for i in range(len(array)):
		for j in range(len(array[0])):
			sum += array[i][j]
	return sum



arr = [[0 for x in range(10)] for y in range(10)]

for i in range(10):
	for j in range(10):
		arr[i][j] = random.randint(0, 9)

print2DArray(arr)
print(findSum(arr))