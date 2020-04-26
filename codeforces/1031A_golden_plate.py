"""
rectagle = w * h
rings = k
(w-4(i-1)) * (h-4(i-1))
"""

w, h, k = map(int, input().split())

res = 0

for i in range(0, k):
	res += 2 * ((w - (i * 4)) + (h - (i * 4))) - 4

print(res)