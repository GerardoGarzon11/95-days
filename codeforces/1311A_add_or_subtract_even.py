for tc in range(0, int(input())):
	a, b = map(int, input().split())

	if a == b:
		print(0)
	else:
		if b > a:
			diff = b - a
			print(1 if diff % 2 != 0 else 2)
		else:
			diff = a - b
			print(2 if diff % 2 != 0 else 1)