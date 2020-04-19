"""
	x1 = a + b
	x2 = a + c
	x3 = b + c
	x4 = a + b + c
"""

"""
	Note: sorting before using map(int, list)
	sorts the input based on string order
	i.e.: 33 comes before 4, 8 comes after 77777
"""
x = sorted(list(map(int, input().split())))

print(x[3] - x[0], x[3] - x[1], x[3] - x[2])
