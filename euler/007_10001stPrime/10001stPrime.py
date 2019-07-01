import datetime

prime_numbers = [2]

def isPrime(candidate):
	for x in prime_numbers:
		if candidate % x == 0:
			return False

	prime_numbers.append(candidate)
	return True

def findPrime(numberOfPrimes):
	candidate = 3
	while len(prime_numbers) < numberOfPrimes:
		isPrime(candidate)
		candidate += 2

	return prime_numbers[-1]

print(datetime.datetime.now())
print(findPrime(int(input())))
print(datetime.datetime.now())
