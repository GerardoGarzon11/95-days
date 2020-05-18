"""
	https://codeforces.com/problemset/problem/702/A
	Input
		n	the number of integers
		a 	array
	Output
			maximum length of an increasing subarray of the given array
"""
n = int(input())

a = list(map(int, input().split()))

inc = [1] * n

if n == 1:
	print(1)
else:
	for i in range(1, n):
		if a[i-1] < a[i]:
			inc[i] = inc[i-1] + 1

	print(max(inc))