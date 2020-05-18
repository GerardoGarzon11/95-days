n, k = map(int, input().split())

mins = k
prob = 0

while mins + (prob + 1) * 5 <= 240 and prob < n:
	mins += (prob + 1) * 5
	prob += 1

print(prob)