# A = (4n + 1) % 4 == 1		+0
# B = (4n + 3) % 4 == 3		+2
# C = (4n + 2) % 4 == 2		+1
# D = (4n) % 4 == 0			+1

x = int(input())

if x % 4 == 1:
	number, letter = 0, 'A'
elif x % 4 == 3:
	number, letter = 2, 'A'
elif x % 4 == 2:
	number, letter = 1, 'B'
else:
	number, letter = 1, 'A'

print(number, letter)