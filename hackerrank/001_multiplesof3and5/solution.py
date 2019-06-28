#!/bin/python3

import sys

def multiplesOf3And5(number):
    # sum of multiples of 3
    maxDiv3 = (number // 3) * 3 if number % 3 != 0 else number - 3
    sumMultiplesOf3 = ((maxDiv3 + 3) * 10 // 2) * ((number - 1) // 3) // 10

    # sum of multiples of 5
    maxDiv5 = (number // 5) * 5 if number % 5 != 0 else number - 5
    sumMultiplesOf5 = ((maxDiv5 + 5) * 10 // 2) * ((number - 1) // 5) // 10

    # sum of multiples of 15
    maxDiv15 = (number // 15) * 15 if number % 15 != 0 else number - 15
    sumMultiplesOf15 = ((maxDiv15 + 15) * 10 // 2) * ((number - 1) // 15) // 10

    # add sums of multiples, subtract multiples of 15 since we already
    # counted them in the sum of multiples of 5 (and 3 too)
    total = sumMultiplesOf3 + sumMultiplesOf5 - sumMultiplesOf15
    print(total)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    multiplesOf3And5(n)
