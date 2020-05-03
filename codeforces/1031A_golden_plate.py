"""
	https://codeforces.com/problemset/problem/1031/A
	Input:
		w	width
		h 	height
		k	number of gilded rings

	Output
		res number of cells to be gilded
"""

def calcGildedCells(width, height, k):
	result = 0

	for i in range(0, k):
		result += 2 * ((width - (i * 4)) + (height - (i * 4))) - 4

	return result

w, h, k = map(int, input().split())

print(calcGildedCells(w, h, k))