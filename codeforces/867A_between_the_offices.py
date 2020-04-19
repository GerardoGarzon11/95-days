# number of days
t = int(input())

days = input()

stof, ftos = 0, 0

for x in range(1, len(days)):
	if days[x-1] == 'F' and days[x] == 'S':
		ftos += 1
	elif days[x-1] == 'S' and days[x] == 'F':
		stof += 1

print("YES" if stof > ftos else "NO")
