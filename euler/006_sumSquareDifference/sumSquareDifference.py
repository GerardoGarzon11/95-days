def squareOfTheSum(number):
	theSum = sum([x for x in range(1, number + 1)])
	return theSum * theSum

def sumOfSquares(number):
	return sum([x*x for x in range (1, number + 1)])

def sumSquareDifference(number):
	return abs(sumOfSquares(number) - squareOfTheSum(number))

number = int(input())

print(sumSquareDifference(number))
