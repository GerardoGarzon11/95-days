#!/bin/python3

def evenFibonacciSum(top):
    if top < 3:
        return 0

    fibo = [1, 1]
    evenFibonacciSum = 0

    while fibo[0] + fibo[1] < top:
        fibo[0], fibo[1] = fibo[1], fibo[0] + fibo[1]
        if fibo[1] % 2 == 0:
            evenFibonacciSum += fibo[1]

    print(evenFibonacciSum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    evenFibonacciSum(n)
