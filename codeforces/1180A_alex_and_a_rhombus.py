n = int(input())

cells = 1

if n == 1:
	print(cells)
else:
	for x in range(2, n + 1):
		cells += 4 * (x - 1)

	print(cells)