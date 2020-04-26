names = []

for n in range(0, int(input())):
	name = input()

	if name in names:
		print("YES")
	else:
		print("NO")
		names.append(name)