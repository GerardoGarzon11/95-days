a, b = [0, 0], [0, 0]

for tc in range(0, int(input())):
	t, x, y = map(int, input().split())

	if t == 1:
		a[0] += x
		a[1] += y
	else:
		b[0] += x
		b[1] += y

print("LIVE" if a[0] >= a[1] else "DEAD")
print("LIVE" if b[0] >= b[1] else "DEAD")