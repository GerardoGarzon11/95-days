#!/bin/python3

def productOfSeries(factors):
    product = 1
    for x in factors:
        product *= x

    return product

def largestProductInASeries(series, length, consecutive):
    largest = 0

    for x in range(0, length - consecutive):
        factors = [int(digit) for digit in series[x:x+consecutive]]
        candidate = productOfSeries(factors)
        if candidate > largest:
            largest = candidate

    return largest

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(largestProductInASeries(num, n, k))
