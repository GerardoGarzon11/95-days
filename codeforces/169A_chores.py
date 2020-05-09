"""
	https://codeforces.com/problemset/problem/169/A
	Input
		n 	number of chores
		a 	Petya chores (more complex)
		b 	Vasya chores (less complex)
	Output
		x	number of ways chores can be distributed
"""

n, a, b = map(int, input().split())

h = sorted(list(map(int, input().split())))

petya_chores = h[-a:]
vasya_chores = h[:b]

print(min(petya_chores) - max(vasya_chores))