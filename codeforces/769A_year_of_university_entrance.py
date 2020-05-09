"""
	https://codeforces.com/problemset/problem/769/A
	Input
		n	number of groups joined
		a 	list of groups joined
	Output
		y	year of university entrance
"""

n = int(input())

a = sorted(list(map(int, input().split())))

print(a[n//2])