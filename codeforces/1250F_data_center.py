n = int(input())

perimeter = 1 * 2 + n * 2

for x in range(n//2, 0, -1):
	if n % x == 0:
		s1 = x
		s2 = n // x
		if s1 * 2 + s2 * 2 < perimeter:
			perimeter = s1 * 2 + s2 * 2

print(perimeter)