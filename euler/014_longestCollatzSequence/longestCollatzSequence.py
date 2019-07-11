def longestCollatzSequence():
	longest = 1 #1
	number = 1
	for x in range(2, 1000001):
		# collatz
		tmpN = x
		n = x
		sequence = 1
		while n > 1:
			if n % 2 == 0:
				n = n / 2
			else:
				n = 3*n + 1
			sequence += 1

		if sequence > longest:
			longest = sequence
			number = tmpN

	return number


print(longestCollatzSequence())
