#!/bin/python3

prime_numbers = [2, 3]

def isPrime(number):
    if number in prime_numbers:
        return False

    for x in prime_numbers:
        if number % x == 0:
            return False
        if x * x > number:
            break

    return True


def nthPrime(number):
    if len(prime_numbers) >= number:
        return prime_numbers[number - 1]

    candidate = prime_numbers[len(prime_numbers) - 1]
    found = False

    while not found:
        if candidate % 5 != 0 or candidate == 5:
            if isPrime(candidate):
                prime_numbers.append(candidate)

        if len(prime_numbers) == number:
            break

        candidate += 2

    return prime_numbers[number - 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(nthPrime(n))
