for tc in range(0, int(input())):
	x = int(input())

	print(x // 2 if x % 2 == 0 else 1 + ((x - 3) // 2))