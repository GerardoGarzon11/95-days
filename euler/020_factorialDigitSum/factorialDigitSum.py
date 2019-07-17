def factorialDigitSum(number):
	factorial_number = 1

	for x in range(number, 0, -1):
		factorial_number *= x

	number_as_list = list(str(factorial_number))

	return sum([int(digit) for digit in number_as_list])

print(factorialDigitSum(int(input())))
