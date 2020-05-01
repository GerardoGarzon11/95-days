def lessFrequent(arr):
	arr = sorted(arr)
	l = arr.count(arr[0])
	return arr[0] if l == 1 else arr[-1]

n, m = map(int, input().split())

xs = []
ys = []

for x in range(0, n):
	row = list(input())
	for y in range(0, m):
		if row[y] == '*':
			xs.append(x)
			ys.append(y)

print(lessFrequent(xs) + 1, lessFrequent(ys) + 1)
"""
x y
0 1
2 0
2 1

0 0"""