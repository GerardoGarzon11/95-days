import datetime

number = 600851475143
prime_numbers = [2]

def isPrime(candidate):
	for x in prime_numbers:
		if candidate % x == 0:
			return False

	prime_numbers.append(candidate)
	return True

def largestPrime(number):
	largestPrime = 1
	x = 3

	while x < number // x:
		if x % 5 != 0:
			if isPrime(x):
				if number % x == 0:
					largestPrime = x
				
		x += 2

	return largestPrime

print(datetime.datetime.now())
print(largestPrime(number))
print(datetime.datetime.now())
