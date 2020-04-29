n = int(input())

a = sorted(list(map(int, input().split())))

if len(a) % 2 != 0:
	print(a[len(a)//2])
else:
	print(a[len(a)//2 - 1])