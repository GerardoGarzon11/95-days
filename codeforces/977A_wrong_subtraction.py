n, k = input().split()

n, k = int(n), int(k)

for x in range(k):
	n = n - 1 if n % 10 != 0 else n // 10

print(n)
