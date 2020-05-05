"""
	https://codeforces.com/problemset/problem/46/A
	Input
		n	number of kids
	Output
			Kids who got the ball

"""

n = int(input())

current = 1
kids = []

for x in range(1, n):
	current += x
	current = current - n if current > n else current
	kids.append(current)

print(*kids)