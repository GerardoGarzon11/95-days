for tc in range(0, int(input())):
	n = int(input())

	found = False
	factor = 2**1
	sum_ = 3

	while not found:
		if n % sum_ == 0:
			found = True
			break

		factor *= 2
		sum_ += factor

	print(n // sum_)
