prime_numbers = [2]

def isPrime(candidate):
	for x in prime_numbers:
		if candidate % x == 0:
			return False
		if x*x > candidate:
			break

	prime_numbers.append(candidate)
	return True

def findPrimeSum(maximum):
	candidate = 3
	while candidate < maximum:
		if candidate % 5 != 0 or candidate == 5:
			isPrime(candidate)
		candidate += 2

	return sum(prime_numbers)

response = findPrimeSum(int(input()))

print(response)
