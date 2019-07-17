fibonacci = [1, 1]

def countDigits(number):
	return len(str(number))

def xDigitFibonacciNumber(numberOfDigits):
	if numberOfDigits == 1:
		return 1

	found = False

	while not found:
		fibonacci.append(fibonacci[len(fibonacci) - 2] + fibonacci[len(fibonacci) - 1])
		digits = countDigits(fibonacci[len(fibonacci) - 1])
		if digits == numberOfDigits:
			found = True
			break

	return len(fibonacci)

print(xDigitFibonacciNumber(int(input())))
