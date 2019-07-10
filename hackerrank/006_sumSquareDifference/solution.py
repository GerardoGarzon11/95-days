#!/bin/python3

def sumOfSquares(n):
    return sum([x*x for x in range(1, n+1)])

def squareOfSum(n):
    sum_ = sum([x for x in range(1, n +1)])
    return sum_ * sum_

def sumSquareDifference(n):
    return squareOfSum(n) - sumOfSquares(n)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumSquareDifference(n))
