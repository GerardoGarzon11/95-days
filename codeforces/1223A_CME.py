for q in range(0, int(input())):
	n = int(input())

	if n == 1:
		print(3)
	elif n == 2:
		print(2)
	elif n % 2 == 0:
		print(0)
	else:
		print(1)
