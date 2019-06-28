fibo = [1, 1]
evenFibonacciSum = 0

while fibo[0] + fibo[1] < 1000000:
	fibo[0], fibo[1] = fibo[1], fibo[0] + fibo[1]
	if fibo[1] % 2 == 0:
		evenFibonacciSum += fibo[1]

print(evenFibonacciSum)
