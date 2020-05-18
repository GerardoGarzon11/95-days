n = int(input())

# x left [0]
# x right [1]
xlr = [0, 0]

for i in range(0, n):
	x, y = map(int, input().split())
	if x < 0:
		xlr[0] += 1
	else:
		xlr[1] += 1

if xlr[0] <= 1 or xlr[1] <= 1:
	print("Yes")
else:
	print("No")