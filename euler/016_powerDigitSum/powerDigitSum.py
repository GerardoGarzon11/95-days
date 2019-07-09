def powerDigitSum(exp):
	bigNumber = 2 ** exp
	bigNumberList = list(str(bigNumber))
	return sum([int(x) for x in bigNumberList])

print(powerDigitSum(int(input())))
