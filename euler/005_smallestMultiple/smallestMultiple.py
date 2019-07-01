divisors = [1, 2, 3, 4, 5
			,6, 7, 8, 9, 10
			,11, 12, 13, 14, 15
			,16, 17, 18, 19, 20]

def divisibleByList(number, numberList):
	for x in numberList:
		if number % x != 0:
			return False 

	return True

def smallestMultiple():
	smallestMultiple = -1
	candidate = 20

	while smallestMultiple == -1:
		if divisibleByList(candidate, divisors):
			smallestMultiple = candidate
		candidate += 20

	print(smallestMultiple)

smallestMultiple()
