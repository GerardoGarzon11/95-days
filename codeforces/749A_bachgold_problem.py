n = int(input())

sum_ = [2] * (n // 2)

if n % 2 == 1:
	sum_[-1] = 3

print(len(sum_))
print(*sum_)