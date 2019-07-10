#!/bin/python3

import sys

divisorsArray = []

def setDivisorsArray(number):
    for x in range(1, number+1):
        divisorsArray.append(x)

def divisibleByAll(number):
    for x in divisorsArray:
        if number % x != 0:
            return False

    return True

def smallestMultiple(number):
    smallestMultiple = -1
    candidate = number

    setDivisorsArray(number)

    while smallestMultiple == -1:
        if divisibleByAll(candidate):
            smallestMultiple = candidate

        candidate += number

    return smallestMultiple

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    divisorsArray = []
    print(smallestMultiple(n))
