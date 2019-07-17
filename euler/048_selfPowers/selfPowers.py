def selfPowers():
	return sum([x**x for x in range(1, 1001)]) % 10000000000

print(selfPowers())
