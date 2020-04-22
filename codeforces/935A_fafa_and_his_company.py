n = int(input())

ways = 0

for x in range(1, (n // 2) + 1):
	if n % x == 0:
		ways += 1

print(ways)
