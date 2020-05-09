"""
	https://codeforces.com/problemset/problem/992/A
	Input
		n	size of array
		a 	array
	Output
		x	number of seconds needed to make all elements explode
"""

n = int(input())

a = list(map(int, input().split()))

# each distinct element is a step needed
not_zeroes = set([i for i in a if i != 0])

# number
print(len(not_zeroes))