#!/bin/python3

import sys

def isPalindrome(number):
    numberString = str(number)

    return True if numberString == numberString[::-1] else False

def largestPalindromeProductBelowNumber(number):
    largestPalindromeProduct = 0

    for x in range(1, 1000):
        for y in range(x, 1000):
            product = x * y
            if largestPalindromeProduct < product < number:
                if isPalindrome(product):
                    largestPalindromeProduct = product

    print(largestPalindromeProduct)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    largestPalindromeProductBelowNumber(n)
