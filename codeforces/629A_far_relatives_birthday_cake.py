# Disclaimer: I'm not satisfied with this solution
# but it works...

"""
	https://codeforces.com/problemset/problem/629/A
"""

def getPairs(n):
	pairs = 0
	for x in range(1, n):
		pairs += x
	return pairs

n = int(input())

# base cases

cols = [0] * n
rows = [0] * n
cake = []

for i in range(0, n):
	cake.append(list(input()))

for x in range(0, n):
	for y in range(0, n):
		if cake[x][y] == 'C':
			cols[y] += 1
			rows[x] += 1

pairs = 0

for j in range(0, n):
	if cols[j] > 1:
		pairs += getPairs(cols[j])
	if rows[j] > 1:
		pairs += getPairs(rows[j])

print(pairs)