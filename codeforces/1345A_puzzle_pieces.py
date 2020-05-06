"""
	https://codeforces.com/contest/1345/problem/A
"""

for tc in range(0, int(input())):
	n, m = map(int, input().split())

	if n == 1 or m == 1:
		print("YES")
	elif n == 2 and m == 2:
		print("YES")
	else:
		print("NO")