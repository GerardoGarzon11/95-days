for tc in range(0, int(input())):
	n = int(input())
	a = list(map(int, input().split()))


	anyFound = False
	odds = []

	for i in range(0, len(a)):
		if a[i] % 2 == 0:
			print(1)
			print(i + 1)
			anyFound = not anyFound
			break
		elif a[i] % 2 != 0:
			if len(odds) == 1:
				print(2)
				print(odds[0], i + 1)
				anyFound = not anyFound
				break
			else:
				odds.append(i + 1)

	if not anyFound:
		print(-1)